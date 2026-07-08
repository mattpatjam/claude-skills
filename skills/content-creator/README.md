# Content Creator — System Summary

A generic, interactive content-creation tool. Works for any business or client — not built around one specific account. First use for a new business runs a one-time setup interview; every use after that (including the first) runs a short per-generation interview, then researches, writes, humanizes, and logs two post options.

Built as a Claude Code skill (`.claude/skills/content-creator/`) for local design and testing, following the same pattern already proven by `linkedin-weekly-posts/`. **The real deployment target is Renner** — see `RENNER-SPEC.md` for the actual engineering handoff. The Claude Code version here is the reference implementation the Renner build gets translated from, not itself the production system.

---

## Files in This Skill

| File | Purpose |
|---|---|
| `SKILL.md` | Orchestration — the step-by-step workflow, what to ask and when. Written so this can be run and tested locally in Claude Code before handing off. |
| `engine.md` | Fixed writing rules, identical for every business. Never edited per client. |
| `config-template.md` | Blank template for a new business's setup answers |
| `RENNER-SPEC.md` | **The actual engineering handoff document.** Translates `SKILL.md` + `engine.md` into APIs, node flow, config schema, and error handling for whoever builds this on Renner (or any platform other than Claude Code). Give this file to the Renner engineer, not the others. |
| `clients/[business-name]-config.md` | One filled-in config per onboarded business (local/Claude Code use only — Renner stores config in its own per-client variable store instead, per `RENNER-SPEC.md`) |
| `clients/[business-name]-post-log.md` | One rotation/no-repeat log per onboarded business (local/Claude Code use only — Renner uses a real Google Sheet per business instead, per `RENNER-SPEC.md`) |

---

## Workflow, Step by Step

1. **Setup interview** (once per business, only on first use) — 9 questions covering who the business is, why they're posting, where, what kind of content, tone, audience, banned topics, cadence, and trusted sources. Produces a config file plus a proposed set of content pillars, confirmed with the person setting it up before being finalized.

2. **Per-generation interview** (every single time content is requested, no exceptions) — 3 short questions: anything specific to write about, anything from the last week worth referencing, anything upcoming worth previewing. This is what keeps output feeling current instead of generic, even with the same fixed engine underneath.

3. **Research** — the business's own recent post history (if any), an industry/trend scan prioritizing their configured trusted sources, and a check against the post log so nothing gets repeated.

4. **Generation** — always exactly two post options, each on a different angle or pillar, built from the engine rules + the business's config + this session's input + the research.

5. **Humanizer pass** — mandatory, runs automatically on both options before anyone sees them.

6. **Display and log** — both options shown for a pick; the chosen one gets logged so future sessions know what's already been covered.

---

## What Needs to Be Ready Before Onboarding a Business

Before running the setup interview for a new business, have on hand:

- **The business's website URL**, and/or a brochure or reference document with their services and positioning. The identity block every post draws facts from comes from here — without it, the tool is guessing.
- **A clear answer on which platform(s)** they're posting to. Format and length defaults can't be set without this (see the benchmark table in `engine.md`).
- **Whether this is a brand-new account or one with existing post history.** Affects whether the research step has anything to check against on day one, and whether a post log needs to be seeded manually with past content before the first real run.
- **Firecrawl access confirmed in whatever environment is running this tool.** Already available in this workspace; flag as a dependency if this gets ported to Renner or elsewhere.
- **The `humanizer` skill available in whatever environment is running this tool.** Already built into this repo; same porting flag applies.

Nice to have but not blocking: a list of trusted sources (publications, associations, competitor accounts) — the tool works without it, just falls back to general web search with lower confidence on facts.

---

## What's Fixed vs. What's Configurable

**Never changes, regardless of business (lives in `engine.md`):**
- The 3 hook types + 7 attention-driver framework
- The 3-beat story arc (and the deeper 5-phase version for narrative content)
- Lists/Steps/Stories retention mechanics
- The platform benchmark table (length/format targets)
- The verify-every-fact rule
- CTA/close rules, the Give:Ask ratio, PS-statement tactic
- The two-options-per-generation rule
- The quality checklist
- The mandatory humanizer pass
- The no-repeat/rotation logging mechanism

**Configurable per business (lives in `clients/[business-name]-config.md`):**
- Identity, credentials, what to draw from
- Purpose, platform(s), content goal
- Tone and voice specifics
- Target audience
- Content pillars (derived from setup answers, confirmed before finalizing)
- Banned topics/words
- Posting cadence
- Trusted sources

---

## Relationship to Other Skills

- **`linkedin-weekly-posts`** — Matthieu's own personal Bali real estate LinkedIn skill. Proven, already working, untouched by this build. Not merged into this engine — kept separate.
- **`humanizer`** — invoked automatically by this skill's Step 5, every time, no exceptions.

## Onboarding a New Client Later

This build is deliberately generic — no client is configured yet. When a business is ready to use this (on Renner or elsewhere), run the setup interview from `SKILL.md` Step 1 to produce their config, rather than hand-writing one. If a business already has answers gathered elsewhere (an existing discovery questionnaire, prior prompt draft, etc.), those answers can be fed directly into the 9 setup questions instead of re-asking from scratch — the interview format doesn't require starting blank.
