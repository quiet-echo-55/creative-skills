# 统一状态卡

```yaml
CHARACTER_ID:
LOCKED:
  BODY_STATE:
    STRUCTURE:
      # 每一侧/每个部位分别记录；功能受限不等于结构缺失
      side:
      present_segments:
      absent_segments:
      joints_present:
      endpoint:
    FUNCTION:
      motor:
      weight_bearing:
      grip_or_fine_control:
      range_of_motion:
  SENSATION_PROFILE:
  VISION_BASELINE:
    left:
      globe_structure:  # intact / altered_or_partially_retained / absent / unknown
      vision:
      ocular_device:
    right:
      globe_structure:  # intact / altered_or_partially_retained / absent / unknown
      vision:
      ocular_device:
  PROSTHESIS_CAPABILITIES:
  TASK_SKILLS:
  CHARACTER_PROFILE:
  HABIT_PROFILE:
  VISUAL_INVARIANTS:
  WORLD_EXCEPTION:
SCENE:
  PROSTHESIS_STATE:
  AID_STATE:
  MOBILITY_MODE:
  SUPPORT_POINTS:
  HAND_OCCUPANCY:
  CLOTHING_STATE:
  POSITION_STATE:
  ENVIRONMENT_STATE:
  FATIGUE_OR_DISCOMFORT:
```

## 使用规则

- `STRUCTURE` 回答“身体还在不在、到哪里”；`FUNCTION` 回答“此刻/长期能做什么”。两者禁止互相替代。
- 不相关或用户未提供的字段留空，不为了把 YAML 填满而发明诊断。
- `TASK_SKILLS` 按任务登记，例如：平地假肢步行 B、下楼 C、无假肢床边转移 A；不要用“截肢几年”替代任务熟练度。
- `CLOTHING_STATE` 建议同时记录衣物通道由天然肢体、残肢、假肢还是空气支撑。
- `globe_structure` 不是布尔值：完整存在、结构改变/部分保留、整体缺失和未知分别记录；必要时附说明，不让“眼球存在/缺失”掩盖不同手术与美容义眼片的差异。
- `ocular_device` 记录当前外观装置、义眼片或外部义眼等相关状态；它与天然眼球结构和视觉能力分开。
- `LOCKED` 表示无事件时不漂移，不代表人物永远不能训练、康复或改变偏好。有依据的长期变化应同步更新。
