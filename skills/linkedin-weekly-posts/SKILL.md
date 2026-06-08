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

Working directory for all generation steps: `Automations/linkedin-automation/`

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
1. Use `mcp__firecrawl__firecrawl_interact` to navigate to Matthieu's LinkedIn activity page:
   `https://www.linkedin.com/in/matthieu-jammers-a40a0726/recent-activity/shares/`
2. Locate last Tuesday's and Thursday's posts
3. Extract for each: hook text (first line), impressions, reactions, comments
4. Infer the content pillar from the post type (Human/Perspective/Proof/Educator)
5. Append entries to `Automations/linkedin-automation/posts_published.md` in this format:
   ```
   ## [YYYY-MM-DD] ([Tuesday/Thursday])
   Pillar: [pillar]
   Theme: [theme]
   Hook: "[hook text]"
   Impressions: [n] | Reactions: [n] | Comments: [n] | Reposts: [n]
   ```
6. Recalculate pillar averages in `Automations/linkedin-automation/post_analytics.json` and update `last_updated`
7. Confirm to Matthieu: "Analytics updated. [Tuesday hook] got X impressions. [Thursday hook] got Y impressions."

**If no:** skip to Step 3.

**If LinkedIn is inaccessible or not logged in:** tell Matthieu and proceed to Step 3 without updating files.

---

## Step 3: Generate Posts

Run this Python script via Bash from `Automations/linkedin-automation/`:

```bash
cd /Users/matt/Desktop/Claude/Automations/linkedin-automation && python3 -c "
import os

with open('.env') as f:
    for line in f:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            os.environ[k] = v

with open('/tmp/linkedin_recent_past.txt') as f:
    recent_past = f.read()

from generate_post import generate_all_posts

scraping_context = 'Scraping unavailable. Write from professional expertise only. Do not fabricate market data.'
results = generate_all_posts(scraping_context, is_give_ask_week=False, recent_past=recent_past)

import json, builtins
with builtins.open('/tmp/linkedin_results.json', 'w') as f:
    json.dump(results, f, default=str)
print('DONE')
" 2>&1
```

Tell Matthieu: "Generating posts now. Takes 1-2 minutes." before running.

If it fails: show the error, diagnose, and fix before retrying.

---

## Step 4: Display Posts

After generation completes, read `/tmp/linkedin_results.json` and display all 4 options clearly using this structure:

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

## Notes

- Step 1 is always first. Never jump to generation without the 3 questions.
- Do not send email. Session display is the delivery for the interactive workflow.
- Character count warnings are non-fatal. LinkedIn's actual limit is 3,000 chars. The 1,400-1,700 target is a readability guideline.
- The Give:Ask week detection uses `post_tracker.json`. For manual session runs, `is_give_ask_week=False` is correct — Give:Ask is handled by the Sunday GitHub Actions run.
- If Matthieu says "humanize it" after seeing a post, invoke the `humanizer` skill.
