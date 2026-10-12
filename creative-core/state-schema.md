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
      correction_baseline:  # 可选：近视等已知状态及矫正后能力
      ocular_device:
    right:
      globe_structure:  # intact / altered_or_partially_retained / absent / unknown
      vision:
      correction_baseline:
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
- 高度近视若已设定，按每只仍有视觉的眼睛记录；眼镜戴上、摘下、损坏或放在何处属于 `SCENE.AID_STATE`，当前能看清什么按已知设定与场景推导。
- `LOCKED` 表示无事件时不漂移，不代表人物永远不能训练、康复或改变偏好。有依据的长期变化应同步更新。

## 可选的作品取向

长篇或多图任务可在角色卡之外简记读者关注、描写浓度与本场视角，只记录用户已给的值及明确采用的创作选择。它不是身体事实，也不是所有角色共享的偏好。例：读者关注衣料与轮廓；本场人物为了舒适穿假肢；伴侣仍偏爱未穿时的形态。这三项可以同时成立。短任务不必建卡或输出表格。

## 3.0 可选事件小卡（不修改原有 LOCKED/SCENE 字段）

长篇出现任务卡住或设备失效时，内部可附加：`EVENT_ID / CURRENT_TASK / RESOURCE_GAP / ATTEMPT / DEVICE_FUNCTION_LOST / DEVICE_LOCATION / RESULT / OPEN_CONSEQUENCE`。其中装置实际能力仍以 `PROSTHESIS_CAPABILITIES` 为准、装置穿戴位置仍属于 `SCENE`；这张卡只记录事件因果，事件结束可归档，不是新增一个互相冲突的身体真相源。

作品的 `AUDIENCE_FOCUS / ATTENTION_DENSITY` 放在可选作品取向里，不按慕残类型推断人物性格。下次续写优先从未解决的装置位置、任务与结果接续，不让一次事故抹除既有 `TASK_SKILLS`。
