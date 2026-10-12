**English** \| [简体中文](evidence-and-data-reuse.zh-CN.md)

# How to verify AI4Science claims and reuse research data

**Updated: 2026-10-12 · Type: source-backed practical guide · Examples are not results measured by this collection.**

## Quick answer

Treat this collection as a **discovery and comparison layer**. Use its guides to find a relevant question, its structured records to locate sources, and the original evidence to support a scientific claim. Neither a catalog entry nor an AI-generated summary establishes independent reproduction.

## A four-step evidence trail

1. **Locate the claim.** Write the specific statement you need to check, including the task, system and conditions.
2. **Locate its source.** Open the original paper or official documentation. Use identifiers and `appearances` to trace related archive notes.
3. **Match the evidence.** Check the method, comparison baseline, result location and limitations. Keep the denominator and experimental setting when reporting a number.
4. **State the boundary.** Say whether the source is a preprint, published paper, official documentation or news, and whether the claim was independently tested.

For example, a claim about Hive's real components belongs to its [official platform description](https://labsland.com/en/labs/electronics-hive/). A claim about Coscientist's laboratory demonstration belongs to the [research paper](https://www.nature.com/articles/s41586-023-06792-0). Availability for your account needs a separate current check.

## What evidence labels mean

| Label or situation | Supports | Does not establish |
| --- | --- | --- |
| Primary documentation checked | What a project or facility documents at the check date | Successful installation, account access or independently measured performance |
| Author-reported experiment | Results under the study's stated conditions | Universal performance, access rights or replication by this collection |
| Abstract-only reading | A discovery pointer and abstract-level account | Full methodological verification |
| Historical snapshot | What a catalog recorded at its snapshot date | Current job availability, facility access or citation totals |
| Collection recommendation | A reading path or selection heuristic | A result attributed to the original authors |

These are interpretation rules, not numeric confidence scores. Individual records may have older or more limited verification; keep those distinctions.

## Choose the right data file

| File | Root shape | Intended use |
| --- | --- | --- |
| [agent-index.json](../agent-index.json) | Object | Select a guide or data endpoint by question |
| [guide-resources.json](../data/guide-resources.json) | Object with `items` | Source-linked examples curated for the new guides |
| [guide-sources.json](../data/guide-sources.json) | Object with `sources` | Source types, check dates and evidence locations |
| [papers.json](../data/papers.json) | Array | Broader scientific-agent bibliography |
| [news.json](../data/news.json) | Array | Dated scientific developments and summaries |
| [remote-labs.json](../data/remote-labs.json) | Object with `items` | Platform evidence and unknown conditions |
| [datasets.json](../data/datasets.json) | Array | CSV paths, exact field names, row counts and snapshots |
| [sources.json](../data/sources.json) | Object with `sources` | Public information-source directory |

JSON and CSV are UTF-8. Many archive descriptions and CSV headers are Chinese. Use the exact fields documented in the inventory; do not silently translate keys. Candidate and included literature tables overlap, so their row counts cannot be summed into a unique paper count.

## Working read-only example

This standard-library Python example fetches curated guide resources and selects records by execution setting. It requires no API key and performs no laboratory action.

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

For larger paper tables, deduplicate by DOI, versionless arXiv identifier or canonical source URL. A new appearance or paper version is not automatically a new work. Missing values mean unknown, not zero, free or permitted.

## Cite and reproduce the lookup

For each reported claim, retain the original URL, evidence location, source type and version or snapshot date. Cite this collection for its organization; cite original sources for scientific findings. To freeze a lookup, use a GitHub commit-specific URL rather than the moving `main` branch. License information appears in [LICENSE](../LICENSE) and [CITATION.cff](../CITATION.cff); third-party works retain their own rights.

Report a broken link, incorrect metadata or unsupported statement through the [repository issues](https://github.com/ppchanning/ai4science-observatory/issues), including the primary source. The [editorial policy](../docs/editorial-policy.md) explains the collection's boundaries.

## Primary sources

- `labsland-hive` — [LabsLand Electronics Hive](https://labsland.com/en/labs/electronics-hive/) · official-platform-documentation · Summary; Access options; Internal Operation
- `coscientist` — [Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0) · peer-reviewed-paper · Main: six demonstrated tasks; Coscientist system architecture

Sources checked on 2026-10-12 for the scoped descriptions above, without independent reproduction. Machine-readable records: [guide-sources.json](../data/guide-sources.json).
