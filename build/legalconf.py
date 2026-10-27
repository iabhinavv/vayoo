# -*- coding: utf-8 -*-
"""Legal identity and ad-tech configuration.

PLACEHOLDER values are deliberately obvious and the build prints a warning for
each one still unfilled. Do not guess at a CIN, GSTIN or registered address --
a legal notice carrying invented statutory identifiers is worse than one that
openly says "to be completed".
"""

PH = "PLACEHOLDER"


def ph(v):
    return isinstance(v, str) and v.startswith(PH)


LEGAL = {
    # --- statutory identity (Consumer Protection (E-Commerce) Rules 2020, r.4(2)) ---
    "entity":        PH + ": registered company name, e.g. Vayoo Technologies Private Limited",
    "cin":           PH + ": Corporate Identity Number from your incorporation certificate",
    "gstin":         PH + ": GSTIN",
    "regd_address":  PH + ": full registered office address with PIN code",
    "oper_address":  PH + ": operating/branch address if different from registered office",

    # --- grievance officer (E-Commerce Rules r.4(5); IT Rules 2021) ---
    "grievance_name":  PH + ": full name of the appointed Grievance Officer",
    "grievance_desig": PH + ": designation, e.g. Grievance Officer",
    "grievance_email": "grievance@vayoo.store",

    # --- DPDP Act 2023 ---
    # Under s.10 only a Significant Data Fiduciary must appoint a DPO. A small
    # D2C brand is very unlikely to be one, so the contact person is named instead.
    "dpo_name":  PH + ": name of the person answering data-protection queries",
    "dpo_email": "privacy@vayoo.store",

    "country_of_origin": PH + ": country of origin of the units as per Legal Metrology rules",
    "effective_date": "27 October 2026",

    # --- ad tech: empty means the tag never loads. Fill in to activate. ---
    "ga4_id":        "",   # e.g. G-XXXXXXXXXX
    "google_ads_id": "",   # e.g. AW-XXXXXXXXX
    "meta_pixel_id": "",   # e.g. 1234567890123456
}


def unfilled():
    return [k for k, v in LEGAL.items() if ph(v)]


def val(key):
    """Render a value, marking placeholders visibly so they cannot ship unnoticed."""
    v = LEGAL[key]
    if ph(v):
        return ('<mark style="background:rgba(229,72,77,.18);color:var(--tx);'
                'padding:2px 7px;border-radius:5px;font-weight:600">[ %s ]</mark>'
                % v.split(": ", 1)[1])
    return v
