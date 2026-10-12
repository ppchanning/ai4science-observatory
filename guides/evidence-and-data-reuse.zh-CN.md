[English](evidence-and-data-reuse.md) \| **简体中文**

# 如何核查 AI4Science 结论并复用研究数据

**更新：2026-10-12 · 类型：有来源的实践指南 · 示例不是本资料库的实测结果。**

## 快速回答

把资料库当作**发现与比较资料的一层**：指南帮助定位问题，结构化记录帮助找到来源，原始证据支撑科研结论。目录条目和 AI 摘要都不能证明独立复现。

## 4 步证据链

1. **定位结论：** 写清要核查的具体陈述，包括任务、系统与条件。
2. **定位来源：** 打开原论文或官方文档，通过标识和 `appearances` 追到归档笔记。
3. **匹配证据：** 检查方法、对照基线、结果位置和限制；报告数字时保留分母与实验场景。
4. **说明边界：** 标明预印本、已发表论文、官方文档或新闻，以及是否独立测试。

例如，Hive 真实元件的说法对应[官方平台描述](https://labsland.com/en/labs/electronics-hive/)；Coscientist 实验示范对应[研究论文](https://www.nature.com/articles/s41586-023-06792-0)。你的账户当前能否使用，需要另外核查。

## 如何理解证据标记

| 标记或情况 | 支持什么 | 尚不能证明什么 |
| --- | --- | --- |
| 核查原始文档 | 项目或设施在核查日的公开描述 | 安装成功、账户接入、独立实测成绩 |
| 作者报告实验 | 研究给定条件下的结果 | 通用性能、权限、资料库独立复现 |
| 仅摘要阅读 | 发现入口和摘要层描述 | 完整方法核查 |
| 历史快照 | 快照日期记录的信息 | 当前岗位、设施权限、被引次数 |
| 资料库建议 | 阅读路径或选型启发 | 原作者的实验结论 |

这些是解释规则，不是数字置信评分。具体条目可能核查更早、证据更有限，应保留差别。

## 选择正确的数据文件

| 文件 | 根节点 | 用途 |
| --- | --- | --- |
| [agent-index.json](../agent-index.json) | 对象 | 按问题选择指南或数据入口 |
| [guide-resources.json](../data/guide-resources.json) | 含 `items` 的对象 | 核心指南的有来源案例 |
| [guide-sources.json](../data/guide-sources.json) | 含 `sources` 的对象 | 来源类型、核查日期与证据位置 |
| [papers.json](../data/papers.json) | 数组 | 科研 Agent 书目 |
| [news.json](../data/news.json) | 数组 | 科学动态及摘要 |
| [remote-labs.json](../data/remote-labs.json) | 含 `items` 的对象 | 平台证据与未知条件 |
| [datasets.json](../data/datasets.json) | 数组 | CSV 路径、准确字段名、记录数与快照 |
| [sources.json](../data/sources.json) | 含 `sources` 的对象 | 公开信源目录 |

JSON/CSV 使用 UTF-8，不少归档描述和 CSV 表头为中文。使用清单中的准确字段名，不能悄悄翻译键。候选与纳入文献表有重叠，记录数不能相加作为独立论文数。

## 可运行的只读示例

下面用 Python 标准库读取指南案例，按执行场景筛选。无需 API Key，也不执行实验动作。

```python
import json
from urllib.request import urlopen

url = "https://ppchanning.github.io/ai4science-observatory/data/guide-resources.json"
with urlopen(url, timeout=20) as response:
    catalog = json.load(response)
for item in catalog["items"]:
    if item["execution_setting"] == "literature":
        print(item["id"], item["name"], item["source_urls"][0])
```

较大论文表按 DOI、去版本 arXiv 标识或规范来源 URL 去重。同一资料再次出现或版本更新，不自动计为新增作品。缺失值表示未知，不代表零、免费或允许使用。

## 引用与复核查询

每条结论保留原始 URL、证据位置、来源类型与版本或快照日期。资料组织引用本集合，科研发现引用原始来源。需要固定查询时，用 GitHub 特定提交链接，不使用会变化的 `main`。许可见 [LICENSE](../LICENSE) 与 [CITATION.cff](../CITATION.cff)，第三方作品保留自身权利。

链接失效、元数据错误或证据不足可通过[仓库 Issues](https://github.com/ppchanning/ai4science-observatory/issues)反馈，并附原始来源。[编辑政策](../docs/editorial-policy.md)解释资料库的边界。

## 原始来源

- `labsland-hive` — [LabsLand Electronics Hive](https://labsland.com/en/labs/electronics-hive/) · official-platform-documentation · Summary; Access options; Internal Operation
- `coscientist` — [Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0) · peer-reviewed-paper · Main: six demonstrated tasks; Coscientist system architecture

核查日期为 2026-10-12。核查支持文中限定范围的描述，不代表独立复现；可机器读取的记录见 [guide-sources.json](../data/guide-sources.json)。
