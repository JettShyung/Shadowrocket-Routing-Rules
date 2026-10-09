# Shadowrocket Routing Rules

Jett 的 Shadowrocket 配置，参考本人 Open-Box 面板的分流类别、规则来源与匹配顺序。策略组语法参考 `shadowrocket_basic.conf`。

**配置入口：[shadowrocket.conf](./shadowrocket.conf)。共 14 个服务分流组、34 个不同规则来源。** 国内默认 `DIRECT`，其余 13 组默认 `PROXY`，使用小火箭当前选择的节点。来源与图标见 [规则来源对照](./docs/rules.md)、[图标对照](./docs/icons.md)。

这是 Shadowrocket 兼容配置；Open-Box 的原图绑定和部分正则无法确认可直接移植，差异在下文列明。

## 导入使用

1. 在 Shadowrocket 中导入自己的节点或订阅。配置不提供节点服务器、密码、订阅令牌。
2. 将 `shadowrocket.conf` 保存到设备后导入；发布到 GitHub 后，也可使用自己的 Raw 链接下载。
3. 选中该配置，将首页的「全局路由」设为「配置」，等待所有远程规则集下载完成。
4. 在首页选择可用节点并连接。每个服务分流组都可在 `PROXY`（当前节点）与 `DIRECT`（直连）之间切换。
5. 用连接记录核对命中的分流组。客户端若保留了以前手动选择的出口，以实际显示为准。

## 分流与默认出口

下面是规则匹配顺序；客户端分组展示顺序另按原页面保留。所有分流组都只提供 `PROXY` 和 `DIRECT` 两个选项。

| 优先级 | 分流组 | 默认出口 | 内容 |
| --- | --- | --- | --- |
| 1 | Test | PROXY | 原页面的 56 个域名后缀、1 个精确域名、2 个 IP 网段 |
| 2 | AI | PROXY | `category-ai-!cn`，包括 ChatGPT、Claude、Gemini 等 |
| 3 | Youtube | PROXY | YouTube |
| 4 | TikTok | PROXY | `tiktok` 与 `tiktok@!cn` |
| 5 | Netflix | PROXY | Netflix 域名和 IP |
| 6 | Google | PROXY | Google |
| 7 | Github | PROXY | GitHub |
| 8 | Microsoft | PROXY | Microsoft |
| 9 | Apple | PROXY | Apple，包含规则集中的中国区域名 |
| 10 | Games | PROXY | Steam、Sony |
| 11 | 区块链金融 | PROXY | 页面指定的 10 个平台规则集 |
| 12 | 国外 | PROXY | GFW 域名和页面指定的 9 个 IP 规则集 |
| 13 | 国内 | DIRECT | CN 域名、CN 与 Private IP |
| 14 | 其他 | PROXY | 未匹配流量 |

原页面的「前置自定义分流」为空，配置保留注释占位，没有额外生效规则。`fast.com`、`ustc.edu.cn`、`workers.dev` 等在 Test 中，所以优先走 Test；这也是参考配置的行为。原页面的未知域名直接进入「其他」。本配置用 `no-resolve` 避免为 IP 规则主动解析域名，但客户端仍可能用连接中已知的 IP 匹配，不能保证与 Open-Box 的「仅 IP 连接」判定完全相同。

## 来源与兼容处理

参考页面为 Open-Box `v0.1.304`，读取日期为 2026-10-09，面板显示 Geo 数据日期为 `2026-10-05T01:08:09Z`。读取过程中只查看页面及取消编辑弹窗，没有保存或更改面板配置。

- **同源规则：**页面选用 [MetaCubeX/meta-rules-dat 的 sing/geo](https://github.com/MetaCubeX/meta-rules-dat/tree/sing/geo)。Shadowrocket 配置使用该项目 `meta/geo/*/classical/*.list` 文本版本，保留同名来源、归属与引用顺序。35 次引用对应 34 个不同来源，Netflix IP 在两组中均保留。这里使用上游当前内容，未恢复面板 10 月 5 日缓存的历史文件。
- **3 份兼容列表：**AI、Netflix 域名、Google 域名原有共 7 条 `DOMAIN-REGEX`。因未确认小火箭支持该规则类型，转换为 `DOMAIN-WILDCARD`；原表达式和转换结果保存在 [rules/compat](./rules/compat/)，并内联进主配置，导入不依赖尚未发布的个人仓库链接。通配符匹配范围略宽，并非正则的完全等价转换；其余条目保留原类型和值。
- **原图：**14 个服务分流组的原图与映射已保存。尚未确认 Shadowrocket 配置支持给策略组绑定这些 SVG，故不添加未经证实的 `icon=` 等字段。当前 `.conf` 保留原组名，不能承诺在小火箭中显示浏览器的原图；详见 [图标对照](./docs/icons.md)。
- **客户端基础项：**沿用所提供小火箭配置的 General 设置，省略第三方 `update-url`，避免更新时覆盖自己的配置。浏览器仅提供分流类别和规则参考。

适配规则使用 `DOMAIN-WILDCARD`，其支持可查 [Shadowrocket 官方更新记录](https://t.me/s/shadowrocketnews?after=950)。配置格式参考 [LOWERTOP 使用手册](https://github.com/LOWERTOP/Shadowrocket)；远程 IP 规则的外层 `no-resolve` 写法也可见 [维护者配置示例](https://raw.githubusercontent.com/haritos90/shadowrocket-config-files/main/h90_main.conf)。这些资料与脚本检查不能替代真机导入验证。

## 更新与校验

Python 3.9 或更新版本即可，无第三方依赖：

```sh
# 下载并转换 3 份兼容列表，同时更新主配置内联块
python3 scripts/update_compat.py

# 离线检查转换边界、内联一致性、配置结构
python3 scripts/update_compat.py --check
python3 tests/check_rules.py --offline

# 下载远程规则，检查实际域名匹配和分流顺序
python3 tests/check_rules.py
```

遇到未知上游正则、意外规则类型或下载失败，更新脚本报错，不用不完整下载覆盖现有文件。不要手工修改主配置的 `BEGIN COMPAT`／`END COMPAT` 块；它们由兼容列表生成。测试只模拟规则匹配，不建立 VPN 或 DNS 请求，也不验证节点可用性。

其余 31 个不同的远程规则集由 Shadowrocket 下载更新。发布新的兼容列表后，还需让客户端更新主配置；仅刷新远程规则集不会改变内联规则。首次规则下载失败时，可暂时使用已有节点的代理模式完成下载，再切回配置模式。

## 发布到 GitHub

推送本仓库到自己的 GitHub 后，配置 Raw 链接为：

```text
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/shadowrocket.conf
```

这是模板，需替换用户名、仓库名和实际分支名。当前未创建远端仓库或推送。无需启用 GitHub Pages，也无需把私人节点和订阅加入公开仓库。

本仓库自行编写的配置、文档和脚本使用 [MIT License](./LICENSE)。引用及转换的规则遵循 [MetaCubeX 及其上游](https://github.com/MetaCubeX/meta-rules-dat) 的许可；浏览器原图属于第三方素材，不以本仓库 MIT 重新授权。感谢 [Johnshall](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) 的配置组织参考，以及 [Open-Box](https://github.com/liandu2024/Open-Box) 和规则维护者。
