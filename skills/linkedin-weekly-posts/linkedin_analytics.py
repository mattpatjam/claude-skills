#!/usr/bin/env python3
"""
Scrapes Matthieu's LinkedIn post performance. Outputs JSON to stdout.
Uses the li_at session cookie from .env (never printed).

Default source is the PROFILE ACTIVITY FEED, not creator analytics.

Why: the creator-analytics "Top performing posts" widget under-reports badly
(it showed 2,208 impressions for a post the profile feed reported at 9,999 on
2026-10-13) and only surfaces ~3 posts. The profile feed carries every post with
its real counts.

Each post is extracted from its own DOM container, so a post's text can never be
paired with another post's metrics. The previous version parsed a flat innerText
slice and searched FORWARD from the metric line for the next "Feed post" block,
which attached every metric to the following post's text.

Usage:
    .venv/bin/python3 .claude/skills/linkedin-weekly-posts/linkedin_analytics.py
    ... --days 14           # widen the window (default 7)
    ... --all               # no date filter
    ... --source analytics  # old creator-analytics widget
    ... --source both       # scrape both and report the discrepancy
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

PROFILE_URL = "https://www.linkedin.com/in/matthieu-jammers-a40a0726/recent-activity/all/"
ANALYTICS_URL = "https://www.linkedin.com/analytics/creator/content/"

env_path = Path(__file__).parent.parent.parent.parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

LI_AT = os.environ.get("LI_AT", "")
if not LI_AT:
    print(json.dumps({"error": "LI_AT not set in .env"}))
    sys.exit(1)

from scrapling.fetchers import DynamicFetcher


def _setup(page):
    page.context.add_cookies([{
        "name": "li_at",
        "value": LI_AT,
        "domain": ".linkedin.com",
        "path": "/",
        "secure": True,
        "httpOnly": True,
    }])


# Each post is read from its own container. We locate the "N impressions" leaf,
# climb to the nearest ancestor that also holds the post body, then pull text and
# metrics from inside that one container only.
PROFILE_JS = r"""() => {
    const warnings = [];
    const isLoggedIn = !document.querySelector('form.login__form, a[href*="/login"]')
                       && !!document.querySelector('nav, [class*="global-nav"]');

    const impRe = /^([\d.,]+)\s*(K|M)?\s+impressions?$/i;
    const leaves = Array.from(document.querySelectorAll('span, div, a, p'))
        .filter(el => el.children.length === 0 && impRe.test((el.textContent || '').trim()));

    const seen = new Set();
    const posts = [];

    for (const leaf of leaves) {
        // Climb to a container that holds both this counter and real body text.
        let node = leaf, container = null;
        for (let i = 0; i < 14 && node; i++) {
            node = node.parentElement;
            if (!node) break;
            const t = (node.innerText || '');
            if (t.length > 300 && /impressions?/i.test(t)) { container = node; break; }
        }
        if (!container) { warnings.push('no container for: ' + leaf.textContent.trim()); continue; }
        if (seen.has(container)) continue;
        seen.add(container);

        // Body text, from inside this container only.
        let body = '';
        for (const sel of ['[class*="update-components-text"]',
                           '[class*="feed-shared-update-v2__description"]',
                           '[class*="feed-shared-inline-show-more-text"]',
                           '[class*="update-components-update-v2__commentary"]']) {
            const el = container.querySelector(sel);
            if (el && (el.innerText || '').trim().length > 40) { body = el.innerText.trim(); break; }
        }
        if (!body) {
            // Fallback: longest line block in the container that is not chrome.
            const lines = (container.innerText || '').split('\n').map(s => s.trim());
            const chrome = /^(Matthieu Jammers|Feed post|View analytics|Boost|Promote this post|Like|Comment|Repost|Send|•\s*You|\+\d+|\d+(st|nd|rd|th)?|…\s*more|This post type)/i;
            const cands = lines.filter(l => l.length > 60 && !chrome.test(l) && !impRe.test(l));
            if (cands.length) body = cands.sort((a, b) => b.length - a.length)[0];
            if (body) warnings.push('body via fallback heuristic');
        }
        body = body.replace(/\s*…\s*more\s*$/i, '').trim();

        // Metrics, from inside this container only.
        const ctext = container.innerText || '';
        const impM = ctext.match(/([\d.,]+)\s*(K|M)?\s+impressions?/i);
        let impressions = null, impRounded = false;
        if (impM) {
            const n = parseFloat(impM[1].replace(/,/g, ''));
            const unit = (impM[2] || '').toUpperCase();
            if (unit === 'K') { impressions = Math.round(n * 1000); impRounded = true; }
            else if (unit === 'M') { impressions = Math.round(n * 1000000); impRounded = true; }
            else { impressions = Math.round(n); }
        }

        const pick = (sels) => {
            for (const s of sels) {
                const el = container.querySelector(s);
                if (!el) continue;
                const m = (el.getAttribute('aria-label') || el.innerText || '').match(/[\d,]+/);
                if (m) return parseInt(m[0].replace(/,/g, ''), 10);
            }
            return null;
        };
        const reactions = pick(['[class*="social-details-social-counts__reactions-count"]',
                                '[class*="social-details-social-counts__social-proof-fallback-number"]',
                                'button[aria-label*="reaction"]']);
        const comments = pick(['[class*="social-details-social-counts__comments"] button',
                               '[class*="social-details-social-counts__comments"]',
                               'button[aria-label*="comment"]']);
        const reposts = pick(['button[aria-label*="repost"]', '[class*="social-details-social-counts__item--right-aligned"] button']);

        const ageM = ctext.match(/(?:^|\n)\s*(\d+)\s*(m|h|d|w|mo|yr)\s*(?:•|\n)/i)
                  || ctext.match(/\b(\d+)(m|h|d|w|mo|yr)\b\s*•/i);
        const age = ageM ? (ageM[1] + ageM[2].toLowerCase()) : null;
        if (!age) warnings.push('no age label for: ' + body.slice(0, 50));

        posts.push({
            impressions, impressions_rounded: impRounded,
            reactions, comments, reposts,
            age,
            hook: body.split('\n')[0].slice(0, 220),
            text_preview: body.slice(0, 400),
            full_len: body.length,
        });
    }

    return { isLoggedIn, url: location.href, counters_found: leaves.length,
             posts, warnings };
}"""

ANALYTICS_JS = r"""() => {
    const isLoggedIn = !document.querySelector('form.login__form, a[href*="/login"]')
                       && !!document.querySelector('nav, [class*="global-nav"]');
    const all = document.body.innerText || '';
    const i = all.indexOf('Top performing posts');
    return { isLoggedIn, url: location.href,
             section: i >= 0 ? all.substring(i, i + 12000) : '' };
}"""

AGE_DAYS = {"m": 0, "h": 0, "d": 1, "w": 7, "mo": 30, "yr": 365}


def age_to_days(age):
    if not age:
        return None
    m = re.match(r"^(\d+)(m|h|d|w|mo|yr)$", age)
    if not m:
        return None
    return int(m.group(1)) * AGE_DAYS[m.group(2)]


def fetch(url, js, scroll=0):
    store = {}

    def action(page):
        try:
            for _ in range(scroll):
                page.mouse.wheel(0, 4000)
                page.wait_for_timeout(1200)
            store["result"] = page.evaluate(js)
        except Exception as e:
            store["error"] = str(e)

    try:
        DynamicFetcher.fetch(url, page_setup=_setup, page_action=action,
                             network_idle=True, wait=5000, headless=True)
    except Exception as e:
        store["error"] = f"fetch failed: {e}"
    return store


def scrape_profile(days, scroll):
    s = fetch(PROFILE_URL, PROFILE_JS, scroll=scroll)
    if "error" in s:
        return {"error": s["error"]}
    r = s.get("result", {})
    if not r.get("isLoggedIn") or "login" in (r.get("url") or "").lower():
        return {"error": "Not authenticated, li_at cookie may have expired"}

    posts = r.get("posts", [])
    for p in posts:
        p["age_days"] = age_to_days(p.get("age"))
    if days is not None:
        kept = [p for p in posts if p["age_days"] is not None and p["age_days"] <= days]
        undated = [p for p in posts if p["age_days"] is None]
    else:
        kept, undated = posts, []

    kept.sort(key=lambda p: (p.get("impressions") or 0), reverse=True)
    out = {
        "source": "profile_feed",
        "window": "all" if days is None else f"{days} days",
        "counters_found": r.get("counters_found"),
        "posts_parsed": len(posts),
        "posts": kept,
    }
    if undated:
        out["excluded_no_date"] = len(undated)
    warn = list(r.get("warnings") or [])
    if r.get("counters_found", 0) > len(posts):
        warn.append(f"{r['counters_found']} counters seen but only {len(posts)} posts parsed")
    if any(p.get("impressions_rounded") for p in kept):
        warn.append("some impressions were displayed rounded (K/M) and are approximate")
    if warn:
        out["warnings"] = warn
    return out


def scrape_analytics():
    s = fetch(ANALYTICS_URL, ANALYTICS_JS)
    if "error" in s:
        return {"error": s["error"]}
    r = s.get("result", {})
    if not r.get("isLoggedIn"):
        return {"error": "Not authenticated, li_at cookie may have expired"}

    section = r.get("section", "")
    posts = []
    # Metrics come AFTER the body on this page too, so slice backwards from each
    # metric line to the previous one. Never search forward for the text.
    hdr = re.compile(r"([\d,.]+K?)\s+impressions\s*[•·]\s*([\d,.]+)\s+engagements?", re.I)
    ms = list(hdr.finditer(section))
    for i, m in enumerate(ms):
        raw = m.group(1)
        rounded = raw.upper().endswith("K")
        imp = int(float(raw[:-1]) * 1000) if rounded else int(raw.replace(",", ""))
        start = ms[i - 1].end() if i else 0
        block = section[start:m.start()]
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        chrome = re.compile(r"^(Matthieu Jammers|Feed post|View analytics|Boost|Promote|Like|Comment|Repost|Send|•|\+\d+|\d+$|This post type)", re.I)
        body = [l for l in lines if len(l) > 60 and not chrome.match(l)]
        text = max(body, key=len) if body else ""
        posts.append({
            "impressions": imp, "impressions_rounded": rounded,
            "engagements": int(m.group(2).replace(",", "")),
            "hook": text.split("\n")[0][:220], "text_preview": text[:400],
        })
    out = {"source": "creator_analytics", "window": "7 days", "posts": posts}
    if any(p["impressions_rounded"] for p in posts):
        out["warnings"] = ["creator analytics rounds to K, values are approximate and historically under-report; prefer profile_feed"]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--source", choices=["profile", "analytics", "both"], default="profile")
    ap.add_argument("--scroll", type=int, default=8)
    a = ap.parse_args()
    days = None if a.all else a.days

    if a.source == "profile":
        res = scrape_profile(days, a.scroll)
    elif a.source == "analytics":
        res = scrape_analytics()
    else:
        prof, anal = scrape_profile(days, a.scroll), scrape_analytics()
        res = {"profile_feed": prof, "creator_analytics": anal}
        if "posts" in prof and "posts" in anal:
            pm = {p["hook"][:40]: p.get("impressions") for p in prof["posts"] if p.get("hook")}
            diffs = []
            for ap_ in anal["posts"]:
                k = ap_["hook"][:40]
                if k in pm and pm[k] and ap_["impressions"]:
                    if abs(pm[k] - ap_["impressions"]) / max(pm[k], 1) > 0.1:
                        diffs.append({"hook": k, "profile_feed": pm[k],
                                      "creator_analytics": ap_["impressions"]})
            res["discrepancies"] = diffs or "none over 10%"

    print(json.dumps(res, indent=2))
    if isinstance(res, dict) and res.get("error"):
        sys.exit(1)


if __name__ == "__main__":
    main()
