# Naming migration

v2.0 removes the `mem-` runtime prefix and opaque SAK / SAE / OOE directory names from active Skills.
The new names describe purpose directly and use kebab-case consistently.

| Legacy ID / directory | v2.0 active name |
|---|---|
| `mem-creative-core` | `creative-core` |
| `mem-disability-foundation` | `disability-foundation` |
| `mem-write-natural` | `writing-natural` |
| `mem-write-physicality` | `writing-physicality` |
| `mem-write-character` | `writing-character` |
| `mem-write-story` | `writing-story` |
| `mem-visual-continuity` | `visual-continuity` |
| `mem-aids-prosthetics` | `assistive-devices` |
| `mem-sak` | `amputation-transfemoral` |
| `mem-sae` | `amputation-transhumeral` |
| `mem-ooe` | `combined-limb-loss` |
| `mem-ocular` | `ocular-loss` |
| `mem-quality-audit` | `quality-audit` |

## Archive naming

2.1 的 archive 文件名仅作为历史路径保留在来源记录中；2.2 post-release cleanup 后当前发布树不含 archive。历史目录包括 MEM-Base、skill-SAK-v2、skill-SAE-v2、skill-OOE-v2、skill-义眼-v2，另有历史整理目录与占位材料。旧说明中的重命名计划不等于当前树仍有这些目录；以 [实际来源映射](SOURCES-AND-DESIGN.md) 为准。

SAK／SAE／OOE 可出现在历史材料中，现役目录与 MANIFEST 仍使用上表语义化名称。OOE 在本仓库指上下肢组合，不是双上肢缺失。
