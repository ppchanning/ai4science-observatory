<p align="center"><strong>English</strong> | <a href="README.zh-CN.md">简体中文</a></p>

<p align="center"><a href="https://ppchanning.github.io/ai4science-observatory/">Documentation site</a> · <a href="agent-index.md">Agent index</a> · <a href="llms.txt">llms.txt</a></p>

<p align="center"><img src="assets/banner.svg" alt="AI4Science Observatory" width="100%"></p>

<h1 align="center">AI4Science Observatory</h1>
<p align="center"><strong>A living reading map for AI scientific discovery, scientific agents, and automated experiments</strong><br>Discover research, follow scientific agents, and explore the path from models to experiments.</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/content-CC_BY_4.0-6366f1" alt="Content license: CC BY 4.0"></a>
  <a href="digests/README.md"><img src="https://img.shields.io/badge/format-digests_%2B_catalogs-0284c7" alt="Digests and catalogs"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/README-English_%2B_简体中文-334155" alt="README available in English and Simplified Chinese"></a>
</p>

<p align="center"><a href="#updates">Updates</a> · <a href="#start-here">Start here</a> · <a href="#explore-the-landscape">Topic map</a> · <a href="#research-and-industry-data">Reusable data</a> · <a href="digests/README.md">Archives</a> · <a href="CONTRIBUTING.md">Contribute</a></p>

**Turn scattered AI4Science developments into a knowledge hub you can read, trace, compare, and explore further.**

AI is entering many stages of scientific research: analyzing data, building models, proposing hypotheses, writing scientific code, operating specialized software, and connecting to physical instruments and remote laboratories. This repository connects those stages to help you understand what a development investigates, how it works, what evidence supports it, and what to read next.

The collection brings together science news digests, paper reading notes, topical bibliographies, public sources, and structured catalogs. Follow daily developments, explore a research question across papers, or download the data to build your own literature and industry analysis.

## Updates

<!-- updates-daily:start -->
- **2026-10-12** — Added [3 bilingual core guides](guides/scientific-agent-selection.md), [1 Agent index](agent-index.md) and a [Pages reading site](https://ppchanning.github.io/ai4science-observatory/); plus [1 installable Skill](skills/ai4science-research/SKILL.md) and Context7 indexing configuration; listed in [2 skill directories](#installable-agent-skill).
- **2026-10-11** — Added [14 news events](digests/ai4science/2026/2026-10-11.md) and [5 scientific-agent papers](digests/scientific-computer-use/2026/2026-10-11.md) in 2 new issues; 1 returning event. Added 1 source, revised 1 source and 2 catalog records across 2 CSVs. Mathematical verification & instrument workflows.
- **2026-10-10** — [11 news items](digests/ai4science/2026/2026-10-10.md) · [5 scientific-agent resources](digests/scientific-computer-use/2026/2026-10-10.md) — Crop breeding & scientific discovery. Cataloged [3 previously archived items](digests/ai4science/2026/2026-09-27.md), fixed 182 archive references, and cleaned up 4 issues. No new resources or issues.
- **2026-10-09** — [9 news items](digests/ai4science/2026/2026-10-09.md) · [5 scientific-agent resources](digests/scientific-computer-use/2026/2026-10-09.md) — Climate models & telescopes.
- **2026-10-08** — [9 news items](digests/ai4science/2026/2026-10-08.md) · [5 scientific-agent resources](digests/scientific-computer-use/2026/2026-10-08.md) — Cell maps & X-ray agents.
- **2026-10-07** — [12 news items](digests/ai4science/2026/2026-10-07.md) · [5 scientific-agent resources](digests/scientific-computer-use/2026/2026-10-07.md) — Protein design & automated labs.
- **2026-10-06** — [7 news items](digests/ai4science/2026/2026-10-06.md) · [5 scientific-agent resources](digests/scientific-computer-use/2026/2026-10-06.md) — Instrument control & quantum sensing.
<!-- updates-daily:end -->

Last 7 days here; [full update history](CHANGELOG.md). Earlier entries follow material dates, backfilled on **2026-10-10**, when this repository launched.

<!-- updates-milestones:start -->
- 🧭 **2026-10-12** — [Three core guides and Agent reading entry points](agent-index.md), with complete English / Chinese versions and a [public reading site](https://ppchanning.github.io/ai4science-observatory/).
- 🚀 **2026-10-10** — [Launched](https://github.com/ppchanning/ai4science-observatory/commit/551b5b6) with [28 reading issues](digests/README.md) and [11 CSV datasets](data/README.md); added [English / Chinese homepages](README.zh-CN.md) and [update history](CHANGELOG.md).
<!-- updates-milestones:end -->

## Core guides and agent access

Three core guides, each available in English and Chinese, with primary sources, scope limits and reusable templates.

| Guide | What you get |
| --- | --- |
| [How to choose a scientific agent: literature, code, tools and experiments](guides/scientific-agent-selection.md) | A task-first comparison of scientific agents, with source-backed examples and a reusable selection checklist. |
| [How to connect an AI agent to a remote laboratory](guides/remote-lab-access.md) | Distinguish real hardware from simulation, verify access and automation permissions, and preserve measurement provenance. |
| [How to verify AI4Science claims and reuse research data](guides/evidence-and-data-reuse.md) | A claim-to-source workflow, evidence labels, deduplication rules and a working read-only JSON example. |

[Read on Pages](https://ppchanning.github.io/ai4science-observatory/) · [Agent index](agent-index.md) · [JSON manifest](agent-index.json) · [llms.txt](llms.txt)

## Installable agent skill

[Read the skill](skills/ai4science-research/SKILL.md): a research workflow connecting guides, JSON evidence and primary sources. Example: Select a scientific agent for a literature review with traceable citations.

```sh
npx skills add ppchanning/ai4science-observatory --skill ai4science-research
```

Install with the Skills CLI into a supported agent; the first run downloads the CLI. The skill itself is a read-only research workflow, returning evidence, unknowns and next checks. Directory indexing is verified separately from installability.

Find this skill on [Agent Skill Hub](https://agentskillhub.dev/u/ppchanning/sk/ai4science-research) and [askill](https://askill.sh/skills/gh/ppchanning/ai4science-observatory/@ai4science-research). For repository navigation and Q&A, use [DeepWiki](https://deepwiki.com/ppchanning/ai4science-observatory); its generated explanations should be checked against the cited source files.

## Start here

| What you want to do | Where to start | What you get |
| --- | --- | --- |
| Catch up on recent developments | [Latest AI4Science digest](digests/ai4science/2026/2026-10-11.md) | Event context, the connection between AI and the scientific problem, original sources, and evidence limitations |
| Understand how agents participate in scientific work | [Latest scientific-agent reading notes](digests/scientific-computer-use/2026/2026-10-11.md) | Reading entry points for scientific software, computational workflows, instrument operation, and remote experiments |
| Build a reading path around a question | [Topic map](topics/README.md) · [Paper catalog](resources/papers.md) | Papers connected by methods and settings, with original sources for checking claims |
| Build your own information feed | [Source directory](resources/sources.md) | Institutions, journals, projects, and specialist media, with collection methods and historical verification information |
| Compare research areas, projects, or industry developments | [Data guide](data/README.md) | Downloadable catalogs of papers, surveys, companies, funding events, jobs, and institutional programs |
| Review developments over time | [Dated archives](digests/README.md) | Individual issues and historical sources for continued reading and retrospective exploration |

For AI4Science researchers, students entering the field, scientific software and laboratory automation developers, and technical readers following the scientific industry. **The homepage is available in English and [Simplified Chinese](README.zh-CN.md). Most existing digests and research archives are in Chinese; the three core guides and Agent index are fully bilingual, with original English paper titles and source links retained.**

## Explore the landscape

### AI for scientific discovery

Explore AI methods through the scientific problems they address: data and representations, prediction and modeling, scientific computing, experiment selection, and result validation. Daily news and interdisciplinary paper catalogs offer a broad view, placing individual papers within their disciplines, methods, and research workflows.

**Start reading:** [Science digests](digests/README.md#ai4science-daily) · [Core papers](data/catalogs/core-papers.csv) · [Surveys](data/catalogs/surveys.csv)

### Scientific agents & computational workflows

Follow how agents organize literature, code, tools, and multistep tasks, and how their outputs are recorded and checked. Notes focus on how systems actually work, what they produce, and the evidence used to validate them, helping you compare scientific workflows.

**Start reading:** [Scientific agents](topics/scientific-agents.md) · [Scientific-agent bibliography](resources/papers.md)

### Scientific computer use & specialized software

Study agents using graphical interfaces, terminals, and specialized software for scientific tasks: what they observe, which actions they take, how results are verified, and where long tasks fail. The collection includes papers on scientific software use, computational environments, and process evaluation.

**Start reading:** [Scientific computer use](topics/computer-use.md) · [Reading-note archive](digests/README.md#scientific-computer-use)

### Remote experiments & physical instruments

Connect remote scientific experiments to the broader research workflow, from tool calls to instrument control, measurement feedback, and closed-loop experimentation. Paper notes and platform directories help distinguish simulated environments, demonstrations on physical equipment, and publicly accessible facilities.

**Start reading:** [Remote experiments](topics/remote-experiments.md) · [Platforms and public evidence](resources/remote-labs.md)

### Data, evaluation & research validity

Examine the data, tasks, and controls used in a study, the conclusions its reported results support, and the limits of those conclusions. Notes preserve versions, measurement targets, and unknown conditions to provide context for comparing methods.

**Start reading:** [Data and evaluation](topics/data-and-evaluation.md) · [Editorial policy](docs/editorial-policy.md)

## A taste of the collection

These examples illustrate the range of the current bibliography. See the [paper catalog](resources/papers.md) for fuller source information, versions, and associated reading issues.

| Area | Selected resource | A question to read with |
| --- | --- | --- |
| Scientific code and agent environments | [ScienceIDE](https://arxiv.org/abs/2609.19134) | How can scientific code become an interactive task environment for agents? |
| Scientific software use | [OSWorld-Science](https://arxiv.org/abs/2609.39903) | What tasks and evaluations are needed to learn and use specialized software? |
| Physical measurements | [Autonomous Quantum Transport Measurements](https://arxiv.org/abs/2609.26661) | How do agents enter physical measurement workflows, and how are experimental results confirmed? |
| Remote laboratory facilities | [A Programmable Optics Cloud Laboratory](https://arxiv.org/abs/2609.16413) | How do remote access, programmatic control, and experimental feedback fit together? |

## Research and industry data

Beyond daily reading, the repository provides **UTF-8 JSON / CSV** for filtering and further analysis. Field definitions, record counts, and snapshot dates are documented in the [data guide](data/README.md) and [dataset inventory](data/datasets.json).

| Data layer | Available material | Common uses |
| --- | --- | --- |
| Research literature | Core papers, surveys, cited works, included papers, and candidate reading sets | Build literature tables, select research directions, and trace related work; candidates and included papers are labeled separately |
| Research and industry | Companies, funding events, jobs, institutional programs, and initiatives involving listed companies | Explore technology transfer, organizational activity, and historical hiring needs |
| News and bibliographies | Deduplicated news JSON, scientific-agent paper JSON, and linked archive paths | Search locally, analyze timelines, and connect reading notes to their sources |
| Sources and facilities | Source-directory JSON and evidence for remote laboratory platforms | Build monitoring lists and find public projects and facility entry points |

Paper tables may overlap; their row counts cannot be added to obtain a unique paper count. Industry records are dated snapshots of public information. Job availability and platform access conditions require fresh verification.

## Collection at a glance

<!-- collection-stats:start -->
As of **2026-10-11**: **18 science digests · 199 deduplicated news events · 12 scientific-agent reading issues · 50 bibliography entries · 171 sources · 11 CSV datasets**.

News archives cover 2026-09-22 through 2026-10-11; reading issues cover 2026-09-28 through 2026-10-11. There may be gaps within these date ranges. New and revised material is archived by date, with current entry points, topic indexes, and structured data maintained together.
<!-- collection-stats:end -->

## How to use this repository

1. **Follow developments:** Choose an event from the latest digest, read the explanation, and open the original source.
2. **Read by topic:** Follow a topic page into its bibliography, then use the methods, limitations, and suggested sections in the reading notes to plan your reading order.
3. **Build your own collection:** Download JSON / CSV and filter by fields in a spreadsheet or analysis tool. Keep source information and snapshot dates.
4. **Contribute and correct:** Submit an [issue](https://github.com/ppchanning/ai4science-observatory/issues) or pull request for missing papers, metadata corrections, or evidence concerns. Include original sources as described in the [contribution guide](CONTRIBUTING.md).

## Repository map

```text
digests/       # Science digests and scientific-agent notes: channel / year / date
topics/        # Reading paths organized by questions and methods
resources/     # Paper, public-source, and remote-laboratory directories
data/          # Downloadable JSON / CSV and dataset inventory
docs/          # Editorial policy, sharing guidance, and design references
skills/        # Installable evidence-guided agent workflow
templates/     # Consistent templates for new material
.github/       # Resource suggestions, corrections, and pull request templates
```

## Sources, contributions & citation

The collection preserves original sources, versions, and evidence limitations, distinguishing preprints, published papers, news, and official cases. Content is curated with AI assistance. A recommendation does not imply that the maintainer has completed the reading; an author's reported result does not imply independent replication. See the [editorial policy](docs/editorial-policy.md).

Contributions of sourced resources, improved reading paths, and factual corrections are welcome; see [CONTRIBUTING](CONTRIBUTING.md). Original commentary and compilation are licensed under [CC BY 4.0](LICENSE); third-party works retain their respective rights. Cite the original papers for scientific claims. To cite this collection's organization and data, use [CITATION.cff](CITATION.cff).

**Related collection:** [Agent Simulation Environments](https://github.com/ppchanning/agent-environments-and-evaluation) focuses on building, generating, and validating agent simulation environments, including tool-service simulation, stateful simulators, and world models. This repository focuses on scientific problems, research workflows, and physical experiments.

[Sharing guide](docs/sharing.md) · [Design references](docs/design-references.md)
