# -*- coding: utf-8 -*-
"""Static site generator for Vayoo.

Emits one real HTML file per URL so Google has something to crawl. The design is
unchanged -- assets/vayoo.css is the original stylesheet, lifted verbatim.

Run:  python3 build/build.py
"""
import json
import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pages as P
import aqidata as AQ
import sitejs
import legal as L
import consent
from legalconf import unfilled
from components import (PRODUCTS, BY_ID, SITE_URL, EMAIL, PHONE_HUMAN, PHONE_TEL,
                        INSTAGRAM, LINKEDIN, money, rel, arrow, DOT)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()

NAV = [("air-purifiers/", "Air purifiers"), ("find-your-fit/", "Find your fit"),
       ("technology/", "Technology"), ("about/", "About"), ("faq/", "FAQ")]
MNAV = [("air-purifiers/", "Air purifiers", "3 models"),
        ("find-your-fit/", "Find your fit", "60 seconds"),
        ("compare/", "Compare", "side by side"),
        ("technology/", "Technology", "HEPA H13"),
        ("about/", "About", "mission &amp; team"),
        ("faq/", "FAQ", "straight answers"),
        ("contact/", "Contact", "talk to us")]

LOGO_W = "assets/derived/logo-white.png"
LOGO_B = "assets/derived/logo-black.png"


def logo(d, h=30):
    r = rel(d)
    st = ' style="height:%dpx"' % h if h != 30 else ''
    return ('<img class="lw" src="%s%s" alt="Vayoo" width="410" height="155"%s>'
            '<img class="ld" src="%s%s" alt="Vayoo" width="410" height="155"%s>'
            % (r, LOGO_W, st, r, LOGO_B, st))


def header(d, active):
    r = rel(d)
    nav = "".join('<a href="%s%s"%s>%s</a>'
                  % (r, href, ' class="on"' if href == active else '', label)
                  for href, label in NAV)
    mnav = "".join('<a href="%s%s">%s <span>%s</span></a>' % (r, h, l, s) for h, l, s in MNAV)
    return (
    '<a class="skip" href="#main">Skip to content</a>'
    '<div class="ambient" aria-hidden="true"><div class="grid"></div></div>'
    '<div class="ann" id="ann"><b>Launching soon across India.</b> Join the list and we will '
    'tell you the day pre-orders open. '
    '<button onclick="document.getElementById(\'ann\').remove()" aria-label="Dismiss">&times;</button></div>'
    '<header class="site" id="hdr"><div class="wrap hdr">'
    '<a class="brand" href="%(r)s" aria-label="Vayoo home">%(logo)s</a>'
    '<nav class="mainnav" aria-label="Primary">%(nav)s</nav>'
    '<span class="sp"></span><div class="hdr-acts">'
    '<button class="icon-btn" id="themeBtn" aria-label="Switch colour theme" title="Switch theme">'
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
    'stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2M12 19.5v2M2.5 '
    '12h2M19.5 12h2M5.2 5.2l1.4 1.4M17.4 17.4l1.4 1.4M18.8 5.2l-1.4 1.4M6.6 17.4l-1.4 1.4"/></svg></button>'
    '<a class="btn btn-p btn-sm hide-sm" href="%(r)snotify/">Notify me</a>'
    '<button class="icon-btn menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false">'
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>'
    '</div></div></header>'
    '<nav class="mnav" id="mnav" aria-label="Mobile" aria-hidden="true">'
    '<div class="wrap mnav-top" style="padding:0">'
    '<a class="brand" href="%(r)s">%(logo)s</a>'
    '<button class="icon-btn" id="mnavClose" aria-label="Close menu">'
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>'
    '%(mnav)s<a class="btn btn-p btn-lg" href="%(r)snotify/">Notify me at launch</a></nav>'
    % dict(r=r or "./", logo=logo(d), nav=nav, mnav=mnav))


IG_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">'
          '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/>'
          '<circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"/></svg>')
LI_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.5 2.5 0 1 0 5 '
          '8.5a2.5 2.5 0 0 0-.02-5zM3 9.5h4v11H3v-11zm7 0h3.8v1.5h.05c.53-.95 1.83-1.95 '
          '3.77-1.95 4.03 0 4.78 2.5 4.78 5.76v5.69h-4v-5.05c0-1.2-.02-2.75-1.75-2.75-1.75 '
          '0-2.02 1.3-2.02 2.66v5.14h-4v-11z"/></svg>')


def footer(d):
    r = rel(d)
    rng = "".join('<a href="%sair-purifiers/%s/">%s %s %s</a>'
                  % (r, p["slug"], p["name"], DOT, p["role"].split()[-3] if False else
                     {"car": "Car", "desk": "Desk", "room": "Room"}[p["space"]])
                  for p in PRODUCTS)
    return (
    '<footer class="site"><div class="wrap"><div class="fgrid">'
    '<div><a class="brand" href="%(r)s" style="margin-bottom:16px">%(logo)s</a>'
    '<p class="small muted" style="max-width:36ch">Air-purifying appliances for every space you '
    'live in &mdash; at a price that does not ask you to choose between health and household '
    'budget.</p><div class="socials">'
    '<a href="%(ig)s" target="_blank" rel="noopener" aria-label="Vayoo on Instagram">%(igs)s</a>'
    '<a href="%(li)s" target="_blank" rel="noopener" aria-label="Vayoo on LinkedIn">%(lis)s</a>'
    '</div></div>'
    '<div><h4>The range</h4><div class="stack">%(rng)s'
    '<a href="%(r)scompare/">Compare all three</a>'
    '<a href="%(r)sfind-your-fit/">Find your fit</a></div></div>'
    '<div><h4>Learn</h4><div class="stack">'
    '<a href="%(r)stechnology/">What HEPA H13 means</a>'
    '<a href="%(r)sfaq/">Air purifier FAQs</a>'
    '<a href="%(r)sabout/">Our story</a>'
    '<a href="%(r)snotify/">Launch updates</a>'
    '<a href="%(r)sfor-investors/">For investors</a></div></div>'
    '<div><h4>Reach us</h4><div class="stack">'
    '<a href="mailto:%(em)s">%(em)s</a>'
    '<a href="tel:%(tel)s">%(ph)s</a>'
    '<span class="small dim">Mon&ndash;Fri, 9am&ndash;6pm IST</span>'
    '<a href="%(r)scontact/">Contact &amp; bulk orders</a>'
    '<a href="%(r)sprivacy/">Privacy Policy</a>'
    '<a href="%(r)sterms/">Terms &amp; Conditions</a>'
    '<a href="#" data-cookie-settings>Cookie settings</a></div></div></div>'
    '<div class="legal"><div>&copy; %(yr)s Vayoo. All rights reserved.</div>'
    '<div class="row"><span>Made in India</span><span>%(dot)s</span><span>Breathe Better</span></div>'
    '</div></div></footer>'
    % dict(r=r or "./", logo=logo(d, 34), ig=INSTAGRAM, li=LINKEDIN, igs=IG_SVG, lis=LI_SVG,
           rng=rng, em=EMAIL, tel=PHONE_TEL, ph=PHONE_HUMAN, yr=date.today().year, dot=DOT))


# --- schema ------------------------------------------------------------------
ORG = {"@type": "Organization", "@id": SITE_URL + "/#org", "name": "Vayoo",
       "url": SITE_URL + "/", "email": EMAIL, "telephone": "+91-7009979996",
       "slogan": "Breathe Better", "logo": SITE_URL + "/" + LOGO_B,
       "sameAs": [INSTAGRAM, LINKEDIN],
       "description": ("Vayoo makes affordable medical-grade HEPA H13 air purifiers for the "
                       "car, the desk and the room in India.")}


def breadcrumbs(trail, path):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"}]
    acc = ""
    for i, (label, href) in enumerate(trail, start=2):
        acc = href if href else path
        items.append({"@type": "ListItem", "position": i, "name": re.sub(r"<[^>]+>", "", label),
                      "item": SITE_URL + "/" + acc})
    return {"@type": "BreadcrumbList", "itemListElement": items}


def product_schema(p, path):
    return {"@type": "Product", "name": p["name"],
            "description": p["tagline"] + " HEPA H13 " + p["role"].lower() +
                           " rated for %d-%d sq.ft." % p["area"],
            "category": p["role"], "brand": {"@type": "Brand", "name": "Vayoo"},
            "image": SITE_URL + "/assets/derived/" + p["id"] + "-product.png",
            "url": SITE_URL + "/" + path,
            "additionalProperty": [
                {"@type": "PropertyValue", "name": "Filter grade", "value": "HEPA H-13"},
                {"@type": "PropertyValue", "name": "Filtration efficiency",
                 "value": "99.95% at 0.3 microns"},
                {"@type": "PropertyValue", "name": "Recommended coverage",
                 "value": "%d-%d sq.ft." % p["area"]}],
            "offers": {"@type": "Offer", "price": str(p["price"]), "priceCurrency": "INR",
                       "availability": "https://schema.org/PreOrder",
                       "url": SITE_URL + "/" + path,
                       "seller": {"@id": SITE_URL + "/#org"}}}


def qa_schema():
    return {"@type": "QAPage", "mainEntity": [
        {"@type": "Question", "name": re.sub(r"<[^>]+>", "", q),
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in P.FAQS]}


# --- page shell --------------------------------------------------------------
SHELL = """<!DOCTYPE html>
<html lang="en-IN" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#07011C">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
{robots}<meta property="og:site_name" content="Vayoo">
<meta property="og:locale" content="en_IN">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{ogtitle}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimg}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%231E0163'/%3E%3Cpath d='M16 25c0-6 3-9 8-10-1 6-3 9-8 10z' fill='%237DCB29'/%3E%3Cpath d='M16 25c0-6-2.5-8.5-7-9.5.8 5.5 2.5 8.5 7 9.5z' fill='%2335A03C'/%3E%3C/svg%3E">
<link rel="stylesheet" href="{r}assets/vayoo.css">
<script src="{r}assets/vayoo-consent.js"></script>
<script type="application/ld+json">{ld}</script>
</head>
<body>
{header}
<main id="main">{crumbs}{body}</main>
{footer}
<script src="{r}assets/vayoo.js" defer></script>
</body>
</html>
"""


def render(page):
    d = page["depth"]
    r = rel(d)
    canon = SITE_URL + "/" + page["path"]
    graph = [ORG] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    ensure_ascii=False, separators=(",", ":"))
    crumbs_html = P.__dict__["rel"] and ""
    if page.get("trail"):
        from components import crumbs as crumbs_fn
        crumbs_html = crumbs_fn(page["trail"], d)
    return SHELL.format(
        title=page["title"], desc=page["desc"], canon=canon,
        robots='<meta name="robots" content="noindex,follow">\n' if page.get("noindex") else "",
        ogtype=page.get("ogtype", "website"), ogtitle=page.get("ogtitle", page["title"]),
        ogimg=page.get("ogimg", SITE_URL + "/assets/c10.png"),
        r=r, ld=ld, header=header(d, page.get("active", "")),
        crumbs=crumbs_html, body=page["body"], footer=footer(d))


# --- registry ----------------------------------------------------------------
def build_registry():
    reg = []
    reg.append(dict(
        path="", depth=0, out="index.html", active="", prio="1.0", freq="weekly",
        title="HEPA H13 Air Purifiers from " + money(1800) + " | Vayoo India",
        ogtitle="Vayoo — Medical-grade clean air from " + money(1800),
        desc=("Medical-grade HEPA H13 air purifiers for the car, the desk and the room. "
              "99.95% of particles at 0.3 microns, from " + money(1800) + ". Launching across India."),
        schema=[{"@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/",
                 "name": "Vayoo", "publisher": {"@id": SITE_URL + "/#org"},
                 "inLanguage": "en-IN"}],
        body=P.home(0)))

    reg.append(dict(
        path="air-purifiers/", depth=1, out="air-purifiers/index.html",
        active="air-purifiers/", prio="0.9", freq="weekly",
        title="HEPA H13 Air Purifiers for Home &amp; Car in India | Vayoo",
        desc=("Three HEPA H13 air purifiers: the C-10 for your car, the D-10 for your desk, the "
              "R-10 for your room. Same medical-grade filter, from " + money(1800) + "."),
        trail=[("Air purifiers", None)],
        schema=[breadcrumbs([("Air purifiers", "air-purifiers/")], "air-purifiers/"),
                {"@type": "ItemList", "name": "Vayoo air purifiers",
                 "itemListElement": [
                   {"@type": "ListItem", "position": i + 1, "name": p["name"],
                    "url": SITE_URL + "/air-purifiers/" + p["slug"] + "/"}
                   for i, p in enumerate(PRODUCTS)]}],
        body=P.air_purifiers(1)))

    ptitles = {
        "c10": ("Vayoo C-10 Car Air Purifier — HEPA H13 | " + money(1800),
                "A HEPA H13 car air purifier for cabins up to 70 sq.ft. Captures 99.95% of "
                "particles at 0.3 microns. RGB lights, low noise. Launch price " + money(1800) + "."),
        "d10": ("Vayoo D-10 Desk Air Purifier — HEPA H13 | " + money(3000),
                "A compact HEPA H13 desk air purifier for workstations of 80–125 sq.ft. "
                "Low-noise, medical-grade filtration. Launch price " + money(3000) + "."),
        "r10": ("Vayoo R-10 Room Air Purifier with AQI Meter | " + money(6500),
                "A HEPA H13 room air purifier for 350–400 sq.ft. with an on-board AQI meter, "
                "so you watch the air change. 3 modes, low noise. Launch price " + money(6500) + "."),
    }
    for p in PRODUCTS:
        path = "air-purifiers/%s/" % p["slug"]
        t, dsc = ptitles[p["id"]]
        reg.append(dict(
            path=path, depth=2, out=path + "index.html", active="air-purifiers/",
            prio="0.9", freq="monthly", title=t, desc=dsc, ogtype="product",
            ogimg=SITE_URL + "/assets/derived/" + p["id"] + "-product.png",
            trail=[("Air purifiers", "air-purifiers/"), (p["name"], None)],
            schema=[breadcrumbs([("Air purifiers", "air-purifiers/"), (p["name"], path)], path),
                    product_schema(p, path)],
            body=P.product(p["id"], 2)))

    reg.append(dict(
        path="compare/", depth=1, out="compare/index.html", active="air-purifiers/",
        prio="0.7", freq="monthly",
        title="Vayoo C-10 vs D-10 vs R-10 — Compare Air Purifiers",
        desc=("Compare the Vayoo C-10, D-10 and R-10 air purifiers side by side: coverage, "
              "price, AQI meter, fan modes and filter grade."),
        trail=[("Compare", None)],
        schema=[breadcrumbs([("Compare", "compare/")], "compare/")],
        body=P.compare(1)))

    reg.append(dict(
        path="find-your-fit/", depth=1, out="find-your-fit/index.html",
        active="find-your-fit/", prio="0.8", freq="monthly",
        title="What Size Air Purifier Do I Need? Room Size Calculator | Vayoo",
        desc=("Work out which size air purifier your room needs in sixty seconds. Coverage "
              "ranges, the sizing maths, and when the honest answer is two units."),
        trail=[("Find your fit", None)],
        schema=[breadcrumbs([("Find your fit", "find-your-fit/")], "find-your-fit/")],
        body=P.find_your_fit(1)))

    reg.append(dict(
        path="technology/", depth=1, out="technology/index.html", active="technology/",
        prio="0.8", freq="monthly",
        title="What HEPA H13 Means — Air Purifier Filter Grades Explained",
        desc=("H13 is a test, not an adjective: 99.95% of particles at 0.3 microns. What the "
              "grades mean, why 0.3 microns, and the words that mean a filter is not HEPA."),
        ogtype="article",
        trail=[("Technology", None)],
        schema=[breadcrumbs([("Technology", "technology/")], "technology/")],
        body=P.technology(1)))

    reg.append(dict(
        path="about/", depth=1, out="about/index.html", active="about/",
        prio="0.6", freq="yearly",
        title="About Vayoo — Affordable Clean Air for India",
        desc=("Vayoo builds medical-grade air purifiers for the people breathing the worst air "
              "and least able to pay for relief. Our mission, vision and founders."),
        trail=[("About", None)],
        schema=[breadcrumbs([("About", "about/")], "about/"), {"@type": "AboutPage"}],
        body=P.about(1)))

    reg.append(dict(
        path="faq/", depth=1, out="faq/index.html", active="faq/", prio="0.7", freq="monthly",
        title="Air Purifier FAQs — HEPA, Sizing &amp; Filters | Vayoo",
        desc=("Straight answers on HEPA H13, fake &ldquo;HEPA-type&rdquo; filters, room sizing, "
              "filter replacement and what an air purifier genuinely cannot do."),
        trail=[("FAQ", None)],
        schema=[breadcrumbs([("FAQ", "faq/")], "faq/"), qa_schema()],
        body=P.faq(1)))

    reg.append(dict(
        path="contact/", depth=1, out="contact/index.html", active="", prio="0.5", freq="yearly",
        title="Contact Vayoo — Support, Bulk Orders &amp; Partnerships",
        desc=("Talk to the founders about products, support, bulk and corporate orders for "
              "offices, clinics, schools and cab fleets."),
        trail=[("Contact", None)],
        schema=[breadcrumbs([("Contact", "contact/")], "contact/"), {"@type": "ContactPage"}],
        body=P.contact(1)))

    reg.append(dict(
        path="notify/", depth=1, out="notify/index.html", active="", noindex=True,
        title="Join the Vayoo Launch List",
        desc="Pre-orders first, your launch price locked, and the Fake HEPA Checklist today.",
        trail=[("Launch list", None)],
        body=P.notify(1)))

    # Audience pages, not search landing pages: noindex keeps the funding figures
    # out of the SERPs and avoids duplicating the About team section.
    reg.append(dict(
        path="investors/", depth=1, out="investors/index.html", active="", noindex=True,
        title="Investor Relations | Vayoo",
        desc="Vayoo is raising a seed round to scale affordable clean-air appliances across India.",
        trail=[("Investor relations", None)],
        body=P.investors(1)))

    reg.append(dict(
        path="for-investors/", depth=1, out="for-investors/index.html", active="", noindex=True,
        title="For Investors \u2014 Meet the Vayoo Founders",
        desc="The founding team behind Vayoo, and where to find the round details.",
        trail=[("For investors", None)],
        body=P.for_investors(1)))

    reg.append(dict(
        path="privacy/", depth=1, out="privacy/index.html", active="", prio="0.4", freq="yearly",
        title="Privacy Policy | Vayoo",
        desc=("What Vayoo collects, why, who we share it with, and your rights under India's "
              "Digital Personal Data Protection Act 2023. Google Ads and Meta Pixel disclosed."),
        trail=[("Privacy Policy", None)],
        schema=[breadcrumbs([("Privacy Policy", "privacy/")], "privacy/")],
        body=L.privacy(1)))

    reg.append(dict(
        path="terms/", depth=1, out="terms/index.html", active="", prio="0.4", freq="yearly",
        title="Terms &amp; Conditions | Vayoo",
        desc=("Terms for using vayoo.store and buying from us: pre-launch status, pricing, "
              "returns, the Watch-It-Work Guarantee, warranty, liability and governing law."),
        trail=[("Terms &amp; Conditions", None)],
        schema=[breadcrumbs([("Terms and Conditions", "terms/")], "terms/")],
        body=L.terms(1)))

    reg.append(dict(
        path="cookies/", depth=1, out="cookies/index.html", active="", prio="0.4", freq="yearly",
        title="Cookie Policy | Vayoo",
        desc=("Every cookie and pixel on vayoo.store: Google Ads, Google Analytics and the Meta "
              "Pixel, what each does, how long it lasts, and how to refuse or withdraw."),
        trail=[("Cookie Policy", None)],
        schema=[breadcrumbs([("Cookie Policy", "cookies/")], "cookies/")],
        body=L.cookies(1)))

    reg.append(dict(
        path="legal/", depth=1, out="legal/index.html", active="", prio="0.3", freq="yearly",
        title="Legal &mdash; Privacy, Terms &amp; Cookies | Vayoo",
        desc=("Vayoo's Privacy Policy, Terms & Conditions and Cookie Policy, plus our "
              "Grievance Officer and company details."),
        trail=[("Legal", None)],
        schema=[breadcrumbs([("Legal", "legal/")], "legal/")],
        body=L.legal_hub(1)))
    return reg


def main():
    reg = build_registry()
    for page in reg:
        out = os.path.join(ROOT, page["out"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(render(page))
        print("  %-46s %6d bytes" % (page["out"], os.path.getsize(out)))

    # sitemap -- indexable pages only
    urls = "".join(
        "  <url><loc>%s/%s</loc><lastmod>%s</lastmod>"
        "<changefreq>%s</changefreq><priority>%s</priority></url>\n"
        % (SITE_URL, p["path"], TODAY, p["freq"], p["prio"])
        for p in reg if not p.get("noindex"))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + urls + '</urlset>\n')

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        # Deliberately no Disallow lines: /notify/, /investors/ and /for-investors/
        # carry <meta robots="noindex">, and a crawler blocked by robots.txt can
        # never read that tag. Allow the crawl, let the tag do the work.
        f.write("User-agent: *\nAllow: /\n\n"
                "Sitemap: %s/sitemap.xml\n" % SITE_URL)

    # 404 reuses the shell so it is on-brand
    # served by the host for any missing path, at any depth -> absolute URLs only
    nf = dict(path="404.html", depth=0, out="404.html", active="", noindex=True,
              title="Page not found | Vayoo", desc="Nothing at this address.",
              body='<section class="sec"><div class="wrap center" style="padding:60px 0">'
                   '<h1>That page moved on.</h1><p class="lede" style="margin:16px auto 30px">'
                   'Nothing at this address. The range is the best place to start.</p>'
                   '<div class="row" style="justify-content:center">'
                   '<a class="btn btn-p btn-lg" href="' + SITE_URL + '/air-purifiers/">See the range'
                   + arrow() + '</a><a class="btn btn-g btn-lg" href="' + SITE_URL + '/">Home</a>'
                   '</div></div></section>')
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(render(nf))

    # site JS, with product and city data injected so they cannot drift
    js = sitejs.TEMPLATE
    js = js.replace("__PRODUCTS__", json.dumps(
        [dict(id=p["id"], slug=p["slug"], name=p["name"], role=p["role"],
              price=p["price"], priceText=money(p["price"]), area=list(p["area"]),
              accent=p["accent"]) for p in PRODUCTS],
        ensure_ascii=False, separators=(",", ":")))
    js = js.replace("__CITIES__", json.dumps(
        [[c, st, a] for c, st, a in sorted(AQ.CITIES)],
        ensure_ascii=False, separators=(",", ":")))
    js = js.replace("__THRESHOLD__", str(AQ.AQI_THRESHOLD))
    with open(os.path.join(ROOT, "assets", "vayoo.js"), "w", encoding="utf-8") as f:
        f.write(js)
    over = sum(1 for c in AQ.CITIES if c[2] > AQ.AQI_THRESHOLD)
    print("  assets/vayoo.js          %d cities (%d above AQI %d), captured %s"
          % (len(AQ.CITIES), over, AQ.AQI_THRESHOLD, AQ.CAPTURED))

    # consent script (gated tags) and its styles
    with open(os.path.join(ROOT, "assets", "vayoo-consent.js"), "w", encoding="utf-8") as f:
        f.write(consent.js())
    css_path = os.path.join(ROOT, "assets", "vayoo.css")
    css = open(css_path, encoding="utf-8").read()
    marker = "/* ---------- cookie consent"
    if marker in css:                      # idempotent: replace, never duplicate
        css = css[:css.index(marker)].rstrip() + "\n"
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css + consent.CSS)
    print("  assets/vayoo-consent.js  + consent styles appended to vayoo.css")

    print("\n  sitemap.xml    %d indexable URLs" % sum(1 for p in reg if not p.get("noindex")))
    print("  robots.txt     written")
    print("  404.html       written")
    print("\n  Pages built: %d" % len(reg))
    miss = unfilled()
    if miss:
        print("\n  !! %d legal placeholders still unfilled in build/legalconf.py:" % len(miss))
        for k in miss:
            print("       - %s" % k)
        print("     These render as visible red markers on the legal pages.")
    ids = [k for k in ("ga4_id", "google_ads_id", "meta_pixel_id")
           if not __import__("legalconf").LEGAL[k]]
    if ids:
        print("\n  i  Ad tags inactive (no ID set): %s" % ", ".join(ids))
        print("     Nothing loads until you fill these in build/legalconf.py.")


if __name__ == "__main__":
    main()
