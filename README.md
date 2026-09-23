# Creative Skills 2.2

用于中文小说、人物设定与可复制绘图提示词的 13 个组合技能。身体结构、残肢、残态、假肢、义眼、辅具、服装和动作保持一致；人物的语言、欲望和关系仍是具体的。

默认写作取向是**细致且自然融入**：允许身体形态、触感、衣料和审美观察，不把描写变成解剖报表、苦难展览或尊重宣言。默认绘图交付是**通用中文自然语言提示词**，不自动生成图片。

面向明确喜爱残疾身体、截肢与残肢描写的成年读者时，身体形态可以成为持续的审美与情欲关注点；残态、生活阻力、失败和求助也可以直接参与情节。小说正文优先使用“大腿／小腿截肢”“上臂／前臂截肢”等顺口表达，以动作、姿态和衣料呈现事实；状态卡仍精确记录侧别、保留关节与终点。人物对自身身体的厌恶、喜爱、调侃或实用态度分别建立，不套同一种接纳轨迹。

## 把仓库交给 AI
将仓库文件提供给 AI，附上任务与已有正文／人物设定，可以直接使用：

> 请先读取 README.md、MANIFEST.json 和 creative-core/SKILL.md，再按我的任务读取对应现行技能及必要引用。历史粗稿已在 2.2 收尾后从 main 移除；必要的来源与取舍记录保留在 docs 中，现役运行不依赖历史 archive。沿用已有角色事实；正文默认细致自然，绘图默认输出可复制中文提示词。内部检查身体、衣物和设备连续性，直接交付我要求的成品。若无法访问文件，请指出缺失文件，不要声称已经读取。

仅给一个网址不保证使用中的 AI 能读取仓库。无法访问时提供实际文件；不要声称这个仓库已作为模型训练或保证所有模型输出同样质量。
按目录安装时保留所需技能及其相对引用目录；单独复制一个 SKILL.md 会丢失组合规则与例集。一般任务只读相关模块，不需要加载历史来源记录。

## 现行技能
| 技能 | 用途 |
|---|---|
| [creative-core](creative-core/SKILL.md) | 状态、路由、设定与事件的关系 |
| [disability-foundation](disability-foundation/SKILL.md) | 结构与功能分离、衣物支撑、残态 |
| [writing-natural](writing-natural/SKILL.md) | 正文、对白、视角、节奏、自然改写 |
| [writing-physicality](writing-physicality/SKILL.md) | 动作、移动、日常任务、支撑与手占用 |
| [writing-character](writing-character/SKILL.md) | 人物、帮助边界、亲密关系、凝视与群像 |
| [writing-story](writing-story/SKILL.md) | 开篇、续写、信息释放、因果与世界观 |
| [visual-continuity](visual-continuity/SKILL.md) | 提示词、构图、材质、多人多图与局部修改 |
| [assistive-devices](assistive-devices/SKILL.md) | 假肢、拐杖、轮椅、义眼等装置 |
| [amputation-transfemoral](amputation-transfemoral/SKILL.md) | 经股截肢 |
| [amputation-transhumeral](amputation-transhumeral/SKILL.md) | 经肱截肢 |
| [combined-limb-loss](combined-limb-loss/SKILL.md) | 上下肢组合的资源与动作 |
| [ocular-loss](ocular-loss/SKILL.md) | 眼部结构、视觉与外观装置 |
| [quality-audit](quality-audit/SKILL.md) | 事实、连续性与阅读效果检查 |

普通正文使用核心与自然写作，涉及身体才叠加基础、动作和命中专项；绘图任务使用核心、基础、视觉与命中专项。详细见 [调用速查](docs/ROUTING-CHEATSHEET.md)。

## 写作要求与粗稿吸收
[写作要求](writing-natural/writing-requirements.md)集中说明正文交付、细致身体描写、长期人物与文风复查。日常与感知、人物关系、故事方法按需读取，已包含具体执行方法和原创例句，不只留下原则摘要。
[来源与吸收对照](docs/SOURCES-AND-DESIGN.md)逐项列出 write-rule 的十部分、disable-skill-pack 的 17 个技能及其现行落点，区分保留、修订和不沿用的内容。

## 2.2 收尾
完成蒸馏回归审计、统一现役命名与眼部结构状态；随后进行 post-release cleanup，从 main 移除整个历史 `archive`。CI 同时运行仓库校验、校验器自检和 release hygiene。2.1 已完成的写作、人物、身体、辅具与视觉方法保持不变。

恢复六个占位技能，加入 [六组原创改写对照](writing-natural/examples.md)及 [四组完整绘图案例](visual-continuity/prompt-template.md)。统一状态命名，区分长期事实与穿脱等即时变化；从旧资料提炼可选择的方法，不继承固定人格、描写配额和未经证实的通用数值。
13 份本地测试均有实际行为案例。静态校验拦截占位正文、空测试和失效内部文件链接；文学效果仍需结合具体输出审阅，见 [验证说明](tests/README.md)。

## 目录与来源
现行技能继续位于根目录，ID 与 MANIFEST 保持一致；docs 为设计与来源，tests 为跨技能案例，scripts 为标准库校验。
历史粗稿已在 2.2 收尾后从 main 移除；必要的来源与取舍记录保留在 docs 中，现役运行和校验不依赖历史 archive。来源记录使用固定提交与历史路径，不产生删除后失效的本地链接。本仓库实际包含技能、摘录和整理材料；旧说明提到的完整小说与原始 ZIP 并未随当前仓库提供，不能据此声称读过全部原作。
参见 [来源与取舍](docs/SOURCES-AND-DESIGN.md)、[身体状态](docs/DISABILITY-MODEL.md)、[架构](docs/ARCHITECTURE.md)、[命名迁移](docs/NAMING-MIGRATION.md)和 [贡献规则](CONTRIBUTING.md)。

## 校验
```bash
python scripts/validate_repo.py
python scripts/test_validate_repo.py
python scripts/validate_release.py
```
