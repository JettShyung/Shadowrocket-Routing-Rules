# 规则来源逐项对照

我使用 [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat) 的 `meta/geo` 规则，按分流顺序列出全部 **35 次引用、34 个不同来源**。Netflix IP 在 Netflix 和国外分组中各引用一次。以下链接均指向保留规则类型的 `classical` 文本。

| 分流组 | 规则集 ID | 上游文本 | 加载方式 |
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

Test 使用配置内的 59 条规则（56 个域名后缀、1 个精确域名、2 个 IP 网段）；未匹配流量由 `FINAL,其他` 处理。完整条目、分流类别与匹配顺序保存在[规则校验数据](../tests/routing.json)中。

远程规则随上游更新；3 份兼容列表由 `scripts/update_compat.py` 更新并内联到主配置。
