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

After all three answers, build this block:

```
RECENT PAST INPUT FROM MATTHIEU (this week):

Q1 — Deal/viewing/conversation: [answer 1]
Q2 — Market/buyer/seller observation: [answer 2]
Q3 — Something said to a client: [answer 3]
```

If any answer is "nothing" or blank: write "Nothing to report" for that item. Do NOT fabricate or prompt for more.
If all three are empty: write `No recent past provided — write from professional expertise only.`

Write this block to `/tmp/linkedin_recent_past.txt` using the Write tool.

---

## Step 2: LinkedIn Analytics Check (Optional)

Ask: "Do you want me to check your LinkedIn analytics first? I'll pull last week's post performance and update the tracking files. Takes about 5 minutes. Yes or no?"

**If yes:**

First, attempt auto-scrape:
1. Use `mcp__firecrawl__firecrawl_interact` to navigate to `https://www.linkedin.com/in/matthieu-jammers-a40a0726/recent-activity/shares/`
2. Locate last Tuesday's, Wednesday's, and Thursday's posts
3. Extract for each: hook text (first line), impressions, reactions, comments
4. Infer the content pillar from the post type (Human/Perspective/Proof/Educator)

**If scraping succeeds:** log the data (format below), confirm results, then skip to Step 3.

**If scraping fails (login wall, blocked, or no data returned):** ask Matthieu:
> "LinkedIn blocked the scrape. Can you check your last three posts and give me the numbers? Just send: Tuesday: X impressions, Y reactions / Wednesday: X impressions, Y reactions / Thursday: X impressions, Y reactions. Or say 'skip' to move on."

If he provides numbers — log them. If he says skip — proceed to Step 3 without logging.

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

## Step 3: Generate Posts

Read `.claude/skills/linkedin-weekly-posts/prompt.md` in full — this contains all writing rules, pillars, themes, format specs, and quality checklist.

Read `/tmp/linkedin_recent_past.txt` for this week's personal context from Matthieu.

Then generate 4 post options following the prompt exactly:
- 2 options for **Tuesday** (same theme, two different pillars)
- 2 options for **Thursday** (same theme, two different pillars — theme must differ from Tuesday)

Weave the recent past input naturally into the posts where relevant (personal story, client observation, market insight). Do not force it — only use it if it genuinely strengthens the post.

Run the full quality checklist from `prompt.md` before outputting anything. If any item fails — rewrite before showing Matthieu.

---

## Step 4: Display Posts

Display all 4 options clearly using this structure:

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

THURSDAY [date] — [theme]
[same structure]
```

After displaying: ask "Which ones are you going with? I can humanize either one before you post."

---

## Step 5: Log the Chosen Posts

Once Matthieu confirms which options he's going with (e.g. "Tuesday Option 1, Thursday Option 2"), log each to `.claude/skills/linkedin-weekly-posts/posts_published.md`:

```
## [YYYY-MM-DD] ([Tuesday/Thursday])
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
- If Matthieu says "humanize it" after seeing a post, invoke the `humanizer` skill.
