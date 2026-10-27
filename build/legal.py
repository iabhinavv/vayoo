# -*- coding: utf-8 -*-
"""Privacy Policy, Terms & Conditions and Cookie Policy.

Drafted against: Digital Personal Data Protection Act 2023 + DPDP Rules 2025
(G.S.R. 846(E), notified 14 Nov 2025, Rule 3 notice/consent duties commencing
~13 May 2027); Consumer Protection Act 2019 and the Consumer Protection
(E-Commerce) Rules 2020; IT Act 2000 s.43A and the SPDI Rules 2011; the CCPA
Guidelines for Prevention of Misleading Advertisements 2022; and the published
advertiser disclosure duties of Google Ads remarketing and the Meta Pixel.

These are drafts, not legal advice. A qualified Indian lawyer must review them
before they go live behind paid traffic.
"""
from components import (EMAIL, PHONE_HUMAN, PHONE_TEL, money, ic, arrow, sechead,
                        checks, rel, DOT)
from legalconf import LEGAL, val

EFF = LEGAL["effective_date"]


def _h(title, sub=""):
    return ('<div class="sec-h rv"><span class="eyebrow">Legal</span>'
            '<h1 style="margin:14px 0 12px">%s</h1>'
            '<p class="lede">%s</p>'
            '<p class="xs dim" style="margin-top:14px">Effective %s '
            '%s Last updated %s</p></div>' % (title, sub, EFF, DOT, EFF))


def _s(n, title, body):
    return ('<div class="card rv" style="margin-bottom:14px" id="s%s">'
            '<h2 style="font-size:1.25rem">%s. %s</h2>%s</div>' % (n, n, title, body))


def _p(t):
    return '<p class="muted" style="margin-top:12px">%s</p>' % t


def _table(headers, rows):
    th = "".join('<th>%s</th>' % h for h in headers)
    tr = "".join('<tr>%s</tr>' % "".join('<td>%s</td>' % c for c in r) for r in rows)
    return ('<div class="tbl-scroll" style="margin-top:14px"><table class="cmp">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tr))


def _ul(items):
    return ('<ul class="checks" style="margin-top:14px">%s</ul>'
            % "".join('<li><span class="ic"><svg viewBox="0 0 24 24" stroke-linecap="round" '
                      'stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg></span>'
                      '<span>%s</span></li>' % i for i in items))


def identity_block():
    return _table(
        ["Detail", "Value"],
        [["Legal entity", val("entity")],
         ["Corporate Identity Number (CIN)", val("cin")],
         ["GSTIN", val("gstin")],
         ["Registered office", val("regd_address")],
         ["Operating address", val("oper_address")],
         ["Website", "vayoo.store"],
         ["Customer care email", '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)],
         ["Customer care phone", '<a href="tel:%s">%s</a>' % (PHONE_TEL, PHONE_HUMAN)],
         ["Customer care hours", "Monday to Friday, 9:00 to 18:00 IST"]])


def grievance_block():
    return _table(
        ["Detail", "Value"],
        [["Name", val("grievance_name")],
         ["Designation", val("grievance_desig")],
         ["Email", '<a href="mailto:%s">%s</a>' % (LEGAL["grievance_email"], LEGAL["grievance_email"])],
         ["Phone", '<a href="tel:%s">%s</a>' % (PHONE_TEL, PHONE_HUMAN)],
         ["Address", val("regd_address")],
         ["Acknowledgement", "Within 48 hours of receipt"],
         ["Resolution", "Within one month of receipt"]])


# =============================================================================
# PRIVACY POLICY
# =============================================================================
def privacy(d=1):
    r = rel(d)
    body = []

    body.append(_s(1, "Who we are", _p(
        "This policy explains how " + val("entity") + " (&ldquo;Vayoo&rdquo;, &ldquo;we&rdquo;, "
        "&ldquo;us&rdquo;) collects and uses personal data when you visit vayoo.store or deal "
        "with us. In the language of the Digital Personal Data Protection Act, 2023 "
        "(&ldquo;DPDP Act&rdquo;) we are the <b>Data Fiduciary</b> and you are the <b>Data "
        "Principal</b>.") + identity_block() + _p(
        "Questions about this policy or about your data go to "
        '<a href="mailto:' + LEGAL["dpo_email"] + '" style="color:var(--accent-tx)">'
        + LEGAL["dpo_email"] + "</a>, attention " + val("dpo_name") + ".")))

    body.append(_s(2, "The short version", _p(
        "We collect very little. The site sets no advertising or analytics cookie until you "
        "say yes. We do not sell personal data. You can withdraw consent at any time and it is "
        "as easy as giving it &mdash; "
        '<a href="#" data-cookie-settings style="color:var(--accent-tx)">open cookie settings</a>'
        ". Everything below is the detail behind those four sentences.")))

    body.append(_s(3, "What we collect, why, and for how long", _p(
        "Itemised, as DPDP Rule 3 requires. We do not collect anything not listed here.")
        + _table(
            ["Data", "Why we process it", "Basis", "Retained"],
            [["Name, email, phone, city (launch-list form)",
              "To tell you when pre-orders open and to honour your launch-price lock",
              "Your consent", "Until you withdraw, or 1 year after the list closes"],
             ["Name, email, phone, message (contact form or direct email)",
              "To answer your enquiry and keep a record of it",
              "Your consent / legitimate use under DPDP s.7",
              "3 years from last contact"],
             ["Order, delivery address, invoice data (once we sell)",
              "To fulfil the order, invoice it and meet tax and warranty obligations",
              "Performance of contract and legal obligation",
              "8 years, as required by tax and company law"],
             ["Theme preference, consent record",
              "To remember your display choice and prove what you consented to",
              "Strictly necessary", "13 months (consent record), until cleared (theme)"],
             ["Device, browser, approximate location, pages viewed, ad interaction",
              "Analytics and advertising measurement &mdash; <b>only if you consent</b>",
              "Your consent", "Per provider; see the "
              '<a href="' + r + 'cookies/" style="color:var(--accent-tx)">Cookie Policy</a>'],
             ["Server logs (IP address, timestamp, user agent)",
              "Security, abuse prevention and diagnosing faults",
              "Legitimate use", "Held by our host; see their policy"]])
        + _p("We do not knowingly collect health data, financial account data, biometric data, "
             "caste, religion or any other special category of data, and we ask you not to send "
             "it to us.")))

    body.append(_s(4, "Advertising, Google Ads and the Meta Pixel", _p(
        "We intend to advertise Vayoo on Google and on Meta platforms (Facebook and Instagram). "
        "If &mdash; and only if &mdash; you accept advertising cookies, the following run on "
        "this site:")
        + _ul([
            "<b>Google Ads and Google Analytics 4</b>, operated by Google LLC and Google India "
            "Private Limited. These set cookies that let us measure which ads lead to visits, "
            "and let Google show you Vayoo ads on other websites and apps you visit. This is "
            "called <i>remarketing</i>.",
            "<b>Meta Pixel</b>, operated by Meta Platforms, Inc. and Meta Platforms Ireland "
            "Limited. This reports your actions on this site back to Meta so we can measure ad "
            "performance and build audiences, including showing Vayoo ads to you and to people "
            "Meta considers similar to you."])
        + _p("Third-party vendors, Google included, use cookies to serve ads based on your "
             "prior visits to this website. These vendors may combine what they collect here "
             "with data they hold about you from elsewhere. We do not control that processing "
             "and we do not receive your identity from them &mdash; we see aggregate reports.")
        + _p("<b>You can refuse all of it and still use this site in full.</b> Nothing on "
             "vayoo.store is withheld from people who decline advertising cookies.")
        + _p("To opt out independently of us:")
        + _ul(['Google ad personalisation: <a href="https://adssettings.google.com" '
               'target="_blank" rel="noopener" style="color:var(--accent-tx)">'
               'adssettings.google.com</a>',
               'Google Analytics browser add-on: <a href="https://tools.google.com/dlpage/gaoptout" '
               'target="_blank" rel="noopener" style="color:var(--accent-tx)">'
               'tools.google.com/dlpage/gaoptout</a>',
               'Meta ad preferences: <a href="https://www.facebook.com/adpreferences" '
               'target="_blank" rel="noopener" style="color:var(--accent-tx)">'
               'facebook.com/adpreferences</a>',
               'Or simply <a href="#" data-cookie-settings style="color:var(--accent-tx)">'
               'withdraw consent here</a>, which stops the tags loading on this site.'])))

    body.append(_s(5, "Consent, and how to withdraw it", _p(
        "Where we rely on consent, that consent is free, specific, informed, unconditional and "
        "unambiguous, given by a clear affirmative action, as DPDP s.6 requires. We do not use "
        "pre-ticked boxes and we do not treat continued browsing as agreement.")
        + _p("Withdrawing is as easy as giving. Use the cookie settings link in the footer of "
             "every page, or write to " + LEGAL["dpo_email"] + ". Withdrawal does not affect "
             "processing already carried out before you withdrew, and we will stop the relevant "
             "processing within a reasonable period of your request.")))

    body.append(_s(6, "Who we share data with", _p(
        "We never sell personal data. We share it only with processors who need it to do a job "
        "for us, under contract, and only for that job:")
        + _table(["Recipient", "What for", "Where"],
                 [["Google LLC / Google India Pvt Ltd",
                   "Launch-list form (Google Forms), analytics and advertising, if consented",
                   "India, United States and other Google locations"],
                  ["Meta Platforms, Inc. / Meta Platforms Ireland Ltd",
                   "Advertising measurement and audiences, if consented",
                   "United States, Ireland and other Meta locations"],
                  ["GitHub, Inc.", "Website hosting", "United States"],
                  ["Logistics and payment partners",
                   "Delivering orders and taking payment, once we begin selling",
                   "India (named here before the first sale)"],
                  ["Government authorities",
                   "Only where we are legally compelled, and only what is compelled", "India"]])
        + _p("Some of these recipients process data outside India. The DPDP Act permits "
             "transfers except to countries the Central Government restricts by notification; "
             "we will stop any transfer that becomes restricted.")))

    body.append(_s(7, "Your rights", _p(
        "Under the DPDP Act you may:")
        + _ul(["<b>Access</b> a summary of the personal data we hold about you and what we do "
               "with it",
               "<b>Correct, complete, update or erase</b> your personal data",
               "<b>Withdraw consent</b> at any time, as easily as you gave it",
               "<b>Nominate</b> another person to exercise these rights if you die or become "
               "incapacitated",
               "<b>Complain</b> to us, and escalate to the Data Protection Board of India if we "
               "do not resolve it"])
        + _p("Write to " + LEGAL["dpo_email"] + " and we will respond within 30 days. We may ask "
             "you to confirm your identity first, so that we do not hand your data to someone "
             "else. These rights are free to exercise.")
        + _p("You also have duties under DPDP s.15 &mdash; in particular, not to impersonate "
             "anyone else or file a false or frivolous complaint.")))

    body.append(_s(8, "Children and young people", _p(
        "This site is not directed at children. We do not knowingly collect personal data from "
        "anyone under 18 without verifiable parental consent, and under DPDP s.9 we do not carry "
        "out behavioural monitoring, profiling or targeted advertising directed at children "
        "&mdash; the advertising audiences we build exclude under-18s.")
        + _p("If you believe a child has given us personal data, write to " + LEGAL["dpo_email"]
             + " and we will delete it.")))

    body.append(_s(9, "Security", _p(
        "We apply reasonable security safeguards appropriate to the small volume of data we "
        "hold: access limited to the founders and staff who need it, multi-factor authentication "
        "on the accounts that hold personal data, encryption in transit (HTTPS across the whole "
        "site), and reliance on providers who encrypt at rest.")
        + _p("No safeguard is perfect. If a personal data breach occurs we will notify each "
             "affected Data Principal and the Data Protection Board of India in the form and "
             "within the time the DPDP Rules require.")))

    body.append(_s(10, "Grievance redressal", _p(
        "If you are unhappy with how we have handled your personal data, contact our Grievance "
        "Officer. This is also the officer appointed under the Consumer Protection "
        "(E-Commerce) Rules, 2020.") + grievance_block()
        + _p("If we do not resolve your complaint to your satisfaction, you may escalate to the "
             "<b>Data Protection Board of India</b> under the DPDP Act, or to the relevant "
             "consumer forum, including the National Consumer Helpline (1915) and the "
             "e-Daakhil portal.")))

    body.append(_s(11, "Changes", _p(
        "We will post any change on this page and update the date at the top. If a change "
        "materially affects how we use your personal data, we will ask for fresh consent rather "
        "than rely on the old one.")))

    return ('<section class="sec-tight"><div class="wrap" style="max-width:860px">'
            + _h("Privacy Policy",
                 "What we collect, what we do with it, and how to make us stop. Written to the "
                 "Digital Personal Data Protection Act, 2023.")
            + "".join(body) + _disclaimer() + '</div></section>')


def _disclaimer():
    return ('<div class="card rv" style="border-color:rgba(229,72,77,.3);margin-top:20px">'
            '<h2 style="font-size:1.1rem">A note on this document</h2>'
            '<p class="muted small" style="margin-top:10px">This policy was drafted against the '
            'DPDP Act 2023 and the DPDP Rules 2025 (notified 14 November 2025; the notice and '
            'consent duties in Rule 3 commence in May 2027), the Consumer Protection '
            '(E-Commerce) Rules 2020, and the IT Act SPDI Rules 2011. It is not legal advice. '
            'Have a qualified Indian lawyer review it before you point paid traffic at this '
            'site.</p></div>')


# =============================================================================
# TERMS AND CONDITIONS
# =============================================================================
def terms(d=1):
    r = rel(d)
    b = []

    b.append(_s(1, "Who you are contracting with", _p(
        "vayoo.store is operated by " + val("entity") + ". These Terms govern your use of the "
        "site and, once we begin selling, any order you place through it. The details below are "
        "published under Rule 4(2) of the Consumer Protection (E-Commerce) Rules, 2020.")
        + identity_block()))

    b.append(_s(2, "Acceptance", _p(
        "By using this site you accept these Terms and our "
        '<a href="' + r + 'privacy/" style="color:var(--accent-tx)">Privacy Policy</a>. '
        "If you do not accept them, please do not use the site. We may update these Terms; the "
        "version in force is the one published here when you use the site or place an order.")))

    b.append(_s(3, "Eligibility", _p(
        "You must be 18 or older and legally capable of entering a contract under the Indian "
        "Contract Act, 1872. If you are under 18, you may use this site only with the "
        "involvement of a parent or guardian, and you may not place an order.")))

    b.append(_s(4, "Pre-launch status &mdash; important", _p(
        "<b>Vayoo products are not yet on sale.</b> Nothing on this site is an offer capable of "
        "acceptance, no payment is taken here, and joining the launch list does not create an "
        "order or reserve stock. Prices shown are intended launch prices.")
        + _p("Launch-list members keep the launch price shown at the time they joined, for the "
             "first order they place within 30 days of pre-orders opening. That is a commitment "
             "we make voluntarily; it is not a deposit, a contract of sale, or a guarantee that "
             "stock will be available.")))

    b.append(_s(5, "Product information and claims", _p(
        "We describe our products as accurately as we can, and we hold evidence for the "
        "performance claims we make. Specifically:")
        + _ul(["<b>HEPA H13</b> describes the grade of the filter media fitted. The figure "
               "&ldquo;99.95% of particles at 0.3 microns&rdquo; is the H13 classification "
               "threshold, not a measurement of any individual unit in your room.",
               "<b>&ldquo;Up to 99.8% of PM2.5&rdquo;</b> is a maximum under test conditions. "
               "Real-world performance depends on room size, sealing, pollutant load and run "
               "time, and will usually be lower.",
               "<b>Air Quality Index figures</b> shown anywhere on this site are illustrative, "
               "used to explain the CPCB bands. They are not live readings, not measurements of "
               "a Vayoo unit, and not a promise of any result.",
               "<b>Third-party measurements</b> are attributed to their source and are not "
               "presented as our own.",
               "<b>We do not claim</b> that our products remove odours, volatile organic "
               "compounds, carbon monoxide or any gas, that they sterilise a room, that they "
               "prevent, treat or cure any disease, or that they produce any health outcome."])
        + _p("Specifications not yet published &mdash; rated CADR, noise in decibels, power "
             "consumption, dimensions and filter life &mdash; are stated as pending rather than "
             "estimated. We will publish them before the first unit ships.")
        + _p("Country of origin: " + val("country_of_origin") + ". Product images are "
             "representative; colours may vary by screen.")))

    b.append(_s(6, "Pricing, taxes and payment", _p(
        "Prices will be displayed in Indian Rupees as a single total figure with the break-up of "
        "charges, including applicable GST, as the E-Commerce Rules require. Delivery charges, "
        "where they apply, will be shown before you confirm an order. We may change prices at "
        "any time before you place an order, subject to the launch-price commitment in "
        "clause 4.")
        + _p("If a product is listed at a materially wrong price because of an obvious error, we "
             "may cancel the order and refund you in full rather than fulfil it. We will tell "
             "you promptly if that happens.")))

    b.append(_s(7, "Orders, cancellation and delivery", _p(
        "An order is an offer to buy. A contract forms only when we confirm dispatch. We may "
        "decline an order &mdash; for example where stock has run out, the delivery address is "
        "outside our service area, or we suspect fraud &mdash; and we will refund any payment "
        "taken.")
        + _p("You may cancel before dispatch for a full refund. Delivery timelines, charges and "
             "serviceable areas will be published before the first sale and shown at checkout.")))

    b.append(_s(8, "Returns, refunds and the Watch-It-Work Guarantee", _p(
        "<b>The Watch-It-Work Guarantee.</b> Shut the room, run the Vayoo R-10 for one hour and "
        "watch the AQI reading on the unit. If that reading does not fall, return the unit "
        "within 30 days of delivery for a full refund, and we will pay for the return pickup.")
        + _p("The Vayoo C-10 and D-10 carry a 30-day no-questions return on the same terms: full "
             "refund, return pickup paid by us.")
        + _p("Both are subject to the unit being returned in working condition with its original "
             "accessories and packaging, and to the return being arranged within 30 days of "
             "delivery. Refunds are made to the original payment method within 7 working days of "
             "the returned unit reaching us.")
        + _p("These rights are in addition to, and do not limit, your statutory rights under the "
             "Consumer Protection Act, 2019.")))

    b.append(_s(9, "Warranty", _p(
        "Warranty period, coverage, service turnaround and replacement-filter supply are being "
        "finalised alongside production and will be published in full before the first unit "
        "ships. Consumable parts, including filters, and damage from misuse, liquid ingress or "
        "unauthorised repair will not be covered.")))

    b.append(_s(10, "Acceptable use", _p(
        "Do not use this site to break the law, to scrape it at a volume that degrades it for "
        "others, to introduce malicious code, to misrepresent your identity, or to infringe "
        "anyone's rights. We may withdraw access if you do.")))

    b.append(_s(11, "Intellectual property", _p(
        "The Vayoo name, logo, product designs, site design, text, images and code are owned by "
        "us or licensed to us. You may read, link to and share this site. You may not copy it "
        "wholesale, resell it, or use our branding to suggest an association we have not agreed "
        "to.")))

    b.append(_s(12, "Third-party links and services", _p(
        "This site links to third parties and embeds a Google Form. We are not responsible for "
        "their content or their handling of your data, which is governed by their own terms and "
        "privacy policies.")))

    b.append(_s(13, "Liability", _p(
        "Nothing in these Terms excludes or limits liability that cannot lawfully be excluded, "
        "including liability for death or personal injury caused by negligence, for fraud, or "
        "under the Consumer Protection Act, 2019.")
        + _p("Subject to that, we are not liable for indirect or consequential loss, and our "
             "total liability in connection with any product is limited to the amount you paid "
             "for it.")
        + _p("<b>Our products are air purifiers, not medical devices.</b> They are not a "
             "treatment for any condition and are not a substitute for medical advice. If you "
             "have a respiratory or cardiac condition, speak to a doctor.")))

    b.append(_s(14, "Force majeure", _p(
        "We are not liable for delay or failure caused by events beyond our reasonable control, "
        "including natural disaster, epidemic, war, civil unrest, strike, fire, failure of "
        "public infrastructure, or government action.")))

    b.append(_s(15, "Grievance redressal", _p(
        "We have appointed a Grievance Officer under the Consumer Protection (E-Commerce) Rules, "
        "2020. Complaints are acknowledged within 48 hours and resolved within one month.")
        + grievance_block()
        + _p("You may also use the National Consumer Helpline on <b>1915</b>, the INGRAM portal, "
             "or file a complaint on the <b>e-Daakhil</b> portal.")))

    b.append(_s(16, "Governing law and jurisdiction", _p(
        "These Terms are governed by the laws of India. Subject to your statutory right to "
        "approach a consumer forum where you reside or work, the courts at the location of our "
        "registered office, " + val("regd_address") + ", have jurisdiction.")))

    return ('<section class="sec-tight"><div class="wrap" style="max-width:860px">'
            + _h("Terms &amp; Conditions",
                 "The rules for using this site and, once we sell, for buying from us. Written "
                 "to the Consumer Protection Act, 2019 and the E-Commerce Rules, 2020.")
            + "".join(b) + _disclaimer() + '</div></section>')


# =============================================================================
# COOKIE POLICY
# =============================================================================
def cookies(d=1):
    r = rel(d)
    b = []

    b.append(_s(1, "What this covers", _p(
        "Cookies are small files a site stores in your browser. This policy covers cookies and "
        "similar technologies &mdash; pixels, local storage and SDKs &mdash; used on "
        "vayoo.store. It sits alongside our "
        '<a href="' + r + 'privacy/" style="color:var(--accent-tx)">Privacy Policy</a>.')))

    b.append(_s(2, "Nothing non-essential loads until you say so", _p(
        "When you first arrive, analytics and advertising are <b>off</b>. No Google Ads tag and "
        "no Meta Pixel is loaded, and no identifier is set for them, until you make a choice. "
        "This is not a notice telling you cookies are already running &mdash; they are not.")
        + _p("We use Google Consent Mode v2, which is set to deny advertising and analytics "
             "storage by default and only switches to granted if you accept.")
        + '<div class="row" style="margin-top:18px">'
          '<a class="btn btn-p btn-sm" href="#" data-cookie-settings>Open cookie settings'
          + arrow() + '</a></div>'))

    b.append(_s(3, "The categories", _p("There are three, and only the first cannot be turned off.")
        + _table(["Category", "What it does", "Can you refuse?"],
                 [["<b>Strictly necessary</b>",
                   "Remembers your light/dark theme choice and records what you consented to, so "
                   "we can prove it and so we stop asking.",
                   "No &mdash; the site cannot work without it, and it does no tracking"],
                  ["<b>Analytics</b>",
                   "Google Analytics 4. Tells us which pages people read and where they leave, "
                   "in aggregate, with IP anonymisation on.", "Yes"],
                  ["<b>Advertising</b>",
                   "Google Ads and the Meta Pixel. Measures which ads bring people here and "
                   "lets Google and Meta show you Vayoo ads elsewhere.", "Yes"]])))

    b.append(_s(4, "What specifically gets set", _p(
        "If you accept the relevant category:")
        + _table(["Name / tool", "Set by", "Purpose", "Typical duration"],
                 [["<code>vayoo.theme</code>, <code>vayoo.consent.v1</code>",
                   "Vayoo (local storage)", "Theme choice and your consent record",
                   "Until you clear it; consent re-asked after 13 months"],
                  ["<code>_ga</code>, <code>_ga_*</code>", "Google Analytics 4",
                   "Distinguishes visitors and sessions for aggregate reporting", "Up to 2 years"],
                  ["<code>_gcl_*</code>", "Google Ads",
                   "Attributes a visit or conversion to an ad click", "Up to 90 days"],
                  ["<code>IDE</code>, <code>test_cookie</code>",
                   "Google (doubleclick.net)", "Ad delivery, frequency capping and remarketing",
                   "Up to 13 months"],
                  ["<code>_fbp</code>", "Meta Pixel",
                   "Identifies the browser for ad delivery and measurement", "Up to 90 days"],
                  ["<code>fr</code>", "Meta (facebook.com)",
                   "Ad delivery and measurement across Meta platforms", "Up to 90 days"]])
        + _p("Durations are set by the providers and can change. Treat this table as indicative "
             "and the providers' own documentation as authoritative.")))

    b.append(_s(5, "Changing your mind", _p(
        "Withdrawing consent is as easy as giving it, which the DPDP Act requires.")
        + _ul(['<a href="#" data-cookie-settings style="color:var(--accent-tx)">Open cookie '
               'settings</a> from here or from the footer of any page, and switch categories off.',
               "Clear your browser's cookies and site data for vayoo.store, which resets "
               "everything including your consent record.",
               "Use your browser's own controls to block cookies generally &mdash; every major "
               "browser has them under Settings, Privacy.",
               'Opt out directly with the providers: <a href="https://adssettings.google.com" '
               'target="_blank" rel="noopener" style="color:var(--accent-tx)">Google ad '
               'settings</a> and <a href="https://www.facebook.com/adpreferences" '
               'target="_blank" rel="noopener" style="color:var(--accent-tx)">Meta ad '
               'preferences</a>.'])
        + _p("Turning advertising off does not remove any feature of this site.")))

    b.append(_s(6, "Do Not Track and Global Privacy Control", _p(
        "There is no agreed standard for how sites should respond to Do Not Track, so we do not "
        "rely on it. Because nothing non-essential loads without your explicit consent, the "
        "practical outcome for a DNT or GPC user is the same: no advertising or analytics "
        "cookies unless you opt in here.")))

    return ('<section class="sec-tight"><div class="wrap" style="max-width:860px">'
            + _h("Cookie Policy",
                 "Exactly what gets set, by whom, for how long, and how to switch it off.")
            + "".join(b) + _disclaimer() + '</div></section>')


# =============================================================================
# LEGAL HUB (keeps the existing /legal/ URL alive)
# =============================================================================
def legal_hub(d=1):
    r = rel(d)
    cards = "".join(
      '<a class="card hov rv" href="%s%s/"><div class="ico">%s</div>'
      '<h2 style="font-size:1.3rem">%s</h2>'
      '<p class="muted small" style="margin:10px 0 12px">%s</p>'
      '<b style="color:var(--accent-tx)">Read it %s</b></a>'
      % (r, slug, ic(icon), title, desc, "&rarr;")
      for slug, icon, title, desc in [
        ("privacy", "shield", "Privacy Policy",
         "What we collect, why, who we share it with, and your rights under the DPDP Act 2023."),
        ("terms", "chart", "Terms &amp; Conditions",
         "Using the site, buying from us, the guarantee, returns, warranty and governing law."),
        ("cookies", "gauge", "Cookie Policy",
         "Every cookie and pixel, who sets it, how long it lasts, and how to refuse it.")])
    return (
    '<section class="sec-tight"><div class="wrap" style="max-width:860px">'
    + _h("Legal", "Three documents, in plain language. Nothing buried.")
    + '<div style="display:grid;gap:14px">' + cards + '</div>'
    + '<div class="card rv" style="margin-top:22px">'
      '<h2 style="font-size:1.2rem">Grievance Officer</h2>'
      '<p class="muted small" style="margin-top:10px">Appointed under the Consumer Protection '
      '(E-Commerce) Rules, 2020. Complaints acknowledged within 48 hours, resolved within one '
      'month.</p>' + grievance_block() + '</div>'
    + '<div class="card rv" style="margin-top:14px;background:var(--surface-2)">'
      '<h2 style="font-size:1.2rem">Company details</h2>' + identity_block() + '</div>'
    + '<div class="row rv" style="margin-top:20px">'
      '<a class="btn btn-s btn-sm" href="#" data-cookie-settings>Cookie settings' + arrow() + '</a>'
      '<a class="btn btn-g btn-sm" href="' + r + 'contact/">Contact us</a></div>'
    '</div></section>')
