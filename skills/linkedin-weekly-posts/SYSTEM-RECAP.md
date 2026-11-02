# LinkedIn Content System, Full Recap

*Written 2026-11-01. Portable brief for running the system from the Claude Desktop app.*

---

## 1. What exists

Two separate skills, both posting from Matthieu's **personal** LinkedIn account, deliberately kept apart (separate voice, separate audience, separate tracking files, never merged):

| Track | Skill name | Audience | Cadence | Volume |
|---|---|---|---|---|
| Real estate / villa management | `linkedin-weekly-posts` | Villa owners and developers (primary), agents and legal partners (referral), investors and buyers (brokerage). Retargeted 2026-11-02 from the old foreign-buyer audience | Tue, Wed, Thu, 6 options per week (2 per day) | 59 logged entries, April 2026 to Oct 2026 |
| Scale-Rise (AI automation) | `scale-rise-linkedin-posts` | Ops managers, founders, directors at B2B service businesses in Europe (Switzerland first) | Once a week, only on explicit request | 3 logged entries, July to Aug 2026 |

Plus a third, portable spin-off: a plain Claude.ai Project version of the system with no tool dependencies, built for Nathalie. That one is the closest existing template for a Desktop-app setup.

---

## 2. File locations (absolute paths)

All of this lives in its own git repo: **github.com/mattpatjam/claude-skills**, checked out at `/Users/matt/Desktop/Claude/.claude/`.

### Real estate track
```
/Users/matt/Desktop/Claude/.claude/skills/linkedin-weekly-posts/
├── SKILL.md                      332 lines   the 8 step workflow Claude follows
├── prompt.md                     796 lines   all writing rules, pillars, themes, format spec, quality checklist
├── voice_reference.md             82 lines   his 5 best posts by engagement rate, as published, rebuilt monthly
├── posts_published.md            493 lines   59 logged posts with engagement numbers
├── post_analytics.json            59 lines   pillar and theme counters, pillar performance averages, known bugs
├── linkedin_analytics.py         352 lines   profile feed scraper (primary)
└── linkedin_analytics_90d.py     171 lines   creator analytics 90 day window (monthly companion)
```

### Scale-Rise track
```
/Users/matt/Desktop/Claude/.claude/skills/scale-rise-linkedin-posts/
├── SKILL.md                      208 lines
├── prompt.md                     271 lines
├── posts_published.md             32 lines
└── post_analytics.json            21 lines
```
No scraper of its own. It reuses `linkedin_analytics.py` from the real estate folder (same account) and isolates its own post by matching the hook text.

### Supporting files
```
/Users/matt/Desktop/Claude/.venv/bin/python3        python 3.12, runs the scrapers
/Users/matt/Desktop/Claude/.env                      LI_AT (the only cookie this skill uses since 2026-11-02; FB_C_USER and FB_XS remain in the file but are no longer read here)
/Users/matt/Desktop/Claude/Personal/wife-linkedin-content-prompt.md    portable no-tools version
```

### The older email automation (separate thing, mostly superseded)
- Repo: **github.com/scale-rise/linkedin-automation** (private). The old `github.com/scalrize/...` URL 301 redirects there.
- GitHub Actions, Sundays 23:45 UTC, emailed 6 post options to matthieu.jammers@gmail.com.
- The local folder `Automations/linkedin-automation/` **no longer exists** in the workspace. `Automations/` now holds only `investment-newsletter/` and `knowledge-dashboard/`. CLAUDE.md still references the old path, so that line is stale.
- In practice the skill-driven flow replaced it: posts are generated on request in-session, not emailed.

---

## 3. The workflow (8 steps, identical shape on both tracks)

1. **Gather recent past.** 4 questions, asked one at a time, never bundled. Real estate asks about the week's deals, client conversations, market observations. Scale-Rise asks about client delivery, cold outreach lessons, what's unresolved, what a prospect said. Written to a temp file. If an answer is "nothing", write "Nothing to report", never fabricate.
2. **Analytics check.** Run the scraper, log last week's numbers into `posts_published.md`, recalculate pillar averages in `post_analytics.json`.
3. **Research.** Scrape Matthieu's own profile (last 60 days of topics, to avoid repeats), Terje H. Nilsen's newsletter, 2 or more news sources (The Bali Sun, Jakarta Post property, Bali Discovery, Indonesia Expat, Nikkei Asia Indonesia), and owner/investor pain point sources (Reddit r/bali and Quora. Facebook group scraping was dropped 2026-11-02, it needed Matthieu's personal session cookie and risked his account). Summarize in 3 to 5 bullets.
4. **Select themes and pillars, get approval before writing a word.**
5. **Generate posts.** 6 options for real estate (2 per day, same theme per day, different pillars), 2 options for Scale-Rise.
6. **Display.** Each option shows hook, full post text, hashtag line, strategic rationale, and a full ready to paste AI image prompt.
7. **Humanize.** The `humanizer` skill runs automatically on the chosen posts. Never waits to be asked.
8. **Log.** Date, pillar, theme, hook into `posts_published.md` with engagement fields left blank, filled in next run. Increment the pillar counter in `post_analytics.json`.

Matthieu posts manually at 11:00 AM WITA. Nothing auto-publishes.

---

## 4. Content pillars and themes

### Real estate, 4 pillars (was 5 until 2026-11-02)
1. The Educator (practical how-to, checklist, pure utility)
2. The Perspective (contrarian take on an industry belief)
3. The Human (anything from the field with a person in it: personal lesson, anonymized client story, a deal that nearly fell through, or a thought forming now while he builds the brokerage. Professional only, no personal ventures)
4. The Proof (specific result, case study, data. Needs one hard verified number or it is not a Proof post)

The Journey was merged into The Human on 2026-11-02. The two overlapped and the split
made the strongest pillar compete with itself. Pre-merge history is preserved in
`post_analytics.json` under `_retired_The_Journey`.

### Real estate, 4 themes (rewritten 2026-11-02 for the Bali Superhost remit)
1. Rental Performance and Management (what drives a villa's income, from the owner's side)
2. Bali Villa and Rental Market (occupancy, nightly rates, supply by area, seasonality. Verified numbers only)
3. Owner Legal and Licensing (rental licensing and compliance, tax on rental income. Always ends with the notary disclaimer)
4. Buying for Income and New Projects (reading rental projections, what developers should plan before handover, what makes a villa rent)

The old themes (Negotiation and Deal Dynamics, Legal Framework for Foreign Buyers,
Construction Due Diligence) belonged to the Bali Exception buyer-side role and were
retired with it. Counts against those names stay in `post_analytics.json` as history.

### The 80/20 rule
Of the 3 posts published per week, at most 1 is a broad macro or thesis take (impressions focused). The other 2 are ground level, specific, grounded in real deal friction (engagement focused).

### Scale-Rise, 4 pillars
Proof / Case Studies, Educator, Behind the Build, Industry Perspective.

### Scale-Rise, 4 themes
AI Automation and Operations, Client Work and Results, Cold Outreach and Sales Systems, Founder Journey.

Rotation rule on both tracks: never the same pillar twice in a row, never a theme repeated inside 60 days, the two options for a given day must use different pillars.

---

## 5. Format spec (both tracks)

- Length (real estate track, revised 2026-11-02): hard ceiling 1,600 characters, never exceeded. Most posts 800 to 1,600. Short posts of 300 to 700 are welcome and at least one of the week's 6 options must be one. Lengths must visibly vary, no two options on the same day within 200 characters of each other.
- Hook: under 200 characters, lines 1 and 2, must create an open loop. One of: surprising statistic, bold claim, painful recognizable question. No emoji on line 1. No "I'm thrilled", no throat clearing.
- Hook components to combine (pick 2 or 3): recency, relevancy, celebrity, proximity, conflict, unusual, ongoing.
- Body: no paragraph over 3 lines, one idea per paragraph, max 5 bullets per list, exactly one verified data point, active voice.
- Retention tools: lists, steps, stories. Story arc in 3 beats (tension or gap, insight or turning point, resolution that feeds the CTA).
- CTA: a genuine low friction question, never a command. No external links in the body.
- Emoji: max 3, none on line 1. Hashtags: max 5, last line of the post.
- "Teach what, not how." If a reader could do Matthieu's job after reading the post, rewrite it.
- **No em dashes, no dashes of any kind as separators.** Enforced during drafting, not as a cleanup pass. Any post containing one gets rewritten before display.
- Once a month: a longer thought leadership post (1,400 to 1,600 chars) on a bigger, more opinionated topic.

---

## 6. What the data says so far (real estate track, as of 2026-10-27)

Pillar performance, average impressions (pre-merge figures, which is how they were measured):
- The Perspective: 5,088 over 14 posts (skewed by one 34,009 outlier, median closer to 900 to 2,000)
- The Journey: 4,869 over 5 posts (now merged into The Human)
- The Proof: 2,200 over 6 posts
- The Educator: 1,696 over 3 posts
- The Human: 1,459 over 11 posts (now 2,525 over 16 posts after absorbing The Journey)

Note on the merge: Journey posts out-reached Human posts by more than 3x, so the
merged 2,525 average flatters the old Human material. Do not read a post landing
below 4,869 as a decline against the old Journey number.

Learnings worth carrying forward:
- **Creator analytics under-reports badly.** On 2026-10-13 the dashboard showed 2,161 impressions for a post the profile feed showed at 10,018, a 78% gap, and surfaced only 3 posts where the feed had 8. The profile activity feed is the source of truth.
- **The differentiator is a hard number, not the genre.** A Proof post carrying a specific outcome (Nirvana sales training, "70% sold out") hit 4,991 impressions and 65 reactions, 3rd of 20 posts. That overturned the earlier conclusion that analytical posts cannot reach personal-story levels.
- **Personal stake framing out-engages market commentary** on this account currently. The Bali Exception departure post hit 10,018 / 97 / 18 and the Bali Superhost arrival post 5,566 / 86 / 19 (1.9% engagement rate, best of the October window).
- Impressions cluster tightly on this account, engagement rate separates posts sharply. Use engagement rate, not raw reach, to judge a post.

Theme counts to date: Bali Market 11, Sales Techniques 8 (now renamed Negotiation and Deal Dynamics, 1), Legal Framework 5, Construction Due Diligence 3, Lombok Market 3, plus several off-rotation personal posts.

Scale-Rise track is thin: 3 posts, best at 724 impressions / 14 engagements (the Switzerland SME angle, 8% of European companies with 10+ employees actually use AI). Two of the three were posted outside the workflow and logged retroactively.

---

## 7. Known issues and open items

- **Scraper date parser is broken.** On 2026-10-27 `linkedin_analytics.py` returned `age: None` for all 20 posts, so `--days` excluded every one. Workaround is `--all`. The date label parser no longer matches LinkedIn's feed markup. Needs fixing before the windowed output can be trusted.
- **One post is held, unpublished.** A Thursday 2026-10-30 post (The Human, Bali market oversupply by product type) was written and humanized then held on 2026-10-27. Full text sits in `posts_published.md` under "Held for future use". The Sanur 3BR 80.5% and Bukit 4BR IDR 1.10M per key figures are reserved for it and must not be reused in another post before it runs.
- Two more are marked SELECTED, humanized, awaiting publish (2026-10-28 Tuesday, 2026-10-29 Wednesday).
- Scale-Rise research steps 3 and 4 (competitor accounts, AI/SaaS thought leaders) are empty placeholders. No profiles configured yet.
- `li_at` cookie expires periodically. Refresh path: Chrome, LinkedIn, DevTools F12, Application, Cookies, `.linkedin.com`, `li_at`, copy the Value, paste into the `LI_AT=` line in `/Users/matt/Desktop/Claude/.env`.
- CLAUDE.md still lists `Automations/linkedin-automation/` as a local folder. It is gone.

---

## 8. Running this from the Claude Desktop app

### What carries over cleanly
The whole thinking layer. Pillars, themes, the 80/20 mix, format spec, quality checklist, rotation rules, the 8 step shape, and the historical performance data in section 6. None of that needs tools.

### What does not carry over
Three dependencies are local to this machine and will not work in Desktop unless you wire them up:

1. **The scraper** (`linkedin_analytics.py`) needs Python 3.12 at `/Users/matt/Desktop/Claude/.venv/bin/python3` plus the `scrapling` package (`DynamicFetcher`). Desktop has no shell.
2. **Research scraping** uses the Scrapling MCP server with cookies attached on every call. Desktop would need its own web fetch capability, and LinkedIn behind a login wall will not open for it.
3. **The tracking files.** `posts_published.md` and `post_analytics.json` are what prevent topic repeats inside 60 days. Desktop cannot read or write them unless you give it filesystem access.

### Recommended setup for Desktop
Mirror the pattern already built for Nathalie in `/Users/matt/Desktop/Claude/Personal/wife-linkedin-content-prompt.md`:

1. Create a Claude.ai **Project** called "LinkedIn Content".
2. Paste `prompt.md` (the full 796 lines) into **Custom instructions**. That is the writing engine.
3. Add as **Project knowledge** files: `posts_published.md` (so it knows what has run), `post_analytics.json` (so it knows what performs), and this recap.
4. Replace Step 2 (analytics) with manual input: paste last week's numbers from the LinkedIn feed into the chat.
5. Replace Step 3 (research) with manual input, or let Desktop web search for news and skip the LinkedIn scrape.
6. Keep Steps 1, 4, 5, 6, 7, 8 exactly as they are. Step 8 becomes "output the log entry, Matthieu pastes it back into the file".
7. Re-upload the two tracking files to Project knowledge every few weeks so the repeat check stays accurate.

Alternative, if you want the full automated version in Desktop: connect a filesystem MCP server pointed at `/Users/matt/Desktop/Claude/` and a browser or scraping MCP. Then the skills run close to as they do here.

---

## 9. Quick reference, how to trigger

| What you want | Say this |
|---|---|
| Real estate posts for the week | "generate my LinkedIn posts" or "do this week's LinkedIn content" |
| Scale-Rise post | "generate my Scale-Rise LinkedIn post" |
| Analytics only | "check my LinkedIn and update the tracking files" |
| Monthly 90 day view | run `linkedin_analytics_90d.py` |
