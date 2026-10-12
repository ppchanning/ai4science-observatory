[English](remote-lab-access.md) \| **简体中文**

# 如何让 AI Agent 接入远程实验室

**更新：2026-10-12 · 类型：有来源的实践指南 · 示例不是本资料库的实测结果。**

## 快速回答

远程实验室适合 Agent 的前提是：有获准使用的动作接口，并返回可识别来源的实验结果。浏览器操作、API 接入和自主实验闭环是不同能力，需要分别核查。

目前仓库的远程实验目录只有 **1 条平台证据记录**：LabsLand Electronics Hive。下面的两个化学案例属于研究示范，不是新增的已核实公共接入设施。本指南是小规模的证据入口，不是完整实验室大全。

## 区分执行场景

| 场景 | 动作由谁执行 | 结果能说明什么 |
| --- | --- | --- |
| 真实远程实验室 | 实际仪器与硬件 | 特定设备和配置中的测量 |
| 数字仿真 | 程序或学习到的转移模型 | 仿真假设下的行为 |
| 科学桌面软件 | 计算机上的科学软件 | 软件或计算操作；物理执行另需证据 |

照片有助于识别设备，但不能单独证明数据完整性。实验室风格的界面也不会把模拟结果变成物理测量。

## 有原始来源的入口

| 入口 | 已有证据 | 接入或自动化边界 |
| --- | --- | --- |
| [LabsLand Electronics Hive](https://labsland.com/en/labs/electronics-hive/) | 官方文档介绍继电器连接真实元件、通过浏览器进行仪器测量 | 当前资格、费用及自动化权限需确认；本指南未证实自主 Agent 成绩 |
| [Coscientist](https://www.nature.com/articles/s41586-023-06792-0) | 连接规划、文档与实验操作的已发表化学示范 | 研究特定设备和集成，不代表通用公开 Agent 接口 |
| [ChemCrow](https://www.nature.com/articles/s42256-024-00832-8) | 化学工具辅助案例，包含物理合成 | 示范所用服务与公开工具子集有区别；未核查当前服务权限 |

Hive 平台页和[测量说明](https://labsland.com/pub/docs/experiments/hive/user/en/taking_measurements.html) 于 2026-10-12 核查。[remote-labs.json](../data/remote-labs.json) 中较早的详细观察保留原核查日期，历史延迟不能当作当前排队或响应保证。

## 接入前核查 6 项

1. **设备：** 真实硬件、软件还是仿真，以及支持的参数范围。
2. **资格：** 账户、预约、费用及设施允许的自动化方式；未确认项标为未知。
3. **动作：** 输入、单位、校验、执行状态和错误；分清配置准备与实验启动。
4. **测量：** 返回文件、单位、时间、校准信息，以及平台实际提供的运行或设备标识。
5. **恢复：** 请求延迟或失败怎样处理，如何避免意外重复执行。
6. **试验：** 按获准流程完成一个小任务，用预期范围或参考值核查产物。

这是资料库的接入建议，不代表每个平台都已提供所有字段。

## 可用的实验记录

```json
{
  "platform": "identified facility",
  "execution_setting": "physical_remote_lab",
  "run_id": null,
  "action_parameters_with_units": {},
  "measurement_artifact": null,
  "apparatus_identifier": null,
  "source_url": null,
  "automation_permission": "unknown"
}
```

这是空白来源模板。缺失字段保持未知；失败请求和界面预览不能计作完成实验。人工浏览器流程不等于公开自动化 API。

## 继续阅读

查看[平台证据笔记](../resources/remote-labs.md)、[科研 Agent 选型](scientific-agent-selection.zh-CN.md)和[证据复用](evidence-and-data-reuse.zh-CN.md)。接入与接口描述引用设施文档，科研结果引用原论文。

## 原始来源

- `labsland-hive` — [LabsLand Electronics Hive](https://labsland.com/en/labs/electronics-hive/) · official-platform-documentation · Summary; Access options; Internal Operation
- `hive-measurement` — [Hive user guide: Taking measurements](https://labsland.com/pub/docs/experiments/hive/user/en/taking_measurements.html) · official-platform-documentation · Taking measurements
- `coscientist` — [Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0) · peer-reviewed-paper · Main: six demonstrated tasks; Coscientist system architecture
- `chemcrow` — [Augmenting large language models with chemistry tools](https://www.nature.com/articles/s42256-024-00832-8) · peer-reviewed-paper · Results and discussion; Code availability

核查日期为 2026-10-12。核查支持文中限定范围的描述，不代表独立复现；可机器读取的记录见 [guide-sources.json](../data/guide-sources.json)。
