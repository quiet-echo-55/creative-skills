# Changelog

## 2.2.0 — 2026-09-06
- 在用户提供的完整 2.1 ZIP 上完成发布收尾，不再依赖残缺的中间包。
- 删除 `archive/legacy/` 的 54 个 synthetic placeholder 镜像；146 个真实 archive 文件继续保留，并规范历史义眼目录名。
- 补入蒸馏审计与 18 例回归，阻止小说语料中的固定数值、动作公式、人格倾向和剧情模板重新变成现役硬规则。
- 清理现役私人品牌措辞及 SAK/SAE/OOE 旧运行时简称，统一使用语义化模块名和明确结构描述。
- 眼部状态统一为 `GLOBE_STRUCTURE + VISION + OCULAR_DEVICE`，分开天然结构、视觉能力与外观装置。
- 修正视觉模块“摘除假肢”措辞为“取下假肢”。
- 新增 `scripts/validate_release.py`；GitHub Actions 运行三项校验。
- `MANIFEST.json` 与 13 个现役 Skill 统一升至 2.2.0。
- Post-release cleanup: archive was subsequently removed from main; provenance remains in `docs/`.

## 2.1.0 — 2026-09-06
- 二次吸收 write-rule 与 disable-skill-pack：集中写作要求，补充日常／感知、关系／经验传递、故事／信息释放方法与例句，逐项记录 17 个旧技能的现行落点。
- 绘图提示词每张独立完整；来源文档不依赖本地存档，自检增加排除 archive 的完整副本验证，用户可以自行移除 archive。
- 恢复六个占位技能，13 个本地测试均补齐行为案例；保留现行目录与 ID。
- 新增六组原创写作对照和四组通用中文提示词；默认细致自然、默认提示词交付。
- 统一状态命名，澄清事实与事件优先关系，补齐眼部装置区分及辅具承重边界。
- 移除当前工作流中的固定动作配额和必需报表，审美细节不必附带励志或接纳叙事。
- 修正现行文档的历史路径与原作可用性说明；archive 原样保留。
- 加强标准库校验与回归自检；教学例集、静态校验和实际模型效果分别记录。

## 历史变更记录
以下保留此前版本记录的原文。旧记录中原始 ZIP 与目录迁移的说法不代表当前文件实际存在，实际范围以 [来源说明](docs/SOURCES-AND-DESIGN.md) 为准。

# Changelog

## 2.0.0

- 新增 `disability-foundation`，把结构存在、功能能力、感觉/视觉和场景状态拆开记录。
- 新增通用肢体缺失/肢体仍在但功能受限/视觉状态区分，避免“瘫痪 = 空裤腿”“失明 = 空眼窝”等结构错误。
- 扩展残肢、残端、义肢、简单棍腿/刚性支柱、义手、义眼、拐杖、助行器、轮椅、转移工具的创作边界。
- 扩展空袖、空裤腿、袜/丝袜/裤袜/leggings 与假肢共同作用时的服装拓扑。
- 扩展单腿跳、短跳转移、爬行/地面移动、轮椅移动、扶物移动、步态不对称等动作分类，并明确“跛行/一瘸一拐”不是所有单腿状态的默认同义词。
- `ocular-loss` 增加“眼球存在但失明/浑浊”与“眼球缺失/义眼”的硬区分。
- `quality-audit` 修复“最终 12 问实际有 14 项”的编号问题，并扩展为 18 项跨模块检查。
- `MEM-Base`、SAK/SAE/OOE/义眼 V2 旧包归档到 `archive/legacy/`；原始 `cangjie-skill-pack.zip` 移到 `archive/source-packs/`。
- `ROUTING-CHEATSHEET.md` 与 `SOURCES-AND-DESIGN.md` 移入 `docs/`。
- 新增 `scripts/validate_repo.py`、CI 工作流和 `tests/disability-regression.json`。
