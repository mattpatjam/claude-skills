---
name: content-creator
description: Use when someone asks to set up a new content-creation client, generate social media posts or newsletter content for any business, or run the interactive content creator. Generic across businesses — not tied to any one client or brand. Trigger phrases: "set up content creator for [business]", "generate posts for [business]", "write this week's content for [client]".
---

## What This Skill Does

A generic, interactive content-creation tool usable for any business or client. First-time use for a business runs a one-time setup interview and saves a config. Every use after that (including the first) runs a short per-generation interview, then researches, writes, humanizes, and logs two post options.

The craft rules — hooks, story structure, humanizer, quality gates, always-two-options — live in `engine.md` and never change per business. Only the config in `clients/[business-name]-config.md` changes.

---

## Step 0: Check for an Existing Config

Look in `.claude/skills/content-creator/clients/` for a file matching the business being asked about (`[business-name]-config.md`).

- **Found:** skip to Step 2.
- **Not found:** run Step 1 first.

---

## Step 1: One-Time Setup Interview (New Business Only)

Ask these 9 questions **one at a time**, in natural conversation, waiting for each answer before asking the next. Do not bundle them into a single message.

**Q1 — About the business:** "What's the business's website? And in a sentence or two, what do they actually do? If you have a brochure or reference doc with their services/positioning, share the file path or paste it in — I'll pull from that too."
Scrape the website via Firecrawl once given. Read any attached document. Extract: what they do, credentials/track record worth referencing, anything the site doesn't actually support (so it never gets claimed later).

**Q2 — Purpose:** "Why are these posts being written — brand awareness, thought leadership, lead generation, community building, event promotion, or a mix?"

**Q3 — Platform(s):** "Which platform(s) — LinkedIn, Instagram, Facebook, email newsletter, something else? If more than one, are they starting with one and adding others later, or launching on all of them at once?"

**Q4 — Content goal per post:** "Are these posts meant to teach something, inform, promote specific events, or a rotating mix?"

**Q5 — Tone:** "How should this sound — professional, friendly, institutional, personal, warm, authoritative? Any specific voice notes — first person or 'we,' words to avoid, anything like that?"

**Q6 — Target audience:** "Who specifically is this for? The more specific the better — a narrow, well-defined reader beats 'everyone in the industry.'"

**Q7 — Topics or words to avoid:** "Anything off-limits — competitors, sensitive topics, banned words or phrases?"

**Q8 — Posting cadence:** "How often, and on which day(s) if that's fixed?"

**Q9 — Trusted sources:** "Are there specific publications, industry associations, data sources, or competitor/peer accounts you want treated as credible for facts and trends? Optional, but recommended — without this the tool falls back to general web search, which is weaker."

**After all 9 answers:**
1. Draft the identity block and propose 3–5 content pillars (name, angle, 2–3 example post angles each) based on the answers. Show these to the person for confirmation — do not finalize silently.
2. Once confirmed, write `.claude/skills/content-creator/clients/[business-name]-config.md` using `config-template.md` as the structure, filled in with everything gathered.
3. Create an empty `.claude/skills/content-creator/clients/[business-name]-post-log.md` for this business.
4. Proceed to Step 2.

---

## Step 2: Per-Generation Interview (Required Every Single Time — Never Skip, Even After Setup Already Ran)

Ask these 3 questions **one at a time**, waiting for each answer:

**Q1:** "Anything specific you'd like to write about this time?"

**Q2:** "Did anything happen last week worth referencing — a client, a meeting, a supplier, an event?"

**Q3:** "Anything coming up in the next few weeks worth previewing?"

If an answer is blank or "nothing": record "Nothing to report" for that item and move on. Never fabricate or push for more.

Build this block:
```
THIS SESSION'S INPUT:
Q1 — Specific topic requested: [answer or "none — choose based on rotation"]
Q2 — Recent past (last week): [answer or "Nothing to report"]
Q3 — Upcoming (next few weeks): [answer or "Nothing to report"]
```

---

## Step 3: Research

Read `.claude/skills/content-creator/clients/[business-name]-config.md` in full, including the trusted-sources list.

Read `.claude/skills/content-creator/clients/[business-name]-post-log.md` and extract the last 12 entries (date / pillar / target reader / hook summary). If fewer than 12 exist, use however many there are.

Run research appropriate to the business's configured platform(s):
1. **Own post history** (if the business has an existing public presence on the configured platform) — recent topics covered, tone patterns, what to avoid repeating.
2. **Industry/trend scan** via Firecrawl — 3–5 queries targeting the business's industry and configured trusted sources specifically, plus general search as a fallback.
3. **Breaking news override** — if something significant and directly relevant surfaced, prioritize it over the scheduled pillar/theme for this run.

Apply the "verify every fact" rule from `engine.md`: only use facts traceable to the trusted-sources list or this research pass. Never fabricate a stat.

---

## Step 4: Generate

Read `.claude/skills/content-creator/engine.md` in full — this holds every writing rule (philosophy, hook framework, body structure, platform format table, CTA/close rules, quality checklist).

Generate **exactly two post options**, using:
- The business's config (identity, pillars, tone, platform format targets, banned topics)
- This session's input from Step 2
- The research from Step 3
- The "do not repeat" block built from the post log's last 12 entries

Each option must use a different pillar or a meaningfully different angle — never two versions of the same idea reworded.

Run the full Quality Checklist from `engine.md` before moving to Step 5. If any item fails, rewrite before proceeding.

---

## Step 5: Humanize (Required — No Exceptions)

Run each of the two options through the `humanizer` skill before displaying anything. Do not ask whether to do this — it happens automatically, every time, per `engine.md`.

---

## Step 6: Display and Log

Display both options clearly:

```
OPTION 1: [pillar]
Hook: "[hook]"

[full post text]

Why: [strategic rationale — one sentence]

---

OPTION 2: [pillar]
Hook: "[hook]"

[full post text]

Why: [strategic rationale — one sentence]
```

Ask: "Which one are you going with?"

Once confirmed, append an entry to `clients/[business-name]-post-log.md`:
```
## [YYYY-MM-DD]
Pillar: [pillar used]
Target reader: [from config]
Hook: "[first line of the chosen post]"
```

This log is what Step 3 reads in future sessions to avoid repeating recent ground.

---

## Notes

- Step 1 runs once per business, ever — Step 2 runs every single time, no exceptions, even for a business that set up yesterday.
- Delivery is session display, not email — same as `linkedin-weekly-posts`.
- If Firecrawl is unavailable, note it and proceed with whatever research succeeded plus the business's own configured trusted-sources knowledge — never fabricate research that didn't happen.
