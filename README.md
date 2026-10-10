# Shadowrocket Routing Rules

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Release](https://img.shields.io/github/v/release/JettShyung/Shadowrocket-Routing-Rules)](https://github.com/JettShyung/Shadowrocket-Routing-Rules/releases)
[![Last Commit](https://img.shields.io/github/last-commit/JettShyung/Shadowrocket-Routing-Rules)](https://github.com/JettShyung/Shadowrocket-Routing-Rules/commits/main)

**当前版本：[v1.0.0](https://github.com/JettShyung/Shadowrocket-Routing-Rules/releases/tag/v1.0.0)** · [更新记录](./CHANGELOG.md)

这是我维护的 Shadowrocket 分流配置，按服务划分 AI、流媒体、开发工具、游戏平台及国内外流量。我在这里公开配置、规则来源和兼容处理脚本，方便直接使用、检查和按需调整。

配置包含 **14 个服务分流组、34 个不同规则来源**。国内流量默认直连，未匹配流量进入「其他」分组。使用前需要自行导入节点或订阅。

## 配置下载

[下载 shadowrocket.conf](https://raw.githubusercontent.com/JettShyung/Shadowrocket-Routing-Rules/main/shadowrocket.conf) · [查看配置](./shadowrocket.conf) · [规则来源](./docs/rules.md)

在 Shadowrocket 中添加以下配置地址：

```text
https://raw.githubusercontent.com/JettShyung/Shadowrocket-Routing-Rules/main/shadowrocket.conf
```

上述地址跟随 `main` 更新。如需固定本次配置，请使用 [v1.0.0 配置](https://raw.githubusercontent.com/JettShyung/Shadowrocket-Routing-Rules/v1.0.0/shadowrocket.conf)。远程规则集仍随各自上游更新。

## 使用方法

1. 在 Shadowrocket 中导入自己的节点或订阅。
2. 在「配置」中添加上述地址，下载并选中配置；也可以下载文件后手动导入。
3. 将首页的「全局路由」设为「配置」，等待远程规则集下载完成。
4. 检查各服务分组的出口，选择可用节点后连接。地区分组按节点名称筛选，自动分组定时测速，手动分组由自己选择节点。
5. 在连接记录中核对规则命中情况。客户端可能保留之前手动选择的出口，以实际显示为准。

### 自动选择与空分组

Shadowrocket 支持 `url-test` 自动策略；[官方 2.2.87 更新公告](https://t.me/ShadowrocketNews/1504)明确记录了延迟测试组自动切换逻辑的优化，[App Store 版本记录](https://apps.apple.com/us/app/shadowrocket/id932747118)也包含相关维护记录。我保留全部节点及 6 个地区的自动策略，供需要按延迟选择节点的使用者选用。

自动组配置了 `interval=300`、`tolerance=100` 和 `timeout=5`。它们依据测试结果和切换公差选择节点，不保证每次测试后都切换，也不代表下载带宽测速。全局路由需要使用「配置」，相应服务的出口也需要选到自动组，流量才会通过该自动策略。

如果分组显示 `None`，请进入分组检查候选节点。地区筛选依据节点名称中的地区关键词，不会通过服务器 IP 自动判断地区。若自动组和手动组同时为空，应先检查节点名称、订阅是否已导入及筛选范围。只有一个候选节点时，也没有其他节点可供切换。

## 分流规则

默认出口：国内为「直连」，Github、Microsoft、Games 为「美国-自动」，区块链金融为「新加坡-自动」，其余服务为「所有-手动」。如果地区分组没有匹配节点，请切换到「所有-手动」并选择可用节点。

规则按下表从上到下匹配，首次命中后使用对应分组。客户端中的分组展示顺序与规则匹配顺序相互独立。

| 优先级 | 分流组 | 覆盖内容 |
| --- | --- | --- |
| 1 | Test | 56 个域名后缀、1 个精确域名、2 个 IP 网段，主要用于测速和网络检测 |
| 2 | AI | ChatGPT、Claude、Gemini 等 AI 服务 |
| 3 | Youtube | YouTube |
| 4 | TikTok | `tiktok` 与 `tiktok@!cn` |
| 5 | Netflix | Netflix 域名和 IP |
| 6 | Google | Google |
| 7 | Github | GitHub |
| 8 | Microsoft | Microsoft |
| 9 | Apple | Apple，包含规则集中的中国区域名 |
| 10 | Games | Steam、Sony |
| 11 | 区块链金融 | Binance、OKX 等 10 个平台规则集 |
| 12 | 国外 | GFW 域名和 9 个 IP 规则集 |
| 13 | 国内 | CN 域名、CN 与 Private IP |
| 14 | 其他 | 未匹配流量 |

`fast.com`、`ustc.edu.cn`、`workers.dev` 等域名优先进入 Test。Apple 等服务规则先于国内规则，因此服务组覆盖的中国区域名也会使用该服务组的出口。

IP 规则带有 `no-resolve`，避免为匹配规则主动解析域名；客户端仍可能使用连接中已知的 IP 匹配。默认关闭 IPv6，并阻断代理连接的 QUIC 流量。

## 规则来源与兼容处理

我使用 [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat) 的 `meta/geo/*/classical/*.list` 规则。配置共引用 35 次，涉及 34 个不同来源；Netflix IP 在 Netflix 和国外分组中各引用一次。完整对照见[规则来源](./docs/rules.md)。

其中 AI、Netflix 域名、Google 域名的 3 份列表包含共 7 条 `DOMAIN-REGEX`。目前将这些表达式转换为 `DOMAIN-WILDCARD`，原表达式与转换结果保存在 [rules/compat](./rules/compat/) 中，并内联到主配置。通配符的匹配范围略宽于原正则，其余条目保留原类型和值。

其余 31 个不同的远程规则集由 Shadowrocket 下载更新。兼容列表更新后，需要重新下载主配置；仅刷新远程规则集不会更新内联规则。首次下载失败时，可以通过已有代理节点完成下载，再切回「配置」模式。

## 开发与校验

版本号记录在 [VERSION](./VERSION)。我从 `v1.0.0` 开始编号，每次发布小更新递增最后一位，例如 `v1.0.1`、`v1.0.2`。发布时同步配置文件头、README 和更新记录，并创建同名 GitHub Release 与标签。

使用 Python 3.9 或更新版本，无需安装第三方依赖：

```sh
# 下载并转换 3 份兼容列表，同时更新主配置
python3 scripts/update_compat.py

# 离线检查转换边界、内联一致性和配置结构
python3 scripts/update_compat.py --check
python3 tests/check_rules.py --offline

# 下载远程规则，检查域名匹配和分流顺序
python3 tests/check_rules.py
```

更新脚本会在未知正则、意外规则类型或下载失败时报错，校验通过后才替换文件。主配置中的 `BEGIN COMPAT` / `END COMPAT` 块由脚本生成，请勿手工修改。

修改分流类别、规则来源或匹配顺序时，请同步[规则校验数据](./tests/routing.json)和相关文档。检查脚本验证配置结构及规则匹配，不验证 DNS、节点可用性或实际 VPN 转发；客户端兼容性仍需真机导入确认。

## 许可与致谢

我编写的配置、文档和脚本采用 [MIT License](./LICENSE)。引用及转换的规则遵循 [MetaCubeX 及其上游](https://github.com/MetaCubeX/meta-rules-dat) 的许可。

感谢 [MetaCubeX](https://github.com/MetaCubeX/meta-rules-dat) 及上游规则维护者，以及 [Johnshall](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) 的配置组织参考。
