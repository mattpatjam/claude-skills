# LinkedIn Posts Published

Log of all posts chosen and published. Used by the skill to avoid repeating themes and pillars from the last 60 days.
Engagement data (`Impressions`, `Reactions`, `Comments`, `Reposts`) is filled in the following week during the analytics check (Step 2).

MEASUREMENT SOURCE (changed 2026-10-13): figures come from the PROFILE ACTIVITY FEED, not the creator-analytics dashboard.
The dashboard under-reports badly (it gave 2,161 for a post the feed measured at 10,018, a 78% gap) and surfaces only ~3 posts where the feed had 8.
`linkedin_analytics.py` was rewritten on 2026-10-13 to read the feed per-post; it also had an off-by-one bug that paired each post's metrics with the NEXT post's text.
Run `--source both` to re-check the two sources against each other. Entries marked "profile feed, verified" were measured with the fixed scraper.

Earlier note: verified against LinkedIn's analytics dashboard on 2026-07-06. Several entries below were corrected from estimates that significantly under-reported real performance.

---

## 2026-10-28 (Tuesday) — PUBLISHED, measured 2026-11-03
Pillar: The Proof
Theme: Bali Market (unit mix / RevPAR per key)
Hook: "A three bedroom villa in Seminyak earns less per night than a two bedroom on the same street. Not per bedroom. In total."
Note: 1,355 chars. Leads with the Seminyak 1BR (IDR 1.80M/key, 74%) vs 3BR (IDR 424k/key, 45%) spread, then pivots
to why the source matters: Bestay operates the 623 villas, so the figure is a record rather than a projection.
Closes on the brokerage being built that way. Seminyak figures are SPENT, do not reuse them in another post.
Open: clearance to publish internal Bestay figures externally not yet confirmed by Matthieu. RESOLVED IN PRACTICE 2026-11-03: he published it, so Bestay portfolio figures have now gone out externally twice. Owner names, named underperforming villas and loss figures remain off limits.
Impressions: 1146 | Reactions: 6 | Comments: 3 | Reposts: 0 (profile feed, verified 2026-11-03, 6 days old. 0.79% engagement rate, mid-pack.)

## 2026-10-29 (Wednesday) — PUBLISHED, measured 2026-11-03
Pillar: The Educator
Theme: Bali Market (channel dependency / distribution)
Hook: "Ask whoever manages your villa what share of last month's bookings came from a single platform. If the answer is above two thirds, you are not running a rental business. You are renting one."
Note: 1,566 chars, close to the 1,600 ceiling, no room to add anything. Hangs on the 15 Oct cancellation window
change (60 days to 30) plus the channel split (68.6% Airbnb, 20.4% Booking.com, 6.91% direct, direct +90% YoY).
Includes the direct-booking platform push as an owner benefit, not a pitch. Channel split figures are SPENT.
Impressions: 664 | Reactions: 2 | Comments: 3 | Reposts: 0 (profile feed, verified 2026-11-03, 4 days old. 0.75% engagement rate. Lowest reach of the recent set, but 3 comments on 664 impressions is a decent reply rate: the "ask your manager X" construction pulls replies even when reach is small.)

## WEEK NOTE 2026-10-27
Thursday 2026-10-30 was written and then HELD at Matthieu's request, see "Held for future use" below.
So this week publishes 2 posts, not 3, which is on the healthy side given 20 posts went out in the five
weeks to 2026-10-27 against the skill's 2 to 3 per week.
NOT WRITTEN, by decision: a second hiring post. The "Week three in the new job" post (1,403 imp) already
announced both roles. Agreed alternative is to reshare Nathalia Valentine Trius's job post with a short
comment rather than spend a content slot. Reshare copy not yet drafted.

---

## ANALYTICS REFRESH 2026-10-27 (profile feed, `--all`)

Scraper returned `counters_found: 20 / posts_parsed: 20` but **every post came back with `age: None`**, so
the `--days` filter excluded all 20 (`excluded_no_date: 20`). Ran with `--all` to recover metrics.
BUG TO FIX: the age/date label parser is no longer matching the feed markup. Dates below are inferred
from content and ordering, not read from the feed. Impressions figures supersede earlier entries for the
same posts (numbers keep accruing as posts age).

Seven posts below had never been logged. Four of them are the week of 2026-10-20.

## 2026-10 (week of 10-20, exact date unconfirmed) — NEWLY LOGGED 2026-10-27
Pillar: The Proof
Theme: OLC Method Case Study (off-rotation)
Hook: "Three weeks ago I finished training the Nirvana Life sales team in Bali. They're now 70% sold o..."
Note: IMPORTANT CORRECTION TO THE 2026-10-20 READ. This is a pure proof/results post with a hard number
and it placed 3rd of 20 on reach with the 3rd-best reaction count. The earlier conclusion that "nothing
analytical came close to personal on reach" was wrong. Proof carrying a specific outcome number performs
at near personal-story level. Personal stories still take the top 2 slots, but the gap is a number, not a genre.
Impressions: 4991 | Reactions: 65 | Comments: 6 | Reposts: 0 (profile feed, verified 2026-10-27)

## 2026-10 (week of 10-20, exact date unconfirmed) — NEWLY LOGGED 2026-10-27
Pillar: The Perspective
Theme: Bali Market (macro fragility, Bali petrol queue + Lyon tourism office fire)
Hook: "Last week Bali queued seven hours for petrol and Lyon's tourism office was set on fire. Same we..."
Note: THIRD infrastructure-fragility post in roughly ten days (after the airport-luggage post and the fuel
shortage post). Out-reached both at 2,934 but drew 13 reactions and ZERO comments, a 0.44% engagement rate,
the worst of all 20 posts. Confirms the pattern: this frame still gets distributed and no longer gets replies.
Retire the macro-fragility frame.
Impressions: 2934 | Reactions: 13 | Comments: 0 | Reposts: 0 (profile feed, verified 2026-10-27)

## 2026-10 (week of 10-20, exact date unconfirmed) — NEWLY LOGGED 2026-10-27
Pillar: The Journey
Theme: New Role / Hiring (off-rotation)
Hook: "Week three in the new job, we are doing things differently and I am hiring for two roles that w..."
Note: Already announces the two open roles (Indonesian sales broker + admin/coordination). ANY further
hiring post this cycle is a repeat of this one. If more reach is wanted on the roles, comment on or reshare
Nathalia Valentine Trius's job post rather than spending a content slot.
Impressions: 1403 | Reactions: 14 | Comments: 1 | Reposts: 0 (profile feed, verified 2026-10-27)

## 2026-10 (week of 10-20, exact date unconfirmed) — NEWLY LOGGED 2026-10-27
Pillar: The Perspective
Theme: Brokerage Positioning (off-rotation)
Hook: "Most developers in Bali do not need another brokerage, all sending the same listing to the same..."
Note: Low reach (670) but 4 comments, a 1.49% engagement rate and one of the best comment rates of the set.
Already stakes out the "we are not another brokerage" positioning. Do not restate the thesis, only extend it
with evidence.
Impressions: 670 | Reactions: 6 | Comments: 4 | Reposts: 0 (profile feed, verified 2026-10-27)

## 2026-10 (week of 10-20, exact date unconfirmed) — NEWLY LOGGED 2026-10-27
Pillar: The Perspective
Theme: Bali Market (data verification)
Hook: "Bali does not have a demand problem or an oversupply problem. It has a data verification proble..."
Note: BEST COMMENT RATE OF ALL 20 POSTS. 5 comments on only 471 impressions, 1.06% comments-per-impression,
roughly 5x the account norm. Lowest reach, most conversation. Signal: this argument makes people reply even
when the algorithm barely distributes it. The thesis is now SPENT as a thesis. The unserved follow-up is the
evidence behind it (actual portfolio numbers), not the claim again.
Impressions: 471 | Reactions: 2 | Comments: 5 | Reposts: 0 (profile feed, verified 2026-10-27)

## 2026-10 (approx., exact date unconfirmed) — NEWLY LOGGED 2026-10-27
Pillar: The Educator
Theme: Legal Framework / Buying Process (hidden cost of waiting)
Hook: "For years, one of the biggest hidden costs of buying in Bali wasn't the price, it was the wait."
Impressions: 1050 | Reactions: 9 | Comments: 2 | Reposts: 0 (profile feed, verified 2026-10-27)

## 2026-10 (approx., exact date unconfirmed) — NEWLY LOGGED 2026-10-27
Pillar: The Proof
Theme: Deal Profile / Client Fit
Hook: "As sales, these are the kind of deals we love to close with a client that:"
Impressions: 898 | Reactions: 9 | Comments: 2 | Reposts: 0 (profile feed, verified 2026-10-27)

## REFRESHED FIGURES 2026-10-27 (posts already logged below, numbers have accrued)
- Departure post ("Yesterday was my last day..."): 10,650 imp | 101 re | 18 co (was 10,018 / 97 / 18)
- BSH announcement ("Five years in the same seat..."): 6,138 imp | 91 re | 20 co (was 5,566 / 86 / 19)
- Hugh Grant / weddings and funerals: 3,919 imp | 24 re | 1 co (was 3,852 / 24 / 1)
- Airport luggage: 2,546 imp | 15 re | 4 co (was 2,334 / 10 / 2)
- Nadal Lombok listing: 2,375 imp | 14 re | 0 co (was 230 / 3 engagements — the old figure was badly wrong)
- Bingin Beach rebuild: 1,845 imp | 19 re | 3 co | 1 rp (was 1,625 / 15 / 3 / 1)
- Swiss coffee group / observation period: 1,744 imp | 14 re | 0 co (was 1,555 / 11 / 0)
- Fuel shortage: 1,146 imp | 11 re | 2 co (was 829 / 6 / 1)
- Switzerland/Bali dual identity: 1,127 imp | 21 re | 2 co (was 52 / 1 engagement — old figure badly wrong)
- Villa management fee: 881 imp | 7 re | 0 co (was 850 / 6 / 0)
- Europe trip / laptop before anyone else: 799 imp | 9 re | 5 co
- Branded residences (BCG link): 498 imp | 6 re | 2 co (was 473 / 6 / 2) — still lowest reach, external link
- Tony Robbins post: 383 imp | 3 re | 2 co | 1 rp — weakest of the set

---

## 2026-10-13 (Monday) — PUBLISHED by Matthieu during the session
Pillar: The Perspective
Theme: Bali Market (management fee economics / labour costs)
Hook: "A villa management fee at half the market rate is not a discount. Somebody downstream absorbs it, and it is usually the person cleaning your villa."
Note: Tuesday Option 1 from the week of 2026-10-13, posted Monday instead. Argument: Badung's statutory minimum wage (IDR 3,791,003/month) is a fixed floor, so a halved management fee comes out of hours, headcount, benefits or insurance, which drives turnover and then service quality. Includes the line about being proud to work for a company that pays full salaries, benefits and health insurance, plus the point that owners choose the fee. NOTE: Matthieu's original "$200/month cleaner" figure was corrected to the statutory IDR 3.79M (~$210-230) before drafting, since $200 sits just below the legal minimum.
Impressions: 850 | Reactions: 6 | Comments: 0 | Reposts: 0 (profile feed, verified 2026-10-20)

## 2026-10-16 (Thursday) — PUBLISHED, confirmed on profile feed 2026-10-20
Pillar: The Educator
Theme: Legal Framework (Bingin Beach redevelopment / spatial planning)
Hook: "Remember the outcry when the government demolished 48 buildings at Bingin Beach. The rebuild plan is public now, and it is a lot smaller than people assumed."
Note: Only post selected for the week of 2026-10-13 (Matthieu chose Thursday only). 1,575 chars, humanized. Phase one itemised from PUPR head I Nyoman Karyasa's direct quote in NusaBali (18 May 2026, article 220990): beach access plus ~3m cliffside staircase, clean water network, rinse areas (tempat bilas), public toilets, land grading (pematangan lahan) for wooden stalls (kedai-kedai berbahan kayu) and a performance stage (stage pertunjukan). Phase two = 2027, scope never published. Commercial conclusion unique to this post: replacement frontage is government built on state land, allocated by the regency, so Bingin beachfront does not return as private leasable frontage.
DATE RESOLUTION: the "June or July" construction estimate applies to PHASE ONE physical work in 2026, not phase two in 2027. Honeycombers misattributed it to 2027 (and contradicted itself with mid-2026 in its own FAQ). NusaBali primary source is authoritative. Open item: unverified whether the tender was awarded or works began, flagged to Matthieu to check on the ground.
Impressions: 1625 | Reactions: 15 | Comments: 3 | Reposts: 1 (profile feed, verified 2026-10-20)

## 2026-10-17 (Friday) — PUBLISHED, single post written on request outside the normal weekly cycle
Pillar: The Perspective
Theme: Bali Market (macro infrastructure fragility / island fuel shortage)
Hook: "One tanker couldn't drop its anchor properly. Four days later, half of Bali couldn't get to work."
Note: Written 2026-10-15 on Matthieu's direct request (his own angle: dependence on petrol for everything, the cleaning lady, the doctor needing to reach an urgent procedure), paired with his own photo alone in the office. 1,384 chars, humanized. Facts verified against Euronews, Jakarta Globe, Tempo and Indonesia Expat: shortage began Sun 11 Oct, Pertamina blamed a tanker anchor problem delaying unloading plus road congestion and panic buying on subsidised Pertalite, 57.9M litres scheduled into Bali 14-17 Oct, one Denpasar resident queued ~7 hours.
POST-MORTEM (2026-10-20): underperformed. 829 impressions is the second-weakest of the fortnight. Two likely causes, both avoidable: (1) CANNIBALISATION, the airport-luggage post on ~10-13 ("the clearest infrastructure signal I have seen all year", 2,511 imp) made the same macro-fragility argument four days earlier, and the villa management fee post on 10-13 had already used the person-who-cleans-your-villa device; (2) VOLUME, 11 posts went out in the 14 days to 10-20, roughly 5 a week against the skill's 2-3, which is diluting reach per post. Lesson: check the last 7 days for argument overlap, not just the 60-day theme list, before committing to an angle.
Impressions: 829 | Reactions: 6 | Comments: 1 | Reposts: 0 (profile feed, verified 2026-10-20)

## 2026-10-09 (approx., 4d before check) — verified against profile activity feed 2026-10-13, missed entirely by the creator-analytics dashboard
Pillar: The Human
Theme: New Role / Observation Period (off-rotation, Far Past + Bali case)
Hook: "When I became Operations Director of a Swiss coffee group, I started changing things in month one. By month three, half the staff had stopped telling me anything."
Note: Far Past Swiss coffee group lesson (changed processes before understanding why they existed, lost the team through silence), tied to a Bali buyer who negotiated an Ubud plot directly with no agent, closed, then found a problem when a lawyer reviewed it. Closing line: "An observation period does not buy you information. It buys you the ability to tell a good deal apart from a good feeling." IMPORTANT: this post already covers the new-role / induction / observation-mode angle. Do not repeat it this cycle.
Impressions: 1555 | Reactions: 11 | Comments: 0 | Reposts: 0 (profile feed, verified)

## 2026-10 (approx., 1w before check) — verified against profile activity feed 2026-10-13, missed by the creator-analytics dashboard
Pillar: The Educator
Theme: Branded Residences / Price Premium
Hook: "Branded residential communities in Bali can sell for close to double the price/m2 of an identical unbranded villa down the road."
Note: built on BCG global real estate research (branded developments rent 20-30% more, sales premiums up to double), argument that buyers pay for the enforced guarantee behind the brand (quality standards, schedule, management locked in) rather than the name. Shared a BCG link, which likely suppressed reach. Lowest reach of the window.
Impressions: 473 | Reactions: 6 | Comments: 2 | Reposts: 0 (profile feed, verified)

## 2026-10 (approx., 1w before check) — verified against profile activity feed 2026-10-13, missed by the creator-analytics dashboard
Pillar: The Journey
Theme: Presence / Time (off-rotation, personal)
Hook: "Unlike Hugh Grant, I did not get four weddings and one funeral this year. I got two of each, and it happened in one month."
Note: two weeks off LinkedIn for family travel, reflection on treating a day as wasted unless something is produced. Teased the career news at the end. Strong performer on a purely personal angle.
Impressions: 3852 | Reactions: 24 | Comments: 1 | Reposts: 0 (profile feed, verified)

## 2026-10-08 (approx., 5d before check) — verified against profile activity feed 2026-10-13
Pillar: The Perspective
Theme: Bali Market (infrastructure angle)
Hook: "I waited two hours for my luggage at Bali airport last week. That is not a travel complaint, it is the clearest infrastructure signal I have seen all year."
Note: airport queue used as an entry point into what Bali is actually building. Highest impressions of the window but weakest engagement rate (0.52%), observational rather than personal-stake.
Impressions: 2334 | Reactions: 10 | Comments: 2 | Reposts: 0 (profile feed, verified)

## 2026-10 (approx., 1w before check) — verified against profile activity feed 2026-10-13
Pillar: The Journey
Theme: Career Transition (off-rotation, personal)
Hook: "Yesterday was my last day at Bali Exception Sales after five years."
Note: departure post, joined as junior salesperson and left as Senior Sales Manager. Paired with the Bali Superhost announcement below as a two-part sequence. CORRECTED 2026-10-13: the creator-analytics dashboard reported 2208 impressions / 13 engagements for this post, but the profile activity feed shows 10,018 impressions, 97 reactions and 18 comments. The profile feed is the reliable figure. Treat creator-analytics "top performing" numbers as a floor, not a measurement, and cross-check against the profile feed each week.
Impressions: 10018 | Reactions: 97 | Comments: 18 | Reposts: 0 (profile feed, verified 2026-10-13)

## 2026-10 (approx., 1w before check) — verified against profile activity feed 2026-10-13
Pillar: The Journey
Theme: Career Transition (off-rotation, personal)
Hook: "Five years in the same seat, and yesterday I walked into a company with more than 1,500 employees in Bali. Here is what I am actually doing there, I said I had news coming - this is it:"
Note: Bali Superhost / Director of Business Development announcement, dual remit (acquire villas/properties + brokerage). Best engagement rate of the window at 1.9% (86 reactions + 19 comments on 5,566 impressions) against 1.15% for the departure post, which out-reached it. Signal: personal-stake posts out-engage market commentary on this account right now.
Impressions: 5566 | Reactions: 86 | Comments: 19 | Reposts: 0 (profile feed, verified; creator-analytics dashboard had reported only 2137/28)

---

## 2026-09 (approx., within last 7 days) — from analytics check 2026-09-23, exact date/theme inferred from content, not confirmed against profile feed. Not logged when originally posted (4 week gap in this skill's use, per Matthieu — off work).
Pillar: The Perspective
Theme: Lombok Market
Hook: "I don't share listings here often. Every now and then, something crosses my desk worth breaking that rule for, this is one of those times."
Note: Rafa Nadal Tennis Academy broke ground on Lombok's south coast, land prices moved 20-30% since, framed as already-happened not forecast.
Impressions: 230 | Reactions: — | Comments: — | Reposts: — | Engagements: 3

## 2026-09 (approx., within last 7 days) — from analytics check 2026-09-23, exact date/theme inferred from content, not confirmed against profile feed. Not logged when originally posted.
Pillar: The Journey
Theme: Personal Identity (Switzerland/Bali, off-rotation, personal)
Hook: "I grew up here in Switzerland and I've built part of my life in Bali. Somewhere along the way I stopped being able to pick one."
Note: written while traveling/visiting family in Switzerland, contrasts a normal family afternoon there with a waiting client message, dual-identity reflection.
Impressions: 52 | Reactions: — | Comments: — | Reposts: — | Engagements: 1

---

## Held for future use (not yet published)
HELD 2026-10-27 at Matthieu's request, pulled from Thursday 2026-10-30. Slot into the next LinkedIn
posts session. Fully written and humanized, ready to publish as is.
Pillar: The Human
Theme: Bali Market (oversupply concentrated by product type)
Hook: "A buyer told me recently that Bali is finished. He owns a six bedroom villa in Canggu. Both of those things are true and only one of them is about Bali."
Length: 1,508 chars. Checked: no em dashes, no separator dashes, no curly quotes, no links, hook 152 chars.
Hashtags: #BaliRealEstate #BaliVilla #PropertyInvestment #ExpatBali #BuyingAbroad

Full text:
A buyer told me recently that Bali is finished. He owns a six bedroom villa in Canggu. Both of those things are true and only one of them is about Bali.

His villa ran under 50% occupancy this year. He reads that as a verdict on the market. I read it as a verdict on the product, and I understand why he would rather not hear the difference.

The market is genuinely softer. Listings up 10.5%, rates down 12.4%, occupancy around 61%.

But in the same twelve months, three bedroom villas in Sanur held 80.5% occupancy. Four bedroom villas on the Bukit earned IDR 1.10M per bedroom per night available on a IDR 6.6M rate.

One island, one year, the same tourists walking off the same planes.

What happened to him is not bad luck. Around 2021 and 2022 plenty of people built the same thing in the same few places, because that is what was selling. Those villas now compete with each other for the same group bookings.

The ones that quietly kept working were smaller, or elsewhere, or both.

If you are buying, here is the part of this that is actually useful. Ask whoever is selling to you where their occupancy numbers come from. Not a market report. Their own book. Someone who manages villas can show you twelve months of what those villas earned, by size and by area. Someone who only sells them cannot.

That gap is roughly the difference between ending up with his villa and ending up with the one in Sanur.

If you own here, have you compared your villa to the market, or to villas actually like yours?

Image Prompt: Documentary editorial photograph, late afternoon: a wide empty six bedroom villa living pavilion seen from the garden, sliding doors open, immaculate furnishing, no guests, a single staff member far in the background straightening a cushion. Warm low angled sunlight, long shadows across polished floor. Beautiful but unused, the emptiness is the subject. Photorealistic, no identifiable faces, 4:5 aspect ratio.

BEFORE PUBLISHING, RECHECK:
- Market figures (listings +10.5%, rates -12.4%, occupancy ~61%) come from the Sept 2026 Bestay monthly
  review. Confirm they have not moved before reposting in a later week.
- Confirm the Canggu six bedroom owner is not identifiable to anyone who knows the villa.
- Confirm clearance to publish internal Bestay portfolio figures externally.
- The Sanur 3BR 80.5% and Bukit 4BR IDR 1.10M/key figures are RESERVED FOR THIS POST. Do not spend them
  in another post in the meantime or this one loses its evidence.

---

Drafted 2026-07-13, bumped from the week of 2026-07-13 to make room for the tax free zone post. Ready to slot into a future week's Bali Market theme.
Pillar: The Perspective
Theme: Bali Market
Hook: "No skyscrapers. No trading floor. Indonesia still wants to turn a Bali island into a Dubai style financial hub."
Full text: 498 hectares on Serangan Island (Kura Kura), capped at 15 meter building height, designated pilot site for Indonesia's first International Financial Center, argument that legal independence (Dubai DIFC model) matters more than skyline.

---

## 2026-08-27 (approx.) — from analytics check 2026-08-31, exact date/theme inferred from content, not confirmed against profile feed
Pillar: The Proof
Theme: OLC Method Case Study (off-rotation — sales training result, not buyer-facing content)
Hook: "Three weeks ago I finished training the Nirvana Life sales team in Bali. They're now 70% sold out of their inventory."
Note: Nirvana Health Club sales training case study result, kept in touch with reps post-training. Best-performing post of the 08-25 to 08-31 window.
Impressions: 5000 | Reactions: — | Comments: — | Reposts: — | Engagements: 128

## 2026-08-22 (Saturday, approx.) — verified against profile activity feed 2026-08-26
Pillar: The Perspective
Theme: Bali Market
Hook: "Is a $200K ocean view villa in Bali a good investment? Wrong question."
Note: buyer pain-point angle, references a live Reddit r/bali thread with no real answer, six-point checklist (net yield, real occupancy, micro-market timing, exit liquidity, distinctive design, construction quality).
Impressions: 4602 | Reactions: ~31 | Comments: — | Reposts: — | Engagements: 64

## 2026-08-20 (Thursday, approx.) — verified against profile activity feed 2026-08-26
Pillar: The Journey
Theme: Personal Business Venture (off-rotation, personal — Lembongan project)
Hook: "Let the games begin...Yesterday I signed a 30 year lease that I think is the start of one of the better stories I'll get to tell for a while."
Note: 30 year lease on Jungutbatu's main commercial street, Nusa Lembongan, with wife Nathalie and business partner Clement Poulin. Best-performing post of the window.
Impressions: 5712 | Reactions: ~80 | Comments: — | Reposts: — | Engagements: 136

## 2026-08-19 (Wednesday, approx.) — verified against profile activity feed 2026-08-26
Pillar: The Human
Theme: Construction Due Diligence (property management angle)
Hook: "A (soon to be) client messaged me this week. His villa's management company won't show him the numbers."
Note: Uluwatu villa, rental management company withholding income/expense breakdown, argument to vet management company with same rigor as land before signing.
Impressions: 1544 | Reactions: — | Comments: — | Reposts: — | Engagements: 6

## 2026-08-18 (Tuesday, approx.) — verified against profile activity feed 2026-08-26
Pillar: The Perspective
Theme: Legal Framework (macro/trending)
Hook: "Everyone doubted Indonesia's Dubai style financial hub plan. On July 21st, it became law anyway."
Note: follow-up to the 2026-06-06 Kura Kura/Serangan Island post — Indonesia's parliament passed the PFII bill into law July 21, formalizing the International Financial Center framework. Includes notary/legal counsel disclaimer.
Impressions: 1044 | Reactions: — | Comments: — | Reposts: — | Engagements: 9

Note: a fifth post in this window ("My friend asked me why Scale-Rise and why target my home in Switzerland?", 2026-08-21 approx., 724 impressions / 14 engagements) is Scale-Rise content, tracked separately under the scale-rise-linkedin-posts skill, not logged here.

---

## 2026-08-13 (Thursday, approx.) — from analytics check, exact date/pillar/theme inferred from content, not confirmed against profile feed
Pillar: The Perspective
Theme: Lombok Market
Hook: "Everyone's racing to build villas in Lombok right now. I think most of them are building the wrong thing."
Impressions: 2000 | Reactions: — | Comments: — | Reposts: — | Engagements: 39

## 2026-08-12 (Wednesday, approx.) — from analytics check, exact date/pillar/theme inferred from content, not confirmed against profile feed
Pillar: The Proof
Theme: Bali Market
Hook: "For once, the Bali headline isn't another regulation or crackdown."
Note: Uluwatu Temple cliff seawall construction, infrastructure angle.
Impressions: 937 | Reactions: — | Comments: — | Reposts: — | Engagements: 9

## 2026-08-11 (Tuesday, approx.) — from analytics check, exact date/pillar/theme inferred from content, not confirmed against profile feed
Pillar: The Human
Theme: Negotiation & Deal Dynamics
Hook: "Six months ago a buyer walked away from a deal after weeks of negotiation. Yesterday I found out why."
Note: Australian client + father, Uluwatu plot, negotiation angle. Theme logged under the new "Negotiation & Deal Dynamics" name (renamed from "Sales Techniques" 2026-08-18, see prompt.md).
Impressions: 2000 | Reactions: — | Comments: — | Reposts: — | Engagements: 41

---

## 2026-08-06 (Thursday)
Pillar: The Journey
Theme: Bali Lifestyle (off-rotation, personal)
Hook: "Video calling my brother in NYC while riding the boat back from Nusa Lembongan, and for five minutes I genuinely questioned everything."
Impressions: 3110 | Reactions: ~37 | Comments: — | Reposts: — | Engagements: 53

## 2026-08-05 (Wednesday)
Pillar: The Perspective
Theme: Legal Framework
Hook: "Bali didn't close the door on foreign investment this year. It just started asking who's serious enough to walk through it."
Note: revised to add Matthieu's take that the crackdown targets small operators who used PT PMA tax incentives to skim/underpay tax on one small shop, not genuine serious investment.
Impressions: 7843 | Reactions: ~44 | Comments: — | Reposts: — | Engagements: 65

## 2026-08-04 (Tuesday)
Pillar: The Human
Theme: Sales Techniques
Hook: "A couple from Dubai landed in Bali last week to buy a villa. Two days later they signed for one that wasn't even on their shortlist."
Note: revised to add a beat on experience-built instinct (5 years, pattern recognition) before final post.
Impressions: 3978 | Reactions: ~32 | Comments: — | Reposts: — | Engagements: 25

---

## 2026-07-30 (Thursday)
Pillar: The Human
Theme: Sales Techniques
Hook: "I used to think I was doing a good job because I cleared everything on my to do list."
Impressions: 375 | Reactions: ~4 | Comments: — | Reposts: —

## 2026-07-29 (Wednesday)
Pillar: The Proof
Theme: Bali Market
Hook: "A friend bought land in Lombok eight months ago. This week someone offered him three times what he paid."
Impressions: 436 | Reactions: — | Comments: — | Reposts: — | Engagements: 11

## 2026-07-28 (Tuesday)
Pillar: The Perspective
Theme: Legal Framework
Hook: "Bali just closed foreign investors out of 18 business sectors overnight, real estate and hotels included, and most people haven't noticed yet."
Impressions: 4000 | Reactions: — | Comments: — | Reposts: — | Engagements: 60

---

## 2026-07-24 (Thursday)
Pillar: The Human
Theme: Construction Due Diligence
Hook: "Two buyers came to me the same week, both scared of the same thing, and picked completely opposite solutions."
Impressions: 380 | Reactions: — | Comments: — | Reposts: — | Engagements: 0

## 2026-07-23 (Wednesday)
Pillar: The Human
Theme: Sales Techniques
Hook: "Most agents treat discovery like a form: three questions, budget, timeline, done. That's not qualification, that's guessing with extra steps."
Impressions: 280 | Reactions: — | Comments: — | Reposts: — | Engagements: 8

## 2026-07-22 (Tuesday)
Pillar: The Perspective
Theme: Legal Framework
Hook: "New KBLIs for PT PMAs are coming next month. Last time this happened, nobody warned us before it hurt."
Impressions: 1000 | Reactions: — | Comments: — | Reposts: — | Engagements: 16

---

## 2026-07-17 (Thursday) — replacement post, personal/photo-led, off standard theme rotation
Pillar: The Human
Theme: Island Diversity (off-rotation, personal)
Hook: "Ask ten tourists where they've been in Bali and you'll get the same three answers back. Canggu, Uluwatu, Ubud."
Impressions: 871 | Reactions: — | Comments: — | Reposts: — | Engagements: 9

## 2026-07-16 (Wednesday) — moved up from originally planned Thursday slot
Pillar: The Perspective
Theme: Bali Market
Hook: "This tax free zone was never built for you. That might still be the best news Bali real estate has had all year."
Impressions: 3000 | Reactions: — | Comments: — | Reposts: — | Engagements: 13

## 2026-07-15 (Tuesday)
Pillar: The Human
Theme: Sales Techniques
Hook: "A buyer is granting me power of attorney today to sign for a villa he's never set foot in. Almost $1 million, on trust alone."
Impressions: 1000 | Reactions: — | Comments: — | Reposts: — | Engagements: 15

## 2026-07-09 (Thursday, approx.) — from analytics check
Pillar: The Human
Theme: Industry Behavior
Hook: "Being stood up by a client is disrespectful. I'm not going to pretend otherwise."
Impressions: 964 | Reactions: — | Comments: — | Reposts: — | Engagements: 27

## 2026-07-08 (Wednesday, approx.) — from analytics check
Pillar: The Perspective
Theme: Bali Market
Hook: "Funding project one with the sales from project two?"
Impressions: 861 | Reactions: — | Comments: — | Reposts: — | Engagements: 12

## 2026-07-07 (Tuesday, approx.) — from analytics check
Pillar: The Human
Theme: Construction Due Diligence
Hook: "Is this normal construction quality?"
Impressions: 1000 | Reactions: — | Comments: — | Reposts: — | Engagements: 17

## 2026-07-02 (Thursday)
Pillar: The Educator
Theme: Sales Techniques
Hook: "Most deals stall at the offer stage because convincing still needs to happen there."
Impressions: 168 | Reactions: — | Comments: — | Reposts: —

## 2026-07-01 (Wednesday)
Pillar: The Perspective
Theme: Bali Market
Hook: "Developers in Bali are building for daily rental. The people who actually live here can barely find a house."
Impressions: 1937 | Reactions: 25 | Comments: — | Reposts: —

## 2026-06-30 (Tuesday)
Pillar: The Educator
Theme: Sales Techniques
Hook: "What is value in Real Estate ?"
Impressions: 573 | Reactions: 14 | Comments: — | Reposts: —

## 2026-06-29 (Monday) — corrected from 06-24
Pillar: The Educator
Theme: Lombok Market
Hook: "The Indonesian government put over $3 billion into Lombok's Mandalika region."
Impressions: 4347 | Reactions: 34 | Comments: 10 | Reposts: —

## 2026-06-28 (Sunday, approx.) — corrected from 06-23
Pillar: The Human
Theme: Industry Behavior
Hook: "Another agent blocked me from entering a property viewing last week."
Impressions: 1738 | Reactions: 30 | Comments: — | Reposts: —

## 2026-06-26 (Friday)
Pillar: The Perspective
Theme: Bali Market
Hook: "Bali has been here before: new regulations, new panic, same ending."
Impressions: 2000 | Reactions: 27 | Comments: — | Reposts: —

## 2026-06-19 (Friday)
Pillar: The Perspective
Theme: Bali Market
Hook: "Bali has no mortgage market. Most people treat that as a quirk, I think it is the most underappreciated structural feature of this market."
Impressions: 2000 | Reactions: — | Comments: — | Reposts: —

## 2026-06-15 (Monday, approx.) — corrected from 06-17
Pillar: The Human
Theme: Sales Techniques
Hook: "The urgency tactic that closes deals in the US just cost me one in Bali. I've been here five years, I should have known better."
Impressions: 3268 | Reactions: 31 | Comments: 13 | Reposts: —

## 2026-06-12 (Friday)
Pillar: The Proof
Theme: Sales Techniques
Hook: "A deal almost died last week. Not because of price, not because of due diligence, and not because the property had a problem."
Impressions: 392 | Reactions: — | Comments: — | Reposts: —

## 2026-06-06 (Saturday, approx.) — newly discovered, not previously logged
Pillar: The Perspective
Theme: Bali Market
Hook: "Nobody builds a financial center in Bali, that's exactly the point."
Impressions: 34009 | Reactions: 458 | Comments: 98 | Reposts: 0
Note: best-performing post by a wide margin (10x the next best). Bold global comparison (Bali vs Dubai DIFC) on a breaking infrastructure announcement. Reference for future Perspective/Trending posts and the Monthly Thought Leadership slot.

---

## Reference only — outside 60-day rotation window

## 2026-04-06 (approx.)
Pillar: The Perspective
Theme: Sales Techniques
Hook: "One of the biggest myths about being a broker is flexibility."
Impressions: 2518 | Reactions: — | Comments: — | Reposts: —
Note: strong evergreen performer, over 60 days old so not counted in active rotation/averages, but a candidate to revisit with a fresh angle later.
