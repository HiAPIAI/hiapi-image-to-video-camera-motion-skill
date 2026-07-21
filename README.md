# hiapi-image-to-video-camera-motion-skill

一个兼容 Codex 与 Claude Code 的专业图生视频运镜 Skill。它会先判断静态图片能够安全支持多大幅度的镜头运动，再根据画面主体、商业目标和模型能力，设计推拉摇移、升降、环绕、跟拍、微距滑动等镜头，并输出可直接交给图生视频模型使用的提示词与结构化运动方案。

## 平台兼容性

核心能力采用通用的 `SKILL.md + references + scripts` 目录结构，Codex 和 Claude Code 均可读取同一套技能文件，无需维护平台专用副本。

| 平台 | 安装位置 | 显式调用方式 |
| --- | --- | --- |
| Codex | `$CODEX_HOME/skills/image-to-video-director/`，未设置时通常为 `~/.codex/skills/image-to-video-director/` | `$image-to-video-director` |
| Claude Code（个人） | `~/.claude/skills/image-to-video-director/` | `/image-to-video-director` |
| Claude Code（项目） | `<项目目录>/.claude/skills/image-to-video-director/` | `/image-to-video-director` |

Claude Code 会使用 `SKILL.md`、`references/` 和 `scripts/`。`agents/openai.yaml` 仅用于 Codex 的技能列表与默认提示界面，Claude Code 会忽略该文件，不影响技能执行。两个平台也都可以根据 `SKILL.md` 中的描述，在符合场景时自动选择该技能。

## 核心能力

- 识别产品、人物、建筑、界面、食物、环境等主体类型，并确认所需素材与制作路径。
- 分析景深、遮挡、边缘余量、刚性结构、文字和身份一致性等风险。
- 区分平移、旋转、变焦、环绕和跟拍，控制运动幅度、速度、节奏与结束画面。
- 根据不同模型的实际能力适配提示词、负面提示词、时长、画幅和相机控制参数。
- 对生成结果进行身份、几何、运动连续性、焦点和收尾质量检查，并给出修正方案。
- 通过确定性的 Python 校验器检查运动计划结构和常见高风险组合。

## 适用场景

- 电商产品展示和品牌广告镜头
- 人像、角色或时尚素材的轻量动态化
- 建筑、室内与风景图片的空间展示
- 食品、美妆、珠宝等细节特写
- 网站和软件界面的确定性平移、缩放或合成方案
- 已生成图生视频结果的失真诊断与提示词修复

## 工作方式

Skill 默认遵循以下流程：

1. 识别主体类型、证据、所需素材和建议制作路径，并等待用户确认。
2. 检查源图能否支撑目标运镜，确定最大安全运动幅度。
3. 明确镜头目的，选择一个主导运动并设计起止画面。
4. 输出中文导演说明、英文模型提示词和结构化运动计划。
5. 在存在已授权生成工具时适配模型、生成视频并进行视觉质检。

对于单张图片无法可靠重建的内容，Skill 会主动降低运动幅度。例如，将 360 度环绕改为小角度弧线移动，或建议补充多视角素材，而不是用提示词强行生成不可见表面。

## 安装

将整个仓库克隆或复制到对应平台的技能目录，并确保目录名为 `image-to-video-director`。安装后重新启动会话，使平台重新发现技能。

Codex 个人安装示例：

```bash
git clone https://github.com/HiAPIAI/hiapi-image-to-video-camera-motion-skill.git ~/.codex/skills/image-to-video-director
```

Claude Code 个人安装示例：

```bash
git clone https://github.com/HiAPIAI/hiapi-image-to-video-camera-motion-skill.git ~/.claude/skills/image-to-video-director
```

Claude Code 项目级安装时，将目标目录改为当前项目下的 `.claude/skills/image-to-video-director`。项目级技能可随项目提交并由团队共享。

运行 `scripts/validate_motion_plan.py` 需要 Python 3.9 或更高版本。

## 使用示例

在 Codex 中可通过 `$image-to-video-director` 显式调用：

```text
使用 $image-to-video-director 分析这张产品图，设计一个 5 秒的缓慢推近镜头，保持包装文字和 Logo 不变。
```

```text
使用 $image-to-video-director 检查这段图生视频为什么人物面部和背景在环绕时变形，并给出更稳妥的重做方案。
```

在 Claude Code 中使用 `/image-to-video-director`：

```text
/image-to-video-director 分析这张建筑图片，设计一个安全的小幅向右弧线运镜，并输出模型可用的英文提示词。
```

## 目录结构

```text
.
├── SKILL.md                         # Skill 入口、工作流与输出契约
├── agents/openai.yaml               # Codex 界面元数据，Claude Code 可忽略
├── references/                      # 运镜、源图分析、模型路由与质检资料
└── scripts/validate_motion_plan.py  # 结构化运动计划校验器
```

## 校验运动计划

将结构化计划保存为 JSON 后运行：

```bash
python scripts/validate_motion_plan.py plan.json
```

严格模式会把警告也视为失败：

```bash
python scripts/validate_motion_plan.py plan.json --strict
```

校验器负责检查字段完整性和高风险运镜组合，不能替代模型参数校验或对实际视频的视觉审查。

## 设计原则

- 一条短视频只保留一个主导镜头运动。
- 优先保护主体身份、产品结构、文字、Logo、光线和空间关系。
- 把大幅平移与环绕视为重建任务，而不是普通风格词。
- 优先生成保守基线，每次只改变一个变量。
- 没有生成或检查工具时，不声称已经生成或通过视觉验收。
