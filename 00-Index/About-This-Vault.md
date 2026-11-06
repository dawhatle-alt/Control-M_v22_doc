---
type: meta
status: extracted
tags:
  - control-m
  - meta
---

# About This Vault

## Purpose
Structured, wikilinked reference copy of the **Control-M User Guide 9.0.27
(Self-Hosted), September 2026** for AI agents (and humans) troubleshooting
Control-M support cases. Companion to the HCU Knowledge Graph vault.

## How it was built
`_tools/parse.py` + `_tools/build_vault.py` read the PDF (via `pdftohtml -xml`),
recover the topic hierarchy from the printed table of contents and heading
font sizes, and convert the PDF's internal cross-reference links into
wikilinks. Every note carries `source_pages` (PDF page numbers) so any claim
can be checked against the original.

## Note types (frontmatter `type`)
| type | folder | one note per |
|---|---|---|
| `doc-topic` | 10-Guide/<section> | level-1 topic; child topics are `##` headings inside the note |
| `doc-topic` (+ `parent:`) | 10-Guide/<section>/<parent> | sub-topic of a long parent (>40 pages) |
| `doc-messages` | 10-Guide/50-Messages | a range of ~80 message IDs |
| `moc` | 00-Index | map of content |
| `finding` / `root-cause` / `resolution` | 40 / 50 / 60 | case-derived knowledge (empty until enriched) |

## Sections (10-Guide)
Getting-Started · Planning · Job-Types · Scheduling-and-Definitions ·
Planning-Utilities · Monitoring · Monitoring-Utilities · Control-M-AI ·
Administration · Reports · Platform-Configuration · System-Configuration ·
EM-Utilities · Server-Utilities · Automation-API-Admin · Messages ·
Plug-ins-and-Connection-Profiles · Application-Integrator ·
Managed-File-Transfer · Plug-in-Configuration · Integrations ·
Migration-Tools · Glossary. Entry points: [[Control-M-Guide-MOC]] (master),
[[Troubleshooting-Entry-Points]] (curated).

## Conventions
- `status: extracted` = generated from the PDF, not yet human-verified.
  `status: verified` after review. Findings/Root causes/Resolutions use
  `skeleton` → `seeded` → `enriched`.
- Wikilinks come from the PDF's own cross-references. A link resolves to the
  note (and `#Heading`) that starts at or just before the target page, so an
  occasional link lands on the neighbouring heading — the `source_pages`
  frontmatter and the alias text always tell you what was meant.
- Tables are reconstructed from text positions; long cells use `<br>` for
  paragraph breaks and `•` for in-cell bullets. Screenshots were not extracted.
- Footnote glossary definitions (repeated on nearly every page of the PDF)
  were dropped; the terms themselves are defined once in [[Glossary]].
- Message IDs: search the ID number — each `doc-messages` note is named by its
  ID range, and each table row starts with the ID.

## Retrieval rules for agents
1. Match a message ID or log string against `10-Guide/50-Messages` first.
2. For a utility or parameter, open its note in EM-Utilities /
   Server-Utilities / Administration and quote the exact syntax row.
3. Match symptoms against `Finding-*` signatures (40-Findings) before
   free-form reasoning; propose a new Finding note when none matches.
4. Every product-behavior claim in a response should cite a note and its
   `source_pages`.
