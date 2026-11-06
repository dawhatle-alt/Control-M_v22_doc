# CLAUDE.md — Control-M User Guide Vault (9.0.27)

This repo is an Obsidian vault: a structured, wikilinked copy of the
**Control-M User Guide 9.0.27 (Self-Hosted)** for use by troubleshooting
agents working BMC Control-M support cases. It is the companion to the HCU
Knowledge Graph vault: HCU answers "what does this archive show", this vault
answers "what does the product do, what does this parameter/utility/message
mean". Notes are the product — treat every edit as a change to a reference a
TSA will rely on.

## Session protocol

1. `git pull` before touching anything.
2. Work in **batches of 3–5 notes**, then STOP and summarize what changed for
   review. Do not continue to the next batch without explicit approval.
3. One folder per session unless told otherwise. Default enrichment order:
   `40-Findings` → `50-Root-Causes` → `60-Resolutions`; `10-Guide` notes are
   edited only to fix extraction defects, never to add claims.
4. Commit per batch with a descriptive message:
   `enrich(findings): Finding-agent-unavailable, Finding-newday-hang — signatures + chains`
5. Never rewrite a `10-Guide` note wholesale. Preserve the deterministic
   content (tables, parameter lists, message rows, `source_pages`) exactly.

## Vault schema

| Folder | type | One note per |
|---|---|---|
| 00-Index | moc / meta | map of content, entry points |
| 10-Guide/<section> | doc-topic | level-1 topic of the User Guide (child topics are `##` headings) |
| 10-Guide/<section>/<parent> | doc-topic | sub-topic of a long parent topic (`parent:` frontmatter) |
| 10-Guide/50-Messages | doc-messages | message-ID range (EM / Server / Agent) |
| 40-Findings | finding | observable abnormal pattern seen in a case |
| 50-Root-Causes | root-cause | underlying mechanism |
| 60-Resolutions | resolution | fix procedure |
| 90-Templates | template | note templates — never edit these during enrichment |
| _tools | — | `parse.py` + `build_vault.py` generators — do not modify during enrichment |

Full conventions live in `00-Index/About-This-Vault.md`. Read it once per
session before editing.

## Status lifecycle

`10-Guide` notes are `status: extracted` (generated from the PDF, not reviewed)
and move to `status: verified` only after a human confirms the extraction
matches the source pages. Findings/Root causes/Resolutions follow
`status: skeleton` → `status: seeded` → `status: enriched`. Flip status ONLY
when the definition of done below is met AND the batch was approved in review.
Never flip status in the same commit that drafts the content.

## Definition of done (per note type)

- **doc-topic (extraction fix)**: the corrected text matches the PDF at the
  `source_pages` cited; no wording added that is not on those pages.
- **finding**: a `## Signature` section with exact grep-able strings (log text
  or message ID); the `10-Guide` message/utility notes it maps to are
  wikilinked; links to ≥1 root cause.
- **root-cause**: mechanism explained in TSA language; every product-behavior
  claim wikilinks the `10-Guide` note (and `source_pages`) that supports it.
- **resolution**: numbered steps; each utility or parameter used is wikilinked
  to its `10-Guide` note; a verification step; a KA placeholder if the KA
  number is unknown (`KA: [TBD]`).

## Content rules

- **Sanitization is absolute.** No customer hostnames, domains, account names,
  IPs, or case numbers anywhere. Use `<hostname>`, `<EM_HOME>`, `<n>`, `<ts>`.
  If source material contains them, strip while drafting — not in a later pass.
- **Wikilinks are the graph.** Every enriched note links to ≥2 other notes.
  New notes must be reachable from a MOC or another linked note — no orphans.
  Link format: `[[Note-Name]]` or `[[Note-Name#Heading]]`, matching the
  filename exactly (case-sensitive).
- **Chains are directional.** Finding → RootCause → Resolution, with backlinks
  stated in prose. One note per concept.
- **No invented facts.** Product behavior claims must come from: a `10-Guide`
  note (cite it with a wikilink), material Darrell provides in-session (cases,
  KAs, docs), or be clearly flagged `> [UNVERIFIED — confirm against docs]`.
  When unsure, write the flag, not a guess.
- **Cite the guide, don't paraphrase it loosely.** When a `10-Guide` note
  answers the question, link it and quote the exact row/step rather than
  restating from memory.
- Version-specific behavior gets tagged inline: `(9.0.27)`. This vault is
  built from 9.0.27; older/newer behavior must be flagged as such.

## New notes

- Findings/RootCauses/Resolutions: copy the matching `90-Templates/tpl-*.md`,
  name as `Finding-<short-symptom>`, `RootCause-<short-mechanism>`,
  `Resolution-<short-action>` (hyphenated, no spaces).
- After adding any note, add it to `00-Index/Troubleshooting-Entry-Points.md`
  (findings) or the relevant section MOC.
- Never create new `10-Guide` notes by hand. Regenerate with `_tools` from a
  newer PDF instead, and diff.

## Never

- Never delete or rename existing notes without explicit instruction (renames
  break wikilinks — if approved, update every backlink in the same commit).
- Never edit `90-Templates/` or `_tools/` during enrichment sessions.
- Never commit directly after drafting a batch without the review stop.
- Never pull content from the internet into notes without flagging the source
  for review — this vault must stay authoritative, not scraped.
- Never touch `.obsidian/` settings.

## Validation before each commit

Run a link check: every `[[target]]` in changed notes resolves to an existing
file (templates' placeholder links like `[[Finding-...]]` are exempt, but only
inside 90-Templates). Report any dangling links in the batch summary instead
of silently creating stubs — stub creation is a review decision.
