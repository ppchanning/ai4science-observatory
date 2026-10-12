**English** | [简体中文](remote-lab-access.zh-CN.md)

# How to connect an AI agent to a remote laboratory

**Updated: 2026-10-12 · Type: source-backed practical guide · Examples are not results measured by this collection.**

## Quick answer

A remote laboratory is useful to an agent when it exposes an authorized action interface and returns identifiable experimental evidence. A browser interface, an API and an autonomous experiment loop are different capabilities. Verify each separately.

The repository's current remote-lab catalog contains **one platform evidence record**, LabsLand Electronics Hive. The two chemistry examples below are research demonstrations, not additional verified public-access facilities. This is a small evidence-based starting point, not an exhaustive laboratory directory.

## Separate the execution settings

| Setting | What executes the action | What the result establishes |
| --- | --- | --- |
| Physical remote laboratory | Actual instruments or hardware | A measurement in that apparatus and configuration |
| Digital simulation | A program or learned transition model | Behavior under the simulator's assumptions |
| Scientific desktop application | Scientific software on a computer | A computational or software operation; physical execution requires separate evidence |

A photograph can help identify equipment but does not by itself establish data integrity. A simulated result does not become a physical measurement when presented in a laboratory-style interface.

## Source-backed entry points

| Entry | Evidence available | Access or automation boundary |
| --- | --- | --- |
| [LabsLand Electronics Hive](https://labsland.com/en/labs/electronics-hive/) | Official documentation describes real components connected by relays and instrument measurements through a browser | Current account entitlement, pricing and permission for automated use require confirmation; no autonomous-agent performance is established here |
| [Coscientist](https://www.nature.com/articles/s41586-023-06792-0) | Published chemistry demonstration connecting planning, documentation and laboratory operations | Study-specific equipment and integration; not proof of a generally accessible agent endpoint |
| [ChemCrow](https://www.nature.com/articles/s42256-024-00832-8) | Published tool-assisted chemistry examples, including physical synthesis | Demonstrated services and the public tool subset differ; current service access remains unverified here |

The Hive platform page and [measurement guide](https://labsland.com/pub/docs/experiments/hive/user/en/taking_measurements.html) were checked on 2026-10-12. Older detailed observations in [remote-labs.json](../data/remote-labs.json) keep their original verification date. Historical latency measurements must not be treated as current queue or response-time guarantees.

## Six checks before an integration

1. **Apparatus:** Identify real hardware, software or simulation, and the supported parameter range.
2. **Entitlement:** Confirm account eligibility, booking, cost and the facility's permitted automation method. Mark unresolved items as unknown.
3. **Action contract:** Identify accepted inputs, units, validation rules, execution status and errors. Distinguish preparing a configuration from actually starting an experiment.
4. **Measurement contract:** Identify returned files, units, timestamps, calibration context and any run or apparatus identifiers the platform actually supplies.
5. **Recovery:** Establish how to handle a failed or delayed request and how to avoid unintentionally repeating an execution.
6. **Bounded pilot:** Use the documented permitted workflow for one test; verify the output against an expected range or reference before broadening the task.

These checks are this collection's integration recommendations. They do not claim that every listed platform exposes all these fields.

## A useful experimental record

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

This is an empty provenance template. Preserve missing fields as unknown. A failed request or an interface preview is not a completed experiment. Do not infer that a human-in-the-loop browser workflow provides a public automation API.

## Continue reading

Read the existing [platform evidence notes](../resources/remote-labs.md), [scientific-agent selection guide](scientific-agent-selection.md) and [evidence reuse guide](evidence-and-data-reuse.md). An agent should cite the facility documentation for access and interface claims, and the original paper for research results.

## Primary sources

- `labsland-hive` — [LabsLand Electronics Hive](https://labsland.com/en/labs/electronics-hive/) · official-platform-documentation · Summary; Access options; Internal Operation
- `hive-measurement` — [Hive user guide: Taking measurements](https://labsland.com/pub/docs/experiments/hive/user/en/taking_measurements.html) · official-platform-documentation · Taking measurements
- `coscientist` — [Autonomous chemical research with large language models](https://www.nature.com/articles/s41586-023-06792-0) · peer-reviewed-paper · Main: six demonstrated tasks; Coscientist system architecture
- `chemcrow` — [Augmenting large language models with chemistry tools](https://www.nature.com/articles/s42256-024-00832-8) · peer-reviewed-paper · Results and discussion; Code availability

Sources checked on 2026-10-12 for the scoped descriptions above, without independent reproduction. Machine-readable records: [guide-sources.json](../data/guide-sources.json).
