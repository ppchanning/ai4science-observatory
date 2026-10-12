[English](scientific-agent-selection.md) | **简体中文**

# 如何选择科研 Agent：文献、代码、工具与实验

**更新：2026-10-12 · 类型：有来源的实践指南 · 示例不是本资料库的实测结果。**

## 快速回答

按**需要交付什么，以及用什么证据验证它**来选择科研 Agent。文献回答需要可追溯段落；计算实验需要可运行代码和结果记录；物理实验需要来自明确仪器的测量。流畅的研究叙述本身不能证明这些能力。

下面比较 4 类代表方案，供选型参考。项目描述依据原始来源，于 2026-10-12 核查；本资料库未独立运行这些系统，也不提供统一性能排名。

## 按任务比较

| 需求 | 代表入口 | 来源支持的能力 | 选择前核查 |
| --- | --- | --- | --- |
| 用科学文献回答问题 | [PaperQA](https://github.com/Future-House/paper-qa) | 带引用的科学文档检索问答 | 文献覆盖、引用段落、模型依赖、文档使用权 |
| 探索计算研究想法 | [The AI Scientist](https://sakana.ai/ai-scientist/) | 作者介绍的想法、代码、计算实验与报告流程 | 可运行产物、实验对照、资源预算、失败案例 |
| 将规划连接到实验操作 | [Coscientist](https://www.nature.com/articles/s41586-023-06792-0) | 结合工具使用与自动实验的化学研究示范 | 原文中的设备和集成条件能否在你的场景复用 |
| 结合化学推理与领域工具 | [ChemCrow](https://www.nature.com/articles/s42256-024-00832-8) | 化学工具增强任务；公开实现包含论文工具的一个子集 | 论文系统与公开版本的区别、所需服务权限 |

各项目的任务和评测不同，分数不能拼成共同排行榜。论文展示硬件实验，也不代表读者今天能接入相关设备。

## 实际选型步骤

1. **写清交付物。** 例如：有来源的文献答案、复现的数值结果、测得的电路响应，并明确产物文件或测量要求。
2. **列出已有接口。** 文档、Python、图形软件和实验室 API 的要求不同；记录权限要求，不公开凭据。
3. **先定义验证方式。** 对应原文段落、测试、基线对照或测量来源。
4. **试一个有边界的任务。** 保留输入、版本、调用、产物、成本和错误，加入一个已知失败或缺输入的案例。
5. **在证据范围内判断。** 文献综合成功后，代码执行和物理实验能力仍需单独验证。

## 可复用的选型记录

下面是空白比较模板，不是实测结果或项目评分。`null` 表示未知。

```json
{
  "task": "answer a scientific question with source passages",
  "required_artifact": "answer plus source URLs and passage locations",
  "execution_setting": "literature",
  "required_interfaces": ["document retrieval"],
  "verifier": "check each claim against the cited passage",
  "tested_project_version": null,
  "observed_result": null,
  "access_conditions": null
}
```

## 在资料库继续找证据

[guide-resources.json](../data/guide-resources.json) 提供这 4 个例子的结构化记录及来源标识。[论文书目](../data/papers.json) 包含科学软件操作和远程实验资料；通过 `appearances` 找阅读笔记，再打开原始来源核查科研结论。

物理接入继续读[远程实验室接入](remote-lab-access.zh-CN.md)；证据整理读[证据判断与数据复用](evidence-and-data-reuse.zh-CN.md)。

## 尚未确认的事项

本指南不确认当前成本、接入资格、安装成功或跨领域表现。应核查最新项目文档，测试目标任务，并区分作者报告与资料库的选型建议。

## 原始来源

- `paperqa` — [PaperQA: scientific document question answering](https://github.com/Future-House/paper-qa) · official-project-documentation · README: overview, citations and configuration
- `ai-scientist` — [The AI Scientist](https://sakana.ai/ai-scientist/) · official-project-report · Overview of the computational research workflow; limitations
- `coscientist` — [Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0) · peer-reviewed-paper · Main: six demonstrated tasks; Coscientist system architecture
- `chemcrow` — [Augmenting large language models with chemistry tools](https://www.nature.com/articles/s42256-024-00832-8) · peer-reviewed-paper · Results and discussion; Code availability

核查日期为 2026-10-12。核查支持文中限定范围的描述，不代表独立复现；可机器读取的记录见 [guide-sources.json](../data/guide-sources.json)。
