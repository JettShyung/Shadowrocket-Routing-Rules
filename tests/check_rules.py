#!/usr/bin/env python3
"""Check the recorded Open-Box policy and real upstream rules, not VPN behavior."""

import argparse
import fnmatch
import ipaddress
import json
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/"


def lines(text):
    return [line.strip() for line in text.splitlines()
            if line.strip() and not line.lstrip().startswith("#")]


def validate(fields, source):
    assert len(fields) == 2 and fields[1], f"Unexpected fields/policy: {source}: {fields}"
    kind, value = fields
    if kind in {"IP-CIDR", "IP-CIDR6"}:
        network = ipaddress.ip_network(value, strict=False)
        assert kind != "IP-CIDR6" or network.version == 6, source
    else:
        assert kind in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "DOMAIN-WILDCARD"}, source
        pattern = r"[A-Za-z0-9_.*?-]+" if kind == "DOMAIN-WILDCARD" else r"[A-Za-z0-9_.-]+"
        assert re.fullmatch(pattern, value), f"Malformed domain: {source}: {value}"
        if kind == "DOMAIN-WILDCARD":
            assert "*" in value or "?" in value, source


def matches(kind, value, domain):
    value, domain = value.lower(), domain.lower()
    return ((kind == "DOMAIN" and domain == value)
            or (kind == "DOMAIN-SUFFIX" and (domain == value or domain.endswith("." + value)))
            or (kind == "DOMAIN-KEYWORD" and value in domain)
            or (kind == "DOMAIN-WILDCARD" and fnmatch.fnmatchcase(domain, value)))


def check_groups(text, reference):
    groups = {}
    for line in lines(text):
        name, value = line.split("=", 1)
        name, parts = name.strip(), [part.strip() for part in value.split(",")]
        assert name not in groups, f"Duplicate group: {name}"
        assert len(parts) == 4 and parts[0] == "select", f"Unexpected node/group settings: {name}"
        members = parts[1:3]
        assert set(members) == {"PROXY", "DIRECT"}, f"Browser outbound copied into {name}"
        assert re.fullmatch(r"select=[01]", parts[3]), f"Invalid default index: {name}"
        groups[name] = members[int(parts[3].split("=")[1])]
    assert list(groups) == reference["proxy_order"] and len(groups) == 14
    for name, policy in groups.items():
        assert policy == ("DIRECT" if name == "国内" else "PROXY"), f"Wrong default: {name}"
    return groups


def check_rules(text, reference, groups):
    expected = [(source, route["name"]) for route in reference["routes"] for source in route["rule_sets"]]
    assert len(expected) == 35 and len({source for source, _ in expected}) == 34
    blocks = re.findall(r"# BEGIN COMPAT (\S+) (\S+)\n(.*?)# END COMPAT \1", text, re.S)
    assert {name for name, _, _ in blocks} == {"category-ai-!cn", "netflix", "google"} and len(blocks) == 3
    for name, policy, body in blocks:
        local = lines((ROOT / "rules" / "compat" / (name + ".list")).read_text())
        assert local and f"# Source: {BASE}geosite/classical/{name}.list" in body, name
        assert lines(body) == [entry + "," + policy for entry in local], f"Stale inline block: {name}"
        for entry in local:
            validate(entry.split(","), name)
    test = [["DOMAIN-SUFFIX", domain, "Test"] for domain in reference["test"]["domain_suffix"]]
    test += [["DOMAIN", domain, "Test"] for domain in reference["test"]["domain"]]
    test += [["IP-CIDR", str(ipaddress.ip_network(cidr, strict=False)), "Test", "no-resolve"]
             for cidr in reference["test"]["ip_cidr"]]
    active = [line.split(",") for line in lines(text)]
    assert active[:len(test)] == test, "Test rules must be first and match the recorded page"
    assert active[-1] == ["FINAL", "其他"] and sum(row[0] == "FINAL" for row in active) == 1
    seen, rules, current = [], [], None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# BEGIN COMPAT "):
            _, _, _, name, policy = line.split()
            current = "geosite/" + name
            seen.append((current, policy))
        elif line.startswith("# END COMPAT "):
            current = None
        elif not line or line.startswith("#") or line == "FINAL,其他":
            continue
        else:
            kind, value, policy, *options = line.split(",")
            assert policy in groups, f"Unknown policy: {line}"
            if kind == "RULE-SET":
                found = re.fullmatch(re.escape(BASE) + r"(geosite|geoip)/classical/([^/]+)\.list", value)
                assert found and current is None, f"Unexpected source: {line}"
                source = "/".join(found.groups())
                assert options == (["no-resolve"] if found[1] == "geoip" else []), line
                seen.append((source, policy))
            else:
                source = current or "Test"
                assert current or line.split(",") in test, f"Unexpected local rule: {line}"
                assert options == (["no-resolve"] if kind.startswith("IP-CIDR") else []), line
                validate([kind, value], source)
            rules.append((kind, value, policy, source))
    assert seen == expected, "Rule sources, policies, or order differ from the recorded page"
    return rules


def download(url):
    with urlopen(url, timeout=30) as response:
        entries = lines(response.read().decode("utf-8-sig"))
    assert entries, f"Empty upstream: {url}"
    fields = [entry.split(",") for entry in entries]
    for row in fields:
        validate(row, url)
        assert row[0] in ({"IP-CIDR", "IP-CIDR6"} if "/geoip/" in url
                          else {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}), url
    return fields


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Check local structure only; no upstream/domain coverage claim")
    args = parser.parse_args()
    reference = json.loads((ROOT / "reference" / "open-box.json").read_text())
    config = (ROOT / "shadowrocket.conf").read_text()
    assert config.count("[Rule]") == config.count("[Proxy Group]") == 1
    group_text, rule_text = config.split("[Proxy Group]", 1)[1].split("[Rule]", 1)
    groups = check_groups(group_text, reference)
    rules = check_rules(rule_text, reference, groups)
    assert matches("DOMAIN-SUFFIX", "apple.com", "apple.com")
    assert matches("DOMAIN-SUFFIX", "apple.com", "www.apple.com")
    assert not matches("DOMAIN-SUFFIX", "apple.com", "fakeapple.com")
    assert not matches("DOMAIN", "apple.com", "www.apple.com")
    assert matches("DOMAIN-WILDCARD", "a-*.example.com", "a-test.example.com")
    assert not matches("DOMAIN-WILDCARD", "a-*.example.com", "a-test.example.com.evil")
    print("PASS: 14 service groups, PROXY/DIRECT defaults, no node groups, 35 ordered sources, 3 matching compatibility blocks.", flush=True)
    if args.offline:
        print("OFFLINE ONLY: remote files and domain coverage were not checked.")
        return
    urls = list(dict.fromkeys(value for kind, value, _, _ in rules if kind == "RULE-SET"))
    assert len(urls) == 31
    with ThreadPoolExecutor(max_workers=4) as pool:
        remote = dict(zip(urls, pool.map(download, urls)))
    expanded = []
    for kind, value, policy, source in rules:
        entries = remote[value] if kind == "RULE-SET" else [[kind, value]]
        expanded.extend((kind, value, policy, source) for kind, value in entries)
    cases = {
        ("Test", "Test"): "fast.com speed.cloudflare.com l.google.com ustc.edu.cn",
        ("AI", "geosite/category-ai-!cn"): "chatgpt.com openai.com claude.ai anthropic.com gemini.google.com",
        ("Youtube", "geosite/youtube"): "youtube.com youtu.be googlevideo.com ytimg.com",
        ("TikTok", "geosite/tiktok"): "tiktok.com tiktokv.com tiktokcdn.com",
        ("Netflix", "geosite/netflix"): "netflix.com nflxvideo.net",
        ("Google", "geosite/google"): "google.com google.cn accounts.google.com",
        ("Github", "geosite/github"): "github.com raw.githubusercontent.com githubassets.com",
        ("Microsoft", "geosite/microsoft"): "microsoft.com live.com office.com",
        ("Apple", "geosite/apple"): "apple.cn apple.com.cn icloud.com.cn captive.apple.com",
        ("Games", "geosite/steam"): "store.steampowered.com steamcommunity.com",
        ("Games", "geosite/sony"): "playstation.com",
        ("区块链金融", "geosite/binance"): "binance.com",
        ("区块链金融", "geosite/okx"): "okx.com",
        ("国外", "geosite/gfw"): "wikipedia.org telegram.org",
        ("国内", "geosite/cn"): "baidu.com qq.com weixin.qq.com alipay.com taobao.com jd.com bilibili.com xiaohongshu.com douyin.com gov.cn",
    }
    for expected, domains in cases.items():
        for domain in domains.split():
            hit = next((rule for rule in expanded if matches(*rule[:2], domain)), None)
            assert hit and hit[2:] == expected, f"{domain}: expected {expected}, got {hit}"
    assert not any(matches(*rule[:2], "unmatched-service.example.invalid") for rule in expanded)
    total = sum(len(domains.split()) for domains in cases.values())
    print(f"PASS: {len(urls)} live remote lists, {len(expanded)} expanded rules, {total} explicit domain cases; unknown domain -> 其他.")
    print("No DNS, GeoIP lookup, node availability, or VPN forwarding is simulated.")


if __name__ == "__main__":
    main()
