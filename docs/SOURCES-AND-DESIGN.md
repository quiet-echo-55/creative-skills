# 来源与取舍

## 2.2 实际读取与发布范围

2.2 以用户提供的完整 2.1 压缩包为本地基线。输入 ZIP SHA256：`3eda17d2668e4881719c2a0c37a6366289421969c59bf0a6da031bcc1d10177d`。解压后共有 252 个文件，其中 archive 200 个；`archive/legacy/` 的 54 个文件全部是 `PLACEHOLDER::<old-path>` synthetic 镜像，不包含额外源码。2.2 构建先删除这 54 个伪历史文件并保留 146 个真实历史文件，补入此前已审阅但未落库的蒸馏审计与回归测试；post-release cleanup 随后从 main 移除剩余 146 个历史文件，当前发布树不含 archive。

本次范围是“在完整 2.1 仓库上完成已审阅改动”，不是声称重新取得 archive 外部所提到的全部原始小说。`disable-skill-pack` 内部提到的 18 部小说与本仓库的蒸馏文档是历史来源说明；仓库并未包含这些小说的完整原作，因此现役规则不会把小说语料中的固定数值、动作顺序或人格倾向当成医学事实。

历史粗稿曾是整个项目的来源，位于 2.2 收尾前提交的 `archive/` 路径。2.2 发布树已移除全部历史文件；现行功能与校验不依赖 archive。下表保留历史路径与吸收关系，便于追溯，不表示这些目录仍在当前仓库中。

| 来源 | 提炼到现行模块 | 不作为默认规则的内容 |
|---|---|---|
| 历史提交中的 `archive/MEM-Base/` | 基础、动作、辅具、视觉 | 每动作说明身体、固定使用方式 |
| 历史提交中的 `archive/MEM-Creative-Skills-v1.1/` | 自然写作、人物、故事与专项 | 数量配额、把案例当定律 |
| 历史提交中的 `archive/skill-SAK-v2/` | 经股专项 | 长度、训练年限与能力的固定对应 |
| 历史提交中的 `archive/skill-SAE-v2/` | 经肱专项 | 以缺手默认人格或全部任务能力 |
| 历史提交中的 `archive/skill-OOE-v2/` | 上下肢组合 | 同侧／对侧难易排名 |
| 历史提交中的 `archive/skill-义眼-v2/` | 眼部结构与装置区分 | 默认所有义眼都是眼球摘除后的同一状态 |
| 历史提交中的 `archive/disable-skill-pack/` | 日常、关系、器械物件、信息与潜台词 | 必拒帮助、必经自卑、必揭露身体、体面等级和固定数值 |
| 历史提交中的 `archive/write-rule.md` | 身体观察与人物表达 | 每次提及必须重报层级等强制流程 |

## write-rule 的十部分如何落地
原始来源为 `archive/write-rule.md`。“已吸收”指方法已写入下列现行文件，运行时无需原文。原文内部的刻板示例或医学泛化不随原则一起照搬。

| 原始部分 | 保留与优化 | 现行入口 |
|---|---|---|
| 角色优先 | 欲望、缺点、关系与选择；不把嘴硬逞强当标准人格 | [写作要求](../writing-natural/writing-requirements.md)、[人物](../writing-character/SKILL.md) |
| 心理差异 | 平静、抗拒、委屈、理性等可混合并波动；不固定类型 | [长期人物与关系](../writing-character/relationship-methods.md) |
| 身体描写 | 设定精确、正文按视角具体写；不每次重报术语 | [身体基础](../disability-foundation/SKILL.md)、[自然写作](../writing-natural/SKILL.md) |
| 生活与动作 | 穿衣、洗浴、购物、移动的资源和步骤；去掉统一动作和数值 | [日常方法](../writing-physicality/scene-methods.md) |
| 身体变化事件 | 选取事件前后与长期后果，后续目标不断线；不强迫完整事故史 | [故事方法](../writing-story/story-methods.md) |
| 假体与辅具 | 位置、能力与穿脱连续；休息或偏好即可主动取下 | [辅具](../assistive-devices/SKILL.md)、[场景方法](../writing-physicality/scene-methods.md) |
| 服装与残态 | 保留空衣物和设备轮廓的具体性，区分各类袜装 | [衣物支撑](../disability-foundation/clothing-topology.md) |
| 互动与调侃 | 普通争吵、双向照顾、默契与边界；不让每次互动变成尊重宣言 | [关系方法](../writing-character/relationship-methods.md) |
| 悲惨化、英雄化、工具化 | 人物可犯错、快乐、失败；不为正面形象抹去痛苦或审美 | [写作要求](../writing-natural/writing-requirements.md)、[质检](../quality-audit/SKILL.md) |
| 每图独立 | 每张提示词完整包含身份、身体、设备、服装、动作与画面约束；心理转可见表现 | [视觉技能](../visual-continuity/SKILL.md)、[独立提示词](../visual-continuity/prompt-template.md) |

## disable-skill-pack 的 17 个技能逐项吸收
以下 ID 均源于历史提交的 `archive/disable-skill-pack/skills/<ID>/`。没有将 17 个粗稿原封不动变成 17 个新技能；共用方法归入既有模块，具体写法进入按需参考文件。

| 旧技能 ID | 吸收的方法及现行落点 | 修订或不沿用 |
|---|---|---|
| amputee-agency | 具体任务中的选择、帮助范围与成本；[关系方法](../writing-character/relationship-methods.md) | 不默认拒绝一切好意，不强制能力考试 |
| amputee-daily-life | 日常微场景、衣物改造、携物、公共空间；[日常方法](../writing-physicality/scene-methods.md) | 不要求固定步数、数字或每次困难 |
| amputee-ensemble | 同任务对照、经验传递、不同资源；[关系方法](../writing-character/relationship-methods.md) | 不强制残疾类型不重复，不以年限排名 |
| amputee-romance | 照顾双向发生、细节记忆累积关系、已有默契；[关系方法](../writing-character/relationship-methods.md) | 不套自卑到接纳，不抹除身体吸引，不强制递减支撑训练 |
| gaze-layers-writing | 叙述观察、外人行为、当事人理解分层；[关系方法](../writing-character/relationship-methods.md) | 不强制三层同场、路人反应或当事人钝感 |
| aids-as-props | 功能／场景／审美选择，辅具的资源、私人用品和线索作用；[辅具](../assistive-devices/SKILL.md)、[故事方法](../writing-story/story-methods.md) | 不固定某侧拐不可替代、鞋跟上限或尊严象征 |
| prosthesis-fitting | 目标、试用、身体与任务反馈、后续选择；[场景方法](../writing-physicality/scene-methods.md) | 不强制试配失败或统一结构；数据不能否定主诉 |
| stump-care-prosthesis | 穿戴与适配分开、例行维护、异常影响后续安排；[场景方法](../writing-physicality/scene-methods.md) | 不照搬防护层顺序、红印计时、医疗处方或必然感染 |
| phantom-limb-writing | 感知与现实并行、注意力改变、幻肢感与痛区分；[场景方法](../writing-physicality/scene-methods.md) | 不当接纳进度条，不规定诱因、锤揉或恢复时限 |
| single-leg-anatomy | 保留结构到功能／衣物推导；[结构参考](../disability-foundation/structure-reference.md)、[经股专项](../amputation-transfemoral/SKILL.md) | 不混同髋离断与骨盆缺失，不统一坐姿或外观 |
| single-leg-mobility | 支撑、地形、楼梯、车内空间与设备位置；[动作技能](../writing-physicality/SKILL.md)、[移动参考](../disability-foundation/movement-reference.md) | 不固定单拐禁令、跳移时长或唯一动作序列 |
| single-leg-amputee-novel | 综合写作要求、语言／结构／认知复查、长期状态；[写作要求](../writing-natural/writing-requirements.md)、[动作技能](../writing-physicality/SKILL.md) | 不默认女性髋离断、强制配角比例、体面等级或禁词次数 |
| disability-opening-structures | 熟悉中的变化、结果在前、边界相遇三种可选结构；[故事方法](../writing-story/story-methods.md) | 不规定 300 字揭露身体或强制私密闯入 |
| disclosure-pacing | 事实／原因／代价／身份按需分层，知识与误解驱动释放；[故事方法](../writing-story/story-methods.md) | 不固定三层、三分之一位置或每个答案再生谜团 |
| disability-combat-compensation | 目标与空间决定动作，装置优势和限制可同源，经验提供线索；[故事方法](../writing-story/story-methods.md)、[组合专项](../combined-limb-loss/SKILL.md) | 不按残疾标签判胜负，不要求必攻弱点或凭步态精准诊断 |
| inverted-worldbuilding | 制度与审美进入商品、分工、空间和争论；交易规则服从设定；[故事方法](../writing-story/story-methods.md) | 不强制献祭、不可逆代价或全社会同声 |
| officialdom-subtext | 利益、承诺、文书与责任流转、物件与动作信号；[故事方法](../writing-story/story-methods.md) | 不删除所有纯信息句，不固定签字借车仪式或解码次数 |

包内总览、摘要与词汇表作为索引交叉核对；测试文件用来识别触发范围和反例，不继承旧通过率。综合 single-leg-amputee-novel 的拐杖、日常、HD 解剖、去 AI 风格与错误清单分别归入对应基础／动作／写作模块，不把错误清单的每条绝对禁令原样提升为现行标准。

## 如何提炼
身体结构、功能、即时状态与个人经验分开。采用“任务—可用资源—选择—结果”的动作方法，保留细致感官与审美描写；不把每一笔观察强制解释成剧情功能。
帮助、凝视、恋爱、公开身体、移动方式均可因人物与场合不同而变化。旧素材中的触摸残肢、藏拐、试配失败、签字借车等只在情节需要时选用。
小说里重复出现的现象不因此成为医学证据；旧测试中的路由命中率也不是文章或图像质量成绩。
新增六组写作对照与四组提示词是原创教学示例，明确其局部人物设定，不继承旧文本的固定腔调。

## 专业事实的支持与边界
核查日期：2026-09-06。以下材料支持限定范围的描述，不用来推出所有人的功能、护理参数或剧情结果。

- [AAOS：拐杖、手杖与助行器](https://www.orthoinfo.org/recovery/how-to-use-crutches-canes-and-walkers?webid=2FDEE455)：腋拐常规承重通过手，不以腋窝压住腋托承担重量。该页面不能证明所有截肢者必须使用同一支数、步态或持侧。
- [Moorfields：面对眼球失去](https://www.moorfields.nhs.uk/for-patients/artificial-eye-creation-and-fitting/coping-with-eye-loss)：区分眼球摘除与眼内容剜除，区分植入物及其外面的壳状义眼。不能从“义眼”一词推定所有人的手术史。
- [Moorfields：人工眼资料](https://moorfields.ae/wp-content/uploads/2020/07/Artificial-eye-English.pdf)：盲眼不一定要摘除才可配外观假体；运动表现受具体条件限制。此处仅支持装置与天然结构不能互相推断。
- [Amputee Coalition：疼痛类型](https://amputee-coalition.org/resources/introduction-to-managing-pain-fs/)：区分残肢痛、幻肢感觉与幻肢痛。不将幻痛直接当作心理接纳程度或角色成长进度。

具体器械新能力、皮肤问题、临床参数与复杂术后外观如需进入创作，应另查相应机构或制造商资料。没有必要时保持描述性中性，不把创作技能扩成处方手册。
