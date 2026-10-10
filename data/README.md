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
| [industry/startups.csv](industry/startups.csv) | 公司主表，37 条 |
| [industry/funding-events.csv](industry/funding-events.csv) | 融资事件，44 条 |
| [industry/research-programs.csv](industry/research-programs.csv) | 机构项目总表，18 条 |
| [industry/public-company-initiatives.csv](industry/public-company-initiatives.csv) | 核心20家公司，20 条 |

书目保留匹配状态，候选集并非全部确认纳入。招聘与融资是历史快照；职位可能关闭，披露金额性质须分别理解。被引数仅对统计日期有效。不重分发原始 Excel、第三方全文或摘要。

## Stable schema

新闻字段：id/title/url/published_at/summary[]/appearances[]/provenance；可选学科和历史核验。书目字段：id/title/DOI/arXiv/URL/作者/日期版本/evidence/limitations/read_first/appearances[]/provenance。appearances 是相对归档路径；可选字段未知时省略，证据可能为字符串或对象。
