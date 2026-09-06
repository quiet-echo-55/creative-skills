# 2.2 收尾审阅记录

本轮基于用户提供的完整 2.1 ZIP 工作。输入 ZIP SHA256：`3eda17d2668e4881719c2a0c37a6366289421969c59bf0a6da031bcc1d10177d`。

本文记录的是 archive 删除前的 2.2 构建收尾状态；随后进行 post-release cleanup，历史 `archive/` 已从 main 移除。下文涉及“真实 archive 来源保留”的表述，均指当时的构建树，不代表当前发布树仍含这些文件。

本轮不重写 2.1 的主体技能，只处理发布层面的最后不一致，并把此前审阅完成但未进入压缩包的蒸馏回归真正落库：

- 删除 `archive/legacy/` 的 54 个 synthetic `PLACEHOLDER::...` 镜像；真实 archive 来源保留。
- 将上传 ZIP 中被转义的历史目录名规范回 `archive/skill-义眼-v2/`，与历史路径和文档一致。
- 增加 `docs/DISTILLATION-AUDIT.md` 与 `tests/distillation-regression.json`，明确哪些旧语料只能作为方法或案例，不能升级成通用硬规则。
- 重写 `archive/README.md`，使目录说明与实际仓库一致；真实历史文件本身不因品牌清理而改写。
- 现役 `creative-core`、`quality-audit` 等不再使用私人项目品牌措辞。
- 现役 Skill、辅助文件和测试不再依赖 `SAK/SAE/OOE` 这类旧运行时简称，改用语义化模块名或明确结构描述。
- 眼部状态使用 `GLOBE_STRUCTURE + VISION + OCULAR_DEVICE`，避免 `globe_present` 名称暗示布尔值，也避免把失明、结构缺失和外观装置混成一件事。
- 修正视觉技能“摘除假肢”为“取下假肢”。
- 新增 release hygiene 校验，并让 CI 运行 `validate_repo.py`、`test_validate_repo.py`、`validate_release.py` 三项检查。
- 全部 13 个现役 Skill frontmatter 与 `MANIFEST.json` 统一升至 2.2.0。

本记录是仓库结构、来源边界和规则一致性的收尾审查，不宣称进行了新的文学模型 A/B 或图像模型通过率实验。仓库中的行为案例仍是验收规范，而不是伪造的模型成绩。
