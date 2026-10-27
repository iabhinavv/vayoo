# Vayoo — SEO & Content Plan
_Prepared 27 Oct 2026. Audit of vayoo site + Indian air-purifier SERP landscape._

---

## 1. The blocking finding

**The site currently has exactly one indexable URL containing ~140 crawlable words.**

| Check | Result |
|---|---|
| `<main id="view">` in raw HTML | **empty (0 characters)** — every word is injected by JS after load |
| Static crawlable text | **140 words**, all of it nav + footer chrome |
| URL structure | hash routes (`#/products`, `#/p/r10`) |
| Canonical tag | missing |
| `og:url`, `twitter:card` | missing |
| JSON-LD | injected by JS only, not in source |
| sitemap.xml / robots.txt | neither exists |
| `vayoo.store` DNS | **NXDOMAIN — the domain does not resolve** |
| Live location | `https://iabhinavv.github.io/vayoo/` |

Google discards everything after `#` in a URL. `#/products` and `#/p/r10` are not
pages to a crawler — they are the same URL as `/`. So no matter how good the copy
is, there is one page to rank, and its crawlable content is a nav menu.

**Nothing else in this plan matters until this is fixed.** Real paths, real HTML.

---

## 2. Competitor landscape — who actually owns these SERPs

Audited the live results for the money terms. Three distinct groups:

**Group A — Marketplaces own transactional intent.**
Amazon, Flipkart, Croma, Smartprix, Bajaj Finserv. They hold "air purifier price",
"air purifier under 10000", and most brand+model queries. Unwinnable head-on.

**Group B — Affiliate listicles own commercial-investigation intent.**
`bestpurifier.in`, `budgetappliancesindia.com`, `reviewsky.in`, `readthisfirst.in`,
`smarthousegears.com`, `instacuppastore.com`, plus Business Today / Deccan Herald
slideshows. They hold "best air purifier India 2026" and every "under ₹X" variant.
These are thin, near-identical, often price-inaccurate pages — several quote
conflicting prices for the same model in the same week.

**Group C — Brand sites rank almost exclusively for their own brand terms.**
Coway, Honeywell, Dyson, Xiaomi, Eureka Forbes, Nirvana Being, Qubo, Airth, Praan.
Nirvana Being runs a Shopify stack (products / collections / pages / blogs /
articles sitemaps) — the only Indian challenger with a real content layer.

**The gap:** nobody in Group C has built a genuine answer layer. Group B ranks on
volume of thin pages, not quality. A brand that publishes accurate, specific,
sourced buying education can take long-tail informational SERPs within months —
and those are exactly the queries that feed AI Overviews and ChatGPT citations.

**What the guides consistently tell buyers to check** (so our pages must answer
each one, better than they do):
- True H13 vs "HEPA-type"/"HEPA-like" — the latter are typically H11, ~95% capture
- CADR matched to room size
- Filter life and replacement cost
- **Avoid ioniser models — they emit ozone** (recurring expert warning)

That last point is a positioning opening, flagged in §7.

---

## 3. Honest ranking expectations

Vayoo is a brand-new domain with no backlinks and no launched product.

| Keyword class | Example | Realistic? |
|---|---|---|
| Head commercial | "air purifier", "best air purifier india" | **No.** 18–24 months minimum, needs real authority |
| Mid commercial | "best car air purifier india" | Possible at 6–12 months |
| Long-tail commercial | "air purifier for car under 2000" | 4–9 months |
| Informational long-tail | "what is h13 hepa filter", "aqi full form" | **3–6 months — this is the wedge** |
| Brand | "vayoo air purifier" | Immediate once indexed |

Strategy: **win the informational long tail and the car/desk niche first**, build
topical authority, then move up. Do not chase "best air purifier india" yet.

> No search-volume figures are quoted anywhere in this plan. I have no keyword-tool
> access in this environment, and inventing volumes would be worse than omitting
> them. Validate every term in Google Keyword Planner and Search Console before
> committing to the Phase 2 build order.

---

## 4. Page architecture — 26 pages, two phases

Hub-and-spoke. `/air-purifiers/` is the commercial hub; `/learn/` is the topical hub.

### Phase 1 — 12 pages (ship with launch)

| # | URL | Page type | Primary keyword | Secondary |
|---|---|---|---|---|
| 1 | `/` | Home | affordable hepa h13 air purifier india | clean air india, air purifier from 1800 |
| 2 | `/air-purifiers/` | Category hub | hepa h13 air purifier india | air purifier for home india |
| 3 | `/air-purifiers/c10-car-air-purifier/` | Product | car air purifier | best car air purifier india, hepa car purifier |
| 4 | `/air-purifiers/d10-desk-air-purifier/` | Product | desk air purifier | small air purifier for office, personal air purifier |
| 5 | `/air-purifiers/r10-room-air-purifier/` | Product | room air purifier | air purifier for bedroom, air purifier with aqi display |
| 6 | `/compare/` | Comparison | vayoo c10 vs d10 vs r10 | which vayoo air purifier |
| 7 | `/find-your-fit/` | Tool | air purifier room size calculator | what size air purifier do i need |
| 8 | `/technology/` | Pillar | hepa h13 filter | what is h13 hepa, medical grade hepa |
| 9 | `/about/` | Trust / E-E-A-T | vayoo air purifier brand | about vayoo |
| 10 | `/contact/` | Trust | vayoo contact support | — |
| 11 | `/faq/` | Support | air purifier faq india | do air purifiers need servicing |
| 12 | `/legal/` | Trust | — | — |

Plus `/notify/` (launch list — `noindex`, it is a conversion page, not a ranking page).

### Phase 2 — 14 pages (the content engine, post-launch)

| # | URL | Primary keyword | Why |
|---|---|---|---|
| 13 | `/learn/what-is-hepa-h13/` | what is h13 hepa filter | Fake-HEPA problem; high AI-citation value |
| 14 | `/learn/hepa-type-vs-true-hepa/` | hepa type vs true hepa | Directly exposes the category's biggest scam |
| 15 | `/learn/what-is-aqi/` | aqi full form, aqi meaning | "Full form" queries are huge in India, low competition |
| 16 | `/learn/pm25-explained/` | what is pm 2.5 | Feeds AQI + health clusters |
| 17 | `/learn/cadr-explained/` | what is cadr in air purifier | Buyers are told to check it, nobody explains it well |
| 18 | `/learn/do-air-purifiers-work/` | do air purifiers really work | High-intent scepticism query |
| 19 | `/learn/ioniser-vs-hepa/` | ioniser air purifier ozone | Positioning + genuine safety education |
| 20 | `/learn/air-purifier-for-asthma/` | air purifier for asthma india | Health intent, high conversion |
| 21 | `/learn/air-purifier-for-babies/` | air purifier for baby room | Parent intent, highest emotional weight |
| 22 | `/learn/car-air-pollution-india/` | car cabin air pollution | Feeds the C-10 |
| 23 | `/learn/delhi-air-pollution-guide/` | delhi air pollution aqi | Seasonal spike Oct–Jan, refresh yearly |
| 24 | `/guides/best-car-air-purifier-india/` | best car air purifier india | Our most winnable commercial term |
| 25 | `/guides/air-purifier-buying-guide-india/` | air purifier buying guide india | Pillar; internal-links to everything |
| 26 | `/guides/best-air-purifier-under-5000/` | best air purifier under 5000 | Dominant Indian budget modifier |

**Internal linking rule:** every `/learn/` page links up to `/technology/` and
across to the one product that solves the problem it describes. Every product page
links down to the two `/learn/` pages that justify its spec.

---

## 5. What goes on each Phase 1 page

Common to all: one `<h1>`, canonical, OG + Twitter tags, static JSON-LD, breadcrumbs,
and a single clear CTA.

**`/` Home** — Callout (who this is for) → the measured problem → the three products
→ why H13 → the guarantee → the offer → launch-list CTA. 700–900 words.

**`/air-purifiers/`** — Category intro that actually helps someone choose (sizing
logic, what H13 means, what we do not claim), then the three cards, then the sizing
tool link. ItemList schema. 500–700 words.

**Product pages** — Above fold: name, role, coverage, price, the one differentiating
feature, guarantee, CTA. Below: what it removes, full spec table, filter & care,
who it suits / who it does not, FAQ. Product + Offer schema. 800–1,200 words each.

**`/compare/`** — The three side by side, plus a short "pick this if…" paragraph per
model. The honest answer to "two rooms?" is two units; say so.

**`/find-your-fit/`** — Keep the existing calculator. Add 300 words explaining the
sizing maths so the page has crawlable substance.

**`/technology/`** — The pillar. What H13 means, why 0.3 microns, the particle-size
table, what HEPA cannot do. This page earns the links. 1,200–1,500 words.

**`/faq/`** — 15–20 genuine questions. QAPage schema (**not** FAQPage — Google
retired FAQ rich results for all sites on 7 May 2026).

---

## 6. The copy — $100M Offers applied

### Value Equation diagnosis for this category

```
          Dream Outcome  ×  Perceived Likelihood
Value = ────────────────────────────────────────
          Time Delay  ×  Effort & Sacrifice
```

Every brand in Indian air purification competes on **Dream Outcome** ("breathe
pure air!"). That is the lazy, undifferentiated half. The real buyer resistance
sits in the bottom half and in Perceived Likelihood:

| Driver | The buyer's actual objection | Our lever |
|---|---|---|
| Perceived likelihood | "Half these HEPA claims are fake. How do I know this works?" | State the grade, publish what we have not measured, **put an AQI meter on the unit so they watch it work** |
| Effort & Sacrifice | "₹15,000, then ₹2,000 filters forever" | ₹1,800 entry, no subscription, no app, no account |
| Time Delay | "Does it do anything in the first hour?" | The meter gives a visible result in minutes |
| Dream Outcome | "My kid coughs all winter" | Status + family framing, not "pure air" |

**We compete on the bottom half.** That is the defensible position and it happens
to be true of this product line.

### The guarantee — the single biggest missing lever

The site currently has **no guarantee at all**. Hormozi's formula is
*X result, Y time, Z consequence* — without the "or what" it has no teeth.

Recommended, named vividly so it gets repeated:

> ### The Watch-It-Work Guarantee
> Shut the room. Run the R-10 for one hour. Watch the AQI number on the unit.
> If it does not fall, you did not get what we sold you — send it back any time in
> the first 30 days. Full refund, and we pay the return pickup.

This works because the product *has a display*. The proof is on the box, not in a
claim. It converts the category's biggest objection ("is this real HEPA or
marketing?") into a thing the buyer can test themselves in sixty minutes.

For the C-10 and D-10 (no meter): a plain 30-day no-questions return, same
return-pickup term.

> **Requires founder sign-off before it goes live** — this is a real commercial
> commitment with real refund and reverse-logistics cost. See §7.

### Lead magnet (for the pre-launch list)

A lead magnet should solve a narrow problem completely, free, and in solving it
reveal the problem the core offer solves.

> **The Fake HEPA Checklist** — six things to check on any listing before you buy,
> and the exact words ("HEPA-type", "HEPA-like", "H11") that mean it is not H13.

It is genuinely useful, it costs nothing, it is accurate, and anyone who reads it
discovers the problem Vayoo exists to solve. Far stronger than "join our newsletter".

### Offer naming (M-A-G-I-C)

Avatar + Goal + Container: **"The Delhi-Winter Clean Air Starter"** for a
seasonal bundle; **"Founding Batch"** for the pre-order cohort.

### Scarcity and urgency — honest only

Do **not** invent "only 500 units". Real, available, costs nothing:
- Pre-orders open to the launch list before anyone else
- Launch-price lock: list members keep ₹1,800/₹3,000/₹6,500 even if retail opens higher

Both are true, both are enforceable, neither is a fake countdown.

---

## 7. Decisions needed from you

These are commercial commitments or facts I cannot invent. The copy is written so
each is a single edit.

1. **Approve or amend the Watch-It-Work Guarantee** (30-day return, we pay pickup).
   This is the highest-leverage item on the whole site. If you will not fund
   returns, say so and I will rewrite it as a service guarantee instead.
2. **Do the units contain an ioniser?** Every buying guide warns against ozone-
   emitting ionisers. If Vayoo is filter-only, that is a strong, honest
   differentiator and it should be stated. I have **not** claimed it anywhere.
3. **Missing specs** — CADR, noise in dB, power draw, dimensions, filter life,
   replacement filter price, warranty length. Spec tables currently say "published
   at launch" rather than carrying invented numbers.
4. **Point `vayoo.store` at the site.** The domain does not resolve today. Until
   it does, nothing can rank and every backlink you earn points at a dead host.
5. **Launch date** — the creatives still say 15 Sept 2025. No date appears on the
   site; confirm one for the launch-list emails.

---

## 8. Technical SEO checklist

Shipped in this change:
- [x] Real URLs, one static HTML file per page
- [x] Unique `<title>` and meta description per page
- [x] Canonical, `og:url`, `og:image`, `twitter:card` per page
- [x] Static JSON-LD in source (Organization, Product + Offer, BreadcrumbList, ItemList, QAPage)
- [x] `sitemap.xml` and `robots.txt`
- [x] Breadcrumbs on every inner page
- [x] Shared external CSS (cacheable across pages)
- [x] `/notify/` set to `noindex`
- [x] India-appropriate `lang="en-IN"`

Still yours to do:
- [ ] DNS for `vayoo.store` → GitHub Pages, then add `CNAME`
- [ ] Verify in Google Search Console, submit sitemap
- [ ] Bing Webmaster Tools (feeds Copilot citations)
- [ ] Google Business Profile if there is a physical address
- [ ] Real OG preview image (1200×630) — currently reusing a square product creative

---

## 9. Legal & advertising compliance (added 27 Oct 2026)

Four pages added: `/privacy/`, `/terms/`, `/cookies/`, and `/legal/` as a hub.
A working consent gate was added because a policy promising consent you do not
collect is the same defect as the "no trackers" line it replaced.

### What the consent gate actually does
- Google Consent Mode v2 defaults set to **denied** before any Google tag can fire
- Meta Pixel not injected at all until advertising consent exists
- Three categories: strictly necessary (locked on), analytics, advertising
- Withdrawal from the footer of every page — DPDP s.6(4) requires it to be as
  easy as giving
- Consent record stored with a timestamp so you can evidence it
- **Verified with live test IDs:** nothing loaded before consent or after
  "Reject all"; `fbevents.js`, the pixel config call and both gtag containers
  loaded only after "Accept all"

### Switching the ad tags on
Fill `ga4_id`, `google_ads_id` and `meta_pixel_id` in `build/legalconf.py`, then
rebuild. Empty means the tag never loads, so the site is safe to publish today.

### Statutory basis used
| Instrument | What it drove |
|---|---|
| DPDP Act 2023 + DPDP Rules 2025 (G.S.R. 846(E), notified 14 Nov 2025) | Itemised notice, consent wording, withdrawal, rights, children, breach, grievance. Rule 3 duties commence ~13 May 2027 |
| Consumer Protection (E-Commerce) Rules 2020 | Entity identity block, named Grievance Officer, 48h/1-month timelines, returns/refund/warranty disclosure |
| Consumer Protection Act 2019 | Liability carve-outs, consumer forum rights |
| IT Act 2000 s.43A + SPDI Rules 2011 | Reasonable security practices |
| CCPA Misleading Advertisements Guidelines 2022 | Claim substantiation clause; disclaimers that cannot contradict the claim |
| Google Ads remarketing policy / Meta Business Tools | Named-vendor disclosure, opt-out links, pixel consent |

### Still required before ads run

1. **Fill the 9 placeholders** in `build/legalconf.py`. They render as red markers
   on the live pages precisely so they cannot ship unnoticed: legal entity name,
   CIN, GSTIN, registered office, operating address, Grievance Officer name and
   designation, data-protection contact, country of origin.
2. **Appoint the Grievance Officer in writing.** The E-Commerce Rules require a
   *named* person with designation and contact, not a role inbox.
3. **Verify "Made in India."** It is in the footer, carried over from the original
   site. If the units are imported, that is a country-of-origin misdeclaration
   under Legal Metrology and the Consumer Protection Act. Confirm or remove.
4. **Hold substantiation for every performance claim** before the first ad runs.
   CCPA penalties are ₹10 lakh, ₹50 lakh on repeat. You need test evidence on
   file for "99.95% at 0.3 microns" and "up to 99.8% of PM2.5."
5. **Create `grievance@` and `privacy@` mailboxes.** Both are published in the
   policies and must actually receive mail.
6. **Lawyer review.** These are solid drafts, not legal advice.
7. **Returns/shipping policy page** before you sell — Google Ads and Meta both
   want it, and the E-Commerce Rules require delivery and refund disclosure.

### One advertising-law detail worth knowing
CCPA guidance is that a disclaimer must be in the same language and font as the
claim it qualifies, and cannot contradict it. The AQI panel's caveat is currently
set smaller and dimmer than the figure it qualifies. It is honest, but if you run
that panel as ad creative, raise the disclaimer to the same prominence.
