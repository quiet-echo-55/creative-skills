# Creative Skills 3.0 设计、收敛与验收说明

## 版本基线

此交付以 2026-10-08 的 `creative-skills-2.3.patch`（其头部注明基于 2.2 主线）为内容基础，整合此前的身体资源、装置事件、动态残态与长篇因果建议。发布目标是源仓库 **2.2 主线**；如目标仓库已包含 2.3 修改，需使用单独的 2.3→3.0 增量文件，避免重复应用。

## 主规则唯一归属

| 事项 | 唯一权威源 | 其他模块只做什么 |
|---|---|---|
| 身体结构、结构与功能分离、衣物拓扑 | `disability-foundation` | 各自引入，不复制整段术语 |
| SAK/SAE/OOE/LBK 等别名与层级 | `amputation-type-registry.md` | 只按类型路由和检查 |
| 动作、承重、手占用与任务可行性 | `writing-physicality` | Natural 只选正文中的观察细节 |
| 设备能力、可及位置、故障/遗失 | `assistive-devices` | Core 保存状态，Story 使用后果 |
| 身体审美与动态残态表达 | `writing-natural/body-attention-methods.md` | Character 不重复形态技巧 |
| 受众关注、视角关系、人物意愿 | `writing-character/devotee-audience.md` | Natural 落到可见细节 |
| 长篇因果与章节持续性 | `writing-story` | Audit 只检查结果 |
| 输出验收 | `quality-audit` | 不另设硬性配额 |

## 收敛策略

1. 不新建根 Skill，不将 LBK、RBK、DAK、OOE 的每种排列扩成独立模块。
2. 保留已有 2.3 原创例集与研究作为按需素材；它们不是每次运行的必读文件。
3. 把原本拟新增的 `embodied-state-methods.md` 融入 `body-attention-methods.md`，把 `difficulty-arc.md` 融入 `story-methods.md`，减少重复参考入口。
4. 不删除原有本地用例和 2.3 回归测试；新测试与其叠加，而不是替换检验标准。
5. 旧 2.2 文档中提到的历史前缀与先前版本号可以作为发行史留存；13 份 `SKILL.md` frontmatter 和 MANIFEST 必须一致为 3.0.0。

## 验收与边界

- 语法：`git apply --check`，检查目标仓库版本与补丁适用性。
- 仓库结构：`python scripts/validate_repo.py && python scripts/test_validate_repo.py && python scripts/validate_release.py`。
- 生成质量：按 `tests/v3-regression.json` 的案例执行实际模型任务，审查对比输出，不将 JSON 用例或静态校验误报为模型已全部通过。
- 医学/康复细节：本项目是创作参考，不替代临床来源；复杂器械具体故障和病理诊断要基于人物设定及可验证资料。

## 故障与困难叙事的平衡

希望保留残态、窘迫、独腿跳移、单手操作、瘫痪转移等身体事实，但拒绝把任何类型残疾固定成一套必然心理状态、意外事故或被动求助方式。可高浓度描述身体形态、丝袜、空袖、外部义眼与吸引，也可完全聚焦于非身体矛盾；决定权属于用户任务和小说既有因果。
