# Data Guide

UTF-8 JSON / CSV。空值表示未知，不能解释为零、免费或已获许可。

| 文件 | 内容 |
| --- | --- |
| [news.json](news.json) | 去重新闻摘要、来源链接、日期 |
| [papers.json](papers.json) | 科学软件操作与远程实验书目 |
| [sources.json](sources.json) | 信源与历史核验 |
| [datasets.json](datasets.json) | CSV 清单、字段、记录数、快照日期 |
| [remote-labs.json](remote-labs.json) | 平台证据及未知条件 |
| [catalogs/cited-papers.csv](catalogs/cited-papers.csv) | 被引文献库，1290 条 |
| [catalogs/core-papers.csv](catalogs/core-papers.csv) | 全部核心论文，282 条 |
| [catalogs/surveys.csv](catalogs/surveys.csv) | 综述论文库，20 条 |
| [catalogs/published-papers.csv](catalogs/published-papers.csv) | 严格纳入，1243 条 |
| [catalogs/conference-candidates.csv](catalogs/conference-candidates.csv) | AI4Sci主会候选，902 条 |
| [catalogs/reading-candidates.csv](catalogs/reading-candidates.csv) | 可follow论文库，1197 条 |
| [industry/jobs.csv](industry/jobs.csv) | 岗位归档，60 条 |
| [industry/startups.csv](industry/startups.csv) | 公司主表，42 条 |
| [industry/funding-events.csv](industry/funding-events.csv) | 融资事件，49 条 |
| [industry/research-programs.csv](industry/research-programs.csv) | 机构项目总表，18 条 |
| [industry/public-company-initiatives.csv](industry/public-company-initiatives.csv) | 核心20家公司，20 条 |

书目保留匹配状态，候选集并非全部确认纳入。招聘与融资是历史快照；职位可能关闭，披露金额性质须分别理解。被引数仅对统计日期有效。不重分发原始 Excel、第三方全文或摘要。

## Stable schema

新闻字段：id/title/url/published_at/summary[]/appearances[]/provenance；可选学科和历史核验。书目字段：id/title/DOI/arXiv/URL/作者/日期版本/evidence/limitations/read_first/appearances[]/provenance。appearances 是相对归档路径；可选字段未知时省略，证据可能为字符串或对象。

## Core-guide data (schema 1.0)

| 文件 | 顶层结构 | 内容 |
| --- | --- | --- |
| [guide-resources.json](guide-resources.json) | object → `items[]` | 核心指南的小型案例目录；与既有完整书目分开计数 |
| [guide-sources.json](guide-sources.json) | object → `sources[]` | 原始来源、证据类型、核查日期和定位提示 |
| [../agent-index.json](../agent-index.json) | object → `guides[]`, `endpoints[]` | 指南、语言、任务别名与公开数据入口 |

用 `source_ids[]` 关联 `sources[].id`。`checked_at` 只表示支持限定描述的来源核查；`independently_reproduced: false` 明确未独立复现。`execution_setting` 区分文献、计算、物理实验与仿真。缺字段或 null 仍表示未知。

完整英文与中文读取、引用流程见 [Agent index](../agent-index.md) / [Agent 索引](../agent-index.zh-CN.md)。原始评论和整理采用 CC BY 4.0，第三方材料权利不变。

2026-10-13 新增的百趣生物 B 轮记录对应[投资界公开报道](https://news.pedaily.cn/202610/570017.shtml)；近亿元为披露量级，非精确金额或估值。

2026-10-14 新增的利太智药种子轮记录对应[36氪公开报道](https://eu.36kr.com/zh/p/4019481828628101)；披露日期为2026-10-10，近5000万元为近似金额，不作为精确金额或估值。

2026-10-15 新增[高维医药 Pre-A 轮](https://news.pedaily.cn/202610/570228.shtml)与[天序智能 Pre-A+ 轮](https://news.pedaily.cn/202610/570192.shtml)，共2家公司、2条融资记录。高维年内累计数亿元不等于本轮金额；天序数千万元为近似量级，原文币种未明确，披露日期为2026-10-13。

2026-10-17 修订百奥几何2026-06-26融资记录的投资方角色：[公司原始披露](https://www.biogeom.com/zh/2026/06/26/百奥几何完成新一轮数亿元战略融资，以微观世/)列明联合领投、跟投与财务顾问。此次为历史记录补全，不是新增融资事件；金额与其他字段不变。

2026-10-18 根据[科创板日报10月17日采访回顾](https://api3.cls.cn/share/article/2507464?app=stib&os=ios&sv=202)，补充天鹜科技2026-07-13 A++轮的投资方角色：上海国投先导与国投创新联合领投、上海国投孚腾资本跟投。仅修订1条历史记录；金额、日期与公司数量不变，不新增融资事件。

### 2026-10-19 论文元数据修订

依照 [Nature 原始论文](https://www.nature.com/articles/s41586-023-06735-9)的署名与在线发表日期，修订 CP00230（Scaling deep learning for materials discovery）的作者拆分、机构、发表日期与验证状态。该记录同时存在于 cited-papers.csv 与 core-papers.csv：修订1条既有论文记录、2份CSV，没有新增论文；行数仍为1290与282。在线发表为2023-11-29，与2023年12月卷期分别保留。

### 2026-10-20 产业资料

根据[科创板日报原始报道](https://api3.cls.cn/share/article/2508541?app=stib&os=ios&sv=241)，新增元材新界1家公司、1条种子轮融资记录（数千万人民币，君联资本领投、小苗朗程跟投）。金额为近似披露，交割日与资金用途未知；归属矛盾的应用案例未采用。

根据[DOIT的AI4S论坛报道](https://www.doit.com.cn/computing/861318107402309.html)，修订中科曙光1条既有业务记录，补充机器学习力场与科学平台进展。模拟规模按企业介绍归属，不新增融资金额、估值或公司。

### 2026-10-21 递送研发合作

根据[新浪科技报道](https://finance.sina.com.cn/roll/2026-10-20/doc-inivvsvv6608915.shtml)，修订剂泰1条既有业务记录，保留公司10月19日公告与媒体10月20日报道的区别。首付款与最高11亿美元附条件里程碑分开；合作不计股权融资、已确认投入或疗效证据，不新增公司或融资行。
