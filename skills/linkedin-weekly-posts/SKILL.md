---
name: linkedin-weekly-posts
description: Use when someone asks to generate LinkedIn posts, do this week's LinkedIn content, create LinkedIn posts for the week, run the weekly content workflow, or do the Monday LinkedIn content creation.
---

## What This Skill Does

Runs the full weekly LinkedIn content creation workflow for Matthieu. Sequence is fixed and non-negotiable:

1. Gather recent-past input (required — Hormozi's #1 content source)
2. Optionally check LinkedIn analytics via browser
3. Generate 4 post options with full context injected
4. Display posts formatted in the session

---

## Step 1: Gather Recent Past (Required — Never Skip)

Ask these 3 questions one at a time in natural conversation. Wait for each answer before asking the next. Do not bundle them.

**Q1:** "What happened this week in a deal, viewing, or client conversation that surprised you, frustrated you, or taught you something? Even something small counts."

**Q2:** "Any observation about a buyer, seller, or the market that stuck with you this week?"

**Q3:** "Anything you said to a client this week that landed well, or that you wish you'd said differently?"

**Q4:** "What's something you're working through or learning right now as a professional — a deal dynamic, a market shift, a skill you're developing? Doesn't need to be resolved."

After all four answers, build this block:

```
RECENT PAST INPUT FROM MATTHIEU (this week):

Q1 — Deal/viewing/conversation: [answer 1]
Q2 — Market/buyer/seller observation: [answer 2]
Q3 — Something said to a client: [answer 3]
Q4 — Something currently being figured out: [answer 4]
```

If any answer is "nothing" or blank: write "Nothing to report" for that item. Do NOT fabricate or prompt for more.
If all four are empty: write `No recent past provided — write from professional expertise only.`

Write this block to `/tmp/linkedin_recent_past.txt` using the Write tool.

---

## Step 2: LinkedIn Analytics Check (Optional)

Ask: "Do you want me to check your LinkedIn analytics first? I'll pull last week's post performance and update the tracking files. Takes about 30 seconds. Yes or no?"

**If yes:**

Run the scraper via Bash:
```
/Users/matt/Desktop/Claude/.venv/bin/python3 /Users/matt/Desktop/Claude/.claude/skills/linkedin-weekly-posts/linkedin_analytics.py
```

Parse the JSON output. It returns `posts` array with `impressions`, `engagements`, `hook`, and `text_preview` for the top 3 posts from the last 7 days.

**If output contains `"error"`:** Tell Matthieu what went wrong. If error says "li_at cookie may have expired", ask him to:
1. Open Chrome → LinkedIn → DevTools (F12) → Application → Cookies → `.linkedin.com` → `li_at` → copy the Value
2. Paste the new value into `.env` replacing the `LI_AT=` line
Then retry once.

**If scraping succeeds:** Present the results clearly:
```
Last 7 days — Top performing posts:

1. [impressions] impressions • [engagements] engagements
   "[hook]"

2. [impressions] impressions • [engagements] engagements
   "[hook]"

3. [impressions] impressions • [engagements] engagements
   "[hook]"
```
Ask: "Want me to log these to the tracking files?" If yes, log them (format below). If no, proceed to Step 3.

**If Matthieu says skip:** proceed to Step 3 without logging.

Log format for `.claude/skills/linkedin-weekly-posts/posts_published.md`:
```
## [YYYY-MM-DD] ([Tuesday/Wednesday/Thursday])
Pillar: [pillar]
Theme: [theme]
Hook: "[hook text]"
Impressions: [n] | Reactions: [n] | Comments: [n] | Reposts: [n]
```

Then recalculate pillar averages in `.claude/skills/linkedin-weekly-posts/post_analytics.json` and update `last_updated`.

**If no:** skip to Step 3.

---

## Step 3: Research (Required — Never Skip)

**Do this before writing a single word of any post. No exceptions.**

Run all of the following using the Scrapling MCP (`mcp__ScraplingServer__fetch`):

1. **Matthieu's LinkedIn profile** — https://www.linkedin.com/in/matthieu-jammers-a40a0726/recent-activity/all/
   Extract: voice patterns, 10 most recent posts and hooks, topics covered in the last 60 days, what's performing. Do not repeat any topic or angle from the last 60 days.

2. **Terje H. Nilsen's newsletter** — https://www.linkedin.com/in/terje-h-nilsen-9905a843/recent-activity/newsletter/
   Extract: what topics he's covering, angles that are performing, gaps Matthieu could fill with a different perspective.

3. **At least 2 news sources** — fetch whichever are most relevant to the themes selected for this week:
   - The Bali Sun: https://thebalirealestate.com/ or balisun.com
   - The Jakarta Post property section: https://www.thejakartapost.com/business/property
   - Bali Discovery: https://balidiscovery.com/
   - Indonesia Expat: https://indonesiaexpat.id/
   - Nikkei Asia (Indonesia): https://asia.nikkei.com/Economy/Indonesia

**After research:** Summarize in 3–5 bullets what's currently being talked about in the market, what Terje is covering, and what topics Matthieu hasn't touched recently. Use this to inform theme and angle selection. Only then proceed to Step 4.

If Scrapling fails on LinkedIn (auth wall): note it and proceed with what was retrieved + post history from `posts_published.md`. Do not fabricate trending data.

---

## Step 4: Select Themes and Subjects (Required — Get Approval Before Writing)

Read `.claude/skills/linkedin-weekly-posts/prompt.md` for the pillar and theme definitions.
Read `.claude/skills/linkedin-weekly-posts/posts_published.md` to check what has been covered in the last 60 days.
Read `/tmp/linkedin_recent_past.txt` for this week's personal input.

Using the research from Step 3 and the recent past input, propose the three themes and specific post angles for the week:

```
TUESDAY [date]
Theme: [theme]
Angle: [one sentence describing the specific take — not the full post]
Why now: [why this angle is timely or relevant based on research]

WEDNESDAY [date]
Theme: [theme]
Angle: [one sentence]
Why now: [why timely]

THURSDAY [date]
Theme: [theme]
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

Weave the recent past input naturally into the posts where relevant (personal story, client observation, market insight). Do not force it — only use it if it genuinely strengthens the post.

Run the full quality checklist from `prompt.md` before outputting anything. If any item fails — rewrite before showing Matthieu.

---

## Step 6: Display Posts

Display all 6 options clearly using this structure:

```
TUESDAY [date] — [theme]

OPTION 1: [pillar]
Hook: "[hook]"

[full post text]

Why: [strategic rationale]
Visual: [image description]

---

OPTION 2: [pillar]
Hook: "[hook]"

[full post text]

Why: [strategic rationale]
Visual: [image description]

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

---

## Step 6: Log the Chosen Posts

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

- Step 1 is always first. Never jump to generation without the 3 questions.
- Do not send email. Session display is the delivery.
- Character count target is 1,200–1,600 chars. LinkedIn's hard limit is 3,000 — the target is a readability guideline, not a hard stop.
- Humanizer runs on every chosen post automatically (Step 5). Never wait to be asked.
