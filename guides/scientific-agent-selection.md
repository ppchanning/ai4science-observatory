**English** \| [简体中文](scientific-agent-selection.zh-CN.md)

# How to choose a scientific agent: literature, code, tools and experiments

**Updated: 2026-10-12 · Type: source-backed practical guide · Examples are not results measured by this collection.**

## Quick answer

Choose a scientific agent by the **artifact you need and the evidence that can verify it**. Literature answers need traceable passages; computational experiments need runnable code and recorded outputs; physical experiments need measurements from identified instruments. A persuasive research narrative is insufficient to establish all three.

This guide compares four representative approaches. It is a selection aid, not a benchmark ranking. Project descriptions below come from the linked primary sources, checked on 2026-10-12; the collection has not independently executed these systems.

## Compare by task

| Need | Representative entry point | Source-supported capability | What to verify before choosing |
| --- | --- | --- | --- |
| Answer a question using scientific documents | [PaperQA](https://github.com/Future-House/paper-qa) | Retrieval-based scientific document answers with citations | Corpus coverage, source passages, model/provider requirements and document rights |
| Explore a computational research idea | [The AI Scientist](https://sakana.ai/ai-scientist/) | An author-described workflow connecting ideas, code, computational experiments and reports | Runnable artifacts, experiment controls, resource budget and failure cases |
| Connect planning to laboratory operations | [Coscientist](https://www.nature.com/articles/s41586-023-06792-0) | A published chemical-research demonstration involving tool use and automated experiments | Which demonstrated equipment and integration can be reproduced in your setting |
| Combine chemistry reasoning with domain tools | [ChemCrow](https://www.nature.com/articles/s42256-024-00832-8) | Tool-augmented chemistry tasks; the public release includes a subset of the paper's tools | Difference between the study system and public implementation; access to required services |

These projects have different tasks and evaluations. Their reported scores do not form a shared leaderboard. Hardware demonstrated in a paper does not establish that a reader can access it today.

## A practical selection procedure

1. **Write the deliverable.** For example: a sourced literature answer, a reproduced numerical result, or a measured circuit response. Specify the required file or measurement.
2. **List available interfaces.** Documents, Python, a graphical application and a laboratory API impose different constraints. Record credentials and permission requirements as requirements, without publishing credentials.
3. **Define the verifier first.** Identify source passages, tests, baseline comparisons or measurement provenance that would make the deliverable checkable.
4. **Try one bounded task.** Save inputs, system version, tool calls, outputs, cost and errors. Include one known failure or missing-input case.
5. **Decide within that scope.** A system that succeeds at document synthesis still needs separate evidence for code execution or physical experimentation.

## Reusable selection record

Use the following as an empty comparison template. `null` means unknown. It is not a measured result or a project rating.

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

## Find related evidence in this collection

Use [guide-resources.json](../data/guide-resources.json) for the four curated examples and source identifiers. The broader [paper bibliography](../data/papers.json) contains dated scientific-computer-use and remote-experiment entries. Follow each record's `appearances` to its reading notes; open the original source before making a scientific claim.

For physical access, continue to [Remote laboratory access](remote-lab-access.md). For a reusable evidence workflow, read [Evidence and data reuse](evidence-and-data-reuse.md).

## What remains unknown

This guide does not establish current operating cost, access eligibility, installation success or cross-domain performance. Recheck current project documentation and test the intended task. Author-reported evidence and this collection's selection advice are separate.

## Primary sources

- `paperqa` — [PaperQA: scientific document question answering](https://github.com/Future-House/paper-qa) · official-project-documentation · README: overview, citations and configuration
- `ai-scientist` — [The AI Scientist](https://sakana.ai/ai-scientist/) · official-project-report · Overview of the computational research workflow; limitations
- `coscientist` — [Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0) · peer-reviewed-paper · Main: six demonstrated tasks; Coscientist system architecture
- `chemcrow` — [Augmenting large language models with chemistry tools](https://www.nature.com/articles/s42256-024-00832-8) · peer-reviewed-paper · Results and discussion; Code availability

Sources checked on 2026-10-12 for the scoped descriptions above, without independent reproduction. Machine-readable records: [guide-sources.json](../data/guide-sources.json).
