# 调用速查

| 用户意图 | 推荐组合 |
|---|---|
| “继续写这个角色” | Core + Write Natural；已有身体差异时加 Foundation；动作复杂时再加 Physicality；命中专项则叠加专项 |
| “写她怎么洗澡/穿衣/走路/跳/爬/转移” | Core + Foundation + Write Natural + Write Physicality + 对应专项；出现器械时加 Aids |
| “角色双腿还在但不能动/瘫痪” | Core + Foundation + Physicality；**不要**自动路由到截肢专项 |
| “眼睛乳白、失明但眼球还在” | Core + Foundation + Ocular；锁定 `globe_present + vision_absent`，不要写成空眼窝 |
| “写她和别人相处/恋爱/被帮助” | Core + Foundation + Write Natural + Write Character + 对应专项 |
| “规划大篇章/案件/冒险” | Core + Write Story + Character；身体状态参与因果时加 Foundation/Physicality/专项 |
| “画人设图/插画/漫画” | Core + Foundation + Visual + 对应专项 + Aids（若有器械） |
| “画空袖/空裤腿/空袜筒/丝袜/裤袜” | Foundation + Visual；先锁天然结构/残肢/假肢的支撑终点，再写衣物空置 |
| “检查设定有没有写错/画错” | Core + Foundation + 对应专项 + Audit |

## 专项叠加

- 经股截肢 + 义眼：`amputation-transfemoral + ocular-loss`
- 经肱 + 经股：`combined-limb-loss + amputation-transhumeral + amputation-transfemoral`
- 没有对应专项：不要硬套最接近的截肢类型，使用 Foundation 的通用结构/功能模型即可。

`combined-limb-loss` 负责上下肢资源耦合；具体经肱/经股解剖分别由 `amputation-transhumeral` / `amputation-transfemoral` 负责。Foundation 始终负责“存在性/功能性、衣物拓扑、动作类型”等跨专项语义。

绘图类默认交付通用中文可复制提示词，不默认调用出图工具；已有正文转配图也使用同一状态。输出模板见 [视觉提示词](../visual-continuity/prompt-template.md)，自然写作示范见 [改写例集](../writing-natural/examples.md)。
