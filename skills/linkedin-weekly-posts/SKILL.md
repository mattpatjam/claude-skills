---
name: linkedin-weekly-posts
description: Use when someone asks to generate LinkedIn posts, do this week's LinkedIn content, create LinkedIn posts for the week, run the weekly content workflow, or do the Monday LinkedIn content creation.
---

## What This Skill Does

Runs the full weekly LinkedIn content creation workflow for Matthieu. Sequence is fixed and non-negotiable:

1. Gather recent-past input (required — Hormozi's #1 content source)
2. Check LinkedIn analytics and log performance (required — always run)
3. Research — scrape Matthieu's profile, Terje's newsletter, and news sources (required — never skip)
4. Select themes and angles for the week — get approval before writing
5. Generate 6 post options (2 per day)
6. Display posts formatted in the session
7. Humanize all chosen posts (required — no exceptions)
8. Log chosen posts to tracking files

---

## Step 1: Gather Recent Past (Required — Never Skip)

Matthieu is Director of Business Development, Real Estate Brokerage and Property Acquisition, at Bali Superhost (villa management), where he is building the real estate brokerage from the ground up. He meets villa owners, developers and investors before they sign. He does not handle guest complaints or day-to-day operations, so never ask about those.

Before the questions, say once: "Easiest is a voice note or rough notes, in your own words. I'll keep your phrasing." His raw words are the main material for the posts, so take them as given.

Ask these 4 questions one at a time in natural conversation. Wait for each answer before asking the next. Do not bundle them.

**Q1 (The pitch):** "What did a villa owner or prospect say in a meeting this week that stuck with you? A question, an objection, a reason they said yes or no."

**Q2 (The market):** "What's shifting in Bali villas or rentals right now that owners or investors should know about? Any number behind it: occupancy, nightly rates, yields, prices, supply?"

**Q3 (The investor):** "Did anyone ask you about buying or investing in a villa this week? What were they getting wrong, or right?"

**Q4 (Your story):** "What's something from your career, sales or real estate, that shapes how you approach these conversations now?"

Q1 is the most valuable answer. If he gives an owner's exact words, keep them exactly. Q4 is the fallback for a quiet week.

After all four answers, build this block. Record his answers **verbatim** (clean up only filler like "um"). Do not summarize or polish them:

```
RECENT PAST INPUT FROM MATTHIEU (this week, his words):

Q1 — The pitch: [answer 1, verbatim]
Q2 — The market (numbers he gave): [answer 2, verbatim]
Q3 — The investor: [answer 3, verbatim]
Q4 — His story: [answer 4, verbatim]
```

If any answer is "nothing" or blank: write "Nothing to report" for that item. Do NOT fabricate or prompt for more.
If all four are empty: write `No recent past provided — write from professional expertise only.`

Any number in Q2 is used only once it is verified (Matthieu's own data or a source on the approved list in `prompt.md`). If it can't be verified, write around it.

Write this block to `/tmp/linkedin_recent_past.txt` using the Write tool.

---

## Step 2: LinkedIn Analytics Check (Required — Always Run)

Run the scraper immediately — do not ask permission:

Run the scraper via Bash:
```
/Users/matt/Desktop/Claude/.venv/bin/python3 /Users/matt/Desktop/Claude/.claude/skills/linkedin-weekly-posts/linkedin_analytics.py
```

It reads the **profile activity feed**, which is authoritative. Do not use the creator-analytics dashboard as the source of truth: on 2026-10-13 it under-reported one post by 78% (2,161 against the feed's 10,018) and surfaced only 3 posts where the feed had 8.

Output is a `posts` array sorted by impressions, each with `impressions`, `impressions_rounded`, `reactions`, `comments`, `reposts`, `age` (e.g. `5d`, `1w`), `age_days`, `hook`, `text_preview`, `full_text`, `full_len`. Top level carries `counters_found`, `posts_parsed` and, when something looks off, `warnings`.

Useful flags:
- `--days 14` widen the window (default 7), `--all` for no date filter
- `--source both` scrape the feed and the dashboard, report `discrepancies` and `coverage`
- `--source analytics` dashboard only (best effort parsing, mid-post fragments are common)

**Checks before trusting the output:**
- `counters_found` should equal `posts_parsed`. A gap means posts were dropped.
- Any `warnings` entry means a post's body or date was recovered by fallback. Read them.
- `impressions_rounded: true` means LinkedIn displayed a rounded `K`/`M` value, so the number is approximate.

**If output contains `"error"`:** Tell Matthieu what went wrong. If error says "li_at cookie may have expired", ask him to:
1. Open Chrome → LinkedIn → DevTools (F12) → Application → Cookies → `.linkedin.com` → `li_at` → copy the Value
2. Paste the new value into `.env` replacing the `LI_AT=` line
Then retry once.

**If scraping succeeds:** Present the results clearly, newest window first:
```
Last 7 days (profile feed):

1. [impressions] impressions • [reactions] reactions • [comments] comments • [age]
   "[hook]"

2. ...
```
Compute and mention the engagement rate where it is informative, since impressions on this account cluster tightly while engagement separates posts sharply.

Log these to the tracking files immediately (format below), then proceed to Step 3.

Log format for `.claude/skills/linkedin-weekly-posts/posts_published.md`:
```
## [YYYY-MM-DD] ([Tuesday/Wednesday/Thursday])
Pillar: [pillar]
Theme: [theme]
Hook: "[hook text]"
Impressions: [n] | Reactions: [n] | Comments: [n] | Reposts: [n]
```

Then recalculate pillar averages in `.claude/skills/linkedin-weekly-posts/post_analytics.json` and update `last_updated`.

**Voice reference (refresh monthly).** Check `.claude/skills/linkedin-weekly-posts/voice_reference.md`. It exists, built 2026-11-02 from a full profile scrape.

**If its `Updated:` date is 30 days old or less:** leave it alone and go to Step 3.

**If it is missing, or its `Updated:` date is more than 30 days old:** rebuild it before going to Step 3.
1. Run the scraper with `--all`.
2. Rank posts by engagement rate, (reactions + comments + reposts) / impressions. Skip any post with fewer than 500 impressions, since the rate is noise below that.
3. Take the top 5 and save each one's `full_text` exactly as published, with its date and engagement numbers:

```
# Voice Reference
Updated: [YYYY-MM-DD]

These are Matthieu's own best posts. Match how they sound, not how they are structured.

## 1. [date] · [rate]% engagement · [impressions] impressions
[full_text, unedited]

## 2. ...
```

Never edit, polish or "fix" the text in this file. Its value is that it is his, as it went out.

---

## Step 3: Research (Required — Never Skip)

**Do this before writing a single word of any post. No exceptions.**

**Cookie authentication — required on every LinkedIn fetch.** Read `LI_AT` from `.env`
and attach it as the `cookies` parameter on every `mcp__ScraplingServer__fetch` (or
`stealthy_fetch`) call to linkedin.com. A fetch without this returns a login wall, not
real data — this is the single most common reason research comes back thin, so do not
skip it:
- `cookies: [{"name": "li_at", "value": "<LI_AT from .env>", "domain": ".linkedin.com", "path": "/"}]`

Run all of the following using the Scrapling MCP (`mcp__ScraplingServer__fetch`):

1. **Matthieu's LinkedIn profile** — https://www.linkedin.com/in/matthieu-jammers-a40a0726/recent-activity/all/ (li_at cookie attached)
   Extract: 10 most recent posts and hooks, topics covered in the last 60 days, what's performing. Do not repeat any topic or angle from the last 60 days.

2. **Terje H. Nilsen's newsletter** — https://www.linkedin.com/in/terje-h-nilsen-9905a843/recent-activity/newsletter/ (li_at cookie attached)
   Extract: what topics he's covering, angles that are performing, gaps Matthieu could fill with a different perspective.

3. **At least 2 news sources** — fetch whichever are most relevant to the themes selected for this week:
   - The Bali Sun: https://thebalirealestate.com/ or balisun.com
   - The Jakarta Post property section: https://www.thejakartapost.com/business/property
   - Bali Discovery: https://balidiscovery.com/
   - Indonesia Expat: https://indonesiaexpat.id/
   - Nikkei Asia (Indonesia): https://asia.nikkei.com/Economy/Indonesia

4. **Owner and investor pain-point sources (required)** — this keeps content pointed at the readers in the "Who This Is For" section of `prompt.md` (owners, developers, investors) rather than only what professionals discuss:
   - Reddit r/bali (https://www.reddit.com/r/bali/) and Quora — search for property/buying/investment threads. No cookie needed.
   - Do not scrape Facebook groups. Dropped 2026-11-02: it needs Matthieu's personal session cookie and risks his account being checkpointed, which costs more than the research is worth.
   Search for villa owner, villa management, rental income, licensing and villa investment threads.
   Extract: what owners and investors are actually confused about, frustrated with, or wish someone had told them — not what agents are discussing.

**After research:** Summarize in 3–5 bullets what's currently being talked about in the market, what Terje is covering, what owners and investors are asking/worried about (from item 4 above), and what topics Matthieu hasn't touched recently. Use this to inform theme and angle selection. Only then proceed to Step 4 (theme selection).

If Scrapling hits a login wall on LinkedIn: this almost always means the cookie parameter was missing or expired, not that scraping is blocked — check the cookie was attached before assuming failure. If it truly failed after that, tell Matthieu that `LI_AT` needs refreshing (see the comment above that variable in `.env`), note it, and proceed with what was retrieved + post history from `posts_published.md`. Do not fabricate trending data.

---

## Step 4: Select Themes and Subjects (Required — Get Approval Before Writing)

Read `.claude/skills/linkedin-weekly-posts/prompt.md` for the pillar and theme definitions.
Read `.claude/skills/linkedin-weekly-posts/posts_published.md` to check what has been covered in the last 60 days.
Read `/tmp/linkedin_recent_past.txt` for this week's personal input.

Using the research from Step 3 and the recent past input, propose the three themes and specific post angles for the week. For each angle, identify which of the four topic types it draws from. The label is not decoration: each type has its own drafting rules in the TOPIC TYPES section of `prompt.md`, and the one chosen here changes how the post gets written in Step 5.

- **Recent Past** — something from the last 7 days: a meeting, an owner's objection, a market observation, or a thing he said that landed
- **Far Past** — a defining moment, early career lesson, or old deal that shaped how Matthieu works
- **Present** — a thought forming right now, an open question he's working through, a real-time observation from building the brokerage
- **Trending** — something being discussed in the market, industry, or news that Matthieu can add a qualified perspective to

Across the three days use at least two different types, and never the same type three days running.

```
TUESDAY [date]
Theme: [theme]
Topic type: [Recent Past / Far Past / Present / Trending]
Angle: [one sentence describing the specific take — not the full post]
Why now: [why this angle is timely or relevant based on research]

WEDNESDAY [date]
Theme: [theme]
Topic type: [Recent Past / Far Past / Present / Trending]
Angle: [one sentence]
Why now: [why timely]

THURSDAY [date]
Theme: [theme]
Topic type: [Recent Past / Far Past / Present / Trending]
Angle: [one sentence]
Why now: [why timely]
```

Rules:
- No two days can share the same theme
- No theme or angle covered in the last 60 days (check `posts_published.md`)
- Weave in the recent past input where it fits the angle naturally
- Thursday should get the strongest hook opportunity — save the best angle for Thursday

Ask: "Does this direction work, or do you want to swap any theme or angle?"

**Wait for Matthieu to approve before writing any full posts.** If he swaps something, update and confirm again before proceeding.

---

## Step 5: Generate Posts

Read `.claude/skills/linkedin-weekly-posts/prompt.md` in full — this contains all writing rules, pillars, themes, format specs, and quality checklist.

Then generate 6 post options following the prompt exactly:
- 2 options for **Tuesday** (same theme, two different pillars)
- 2 options for **Wednesday** (same theme, two different pillars — theme must differ from Tuesday)
- 2 options for **Thursday** (same theme, two different pillars — theme must differ from Tuesday and Wednesday)

**Write from his words, not from scratch.** Before drafting, read `voice_reference.md` and `/tmp/linkedin_recent_past.txt`. Where a post draws on his answers, start from his actual sentences and edit them down (cut, reorder, tighten). Keep his phrasing, his rhythm and his slightly non-native English turns where they read naturally. Do not swap his words for smoother generic ones. If a post has no input from him to draw on, match the sentence length and tone of the voice reference posts.

**Vary the shape across the 6 options.** They must not all follow hook, story, lesson, question:
- At least 1 option is a short post (300 to 700 characters)
- At least 2 options do not end with a question
- At least 1 option has no explicit lesson or takeaway line; it shows what happened and lets the reader draw the conclusion
- Lengths are genuinely varied, with no two options on the same day within 200 characters of each other. Six options of similar length reads as machine-written even when each one is good.
- No option exceeds 1,600 characters. Hard ceiling, no exceptions.

**One real detail per post.** Every post includes at least one specific thing only Matthieu could know: a named area, an exact verified number, or something an owner or investor actually said. A post that could have been written by anyone in Bali real estate gets rewritten.

Before writing a single word of any post, internalize this non-negotiable formatting rule from CLAUDE.md: **no em dashes, no dashes of any kind as separators or connectors.** Replace every instance with a comma, period, or parentheses. This applies during drafting — not as a post-processing step. If you catch a dash while writing, fix it before moving on.

Run the full quality checklist from `prompt.md` before outputting anything. If any item fails — rewrite before showing Matthieu. Also scan every post for dashes (—, –, or - used as separators) before displaying. Any post containing one must be rewritten.

---

## Step 6: Display Posts

Display all 6 options clearly using this structure. Every option's post text always ends with its hashtag line, and every option always includes a ready-to-paste AI image prompt — this is not optional and never needs to be requested:

```
TUESDAY [date] — [theme]

OPTION 1: [pillar]
Hook: "[hook]"

[full post text]

[Hashtag line — max 5, relevant]

Why: [strategic rationale]
Image Prompt: [full ready-to-paste AI image generation prompt — subject, setting, mood/lighting, style, aspect ratio. Not a one-line description.]

---

OPTION 2: [pillar]
Hook: "[hook]"

[full post text]

[Hashtag line — max 5, relevant]

Why: [strategic rationale]
Image Prompt: [full ready-to-paste AI image generation prompt]

Recommendation: [Option 1 or 2 — one sentence why]
[Warning if char count failed validation]

---

WEDNESDAY [date] — [theme]
[same structure]

---

THURSDAY [date] — [theme]
[same structure]
```

After displaying: ask "Which ones are you going with? I can humanize any of them before you post."

---

## Step 7: Humanize the Chosen Posts (Required — No Exceptions)

Once Matthieu confirms which options he's going with, invoke the `humanizer` skill on **each chosen post** before logging or delivering. No exceptions — every post that gets selected must pass through the humanizer before it is considered done.

Do not ask if he wants this. Just do it. Show the humanized version and confirm it's ready to post.

The final delivered version of every chosen post keeps its hashtag line and Image Prompt attached underneath — humanizing only touches the post body copy, never drop or forget the hashtags/image prompt when presenting the final version.

---

## Step 8: Log the Chosen Posts

Once Matthieu confirms which options he's going with (e.g. "Tuesday Option 1, Wednesday Option 2, Thursday Option 1"), log each to `.claude/skills/linkedin-weekly-posts/posts_published.md`:

```
## [YYYY-MM-DD] ([Tuesday/Wednesday/Thursday])
Pillar: [pillar used]
Theme: [theme used]
Hook: "[first line of the post]"
Impressions: — | Reactions: — | Comments: — | Reposts: —
```

Leave the engagement fields as `—` — they get filled in during Step 2 the following week when analytics are checked.

Also update `.claude/skills/linkedin-weekly-posts/post_analytics.json` to increment the count for that pillar under `pillars_used`.

This log is what Step 3 uses in future sessions to avoid repeating themes and pillars from the last 60 days.

---

## Notes

- **Never skip a step.** Steps 1 to 8 run in order, every time, unless Matthieu explicitly says to skip one in that session. A step he skipped last week is not skipped this week.
- Step 1 is always first. Never jump to generation without the 4 questions.
- Delivery is the session display. There is no email step and nothing is sent anywhere.
- Character count: hard ceiling 1,600 characters, never exceeded. Most posts land between 800 and 1,600, and short posts (300 to 700) are welcome and expected. Vary the lengths deliberately.
- Cadence: three posts a week, Tuesday, Wednesday and Thursday, two options each. All six are produced in one session.
- The humanizer is a final polish, not the fix for a robotic draft. The voice comes from his words (Step 1) and the voice reference (Step 2).
- Humanizer runs on every chosen post automatically (Step 7). Never wait to be asked.
