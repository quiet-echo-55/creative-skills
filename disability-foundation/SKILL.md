---
name: disability-foundation
version: 2.2.0
description: 通用身体差异与残疾创作基础层。用于肢体缺失、残肢、肢体仍在但瘫痪/无力/活动受限、视觉缺失、假肢/义眼/辅具、空袖/空裤腿/袜筒、丝袜/裤袜以及跳跃、爬行、跛行、转移等跨写作与视觉任务。核心规则是结构存在与功能能力分离，再由当前任务推导动作和服装拓扑；不替用户决定具体诊断、截肢层级或人格。
---

# Disability Foundation

## 1. 任务

本 Skill 是所有身体差异任务的通用底层。它负责四件事：

1. 区分**身体结构是否存在**与**该结构能否完成任务**；
2. 把残肢、假肢、辅具、衣物和动作放进同一状态链；
3. 给没有专项 Skill 的身体状态一个安全的通用表示；
4. 为 Write Physicality / Visual / Audit 提供共享不变量。

它不从“残疾”这个词自动推断截肢、瘫痪、失明原因、疼痛、心理反应或器械选择。

## 2. 第一硬规则：PRESENCE ≠ FUNCTION

任何身体部位都分开问：

- `PRESENCE`：天然结构是否存在、保留到哪里；
- `FUNCTION`：主动运动、承重、抓握、感觉、视觉等能力如何。

因此：

- **双腿存在但完全瘫痪**：两条腿仍然支撑裤腿、丝袜和裤袜轮廓；不能因为“不走路”画成空裤腿。
- **一只眼存在但失明/浑浊**：眼球仍在；不能自动改成眼球缺失、义眼或空眼窝。
- **一条手臂存在但无力/挛缩/活动受限**：袖子仍有实体支撑；动作能力另行判断。
- **先天肢体差异**：不能自动补“手术后残肢、疤痕、幻肢”等后天截肢叙事。

当用户只给功能标签、没有给结构事实时，保持结构未知，不擅自删除身体部位。

## 3. 通用状态最小集

### LOCKED

- `BODY_STATE.STRUCTURE`：side / present_segments / absent_segments / joints_present / endpoint；
- `BODY_STATE.FUNCTION`：motor / weight_bearing / grip / range_of_motion / task-specific capacity；
- `SENSATION_PROFILE`：normal / reduced / absent / hypersensitive / phantom（只有设定存在时）；
- `VISION_BASELINE`：每只眼分别登记 globe presence 与 vision；
- `PROSTHESIS_CAPABILITIES`；
- `TASK_SKILLS`；
- `HABIT_PROFILE`；
- `VISUAL_INVARIANTS`；
- `WORLD_EXCEPTION`。

### SCENE

- `PROSTHESIS_STATE`；
- `AID_STATE`；
- `MOBILITY_MODE`；
- `SUPPORT_POINTS`；
- `HAND_OCCUPANCY`；
- `CLOTHING_STATE`；
- `POSITION_STATE`；
- `ENVIRONMENT_STATE`；
- `FATIGUE_OR_DISCOMFORT`。

不需要每次向用户展示全部字段；它们首先用于内部保持连续性。

## 4. 残肢与缺失部位

描写时先确认：

1. 保留什么天然结构；
2. 缺失从哪里开始；
3. 当前残肢/缺失侧被什么覆盖；
4. 当前动作是否真的调用这个身体事实。

`残肢` 指保留下来的身体段，`残端` 只是最远端区域。残肢长度、形状、疤痕、皮肤、敏感度、幻肢感与是否能压/夹/顶物体都是个体变量，不自动添加。

避免反复用“残缺、残破、不完整”替代具体结构；也不要为了提醒读者而每章固定揉残肢、摸断臂或整理空袖。

## 5. 衣物拓扑

对每个袖管、裤腿、袜筒先标记它由什么支撑：

- `ANATOMICAL_SUPPORT`：天然肢体；
- `RESIDUAL_SUPPORT`：残肢只支撑到自身终点；
- `PROSTHETIC_SUPPORT`：假肢/义肢支撑；
- `UNSUPPORTED`：真正空置，按重力/风/动作形成褶皱；
- `MODIFIED`：折起、卷起、塞入、固定、剪短或定制服装。

特别规则：

- 长袖/裤腿在残肢范围内仍有体积，空置从残肢末端以后开始；
- 裤袜/tights 是共享腰胯 + 两条腿筒的一件衣物，缺失侧腿筒要明确是覆盖残肢后空置、折入/固定、改短，还是被假肢撑起；
- 过膝袜/长筒袜/独立丝袜本来就是左右独立，可只穿一只；不要与连裤袜混为一谈；
- 完整但瘫痪的腿仍把裤袜和裤腿撑成完整轮廓；
- 假肢穿在衣物里面时，接受腔、人工关节、支柱、假脚可能改变轮廓；
- 鞋是否穿在假脚/末端上取决于该装置结构，不按“天然脚数量”简单计数。

详见 `clothing-topology.md`。

## 6. 动作类型先分类，再描写

不要把所有非标准移动都写成“艰难地走”。先区分：

- 天然/假肢参与的步行；
- 步态不对称/跛行；
- 单腿连续跳移；
- 几步短跳转移；
- 拐杖/助行器支撑移动；
- 扶墙/家具挪动；
- 轮椅移动；
- 坐姿挪动；
- 爬行/跪行/地面移动；
- 他人协助；
- 世界观移动。

“一瘸一拐”是步态结果，不是“少一条腿”的默认同义词。爬行也不是一个抽象标签：要知道手、膝、残肢、前臂或其他接触面到底在哪里。

详见 `movement-reference.md`，具体动作链交给 `writing-physicality`。

## 7. 器械与假体

按当前任务需要检查器械信息，未知且无关的项目不补填：`STATE / LOCATION / CONTROL / SUPPORT / HAND_COST / TASK_FIT / MAINTENANCE / FAILURE`。

不要因“高级”“仿生”“魔法”自动获得天然肢体全部功能。简单棍腿/刚性支柱也要明确有没有人工膝、末端是什么、坐姿时是否需要取下或改变位置；不存在的关节不能为了画面好看自动弯曲。

具体器械交给 `assistive-devices`。

## 8. 人物纪律

身体差异会影响动作和资源，但不自动决定：

- 性格；
- 自尊；
- 是否自嘲；
- 是否喜欢展示残肢；
- 是否使用假肢/轮椅；
- 是否拒绝帮助；
- 恋爱态度；
- 战斗力；
- 痛苦程度。

人物可以拥有这些特质，但来源必须是角色设定和剧情，而不是“残疾人默认值”。

## 9. 与专项的关系

- Foundation 定义共用语义；
- `amputation-transfemoral` / `amputation-transhumeral` / `combined-limb-loss` / `ocular-loss` 给命中范围更精确的结构边界；
- 用户已经锁定的事实永远高于专项默认；
- 没有专项时继续使用 Foundation，不要为了套模块擅自改身体状态。
