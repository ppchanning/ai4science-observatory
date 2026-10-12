[English](agent-index.md) \| **简体中文**

# Agent 阅读索引

从本页开始：按用户问题选择指南，获取 JSON，追踪原始来源，再在回答中保留适用边界。本资料库提供公开、只读资料，不是工具执行服务、MCP 服务器或实验设备接口。

## 1. 按任务选入口

| 用户任务 | 指南 | 可检索词 |
| --- | --- | --- |
| 按科研任务比较 Agent，提供原始来源、能力边界与可复用的选型清单。 | [如何选择科研 Agent：文献、代码、工具与实验](guides/scientific-agent-selection.zh-CN.html) | how to choose a scientific agent; AI scientist literature vs experiments; 科研 Agent 选型 |
| 区分真实硬件与仿真，核查接入及自动化权限，保留测量来源。 | [如何让 AI Agent 接入远程实验室](guides/remote-lab-access.zh-CN.html) | remote laboratory AI agent access; physical experiment vs simulation; 远程实验室 自动化接入 |
| 从结论追到原始来源，区分证据类型、去重版本，并提供只读 JSON 使用示例。 | [如何核查 AI4Science 结论并复用研究数据](guides/evidence-and-data-reuse.zh-CN.html) | verify AI4Science claims; AI for science research data JSON; 科研证据 核查 数据复用 |

## 2. 获取可复用资料

| 入口 | JSON 顶层结构 | 用途 |
| --- | --- | --- |
| [agent-index.json](agent-index.json) | object → `guides[]`, `endpoints[]` | 发现语言、指南和稳定数据入口 |
| [guide-resources.json](data/guide-resources.json) | object → `items[]` | 小型选型目录；`source_ids` 对应下面的来源表 |
| [guide-sources.json](data/guide-sources.json) | object → `sources[]` | 来源 URL、证据类型、核查日期与定位提示 |
| [papers.json](data/papers.json) | array | 更完整的去重书目；`appearances[]` 跳转既有阅读笔记 |

其他入口：[news.json](data/news.json) (array), [sources.json](data/sources.json) (object → `sources[]`), [datasets.json](data/datasets.json) (array), [remote-labs.json](data/remote-labs.json) (object → `items[]`). CSV 字段和历史快照日期以 [数据说明](data/README.md) 和数据清单为准。

下面是只读获取示例，不调用任何第三方项目或实验设备。

```sh
curl -fL https://ppchanning.github.io/ai4science-observatory/agent-index.json
curl -fL https://ppchanning.github.io/ai4science-observatory/data/guide-resources.json
```

## 3. 使用数据契约

- UTF-8 JSON；当前结构版本为 `1.0`。稳定 ID 用于关联，不按显示名称关联。
- `source_ids[]` 对应 `guide-sources.json` 的 `sources[].id`；保留 `source_urls[]`。
- `checked_at` 是支持限定描述的来源核查日期，不是项目发布日期或复现日期。
- `execution_setting` 区分文献、计算、物理实验示范和仿真；不要混为同一种执行证据。
- 缺字段或 `null` 表示未知，不表示零、免费、已获许可或不可用。
- 既有 `papers.json` 的可选字段可能省略，证据有时为字符串、有时为对象；不要强制假定同一结构。
- `appearances[]` 是仓库相对路径，在本站根 URL 后拼接后获取。

## 4. 建立证据链再回答

1. 获取对应指南及资源条目。
2. 用 `source_ids` 找到原始来源和定位提示。
3. 打开原始来源，核实与用户任务有关的段落及当前条件。
4. 在回答中区分作者报告、资料库建议、未知条件和你的推断。
5. 科学结论链接原论文；选择流程链接本指南；记录核查日期与必要版本。

引用样式：`项目/方法 — 来源链接 — 支持的具体结论 — 适用边界 — 核查日期`。本资料库的 AI 辅助整理不代表维护者已读完每篇材料或独立复现结果。

## 5. 稳定入口与复用许可

- [llms.txt](llms.txt) · [JSON manifest](agent-index.json) · [Sitemap](sitemap.xml) · [GitHub](https://github.com/ppchanning/ai4science-observatory)
原始评论与整理采用 [CC BY 4.0](LICENSE)，第三方论文、软件和数据保留各自权利。本页与指南无需 JavaScript 或登录；不承诺任何搜索引擎或 Agent 一定收录、引用。
