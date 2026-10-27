# -*- coding: utf-8 -*-
"""Shared markup components for the Vayoo static site.

Every class name here matches assets/vayoo.css, which was lifted verbatim from
the original single-file build. The design is unchanged; only the routing is.
"""

RUPEE = '₹'
DOT = '·'

# --- site-wide constants -----------------------------------------------------
# Switch SITE_URL to "https://vayoo.store" on the day DNS resolves, then rebuild.
# Canonicals must point somewhere that actually loads, so until then they point
# at the live GitHub Pages host.
SITE_URL = "https://iabhinavv.github.io/vayoo"
BRAND = "Vayoo"
EMAIL = "abhinav@vayoo.store"
PHONE_HUMAN = "+91 70099 79996"
PHONE_TEL = "+917009979996"
INSTAGRAM = "https://www.instagram.com/vayoo.store"
LINKEDIN = "https://www.linkedin.com/company/vayoo-store"
NOTIFY_FORM = ("https://docs.google.com/forms/d/e/"
               "1FAIpQLSespDmvGhLIowHJU-HN2L1urQNjpe9_Mu_uBD-mF2-ebmoYPA/viewform")


def rel(depth):
    """Relative prefix to the site root, so the build works both on a project
    subpath (iabhinavv.github.io/vayoo/) and on a bare domain."""
    return "" if depth == 0 else "../" * depth


# --- products ----------------------------------------------------------------
PRODUCTS = [
    dict(
        id="c10", slug="c10-car-air-purifier", name="Vayoo C-10",
        role="Portable Car Air Purifier", space="car", price=1800,
        area=(50, 70), accent="#C42FA6",
        tagline="Your commute is the dirtiest air you breathe all day.",
        feats=["Aesthetic RGB mood lights", "Vertical wind circulation",
               "HEPA H-13 filter", "Low-noise operation"],
        highlight="Vertical wind circulation",
        highlight_note=("Air is drawn in and pushed upward through the cabin rather "
                        "than across it, so it turns over the whole volume instead of "
                        "one seat."),
        fits="Hatchbacks, sedans and cabs, and any enclosed space of roughly 50-70 sq.ft.",
        not_for=("A 7-seater MPV with the middle row full, or an SUV with the boot "
                 "open. Past about 70 sq.ft. of cabin you want two, or the D-10 "
                 "wedged in the footwell."),
    ),
    dict(
        id="d10", slug="d10-desk-air-purifier", name="Vayoo D-10",
        role="Compact Desk Air Purifier", space="desk", price=3000,
        area=(80, 125), accent="#7B3FE4",
        tagline="You breathe the one metre around your face for nine hours a day.",
        feats=["RGB lights", "Low-noise operation", "HEPA H-13 filter",
               "Built for workstations"],
        highlight="Low-noise operation",
        highlight_note=("Built to run beside you all day without competing with a "
                        "call, a lecture or a game."),
        fits="Workstations, office cabins, study tables and gaming setups of roughly 80-125 sq.ft.",
        not_for=("A full bedroom. At 120 sq.ft. it is working hard; a 10x12 bedroom "
                 "with the door shut is the top of its range, not its comfort zone."),
    ),
    dict(
        id="r10", slug="r10-room-air-purifier", name="Vayoo R-10",
        role="Premium Room Air Purifier", space="room", price=6500,
        area=(350, 400), accent="#7DCB29", badge="Most popular",
        tagline="The whole room, and the number on the front to prove it.",
        feats=["3 fan modes", "On-board AQI meter display", "Low-noise operation",
               "HEPA H-13 filter"],
        highlight="On-board AQI meter",
        highlight_note=("A live readout on the unit itself. It is the difference "
                        "between hoping the air got better and watching it happen."),
        fits="Bedrooms, living rooms, nurseries and small offices of roughly 350-400 sq.ft.",
        not_for=("An open-plan floor, or a room with a window open. Past 400 sq.ft. "
                 "the honest answer is two units, and we would rather tell you that "
                 "than sell you one."),
    ),
]
BY_ID = {p["id"]: p for p in PRODUCTS}
SPACE_LABEL = {"car": "Car", "desk": "Desk & workstation", "room": "Room"}


def money(n):
    return RUPEE + format(int(n), ",d").replace(",", ",")


# --- icons (same set as the original build) ----------------------------------
ICON = {
 'car': '<path d="M5 17h14M6.5 17v1.5M17.5 17v1.5M4 13l1.6-4.4A2 2 0 0 1 7.5 7h9a2 2 0 0 1 1.9 1.6L20 13v4H4v-4z"/><circle cx="7.5" cy="14.5" r=".9" fill="currentColor"/><circle cx="16.5" cy="14.5" r=".9" fill="currentColor"/>',
 'desk': '<rect x="3" y="4.5" width="18" height="12" rx="2"/><path d="M8 20h8M12 16.5V20"/>',
 'room': '<path d="M4 10.5L12 4l8 6.5V20H4v-9.5z"/><path d="M9.5 20v-6h5v6"/>',
 'shield': '<path d="M12 3l7.5 3v5.5c0 4.6-3.1 8.3-7.5 9.5-4.4-1.2-7.5-4.9-7.5-9.5V6L12 3z"/><path d="M8.8 12l2.3 2.3 4.1-4.6"/>',
 'wind': '<path d="M3 8.5h9.5a2.7 2.7 0 1 0-2.7-2.7M3 15.5h13a2.7 2.7 0 1 1-2.7 2.7M3 12h16"/>',
 'bolt': '<path d="M13 2.5L4.5 13.5H11l-1 8 8.5-11H12l1-8z"/>',
 'leaf': '<path d="M20 4C9 4 4.5 9 4.5 15.5c0 2.2 1 3.9 1 3.9M5.5 19.4S9 12 20 4"/><path d="M5.5 19.4c8 1.3 13-3.4 14.5-15.4"/>',
 'factory': '<path d="M3 20h18V9l-6 3.5V9l-6 3.5V4H3v16z"/><path d="M7 16.5h1.5M11.5 16.5H13M16 16.5h1.5"/>',
 'gauge': '<path d="M4.2 17a9 9 0 1 1 15.6 0"/><path d="M12 13.5l4-3.5"/><circle cx="12" cy="14.5" r="1.4" fill="currentColor" stroke="none"/>',
 'heart': '<path d="M12 20s-7.5-4.6-7.5-9.5A4.2 4.2 0 0 1 12 8a4.2 4.2 0 0 1 7.5 2.5C19.5 15.4 12 20 12 20z"/>',
 'rupee': '<path d="M7 4h10M7 8.5h10M7 20l7.5-7.5a4.2 4.2 0 0 0-3-7H7"/>',
 'chart': '<path d="M4 19V5M4 19h16"/><path d="M8 15l3.5-4.5L15 14l4.5-6"/>',
 'spark': '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9L12 3z"/>',
 'people': '<circle cx="9" cy="8" r="3.2"/><path d="M3.5 19.5c0-3 2.5-5 5.5-5s5.5 2 5.5 5"/><path d="M16 5.4a3.2 3.2 0 0 1 0 5.2M17.5 14.9c2 .6 3.2 2.4 3.2 4.6"/>',
 'clock': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 1.8"/>',
 'mail': '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M4 7l8 5.5L20 7"/>',
 'phone': '<path d="M6.5 3.5h3l1.5 4-2 1.5a11 11 0 0 0 5 5l1.5-2 4 1.5v3a2 2 0 0 1-2.2 2C11 18.7 5.3 13 4.5 5.7A2 2 0 0 1 6.5 3.5z"/>',
}


def ic(name):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round">' + ICON[name] + '</svg>')


def check():
    return ('<svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M4 12.5l5 5L20 6.5"/></svg>')


def arrow():
    return ('<svg class="arw" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M5 12h13M13 6l6 6-6 6"/></svg>')


# --- building blocks ---------------------------------------------------------
def sechead(label, title, lede="", mid=False):
    return ('<div class="sec-h%s rv"><span class="eyebrow">%s</span><h2>%s</h2>%s</div>'
            % (" mid" if mid else "", label, title,
               '<p class="lede">%s</p>' % lede if lede else ""))


def checks(items):
    """items: list of (bold, rest) or plain strings."""
    out = []
    for it in items:
        if isinstance(it, (tuple, list)):
            inner = "<b>%s</b> &mdash; %s" % (it[0], it[1])
        else:
            inner = it
        out.append('<li><span class="ic">%s</span><span>%s</span></li>' % (check(), inner))
    return '<ul class="checks">%s</ul>' % "".join(out)


def crumbs(trail, depth):
    """trail: list of (label, href_or_None). Renders visible crumbs."""
    r = rel(depth)
    bits = ['<a href="%s">Home</a>' % (r or "./")]
    for label, href in trail:
        bits.append('<span>/</span>')
        bits.append('<a href="%s%s">%s</a>' % (r, href, label) if href else label)
    return '<div class="wrap"><div class="crumbs">%s</div></div>' % "".join(bits)


def pcard(p, depth):
    r = rel(depth)
    feats = "".join('<li>%s</li>' % f for f in p["feats"])
    return (
        '<article class="pcard rv" style="--pc:%(accent)s">'
        '<div class="pcard-art">'
        '<span class="badge">%(icon)s%(space)s %(dot)s %(a0)d&ndash;%(a1)d sq.ft.</span>'
        '<a href="%(r)sair-purifiers/%(slug)s/" aria-label="%(name)s">'
        '<img src="%(r)sassets/derived/%(id)s-product.png" alt="%(name)s %(role)s" loading="lazy" width="320" height="480"></a>'
        '</div>'
        '<div class="pcard-body">'
        '<div class="pcard-title"><div>'
        '<a href="%(r)sair-purifiers/%(slug)s/"><h3>%(name)s</h3></a>'
        '<div class="role">%(role)s</div></div>'
        '<div class="pcard-price"><span class="v tnum">%(price)s</span>'
        '<span class="u">Launch price</span></div></div>'
        '<ul class="pcard-feats">%(feats)s</ul>'
        '<div class="pcard-cta">'
        '<a class="btn btn-p btn-sm" href="%(r)sair-purifiers/%(slug)s/">View details%(arw)s</a>'
        '<a class="btn btn-g btn-sm" href="%(r)snotify/">Notify me</a>'
        '</div></div></article>'
        % dict(accent=p["accent"], icon=ic(p["space"]), space=SPACE_LABEL[p["space"]],
               dot=DOT, a0=p["area"][0], a1=p["area"][1], r=r, slug=p["slug"],
               name=p["name"], role=p["role"], id=p["id"],
               price=money(p["price"]), feats=feats, arw=arrow())
    )


def guarantee_block(depth, product=None):
    """The named guarantee. R-10 gets the meter version; others the plain return."""
    r = rel(depth)
    has_meter = product is None or product["id"] == "r10"
    if has_meter:
        body = ("<p class=\"lede\">Shut the room. Run the R-10 for one hour. Watch the AQI "
                "number on the front of the unit.</p>"
                "<p class=\"muted\" style=\"margin-top:14px\">If that number does not fall, you "
                "did not get what we sold you. Send it back any time in the first 30 days "
                "&mdash; full refund, and we pay for the return pickup.</p>")
    else:
        body = ("<p class=\"lede\">Run it for 30 days in the space you bought it for.</p>"
                "<p class=\"muted\" style=\"margin-top:14px\">If you are not convinced it is "
                "doing anything, send it back. Full refund, no questions, and we pay for the "
                "return pickup.</p>")
    return (
        '<div class="card rv" style="border-color:rgba(125,203,41,.35)">'
        '<div class="ico leaf">%s</div>'
        '<span class="eyebrow">Our guarantee</span>'
        '<h3 style="margin:12px 0 14px">The Watch-It-Work Guarantee</h3>'
        '%s'
        '<p class="xs dim" style="margin-top:16px">Most of this category asks you to take '
        '&ldquo;99.95%%&rdquo; on faith. We would rather you tested it in your own room and '
        'kept the receipt.</p>'
        '</div>' % (ic("shield"), body)
    )


def cta_band(depth):
    r = rel(depth)
    return (
        '<section class="sec"><div class="wrap"><div class="cta-band rv">'
        '<span class="tag tag-leaf">Pre-launch</span>'
        '<h2 style="margin-top:16px">Clean air is a birth-right, not a price bracket.</h2>'
        '<p class="lede">All three models are in final production. Join the launch list and '
        'you get three things: pre-orders before anyone else, your launch price locked in, '
        'and the Fake HEPA Checklist today.</p>'
        '<div class="row" style="justify-content:center;margin-top:28px">'
        '<a class="btn btn-leaf btn-lg" href="%snotify/">Join the launch list%s</a>'
        '<a class="btn btn-g btn-lg" href="%sfind-your-fit/" '
        'style="color:#fff;border-color:rgba(255,255,255,.3)">Find my fit</a>'
        '</div></div></div></section>' % (r, arrow(), r)
    )


def faq_block(items, heading="Questions buyers actually ask"):
    rows = []
    for q, a in items:
        rows.append('<div class="card rv"><h3>%s</h3><p class="muted" style="margin-top:10px">%s</p></div>' % (q, a))
    return ('<section class="sec"><div class="wrap">'
            + sechead("FAQ", heading)
            + '<div style="display:grid;gap:14px">%s</div></div></section>' % "".join(rows))


def dl(rows):
    out = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (k, v) for k, v in rows)
    return '<dl class="dl">%s</dl>' % out
