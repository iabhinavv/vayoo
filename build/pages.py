# -*- coding: utf-8 -*-
"""Page copy for the Vayoo site.

Copy is built on the $100M Offers value equation: the category competes on the
top half (bigger purity claims), so we compete on the bottom half -- perceived
likelihood (prove it), effort (no app, no subscription) and price.

Every factual claim here traces to Vayoo's own material or a cited third party.
Specs Vayoo has not measured are marked as published at launch, not invented.
"""
from components import (PRODUCTS, BY_ID, SPACE_LABEL, money, ic, check, arrow,
                        sechead, checks, pcard, guarantee_block, cta_band,
                        faq_block, dl, rel, DOT, RUPEE, EMAIL, PHONE_HUMAN,
                        PHONE_TEL, NOTIFY_FORM, INSTAGRAM, LINKEDIN)

# The measured anchor for the whole site. Real, cited, caveated.
NEWSLAUNDRY = ("Newslaundry, measuring a Delhi office on 8 January 2026. "
               "A single room on a single day, not a controlled study.")


def flow_svg():
    return ('<svg class="flowlines" viewBox="0 0 400 400" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M-20 60 C 120 20, 260 100, 420 50"/>'
            '<path d="M-20 130 C 130 90, 250 170, 420 120"/>'
            '<path d="M-20 200 C 120 165, 270 240, 420 195"/>'
            '<path d="M-20 270 C 140 230, 250 310, 420 260"/>'
            '<path d="M-20 340 C 110 300, 280 375, 420 330"/>'
            '<path d="M-20 380 C 150 345, 240 400, 420 370"/></svg>')


def aqi_panel():
    import aqidata as A
    return (
    '<div class="aqi-panel rv" id="aqiPanel">' + flow_svg() +
    '<div class="aqi-head"><span class="lbl">Air quality index</span>'
    '<div class="seg" role="tablist">'
    '<button data-aqi="out" class="on" role="tab" aria-selected="true">Outdoors</button>'
    '<button data-aqi="in" role="tab" aria-selected="false">With Vayoo</button>'
    '</div></div>'
    '<form class="aqi-search" id="aqiSearch" role="search" autocomplete="off">'
    '<input id="cityIn" type="search" placeholder="Check my city" '
    'aria-label="Check my city" list="cityList" spellcheck="false">'
    '<datalist id="cityList"></datalist>'
    '<button type="submit" class="btn btn-leaf btn-sm">Check</button>'
    '</form>'
    '<p class="aqi-city" id="aqiCity"></p>'
    '<div class="gauge-wrap">'
    '<svg class="gauge" viewBox="0 0 240 200" aria-hidden="true">'
    '<defs><linearGradient id="gg" x1="0" y1="1" x2="1" y2="0">'
    '<stop offset="0" stop-color="#7DCB29"/><stop offset=".4" stop-color="#F2B12C"/>'
    '<stop offset=".75" stop-color="#E5484D"/><stop offset="1" stop-color="#A32330"/>'
    '</linearGradient></defs>'
    '<path d="M32 168a100 100 0 1 1 176 0" fill="none" stroke="rgba(255,255,255,.12)" '
    'stroke-width="14" stroke-linecap="round"/>'
    '<path id="gArc" d="M32 168a100 100 0 1 1 176 0" pathLength="500" fill="none" '
    'stroke="url(#gg)" stroke-width="14" stroke-linecap="round" stroke-dasharray="500" '
    'stroke-dashoffset="500" style="transition:stroke-dashoffset 1.1s cubic-bezier(.22,1,.36,1)"/>'
    '</svg>'
    '<div class="gauge-val"><span class="v tnum" id="gVal">0</span><span class="u">AQI</span>'
    '<div><span class="gauge-band" id="gBand"><i></i><span>&mdash;</span></span></div></div>'
    '</div>'
    '<div class="aqi-foot"><p id="gMsg"></p><div id="gCta"></div>'
    '<p class="aqi-note">Outdoor figures are a snapshot of US AQI readings taken on '
    + A.CAPTURED + ', from <a href="' + A.SOURCE_URL + '" target="_blank" rel="noopener '
    'nofollow">' + A.SOURCE_NAME + '</a> &mdash; not a live feed. Indian air swings hard by '
    'season, so treat these as indicative rather than today&rsquo;s number. The &ldquo;with '
    'Vayoo&rdquo; figure illustrates the Good band and is not a performance claim for any '
    'Vayoo model.</p></div></div>')


# =============================================================================
# HOME
# =============================================================================
def home(d=0):
    r = rel(d)
    return (
    # ---- hero
    '<section class="hero"><div class="wrap hero-grid"><div>'
    '<span class="pill"><span class="dot"></span>For families in Delhi NCR, Mumbai, '
    'Bengaluru &amp; Kolkata</span>'
    '<h1>Medical-grade clean air.<br><span class="gr">From ' + money(1800) + '.</span></h1>'
    '<p class="lede">Vayoo makes HEPA H13 air purifiers for the car, the desk and the room. '
    'H13 is the grade hospitals specify &mdash; it captures 99.95% of particles down to '
    '0.3 microns. We put it in three sizes and priced it so you are not choosing between '
    'your family&rsquo;s lungs and the household budget.</p>'
    '<div class="hero-cta">'
    '<a class="btn btn-p btn-lg" href="' + r + 'air-purifiers/">See the range' + arrow() + '</a>'
    '<a class="btn btn-s btn-lg" href="' + r + 'find-your-fit/">Find my purifier</a>'
    '</div>'
    '<div class="hero-facts">'
    '<div><b class="tnum">99.95%</b><span>OF PARTICLES AT 0.3&micro;m</span></div>'
    '<div><b class="tnum">99.8%</b><span>OF PM2.5 CLEARED</span></div>'
    '<div><b class="tnum">' + money(1800) + '</b><span>STARTING PRICE</span></div>'
    '</div></div>'
    '<div>' + aqi_panel() + '</div></div></section>'

    # ---- the stick: what going without looks like, with a real measurement
    '<section class="sec"><div class="wrap">'
    + sechead("The problem", "Shutting the door buys you almost nothing",
              "Most people assume indoors is safe. Someone actually measured it.")
    + '<div class="grid g3 rv">'
      '<div class="card"><div class="ico">' + ic('factory') + '</div>'
      '<div class="stat" style="padding:0;border:0;background:none">'
      '<div class="v tnum">348</div></div>'
      '<h3 style="margin-top:6px">Outside</h3>'
      '<p class="muted small" style="margin-top:8px">Delhi, a severe-AQI January morning. '
      'The number everyone talks about.</p></div>'

      '<div class="card" style="border-color:rgba(229,72,77,.35)"><div class="ico">' + ic('room') + '</div>'
      '<div class="stat" style="padding:0;border:0;background:none">'
      '<div class="v tnum">309</div></div>'
      '<h3 style="margin-top:6px">Inside, doors shut</h3>'
      '<p class="muted small" style="margin-top:8px">No purifier. You are breathing the same '
      'air as the street, just with a roof over it.</p></div>'

      '<div class="card" style="border-color:rgba(125,203,41,.4)"><div class="ico leaf">' + ic('leaf') + '</div>'
      '<div class="stat" style="padding:0;border:0;background:none">'
      '<div class="v tnum">48</div></div>'
      '<h3 style="margin-top:6px">Same room, purifier running</h3>'
      '<p class="muted small" style="margin-top:8px">The only one of these three numbers you '
      'can actually do something about today.</p></div>'
      '</div>'
      '<p class="xs dim rv" style="margin-top:20px">Source: ' + NEWSLAUNDRY + ' We did not run '
      'this test and it was not run on a Vayoo unit &mdash; it is here because it is the '
      'clearest published measurement of the gap we are selling into.</p>'
    '</div></section>'

    # ---- the range
    '<section class="sec-tight"><div class="wrap">'
    + sechead("The range", "One for the car.<br>One for the desk.<br>One for the room.",
              "Same medical-grade filter in all three. What changes is the volume of air each "
              "one is built to turn over.")
    + '<div class="grid g3">' + "".join(pcard(p, d) for p in PRODUCTS) + '</div>'
    + '<div class="row rv" style="margin-top:26px;justify-content:space-between;gap:16px">'
      '<p class="small dim" style="max-width:52ch">Not sure which size fits your space? '
      'The sizing tool asks two questions and gives you one answer.</p>'
      '<div class="row"><a class="btn btn-s btn-sm" href="' + r + 'find-your-fit/">Find my fit</a>'
      '<a class="btn btn-g btn-sm" href="' + r + 'compare/">Compare all three</a></div></div>'
    '</div></section>'

    # ---- value equation: why this is 1,800 and not 18,000
    '<section class="sec"><div class="wrap split">'
    '<div class="rv"><span class="eyebrow">Why it costs this little</span>'
    '<h2 style="margin:14px 0 18px">The filter is not the expensive part.</h2>'
    '<p class="lede" style="margin-bottom:26px">An H13 filter is a graded, manufactured '
    'commodity. What tends to sit on top of it is an app, an account, a subscription, a '
    'companion cloud service and a Wi-Fi chip that will be unsupported in four years. '
    'We left all of that out and spent the money on the filter.</p>'
    + checks([
        ("No app, no account", "plug it in and press the button. That is the whole setup."),
        ("No subscription", "no filter club, no auto-ship you have to remember to cancel."),
        ("Nothing to go obsolete", "there is no cloud service to switch off in 2031."),
        ("The same H13 in all three", "the " + money(1800) + " C-10 filters to the same grade "
         "as the " + money(6500) + " R-10. You are paying for airflow and coverage, never for "
         "a better filter."),
      ])
    + '</div>'
    '<div class="rv"><div class="card" style="padding:0;overflow:hidden;border-radius:var(--r-xl)">'
    '<div style="aspect-ratio:1/1;background:radial-gradient(circle at 50% 60%,#7DCB29 0%,#33065C 55%,#1E0163 100%);position:relative;overflow:hidden">'
    + flow_svg() +
    '<img src="' + r + 'assets/derived/r10-product.png" alt="Vayoo R-10 room air purifier with on-board AQI meter" '
    'style="position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:44px 40px;z-index:2;'
    'filter:drop-shadow(0 30px 44px rgba(0,0,0,.5))" width="304" height="520"></div>'
    '<div style="padding:24px"><div class="row" style="justify-content:space-between">'
    '<div><h3>Vayoo R-10</h3><p class="small muted">Room air purifier ' + DOT + ' 350&ndash;400 sq.ft.</p></div>'
    '<div class="pcard-price"><span class="v tnum">' + money(6500) + '</span>'
    '<span class="u">Launch price</span></div></div>'
    '<a class="btn btn-p btn-block btn-sm" href="' + r + 'air-purifiers/r10-room-air-purifier/" '
    'style="margin-top:18px">Explore the R-10' + arrow() + '</a></div></div></div>'
    '</div></section>'

    # ---- guarantee
    '<section class="sec-tight"><div class="wrap" style="max-width:860px">'
    + guarantee_block(d) +
    '</div></section>'

    # ---- mission
    '<section class="sec-tight"><div class="wrap"><div class="grid g2">'
    '<div class="card rv" style="border-color:rgba(196,47,166,.3)"><div class="ico">' + ic('spark') + '</div>'
    '<h3>Our mission</h3><p class="muted" style="margin-top:10px">To become India&rsquo;s number '
    'one clean-tech appliances brand, and help India become cleaner and fresher in the process.</p></div>'
    '<div class="card rv" style="border-color:rgba(125,203,41,.3)"><div class="ico leaf">' + ic('leaf') + '</div>'
    '<h3>Our vision</h3><p class="muted" style="margin-top:10px">To give India the birth-right of '
    'pure air to breathe, and build a better tomorrow for the generation after this one.</p></div>'
    '</div><p class="quote rv" style="margin-top:36px;max-width:44ch">The best time to make a '
    'change was yesterday. The second best time is now.</p></div></section>'

    + cta_band(d))


# =============================================================================
# CATEGORY HUB
# =============================================================================
def air_purifiers(d=1):
    r = rel(d)
    return (
    '<section class="sec-tight"><div class="wrap">'
    '<div class="sec-h rv"><span class="eyebrow">The range</span>'
    '<h1 style="margin:14px 0 12px">HEPA H13 air purifiers for Indian homes and cars</h1>'
    '<p class="lede">Three purifiers, one filter grade. The C-10 for a car cabin, the D-10 for '
    'a desk, the R-10 for a room. Pick by the volume of air you need to turn over &mdash; the '
    'filtration does not change between them.</p></div>'

    '<div class="grid g3">' + "".join(pcard(p, d) for p in PRODUCTS) + '</div>'

    '<div class="card rv" style="margin-top:34px"><div class="split" style="gap:30px;align-items:center">'
    '<div><h2 style="font-size:1.5rem">Sizing is the whole game</h2>'
    '<p class="muted small" style="margin-top:10px">A purifier rated below your room size will '
    'run flat out and never turn the air over. One rated well above it is money spent on '
    'capacity you cannot use. The coverage figure on each model is the honest number to '
    'measure against.</p></div>'
    '<div class="row" style="justify-content:flex-end">'
    '<a class="btn btn-p" href="' + r + 'find-your-fit/">Find my fit' + arrow() + '</a>'
    '<a class="btn btn-g" href="' + r + 'compare/">Compare specs</a></div></div></div>'

    '<div class="split" style="margin-top:50px;gap:34px;align-items:start">'
    '<div class="rv"><h2>How to choose, in three lines</h2>'
    '<p class="muted" style="margin-top:14px">Measure the room in feet and multiply length by '
    'breadth. Match that number to the coverage range on the model &mdash; and if you land '
    'between two, take the larger one. An oversized purifier runs slower and quieter; an '
    'undersized one runs flat out and still falls short.</p>'
    '<p class="muted" style="margin-top:14px">Then shut the door. Every coverage figure in this '
    'category, ours included, assumes a closed room. An open window undoes the work as fast as '
    'the filter does it.</p></div>'
    '<div class="rv"><div class="card" style="background:var(--surface-2)">'
    '<h3 style="margin-bottom:14px">What H13 means, briefly</h3>'
    '<p class="small muted">HEPA filters are graded. H13 is the first grade classed as '
    'medical-grade, and it is defined by a test: it must capture 99.95% of particles at 0.3 '
    'microns &mdash; the hardest size to trap.</p>'
    '<p class="small muted" style="margin-top:12px">Watch for &ldquo;HEPA-type&rdquo;, '
    '&ldquo;HEPA-like&rdquo; and &ldquo;HEPA-style&rdquo; on other listings. Those phrases '
    'specifically mean the filter does <b>not</b> meet the standard; they are usually H11, '
    'which catches around 95%.</p>'
    '<a class="btn btn-s btn-sm" style="margin-top:16px" href="' + r + 'technology/">'
    'How the filtration works' + arrow() + '</a></div></div></div>'
    '</div></section>' + cta_band(d))


# =============================================================================
# PRODUCT PAGE
# =============================================================================
PRODUCT_COPY = {
 "c10": dict(
   intro=("A commute is the most concentrated dose of polluted air most people get all day. "
          "Windows up, exhaust from the vehicle in front being pulled straight into the cabin, "
          "and the same air recirculating for forty minutes. The C-10 sits in that cabin and "
          "keeps working the whole way."),
   who=["Anyone with a daily drive through Delhi NCR, Mumbai, Bengaluru or Kolkata traffic",
        "Cab and fleet drivers who spend six hours a day in the cabin",
        "Parents doing the school run with a child in the back",
        "Anyone whose car smells of the road by the time they park"],
   removes=[("PM2.5 and PM10", "the fine particulate that drives most of India&rsquo;s AQI readings"),
            ("Vehicle exhaust soot", "black carbon from the diesel in front of you"),
            ("Road dust", "the construction and kerbside dust that gets pulled in at every light"),
            ("Pollen", "seasonal allergens, at the size range HEPA is graded for")]),
 "d10": dict(
   intro=("You breathe the air within a metre of your face for eight to ten hours a day. The "
          "D-10 is built for that metre &mdash; a workstation, an office cabin, a study table, "
          "a gaming setup &mdash; and it is quiet enough that you forget it is running."),
   who=["Anyone working from home in a room they cannot ventilate",
        "Office cabins and small meeting rooms",
        "Students at a study table through exam season",
        "Gaming setups where a loud fan is not an option"],
   removes=[("PM2.5 and PM10", "the fraction small enough to cross from lung into bloodstream"),
            ("Dust and dust-mite debris", "the everyday load in any Indian home, and a common asthma trigger"),
            ("Pet dander", "skin flakes and hair fragments that stay airborne for hours"),
            ("Mould spores", "airborne spores released in damp and monsoon conditions")]),
 "r10": dict(
   intro=("The R-10 is the one with the number on the front. It is built for bedrooms, living "
          "rooms and nurseries &mdash; and the on-board AQI meter means cleaner air is "
          "something you watch happen rather than take on trust. That matters more than it "
          "sounds in a category where half the filtration claims are decoration."),
   who=["Bedrooms, especially a child&rsquo;s or an elderly parent&rsquo;s",
        "Living rooms through the October-to-January smog season",
        "Nurseries, where the buyer most wants proof rather than promises",
        "Anyone who has been burned by a purifier that showed no evidence of working"],
   removes=[("PM2.5 and PM10", "the fine particulate that drives most of India&rsquo;s AQI readings"),
            ("Smoke and soot", "crop-burning haze, cooking smoke, incense, Diwali fallout"),
            ("Dust and dust-mite debris", "a common asthma and rhinitis trigger"),
            ("Pollen and pet dander", "seasonal allergens and airborne skin flakes"),
            ("Mould spores", "released in damp and monsoon conditions")]),
}

PRODUCT_FAQ = {
 "c10": [("Does a car air purifier actually do anything?",
          "In a sealed cabin, yes &mdash; a car is a small volume, which is the easiest case for "
          "a filter. What it cannot do is help with the window down, because you are then "
          "replacing the cabin air faster than any filter can clean it."),
         ("Where does it sit?",
          "Anywhere it can draw air freely and will not slide. A cup holder is the usual answer. "
          "Keep a few inches clear around the intake."),
         ("Will it drain the battery?",
          "It runs from the car&rsquo;s USB supply. Exact power draw is published with the full "
          "specification sheet at launch.")],
 "d10": [("Is it quiet enough for calls?",
          "It is built for low-noise operation beside a person all day. We have not published a "
          "decibel figure because we have not measured one we would stand behind &mdash; that "
          "number comes with the full spec sheet at launch."),
         ("Can I use it in a bedroom instead?",
          "At the top of its range, yes. It is rated for 80&ndash;125 sq.ft., so a small bedroom "
          "with the door shut is within reach. A 350 sq.ft. room is the R-10&rsquo;s job."),
         ("Does it need to run all day?",
          "A purifier cleans by turning the room&rsquo;s air over repeatedly, so it works best "
          "running continuously in a closed room rather than in bursts.")],
 "r10": [("What does the AQI meter actually show?",
          "The air quality in the room, on the unit itself. It is the reason our guarantee can "
          "be what it is: you do not have to believe us, you can watch the number."),
         ("Is 350&ndash;400 sq.ft. my whole flat?",
          "No. It is one closed room. An open-plan living-dining space usually measures past "
          "400 sq.ft., and the honest answer there is two units."),
         ("How long before I see a difference?",
          "A purifier does not clean a room instantly &mdash; it works by turning the air over "
          "repeatedly. Our guarantee is built around an hour in a closed room, which is a fair "
          "test of whether it is doing anything at all.")],
}


def product(pid, d=2):
    p = BY_ID[pid]
    r = rel(d)
    copy = PRODUCT_COPY[pid]
    others = [o for o in PRODUCTS if o["id"] != pid]

    removes = "".join(
        '<div class="card"><h3>%s</h3><p class="small muted" style="margin-top:8px">%s</p></div>'
        % (t, b) for t, b in copy["removes"])

    return (
    '<div class="wrap"><div class="pdp" style="--pc:' + p["accent"] + '">'
    '<div class="gal"><div class="gal-main">' + flow_svg() +
    '<img src="' + r + 'assets/derived/' + p["id"] + '-product.png" alt="' + p["name"] + ' ' +
    p["role"].lower() + '" style="position:relative;z-index:2" width="320" height="520"></div></div>'

    '<div class="buy">'
    '<div>' + ('<span class="tag tag-leaf" style="margin-bottom:12px">' + p["badge"] + '</span>'
               if p.get("badge") else
               '<span class="tag tag-acc" style="margin-bottom:12px">Launching soon</span>') +
    '<h1>' + p["name"] + '</h1>'
    '<p class="lede" style="margin-top:10px">' + p["tagline"] + '</p></div>'
    '<div class="price-row"><span class="v tnum">' + money(p["price"]) + '</span>'
    '<span class="small dim">Launch price ' + DOT + ' ' + p["role"] + '</span></div>'
    '<div class="spec-strip">'
    '<div><b class="tnum">' + str(p["area"][0]) + '&ndash;' + str(p["area"][1]) + '</b><span>sq.ft. coverage</span></div>'
    '<div><b>H-13</b><span>HEPA grade</span></div>'
    '<div><b class="tnum">99.95%</b><span>at 0.3 microns</span></div></div>'
    '<p class="muted">' + copy["intro"] + '</p>'
    + checks(p["feats"]) +
    '<div class="row" style="gap:10px">'
    '<a class="btn btn-p btn-lg" href="' + r + 'notify/" style="flex:2">Notify me at launch</a>'
    '<a class="btn btn-s btn-lg" href="' + r + 'compare/" style="flex:1">Compare</a></div>'
    '<p class="xs dim" style="margin-top:-8px">Not yet on sale. Joining the launch list places '
    'no order and takes no payment &mdash; it locks your launch price and puts you ahead of '
    'general release.</p>'
    '<div class="card" style="background:var(--surface-2);padding:20px">'
    '<span class="eyebrow">Suits</span><p class="small" style="margin-top:10px">' + p["fits"] + '</p></div>'
    '</div></div></div>'

    # ---- what it removes
    '<section class="sec"><div class="wrap">'
    + sechead("What it removes", "What an H13 filter catches",
              "H13 is graded to capture 99.95% of particles at 0.3 microns &mdash; the hardest "
              "size to trap. Everything below is at or above that size range.")
    + '<div class="grid g3 rv">' + removes + '</div>'
    + '<p class="xs dim rv" style="margin-top:22px">Particle filtration only. A HEPA filter is '
      'not a gas filter &mdash; it does not claim to remove odour molecules, VOCs or carbon '
      'monoxide, and neither do we.</p>'
    '</div></section>'

    # ---- who it is and is not for
    '<section class="sec-tight"><div class="wrap"><div class="split" style="gap:34px;align-items:start">'
    '<div class="rv"><h2>Who this is for</h2>'
    + checks(copy["who"]) + '</div>'
    '<div class="rv"><div class="card" style="background:var(--surface-2)">'
    '<h3>Who it is not for</h3><p class="muted small" style="margin-top:12px">' + p["not_for"] + '</p>'
    '<p class="xs dim" style="margin-top:14px">We would rather lose the sale than have you buy '
    'the wrong size and conclude that purifiers do not work.</p>'
    '<a class="btn btn-s btn-sm" style="margin-top:16px" href="' + r + 'find-your-fit/">'
    'Check my room size' + arrow() + '</a></div></div></div></div></section>'

    # ---- highlight + specs
    '<section class="sec-tight"><div class="wrap"><div class="split" style="gap:34px;align-items:start">'
    '<div class="rv"><h2>' + p["highlight"] + '</h2>'
    '<p class="muted" style="margin-top:14px">' + p["highlight_note"] + '</p>'
    '<h3 style="margin-top:28px">Specifications</h3>'
    + dl([("Model", p["name"]), ("Category", p["role"]),
          ("Recommended coverage", "%d&ndash;%d sq.ft." % p["area"]),
          ("Filter grade", "HEPA H-13 (medical grade)"),
          ("Filtration efficiency", "99.95% at 0.3 microns"),
          ("PM2.5 clearance", "Up to 99.8%"),
          ("Noise", "Low-noise operation"),
          ("Launch price", money(p["price"]))])
    + '<p class="xs dim" style="margin-top:14px">Rated CADR, decibel figures, power draw, '
      'dimensions and filter life are published with the full specification sheet at launch. '
      'We would rather leave a row blank than fill it with a number we have not measured.</p></div>'
    '<div class="rv">' + guarantee_block(d, p) + '</div>'
    '</div></div></section>'

    + faq_block(PRODUCT_FAQ[pid], "Questions about the " + p["name"])

    # ---- related
    + '<section class="sec-tight"><div class="wrap">'
    + sechead("Also consider", "The other two in the range")
    + '<div class="grid g3">' + "".join(pcard(o, d) for o in others) +
      '<div class="card hov rv" style="display:grid;place-content:center;text-align:center;gap:14px">'
      '<div class="ico" style="margin:0 auto">' + ic('chart') + '</div>'
      '<h3>See all three side by side</h3>'
      '<p class="small muted">Coverage, price and features in one table.</p>'
      '<a class="btn btn-s btn-sm" href="' + r + 'compare/" style="justify-self:center">'
      'Open comparison</a></div>'
    '</div></div></section>' + cta_band(d))


def filter_viz():
    dots = "".join('<circle cx="%d" cy="%d" r="%d" fill="#E5484D" opacity=".8"/>' % (x, y, 2 + i % 3)
                   for i, (x, y) in enumerate([(38,88),(70,120),(52,152),(96,75),(112,140),
                                               (140,105),(168,160),(186,92),(150,175),(80,178)]))
    bars = "".join('<line x1="%d" y1="60" x2="%d" y2="190" stroke="currentColor" '
                   'stroke-opacity=".28" stroke-width="1.6"/>' % (246 + i * 5.4, 246 + i * 5.4)
                   for i in range(8))
    pleats = "".join('<path d="M%d 54 l4.7 12 l-4.7 12 l4.7 12 l-4.7 12 l4.7 12 l-4.7 12 l4.7 12 '
                     'l-4.7 12 l4.7 12" fill="none" stroke="#E15AD0" stroke-opacity=".45" '
                     'stroke-width="1.3"/>' % (326 + i * 9.4) for i in range(13))
    waves = "".join('<path d="M%d %d q 14 -9 28 0" fill="none" stroke="#7DCB29" '
                    'stroke-opacity=".75" stroke-width="1.8" stroke-linecap="round"/>'
                    % (x, 84 + (i % 3) * 30) for i, x in enumerate([500,540,580,620,660,700]))
    return (
    '<svg class="filterviz" viewBox="0 0 720 250" role="img" aria-label="Dirty air passes '
    'through a pre-filter and a HEPA H-13 filter and leaves clean">'
    '<defs><linearGradient id="fv1" x1="0" y1="0" x2="1" y2="0">'
    '<stop offset="0" stop-color="#E5484D" stop-opacity=".55"/>'
    '<stop offset="1" stop-color="#E5484D" stop-opacity="0"/></linearGradient>'
    '<linearGradient id="fv2" x1="0" y1="0" x2="1" y2="0">'
    '<stop offset="0" stop-color="#7DCB29" stop-opacity="0"/>'
    '<stop offset="1" stop-color="#7DCB29" stop-opacity=".6"/></linearGradient></defs>'
    '<g class="lyr"><rect x="0" y="60" width="230" height="130" fill="url(#fv1)" rx="8"/>' + dots +
    '<text x="10" y="42" fill="currentColor" font-size="13" font-weight="600" opacity=".85">Air in</text>'
    '<text x="10" y="215" fill="currentColor" font-size="11.5" opacity=".5">'
    'PM2.5 ' + DOT + ' smoke ' + DOT + ' dust ' + DOT + ' pollen ' + DOT + ' dander</text></g>'
    '<g class="lyr"><rect x="238" y="52" width="52" height="146" rx="10" fill="none" '
    'stroke="currentColor" stroke-opacity=".35" stroke-width="1.5"/>' + bars +
    '<text x="264" y="42" fill="currentColor" font-size="12" font-weight="600" '
    'text-anchor="middle" opacity=".85">Pre-filter</text>'
    '<text x="264" y="218" fill="currentColor" font-size="11" text-anchor="middle" '
    'opacity=".5">Hair, large dust</text></g>'
    '<g class="lyr"><rect x="318" y="40" width="130" height="170" rx="14" '
    'fill="rgba(196,47,166,.14)" stroke="#C42FA6" stroke-opacity=".55" stroke-width="1.6"/>' + pleats +
    '<text x="383" y="28" fill="currentColor" font-size="13.5" font-weight="700" '
    'text-anchor="middle">HEPA H-13</text>'
    '<text x="383" y="232" fill="currentColor" font-size="11.5" text-anchor="middle" '
    'opacity=".6">99.95% at 0.3 microns</text></g>'
    '<g class="lyr"><rect x="478" y="60" width="242" height="130" fill="url(#fv2)" rx="8"/>' + waves +
    '<text x="710" y="42" fill="currentColor" font-size="13" font-weight="600" '
    'text-anchor="end" opacity=".85">Clean air out</text>'
    '<text x="710" y="215" fill="currentColor" font-size="11.5" text-anchor="end" '
    'opacity=".5">Up to 99.8% of PM2.5 cleared</text></g></svg>')


# =============================================================================
# COMPARE
# =============================================================================
def compare(d=1):
    r = rel(d)
    def yes(): return '<span style="color:var(--leaf);font-weight:600">&#10003; Yes</span>'
    def no():  return '<span class="dim">&mdash;</span>'
    rows = [
      ("Best for", lambda p: SPACE_LABEL[p["space"]]),
      ("Coverage", lambda p: "%d&ndash;%d sq.ft." % p["area"]),
      ("Launch price", lambda p: '<b class="tnum">%s</b>' % money(p["price"])),
      ("Filter grade", lambda p: "HEPA H-13"),
      ("Efficiency at 0.3&micro;m", lambda p: "99.95%"),
      ("PM2.5 clearance", lambda p: "Up to 99.8%"),
      ("RGB lighting", lambda p: yes() if "RGB" in " ".join(p["feats"]) else no()),
      ("AQI meter display", lambda p: yes() if "AQI" in " ".join(p["feats"]) else no()),
      ("Multiple fan modes", lambda p: yes() if "modes" in " ".join(p["feats"]) else no()),
      ("Low-noise operation", lambda p: yes()),
      ("", lambda p: '<a class="btn btn-p btn-sm" href="%sair-purifiers/%s/">View%s</a>'
                     % (r, p["slug"], arrow())),
    ]
    head = "".join(
      '<th style="--pc:%s"><a class="ph" href="%sair-purifiers/%s/">'
      '<img src="%sassets/derived/%s-product.png" alt="" width="44" height="56">'
      '<span><b>%s</b><span>%s</span></span></a></th>'
      % (p["accent"], r, p["slug"], r, p["id"], p["name"], p["role"]) for p in PRODUCTS)
    body = "".join('<tr><th>%s</th>%s</tr>'
                   % (label, "".join('<td>%s</td>' % fn(p) for p in PRODUCTS))
                   for label, fn in rows)
    picks = "".join(
      '<div class="card rv"><h3>%s</h3><p class="muted small" style="margin-top:10px">%s</p></div>'
      % (t, b) for t, b in [
        ("Pick the C-10 if the problem is your commute",
         "You spend forty minutes a day sealed in a cabin behind a diesel exhaust. It is the "
         "smallest volume of air you breathe and the dirtiest, which makes it the cheapest "
         "problem on this page to fix."),
        ("Pick the D-10 if the problem is where you work",
         "A desk, a cabin, a study table. You are stationary for nine hours and you want "
         "something quiet enough to forget about."),
        ("Pick the R-10 if the problem is where you sleep",
         "A bedroom or a nursery, and you want evidence rather than a promise. It is the only "
         "one of the three with a meter on the front, which is also why it carries the stronger "
         "guarantee."),
        ("Pick two if you have two rooms",
         "One unit does one closed room. We would rather say that plainly than let you buy a "
         "single R-10 for a three-bedroom flat and feel cheated in November."),
      ])
    return (
    '<section class="sec-tight"><div class="wrap">'
    '<div class="sec-h rv"><span class="eyebrow">Side by side</span>'
    '<h1 style="margin:14px 0 12px">Vayoo C-10 vs D-10 vs R-10</h1>'
    '<p class="lede">All three carry the same HEPA H13 grade. The differences are coverage, '
    'controls and whether the unit shows you a number.</p></div>'
    '<div class="tbl-scroll rv"><table class="cmp">'
    '<thead><tr><th></th>' + head + '</tr></thead><tbody>' + body + '</tbody></table></div>'
    '<p class="xs dim rv" style="margin-top:22px">Rated CADR, noise in decibels, power '
    'consumption and dimensions are published with the full specification sheets at launch.</p>'
    '<div style="margin-top:40px">' + sechead("Choosing", "Which one is actually yours?") +
    '<div class="grid g2">' + picks + '</div></div>'
    '</div></section>' + cta_band(d))


# =============================================================================
# FIND YOUR FIT
# =============================================================================
def find_your_fit(d=1):
    opts = "".join(
      '<button class="opt" data-space="%s"><b>%s</b><span>%s</span></button>' % o
      for o in [("car", "In the car", "Cabin of a hatchback, sedan or cab"),
                ("desk", "At a desk", "Workstation, office cabin or gaming setup"),
                ("room", "In a room", "Bedroom, living room, nursery or small office")])
    tips = "".join(
      '<div class="card"><div class="ico leaf">%s</div><h3>%s</h3>'
      '<p class="small muted" style="margin-top:9px">%s</p></div>' % t
      for t in [("clock", "Give it time to work",
                 "A purifier does not clean a room instantly. It cleans by turning the "
                 "room&rsquo;s air over repeatedly, which is why matching the model to the "
                 "space matters more than any single number."),
                ("room", "Shut the door",
                 "An open window undoes the work as fast as the filter does it. Every rated "
                 "coverage figure in this category assumes a closed space."),
                ("heart", "Size up, not down",
                 "If your room sits between two models, take the larger. An oversized purifier "
                 "runs slower and quieter; an undersized one runs flat out and still falls short.")])
    return (
    '<section class="sec-tight"><div class="wrap" style="max-width:900px">'
    '<div class="sec-h mid rv"><span class="eyebrow">Find your fit</span>'
    '<h1 style="margin:14px 0 12px">What size air purifier do I need?</h1>'
    '<p class="lede">Two questions. The answer is whichever model is rated to actually turn '
    'over the volume of air you are asking it to clean.</p></div>'
    '<div class="tool rv">'
    '<div class="tool-head"><span class="eyebrow">Step 1</span>'
    '<h2 style="margin-top:10px;font-size:1.4rem">Where does it need to work?</h2></div>'
    '<div class="tool-body" id="toolBody">'
    '<div class="opts">' + opts + '</div>'
    '<div class="rangebox" id="areaBox" hidden>'
    '<div class="row" style="justify-content:space-between">'
    '<div><span class="eyebrow">Step 2</span>'
    '<h2 style="margin-top:8px;font-size:1.4rem">How big is the space?</h2></div>'
    '<div class="center"><b class="tnum" id="areaOut" style="font-size:1.7rem;letter-spacing:-.03em">180</b>'
    '<div class="xs dim">sq. ft.</div></div></div>'
    '<input type="range" id="areaR" min="40" max="500" step="10" value="180" '
    'style="--p:30.4%" aria-label="Room area in square feet">'
    '<div class="row" style="justify-content:space-between">'
    '<span class="xs dim">40 sq.ft.</span><span class="xs dim">500 sq.ft.</span></div>'
    '<p class="xs dim">Length &times; breadth of the room in feet. A standard 10&times;12 '
    'bedroom is 120 sq.ft.; a 14&times;16 living room is 224 sq.ft.</p></div>'
    '<div id="resultBox"><p class="small dim">Pick a space above to see the recommendation.</p></div>'
    '</div></div>'
    '<div class="grid g3 rv" style="margin-top:30px">' + tips + '</div>'
    '<div class="card rv" style="margin-top:30px">'
    '<h2 style="font-size:1.4rem">How the sizing maths works</h2>'
    '<p class="muted" style="margin-top:12px">A purifier is rated for a floor area because the '
    'real variable is the volume of air it can move in an hour. Measure the room in feet, '
    'multiply length by breadth, and compare that to the coverage range on the model. Indian '
    'ceilings are usually close enough to ten feet that floor area is a fair proxy; if yours '
    'are notably higher, treat the room as larger than it measures.</p>'
    '<p class="muted" style="margin-top:12px">Two rules hold up across almost every room. '
    'First, <b>size up rather than down</b> &mdash; a unit running at a low setting in a room '
    'it comfortably covers is quieter, lasts longer and still turns the air over more times '
    'per hour than a smaller unit at full tilt. Second, <b>one unit cleans one closed room</b>. '
    'Purifiers do not pull air around corners, and an open door to an unfiltered room is, as '
    'far as the filter is concerned, an open window.</p>'
    '<p class="muted" style="margin-top:12px">If your space is larger than 400 sq.ft. or opens '
    'onto another room, the honest answer is more than one unit. '
    '<a href="' + rel(d) + 'contact/" style="color:var(--accent-tx)">Tell us the layout</a> '
    'and we will say what will actually work rather than sell you one and hope.</p></div>'
    '</div></section>' + cta_band(d))


# =============================================================================
# TECHNOLOGY (pillar)
# =============================================================================
def technology(d=1):
    r = rel(d)
    scale = dl([("A human hair", "&asymp; 70 microns"), ("Fine beach sand", "&asymp; 90 microns"),
                ("Pollen", "10&ndash;100 microns"), ("PM10 dust", "&le; 10 microns"),
                ("PM2.5", "&le; 2.5 microns"), ("HEPA H-13 test size", "0.3 microns")])
    grades = dl([("H11", "&ge; 95% at 0.3&micro;m"), ("H12", "&ge; 99.5%"),
                 ("H13", "&ge; 99.95% &mdash; first medical-grade"), ("H14", "&ge; 99.995%")])
    cards = "".join(
      '<div class="card hov rv"><div class="ico">%s</div><h3>%s</h3>'
      '<p class="muted small" style="margin-top:10px">%s</p></div>' % c
      for c in [("shield", "Every model, the same grade",
                 "The C-10 at " + money(1800) + " uses the same H13 grade as the R-10 at " +
                 money(6500) + ". The price difference is airflow and coverage, never "
                 "filtration quality."),
                ("wind", "Coverage is the other half",
                 "Filtration grade tells you what a filter catches. Coverage tells you how much "
                 "air it can catch it in. Both matter; only one changes between our models."),
                ("gauge", "Measured, not implied",
                 "The R-10 shows the room&rsquo;s AQI on the unit. We would rather you watched "
                 "the number than believed a claim.")])
    return (
    '<section class="sec-tight"><div class="wrap">'
    '<div class="sec-h mid rv"><span class="eyebrow">Technology</span>'
    '<h1 style="margin:14px 0 12px">What HEPA H13 actually means</h1>'
    '<p class="lede">There is a great deal of noise in this category. Here is the part that is '
    'measurable, the part that is marketing, and the part we deliberately do not claim.</p></div>'
    '<div class="rv" style="margin-bottom:50px">' + filter_viz() + '</div>'

    '<div class="split" style="margin-bottom:56px;align-items:start">'
    '<div class="rv"><h2>H13 is a test, not an adjective</h2>'
    '<p class="lede" style="margin-top:16px">HEPA filters are graded on a formal scale. H13 is '
    'the first grade classed as medical-grade, and it is defined by a measurement: it must '
    'capture <b>99.95% of particles at 0.3 microns</b>.</p>'
    '<p class="muted" style="margin-top:16px">0.3 microns is not chosen because it is the '
    'smallest particle. It is chosen because it is the <i>hardest</i> one to catch. Larger '
    'particles are trapped by simple interception. Much smaller ones move erratically enough '
    'that they collide with the fibres anyway. The 0.3 micron range slips through both '
    'mechanisms most easily &mdash; so grading a filter there grades it at its worst case.</p>'
    '<p class="muted" style="margin-top:16px">That is why the number is worth quoting. A filter '
    'that holds 99.95% at its weakest point does better than that everywhere else.</p></div>'
    '<div class="rv"><div class="card" style="background:var(--surface-2)">'
    '<h3 style="margin-bottom:16px">The grades, in order</h3>' + grades +
    '<p class="xs dim" style="margin-top:14px">Below H11, a filter is not HEPA at all, whatever '
    'the box says.</p></div></div></div>'

    # --- the fake HEPA section: the lead magnet's subject, on-page
    '<div class="card rv" style="margin-bottom:46px;border-color:rgba(229,72,77,.3)">'
    '<div class="ico">' + ic('factory') + '</div>'
    '<h2 style="font-size:1.6rem">The words that mean it is not HEPA</h2>'
    '<p class="muted" style="margin-top:12px;max-width:72ch">This is the single most useful '
    'thing you can learn before buying anything in this category. &ldquo;HEPA&rdquo; is a '
    'standard. These phrases are built to sound like it and are specifically not it:</p>'
    '<div class="grid g3" style="margin-top:20px">'
    '<div class="card" style="background:var(--surface-2)"><h3>&ldquo;HEPA-type&rdquo;</h3>'
    '<p class="small muted" style="margin-top:8px">Not graded HEPA. Typically H11 at best, '
    'which catches around 95% &mdash; meaning it passes roughly a hundred times more particles '
    'than H13 at the test size.</p></div>'
    '<div class="card" style="background:var(--surface-2)"><h3>&ldquo;HEPA-like&rdquo; / '
    '&ldquo;HEPA-style&rdquo;</h3><p class="small muted" style="margin-top:8px">Marketing '
    'constructions with no standard behind them at all. If a listing uses these, the filter '
    'did not pass the test.</p></div>'
    '<div class="card" style="background:var(--surface-2)"><h3>&ldquo;99.97% efficient&rdquo; '
    'with no size</h3><p class="small muted" style="margin-top:8px">An efficiency figure means '
    'nothing without the particle size it was measured at. Ask at what micron rating &mdash; '
    'if the listing will not say, assume the worst.</p></div></div>'
    '<p class="small muted" style="margin-top:20px">Vayoo states H13 and states the test size, '
    'because a grade you cannot check is a decoration.</p></div>'

    '<div class="split" style="margin-bottom:50px;align-items:start">'
    '<div class="rv"><h2>Why 0.3 microns is the number that matters</h2>'
    '<p class="muted" style="margin-top:14px">PM2.5 &mdash; particulate under 2.5 microns &mdash; '
    'is the fraction small enough to pass from the lung into the bloodstream. It is what India&rsquo;s '
    'AQI is mostly driven by, and it is what an H13 filter is built for. The table opposite puts '
    'the sizes in order; note how far below everything familiar the test size sits.</p>'
    '<p class="muted" style="margin-top:14px">A filter graded at 0.3 microns is therefore '
    'comfortably inside the range that does the damage. That is the entire technical case for '
    'H13 over H11, and it is why we did not build a cheaper model on a lower grade.</p></div>'
    '<div class="rv"><div class="card" style="background:var(--surface-2)">'
    '<h3 style="margin-bottom:16px">The scale of the thing</h3>' + scale +
    '<p class="xs dim" style="margin-top:16px">For comparison: a human hair is roughly 230 times '
    'wider than the particle an H13 filter is tested against.</p></div></div></div>'

    '<div class="grid g3" style="margin-bottom:30px">' + cards + '</div>'

    '<div class="card rv" style="border-color:rgba(125,203,41,.3)">'
    '<div class="ico leaf">' + ic('leaf') + '</div>'
    '<h2 style="font-size:1.6rem">What we do not claim</h2>'
    '<p class="muted" style="margin-top:12px;max-width:72ch">A HEPA filter is a particle filter. '
    'It does not remove odour molecules, volatile organic compounds or carbon monoxide &mdash; '
    'those need a gas-phase medium such as activated carbon, and no amount of HEPA grading '
    'changes that. It does not sterilise a room. It cannot clean air that is being replaced '
    'through an open window. And it will not fix the air outside your front door.</p>'
    '<p class="muted" style="margin-top:12px;max-width:72ch">Anyone telling you otherwise is '
    'selling you a story rather than a filter.</p>'
    '<div class="row" style="margin-top:22px">'
    '<a class="btn btn-p" href="' + r + 'air-purifiers/">See the range' + arrow() + '</a>'
    '<a class="btn btn-g" href="' + r + 'find-your-fit/">Find my fit</a></div></div>'
    '</div></section>' + cta_band(d))


# =============================================================================
# ABOUT
# =============================================================================
FOUNDERS = [
 dict(n="Praful Chauhan", r="Co-Founder", i="PC",
      li="https://www.linkedin.com/in/praful-chauhan-18037816a/",
      b=["Extensive background in marketing and building modern D2C businesses.",
         "Proven track record in driving early-stage startup growth and brand awareness.",
         "Passionate about delivering high-quality, affordable clean-tech appliances to the Indian masses."]),
 dict(n="Abhinav Verma", r="Co-Founder", i="AV",
      li="https://www.linkedin.com/in/iabhinavv",
      b=["Core expertise in finance, operations and scaling consumer-focused startups.",
         "Experienced in establishing lean supply chains for accessible pricing strategies.",
         "Committed to revolutionising air quality in India for vulnerable communities."]),
]
LI_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.5 2.5 0 1 0 5 8.5a2.5 '
          '2.5 0 0 0-.02-5zM3 9.5h4v11H3v-11zm7 0h3.8v1.5h.05c.53-.95 1.83-1.95 3.77-1.95 4.03 0 '
          '4.78 2.5 4.78 5.76v5.69h-4v-5.05c0-1.2-.02-2.75-1.75-2.75-1.75 0-2.02 1.3-2.02 '
          '2.66v5.14h-4v-11z"/></svg>')


def about(d=1):
    cards = "".join(
      '<div class="card hov rv"><div class="ico">%s</div><h3>%s</h3>'
      '<p class="muted" style="margin-top:12px">%s</p></div>' % c
      for c in [("people", "What we are solving, and for whom",
                 "The crisis of unbreathable air in India&rsquo;s metros &mdash; for the mass "
                 "majority of youth, elderly and children who cannot afford an expensive "
                 "purifier but deserve fresh air exactly as much as anyone who can."),
                ("clock", "Why now, and why us",
                 "We came to this from the inside. The founding team grew up in cities where AQI "
                 "was never a word anyone used, and met the problem head-on when work moved them "
                 "to Delhi NCR."),
                ("rupee", "Our USP",
                 "Being the brand that is there for the masses &mdash; affordable, with no "
                 "compromise on quality. Because not just you, but everyone deserves to breathe "
                 "better."),
                ("heart", "How we build",
                 "Lean supply chains, a small team, and a refusal to publish a specification we "
                 "have not measured. If a number is not on this site yet, it is because we do "
                 "not have it confirmed &mdash; not because it is inconvenient.")])
    team = "".join(
      '<div class="card hov rv founder"><div class="founder-top">'
      '<div class="row" style="gap:14px"><div class="avatar">%s</div>'
      '<div><h3>%s</h3><p class="small" style="color:var(--accent-tx)">%s</p></div></div>'
      '<a class="li-link" href="%s" target="_blank" rel="noopener" '
      'aria-label="%s on LinkedIn">%s</a></div>%s</div>'
      % (f["i"], f["n"], f["r"], f["li"], f["n"], LI_SVG, checks(f["b"])) for f in FOUNDERS)
    return (
    '<section class="sec-tight"><div class="wrap">'
    '<div class="sec-h mid rv" style="max-width:56ch"><span class="eyebrow">Our story</span>'
    '<h1 style="margin:16px 0 18px">Clean air, for the people breathing the worst of it</h1>'
    '<p class="lede">The best time to make a change was yesterday. The second best time is now.</p></div>'
    '<div class="grid g2 rv" style="margin-bottom:44px">'
    '<div class="card" style="border-color:rgba(196,47,166,.3)"><div class="ico">' + ic('spark') + '</div>'
    '<h2 style="font-size:1.4rem">Our mission</h2><p class="muted" style="margin-top:10px">To '
    'become India&rsquo;s number one clean-tech appliances brand, and help India become cleaner '
    'and fresher in the process.</p></div>'
    '<div class="card" style="border-color:rgba(125,203,41,.3)"><div class="ico leaf">' + ic('leaf') + '</div>'
    '<h2 style="font-size:1.4rem">Our vision</h2><p class="muted" style="margin-top:10px">To give '
    'India the birth-right of pure air to breathe, and build a better tomorrow for the '
    'generation after this one.</p></div></div>'
    '<div class="grid g2" style="gap:clamp(16px,2.5vw,22px)">' + cards + '</div>'
    '</div></section>'
    '<section class="sec-tight"><div class="wrap">'
    + sechead("The team", "Two founders, and a team of young enthusiasts",
              "Our team brings together experience in D2C businesses, marketing, finance and "
              "startups. Beyond the founders, a team of young enthusiasts runs day-to-day "
              "operations.")
    + '<div class="grid g2">' + team + '</div></div></section>' + cta_band(d))


# =============================================================================
# CONTACT
# =============================================================================
def contact(d=1):
    r = rel(d)
    return (
    '<section class="sec-tight"><div class="wrap">'
    '<div class="sec-h mid rv"><span class="eyebrow">Contact</span>'
    '<h1 style="margin:14px 0 12px">Talk to the people who built it</h1>'
    '<p class="lede">Product questions, support, bulk orders, partnerships. It reaches the '
    'founders, not a queue.</p></div>'
    '<div class="split" style="align-items:start;gap:clamp(24px,4vw,44px)">'
    '<div style="display:grid;gap:16px">'
    '<a class="card hov rv" href="mailto:' + EMAIL + '"><div class="ico">' + ic('mail') + '</div>'
    '<h2 style="font-size:1.3rem">Email us</h2>'
    '<p class="small muted" style="margin:8px 0 12px">We reply within 24 hours on working days.</p>'
    '<b style="color:var(--accent-tx)">' + EMAIL + '</b></a>'
    '<a class="card hov rv" href="tel:' + PHONE_TEL + '"><div class="ico">' + ic('phone') + '</div>'
    '<h2 style="font-size:1.3rem">Call us</h2>'
    '<p class="small muted" style="margin:8px 0 12px">Monday to Friday, 9am to 6pm IST.</p>'
    '<b style="color:var(--accent-tx)">' + PHONE_HUMAN + '</b></a>'
    '<div class="card rv"><h3 style="margin-bottom:12px">Follow along</h3>'
    '<p class="small muted" style="margin-bottom:14px">Product updates and launch news land '
    'here first.</p><div class="row">'
    '<a class="btn btn-g btn-sm" href="' + INSTAGRAM + '" target="_blank" rel="noopener">Instagram</a>'
    '<a class="btn btn-g btn-sm" href="' + LINKEDIN + '" target="_blank" rel="noopener">LinkedIn</a>'
    '</div></div></div>'
    '<div class="rv" style="display:grid;gap:16px">'
    '<div class="card"><h2 style="font-size:1.3rem">Bulk and corporate orders</h2>'
    '<p class="muted" style="margin-top:12px">Offices, clinics, schools, cab fleets and '
    'housing societies. Tell us how many units and how many rooms, and we will come back with '
    'a sizing plan and a price rather than a catalogue.</p>'
    '<a class="btn btn-p btn-sm" style="margin-top:16px" href="mailto:' + EMAIL +
    '?subject=Vayoo%20%E2%80%94%20bulk%20order%20enquiry">Email the founders' + arrow() + '</a></div>'
    '<div class="card" style="background:var(--surface-2)">'
    '<h3>Before you write in about sizing</h3>'
    '<p class="small muted" style="margin-top:10px">Nine out of ten sizing questions are '
    'answered in sixty seconds by the fit tool. If yours is an odd layout &mdash; an open-plan '
    'floor, a double-height ceiling, a shop front &mdash; write to us instead and describe it.</p>'
    '<a class="btn btn-s btn-sm" style="margin-top:14px" href="' + r + 'find-your-fit/">'
    'Try the fit tool' + arrow() + '</a></div></div>'
    '</div></div></section>')


# =============================================================================
# FAQ  (QAPage -- not FAQPage; Google retired FAQ rich results 7 May 2026)
# =============================================================================
FAQS = [
 ("Do air purifiers actually work in Indian conditions?",
  "In a closed room, yes. The clearest published measurement we know of is a Delhi office in "
  "January 2026, where the indoor reading was 309 against 348 outside with no purifier running, "
  "and 48 with one running. What a purifier cannot do is help with a window open, or clean the "
  "air outside your door."),
 ("What does HEPA H13 mean?",
  "HEPA filters are graded. H13 is the first grade classed as medical-grade and must capture "
  "99.95% of particles at 0.3 microns &mdash; the hardest particle size to trap. Grades below "
  "it (H11, H12) catch measurably less."),
 ("Is &ldquo;HEPA-type&rdquo; the same thing?",
  "No, and the distinction matters more than almost anything else on a listing. "
  "&ldquo;HEPA-type&rdquo;, &ldquo;HEPA-like&rdquo; and &ldquo;HEPA-style&rdquo; specifically "
  "mean the filter did not meet the HEPA standard. They are usually H11, around 95% capture."),
 ("Which Vayoo model do I need?",
  "Measure the room in feet and multiply length by breadth. Up to about 70 sq.ft. or a car "
  "cabin, the C-10. Between 80 and 125 sq.ft., the D-10. From there up to 400 sq.ft., the R-10. "
  "If you fall between two, take the larger."),
 ("Can one unit cover my whole flat?",
  "No. One unit cleans one closed room. Purifiers do not pull air around corners, and an open "
  "door to an unfiltered room behaves like an open window. A multi-room home needs a unit per "
  "room you actually use."),
 ("How long before I notice a difference?",
  "A purifier works by turning a room&rsquo;s air over repeatedly rather than cleaning it in "
  "one pass. Our guarantee is built around one hour in a closed room, which is a fair test of "
  "whether it is doing anything at all."),
 ("Do I need to run it all day?",
  "It works best running continuously in a closed room. Running it in short bursts means the "
  "room reloads with unfiltered air between sessions."),
 ("Can I wash the HEPA filter?",
  "Never. Water destroys the fibre structure that does the filtering. The pre-filter layer "
  "catches hair and larger dust and can be vacuumed; the H13 layer is a replacement part."),
 ("How often will I need to replace the filter?",
  "It depends entirely on what you are asking it to clean &mdash; a car in Delhi traffic loads "
  "a filter far faster than a bedroom in a coastal town. Replacement intervals and pricing are "
  "published with the full specification sheet at launch."),
 ("Does it remove smells, or cooking odour?",
  "No, and we will not claim it does. A HEPA filter is a particle filter. Odour molecules and "
  "VOCs need a gas-phase medium such as activated carbon."),
 ("Does it produce ozone?",
  "Vayoo units filter air mechanically through H13 media. Buying guides routinely warn against "
  "ioniser-based purifiers because ionisers can emit ozone &mdash; worth checking on any "
  "product you are comparing."),
 ("What is the AQI meter on the R-10 for?",
  "It shows the air quality in the room, on the unit. It is why the R-10 carries our stronger "
  "guarantee: you do not have to believe the claim, you can watch the number."),
 ("What is your guarantee?",
  "The Watch-It-Work Guarantee. Shut the room, run the R-10 for an hour, watch the AQI number. "
  "If it does not fall, send it back within 30 days for a full refund and we pay the return "
  "pickup. The C-10 and D-10 carry a 30-day no-questions return on the same terms."),
 ("Are the products on sale yet?",
  "Not yet. All three are in final production. Joining the launch list places no order and "
  "takes no payment &mdash; it locks your launch price and puts you ahead of general release."),
 ("Why is Vayoo cheaper than the big brands?",
  "We did not build an app, an account system, a subscription or a cloud service, and we are "
  "not paying for a decade of brand advertising. The H13 filter is the part that does the work "
  "and that is where the money went."),
 ("Do you ship across India?",
  "Delivery coverage, shipping charges and timelines are confirmed before the first unit ships. "
  "Join the launch list and you will get those details in the launch email."),
 ("Is there a warranty?",
  "Warranty terms, service turnaround and replacement-filter supply are being finalised "
  "alongside production and will be published in full before the first unit ships."),
 ("Do you sell to offices, clinics or cab fleets?",
  "Yes. Write to " + EMAIL + " with the number of rooms and their rough sizes, and we will come "
  "back with a sizing plan rather than a catalogue."),
]


def faq(d=1):
    r = rel(d)
    rows = "".join(
      '<div class="card rv"><h2 style="font-size:1.15rem">%s</h2>'
      '<p class="muted" style="margin-top:10px">%s</p></div>' % (q, a) for q, a in FAQS)
    return (
    '<section class="sec-tight"><div class="wrap" style="max-width:860px">'
    '<div class="sec-h rv"><span class="eyebrow">FAQ</span>'
    '<h1 style="margin:14px 0 12px">Air purifier questions, answered straight</h1>'
    '<p class="lede">Including the ones where the honest answer is &ldquo;no&rdquo; or '
    '&ldquo;we have not measured that yet&rdquo;.</p></div>'
    '<div style="display:grid;gap:14px">' + rows + '</div>'
    '<div class="card rv" style="margin-top:26px;background:var(--surface-2)">'
    '<h3>Not answered here?</h3><p class="muted small" style="margin-top:10px">Write to us. '
    'The founders read it.</p><div class="row" style="margin-top:14px">'
    '<a class="btn btn-p btn-sm" href="' + r + 'contact/">Contact us' + arrow() + '</a>'
    '<a class="btn btn-g btn-sm" href="' + r + 'technology/">Read the technology page</a>'
    '</div></div></div></section>' + cta_band(d))


# =============================================================================
# NOTIFY  (conversion page, noindex)
# =============================================================================
def notify(d=1):
    r = rel(d)
    return (
    '<section class="sec-tight"><div class="wrap" style="max-width:980px">'
    '<div class="sec-h mid rv" style="max-width:56ch"><span class="eyebrow">Pre-launch</span>'
    '<h1 style="margin:16px 0 16px">Three things, for an email address</h1>'
    '<p class="lede">All three models are in final production. The list is how we tell you the '
    'day pre-orders open &mdash; and it is the only way to lock the launch price.</p></div>'
    '<div class="split" style="align-items:start;gap:clamp(24px,4vw,40px)">'
    '<div class="rv"><div class="card" style="padding:0;overflow:hidden">'
    '<iframe src="' + NOTIFY_FORM + '?embedded=true" width="100%" height="820" frameborder="0" '
    'marginheight="0" marginwidth="0" title="Vayoo launch list signup form" '
    'style="display:block;border:0;background:#fff">Loading&hellip;</iframe></div></div>'
    '<div class="rv" style="display:grid;gap:16px">'
    '<div class="card" style="border-color:rgba(125,203,41,.35)">'
    '<div class="ico leaf">' + ic('bolt') + '</div>'
    '<h2 style="font-size:1.3rem">What you get</h2>'
    + checks([("Pre-orders first", "the list orders before general release, while the founding "
               "batch is still available."),
              ("Your launch price, locked", money(1800) + " / " + money(3000) + " / " +
               money(6500) + " &mdash; held for you even if retail opens higher."),
              ("The Fake HEPA Checklist", "six things to check on any listing before you buy, "
               "sent the moment you join. Useful even if you never buy from us."),
              ("The full spec sheet", "CADR, noise, filter life and warranty, the day they are "
               "published.")])
    + '</div>'
    '<div class="card" style="background:var(--surface-2)">'
    '<h3>What you will not get</h3>'
    + checks([("No drip campaign", "we write when there is something to say."),
              ("No payment taken", "joining the list is not an order and costs nothing."),
              ("No data sold", "ask us to delete your details and we will.")])
    + '</div>'
    '<div class="card"><h3>Still deciding which one?</h3>'
    '<p class="small muted" style="margin-top:10px">The fit tool takes sixty seconds and will '
    'tell you if the honest answer is two units.</p>'
    '<a class="btn btn-s btn-sm" style="margin-top:14px" href="' + r + 'find-your-fit/">'
    'Find my fit' + arrow() + '</a></div>'
    '</div></div></div></section>')


# =============================================================================
# LEGAL
# =============================================================================
def legal(d=1):
    return (
    '<section class="sec-tight"><div class="wrap" style="max-width:780px">'
    '<div class="sec-h rv"><span class="eyebrow">Legal</span>'
    '<h1 style="margin:14px 0 12px">Privacy and terms</h1>'
    '<p class="lede">Plain language, because there is not much to hide behind at this stage.</p></div>'
    '<div class="card rv" style="margin-bottom:18px" id="privacy"><h2 style="font-size:1.4rem">Privacy</h2>'
    '<p class="muted" style="margin-top:12px">This site runs no analytics, advertising trackers '
    'or third-party scripts. Your theme preference is stored in your own browser and never '
    'leaves it; clearing your browser data removes it.</p>'
    '<p class="muted" style="margin-top:12px">The launch-list form is a Google Form. Details you '
    'submit there are held in Google&rsquo;s systems under Google&rsquo;s privacy terms, and are '
    'used by us only to contact you about the launch and to fulfil an order. We do not sell '
    'personal data.</p>'
    '<p class="muted" style="margin-top:12px">To access or delete anything you have sent us, '
    'write to <a href="mailto:' + EMAIL + '" style="color:var(--accent-tx)">' + EMAIL + '</a>.</p></div>'
    '<div class="card rv" id="terms"><h2 style="font-size:1.4rem">Terms</h2>'
    '<p class="muted" style="margin-top:12px">Vayoo products are not yet on sale. Nothing on '
    'this site is an offer of sale, and no payment is taken here. Prices shown are intended '
    'launch prices and may change before products go on sale; launch-list members keep the '
    'price shown at the time they joined.</p>'
    '<p class="muted" style="margin-top:12px">Product specifications shown are those confirmed '
    'at the time of writing. Full specification sheets, warranty terms and service details are '
    'published before the first unit ships. Air quality figures used to illustrate the AQI '
    'bands are illustrative and are not live readings or performance guarantees for any Vayoo '
    'model. Third-party measurements are attributed where used.</p>'
    '<p class="muted" style="margin-top:12px">The Watch-It-Work Guarantee applies from the date '
    'of delivery and requires the unit to be returned in working condition with its original '
    'accessories. Full terms are published alongside the warranty before the first unit ships.</p>'
    '<p class="muted" style="margin-top:12px">Questions about any of this: '
    '<a href="mailto:' + EMAIL + '" style="color:var(--accent-tx)">' + EMAIL + '</a> or '
    + PHONE_HUMAN + '.</p></div></div></section>')


# =============================================================================
# INVESTOR RELATIONS  (noindex -- audience page, not a search landing page.
# Carried over from the previous build; figures are Vayoo's own projections.)
# =============================================================================
MARKET = [("TAM", 2900, "Total addressable market, industrial and domestic"),
          ("SAM", 1800, "Serviceable addressable market"),
          ("SOM", 907, "Serviceable obtainable market")]


def investors(d=1):
    r = rel(d)
    bars = "".join(
      '<div><div class="row" style="justify-content:space-between;margin-bottom:9px">'
      '<div class="row" style="gap:10px"><b style="font-size:1.02rem">%s</b>'
      '<span class="small dim">%s</span></div>'
      '<b class="tnum" style="font-size:1.15rem">%s%d Cr</b></div>'
      '<div style="height:12px;border-radius:100px;background:var(--surface-2);overflow:hidden">'
      '<div style="height:100%%;width:%.1f%%;border-radius:100px;background:var(--grad-cta)"></div>'
      '</div></div>' % (k, lbl, RUPEE, v, v / 2900.0 * 100) for k, v, lbl in MARKET)
    stats = "".join(
      '<div class="stat"><div class="v tnum">%s</div><div class="k">%s</div>'
      '<div class="d">%s</div></div>' % s
      for s in [("28.51%", "Industry CAGR",
                 "The estimated growth rate of the Indian air purifier industry through 2030."),
                (money(1800), "Entry price",
                 "The segment we are building for is the one nobody is currently pricing for."),
                ("3", "Form factors",
                 "Car, desk and room &mdash; one brand covering every space a customer moves "
                 "through in a day.")])
    return (
    '<section class="sec-tight"><div class="wrap">'
    '<div class="sec-h mid rv" style="max-width:58ch">'
    '<span class="tag tag-acc">Investor relations</span>'
    '<h1 style="margin:18px 0 16px">Be part of the change in how India breathes</h1>'
    '<p class="lede">Vayoo is raising a seed round to put the vision into execution and scale '
    'into a market that is large, growing fast, and almost entirely priced out of reach of the '
    'people worst affected.</p></div>'
    '<div class="cta-band rv" style="text-align:left;margin-bottom:40px">'
    '<div class="split" style="align-items:center"><div>'
    '<span class="eyebrow" style="color:rgba(255,255,255,.7)">The ask</span>'
    '<div style="font-size:clamp(2.4rem,6vw,3.6rem);font-weight:650;letter-spacing:-.04em;'
    'margin:12px 0 6px" class="tnum">' + RUPEE + '50 Lac</div>'
    '<p style="font-size:1.1rem;color:rgba(255,255,255,.86)">Seed round for 10% equity</p>'
    '<a class="btn btn-leaf btn-lg" href="mailto:' + EMAIL +
    '?subject=Vayoo%20%E2%80%94%20Investor%20enquiry" style="margin-top:24px">'
    'Contact the founders' + arrow() + '</a></div>'
    '<div style="background:rgba(0,0,0,.3);border:1px solid rgba(255,255,255,.16);'
    'border-radius:var(--r-lg);padding:26px;backdrop-filter:blur(8px)">'
    '<h2 style="font-size:1.1rem;display:flex;gap:9px;align-items:center;margin-bottom:12px">'
    '<span style="width:26px;height:26px;display:grid;place-items:center;color:#7DCB29">'
    + ic('bolt') + '</span>Goal for the next two years</h2>'
    '<p style="color:rgba(255,255,255,.86)">Reach ' + RUPEE + '20 crore in revenue while staying '
    'EBITDA-positive from the first quarter, through aggressive D2C and e-commerce execution.</p>'
    '</div></div></div>'
    + sechead("Market", "A large market, growing fast, badly served at the bottom",
              "The Indian air purifier market is expanding at an estimated <b>28.51% CAGR "
              "through 2030</b> &mdash; and almost all of that supply is priced for the top of "
              "the pyramid.")
    + '<div class="card rv" style="margin-bottom:26px">'
      '<div style="display:grid;gap:22px">' + bars + '</div></div>'
    '<div class="grid g3 rv" style="margin-bottom:30px">' + stats + '</div>'
    '<div class="card rv"><h2 style="font-size:1.4rem">Why this team</h2>'
    '<p class="muted" style="margin-top:12px;max-width:74ch">Our combined experience spans D2C '
    'businesses, marketing, finance and startups. We came to this problem as customers first '
    '&mdash; the founding team grew up in cities where AQI was never a concern and met it '
    'directly when work moved them to Delhi NCR.</p>'
    '<div class="row" style="margin-top:22px">'
    '<a class="btn btn-s" href="' + r + 'for-investors/">Meet the founders' + arrow() + '</a>'
    '<a class="btn btn-g" href="mailto:' + EMAIL +
    '?subject=Vayoo%20%E2%80%94%20Investor%20enquiry">Request the deck</a></div></div>'
    '<p class="xs dim rv" style="margin-top:24px;max-width:74ch">Figures on this page are '
    'Vayoo&rsquo;s own estimates and projections prepared for fundraising discussions. They are '
    'forward-looking, not guarantees, and should be read alongside the full materials available '
    'on request.</p>'
    '</div></section>')


def for_investors(d=1):
    r = rel(d)
    team = "".join(
      '<div class="card hov rv founder"><div class="founder-top">'
      '<div class="row" style="gap:14px"><div class="avatar">%s</div>'
      '<div><h3>%s</h3><p class="small" style="color:var(--accent-tx)">%s</p></div></div>'
      '<a class="li-link" href="%s" target="_blank" rel="noopener" '
      'aria-label="%s on LinkedIn">%s</a></div>%s</div>'
      % (f["i"], f["n"], f["r"], f["li"], f["n"], LI_SVG, checks(f["b"])) for f in FOUNDERS)
    return (
    '<section class="sec-tight"><div class="wrap">'
    '<div class="sec-h rv"><span class="eyebrow">The team</span>'
    '<h1 style="margin:14px 0 12px">Two founders, and a team of young enthusiasts</h1>'
    '<p class="lede">Our team brings together experience in D2C businesses, marketing, finance '
    'and startups. Beyond the founders, a team of young enthusiasts runs day-to-day '
    'operations.</p></div>'
    '<div class="grid g2">' + team + '</div>'
    '<div class="card rv" style="margin-top:30px;background:var(--surface-2)">'
    '<h2 style="font-size:1.3rem">Looking at Vayoo as an investment?</h2>'
    '<p class="muted small" style="margin-top:10px">The round, the market sizing and the '
    'two-year goal are on the investor relations page.</p>'
    '<a class="btn btn-p btn-sm" style="margin-top:14px" href="' + r + 'investors/">'
    'Investor relations' + arrow() + '</a></div>'
    '</div></section>')
