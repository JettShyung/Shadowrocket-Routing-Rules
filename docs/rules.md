# 规则来源逐项对照

页面来源：[MetaCubeX / sing/geo](https://github.com/MetaCubeX/meta-rules-dat/tree/sing/geo)。以下按实际分流顺序列出全部 **35 次引用、34 个不同来源**；Netflix IP 保留两次引用。链接指向同源 `classical` 文本，保留域名关键字等类型，不使用只含裸域名的列表。

| 分流组 | 页面规则集 ID | 小火箭同源文本 | 加载方式 |
| --- | --- | --- | --- |
| AI | `geosite/category-ai-!cn` | [category-ai-!cn.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/category-ai-!cn.list) | [兼容列表](../rules/compat/category-ai-!cn.list)内联，原正则写在注释中 |
| Youtube | `geosite/youtube` | [youtube.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/youtube.list) | RULE-SET |
| TikTok | `geosite/tiktok` | [tiktok.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/tiktok.list) | RULE-SET |
| TikTok | `geosite/tiktok@!cn` | [tiktok@!cn.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/tiktok@!cn.list) | RULE-SET |
| Netflix | `geosite/netflix` | [netflix.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/netflix.list) | [兼容列表](../rules/compat/netflix.list)内联，原正则写在注释中 |
| Netflix | `geoip/netflix` | [netflix.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/netflix.list) | RULE-SET，no-resolve |
| Google | `geosite/google` | [google.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/google.list) | [兼容列表](../rules/compat/google.list)内联，原正则写在注释中 |
| Github | `geosite/github` | [github.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/github.list) | RULE-SET |
| Microsoft | `geosite/microsoft` | [microsoft.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/microsoft.list) | RULE-SET |
| Apple | `geosite/apple` | [apple.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/apple.list) | RULE-SET |
| Games | `geosite/steam` | [steam.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/steam.list) | RULE-SET |
| Games | `geosite/sony` | [sony.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/sony.list) | RULE-SET |
| 区块链金融 | `geosite/zb` | [zb.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/zb.list) | RULE-SET |
| 区块链金融 | `geosite/okx` | [okx.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/okx.list) | RULE-SET |
| 区块链金融 | `geosite/binance` | [binance.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/binance.list) | RULE-SET |
| 区块链金融 | `geosite/bybit` | [bybit.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/bybit.list) | RULE-SET |
| 区块链金融 | `geosite/huobi` | [huobi.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/huobi.list) | RULE-SET |
| 区块链金融 | `geosite/8btc` | [8btc.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/8btc.list) | RULE-SET |
| 区块链金融 | `geosite/nexo` | [nexo.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/nexo.list) | RULE-SET |
| 区块链金融 | `geosite/gateio` | [gateio.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/gateio.list) | RULE-SET |
| 区块链金融 | `geosite/onekey` | [onekey.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/onekey.list) | RULE-SET |
| 区块链金融 | `geosite/kucoin` | [kucoin.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/kucoin.list) | RULE-SET |
| 国外 | `geosite/gfw` | [gfw.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/gfw.list) | RULE-SET |
| 国外 | `geoip/cloudflare` | [cloudflare.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/cloudflare.list) | RULE-SET，no-resolve |
| 国外 | `geoip/facebook` | [facebook.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/facebook.list) | RULE-SET，no-resolve |
| 国外 | `geoip/cloudfront` | [cloudfront.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/cloudfront.list) | RULE-SET，no-resolve |
| 国外 | `geoip/fastly` | [fastly.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/fastly.list) | RULE-SET，no-resolve |
| 国外 | `geoip/google` | [google.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/google.list) | RULE-SET，no-resolve |
| 国外 | `geoip/netflix` | [netflix.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/netflix.list) | RULE-SET，no-resolve |
| 国外 | `geoip/telegram` | [telegram.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/telegram.list) | RULE-SET，no-resolve |
| 国外 | `geoip/tor` | [tor.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/tor.list) | RULE-SET，no-resolve |
| 国外 | `geoip/twitter` | [twitter.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/twitter.list) | RULE-SET，no-resolve |
| 国内 | `geosite/cn` | [cn.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/classical/cn.list) | RULE-SET |
| 国内 | `geoip/cn` | [cn.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/cn.list) | RULE-SET，no-resolve |
| 国内 | `geoip/private` | [private.list](https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/classical/private.list) | RULE-SET，no-resolve |

Test 无远程规则集，使用页面手填的 59 条规则；其他使用 `FINAL,其他`。完整手填条目与分流类别见 [reference/open-box.json](../reference/open-box.json)。Test 原填 `74.125.250.129/24` 已规范为相同网段 `74.125.250.0/24`。

面板 Geo 缓存日期为 2026-10-05，迁移时读取同名来源的当前文本，内容可能已随上游更新。原图和分组对应关系见 [icons.md](./icons.md)。
