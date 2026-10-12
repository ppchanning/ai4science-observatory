# SelfRef Agent Library: static publishing source

This directory builds [SelfRef Agent Library](https://www.selfref.org/agents/) from **AI4Science Observatory** and **Agent Simulation Environments**. It publishes searchable English / Chinese pages, guide mirrors, original public archives, evidence records, a JSON catalog, reading protocols and downloadable research skills. GitHub remains the source of record.

The server serves static files. Search runs in the browser; all cards and articles are present in HTML before JavaScript. There is no user database, model inference endpoint, autonomous collector or public execution service.

## Build

Requires Node.js 20+, Python 3 (for reproducible ZIP archives) and `marked` 17.0.5. Install the pinned dependency with `npm ci` in this directory, then run:

```sh
node build.mjs --science=SCIENCE_REPO --simulation=SIMULATION_REPO --output=EMPTY_OUTPUT_DIRECTORY
```

If a trusted workspace already provides Marked, set `SELFREF_MARKED_PATH` to its `lib/marked.esm.js` instead. No dependency is needed on the serving host.

For a local preview, add `--base=http://127.0.0.1:PORT/agents/`. Production builds use the SelfRef URL by default. Every build requires an empty output directory so deleted source files cannot linger in a release.

Use the two clean, published repository checkouts. The output must be outside both repositories. Deploy only a successfully validated build, with both source revisions verified against GitHub. Host addresses, credentials and local publishing state stay outside the repository.

## Publication contract

- Only tracked public Markdown, JSON, CSV, original SVG and citation/license files in the explicit content allowlist are mirrored. Skill packages contain only the approved `SKILL.md` and original curation license.
- Do not copy third-party full text, private source materials, internal instructions, credentials, local paths, logs or source caches.
- `catalog.json` is a root object with `entries[]`; the schema distinguishes guides, resources, skills and collections. Resource records preserve primary-source locators, historical check dates and evidence limitations.
- Source revisions are pinned GitHub commits. Skill versions derive from content SHA-256, not a fabricated release number; ZIP files have deterministic content and timestamps.
- `release.json` records the collection revisions and catalog content revision. Build timestamps do not create new research activity. Homepage updates come from the real collection records, limited to 7 calendar days in Asia/Shanghai.
- Review HTML/local links, catalog source joins, schemas, ZIP content/checksums, English/Chinese routes and browser search before publication. Inspect public content for private information.
- Preview locally, upload to a new release directory, verify it, then atomically switch the serving symlink. Keep the preceding release for rollback. Do not overwrite the main SelfRef site or other applications.

Original code, design and curation in this directory follow the repository's CC BY 4.0 license. Marked retains its MIT license; linked sources retain their respective rights.

Run `python3 verify.py OUTPUT_DIRECTORY` before upload. It checks all internal files and anchors, record counts, source IDs, Markdown SHA-256 values, ZIP contents and private deployment markers. `catalog.schema.json` is also available for full JSON Schema validation.

## Public mirror

The GitHub Pages workflow preserves the original collection site and builds a second library at [the Pages mirror](https://ppchanning.github.io/ai4science-observatory/library/). It runs on main pushes, manual dispatch and daily at 23:50 Asia/Shanghai, using only the two public checkouts; it creates no Git commits or research activity. The serving host remains the primary SelfRef address.
