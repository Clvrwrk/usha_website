#!/usr/bin/env python3
"""Generates the USHA v1.0 page artboards (desktop 1440 + mobile 390) as .dc.html files.
Home (Main/HomeMobile) and DesignSystem are hand-authored and not touched here.
Run: python3 build.py  -> writes <Page>.dc.html and <Page>Mobile.dc.html next to this file."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Syne:wght@600;700;800&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet">'

CSS = r"""
body { margin: 0; background: #0D1B2A; font-family: Manrope, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 16px; line-height: 1.7; color: #F8F9FA; }
a { color: #00D2FF; text-decoration: none; } a:hover { color: #FFB703; }
.light, .tint, .paper { color: #0D1B2A; }
.light { background: #F8F9FA; } .tint { background: #F1F4F7; } .paper { background: #EEF2F6; } .dark { background: #0D1B2A; color: #F8F9FA; }
.light a, .tint a, .paper a { color: #0089A8; } .light a:hover, .tint a:hover, .paper a:hover { color: #6C1FA0; }
.sec { padding: 89px 56px; } .m .sec { padding: 56px 24px; }
.wrap { max-width: 1216px; margin: 0 auto; display: flex; flex-direction: column; gap: 34px; }
.m .wrap { gap: 24px; }
.eyebrow { font-family: Syne, sans-serif; font-weight: 700; font-size: 13px; letter-spacing: 0.22em; text-transform: uppercase; margin: 0; }
.m .eyebrow { font-size: 12px; }
.dark .eyebrow { color: #00D2FF; } .light .eyebrow, .tint .eyebrow, .paper .eyebrow { color: #6C1FA0; }
.display { font-family: 'Space Grotesk', 'Helvetica Neue', Arial, sans-serif; font-weight: 700; letter-spacing: -0.02em; line-height: 1.08; margin: 0; text-wrap: balance; }
.h-xl { font-size: 66px; } .h-l { font-size: 55px; } .h-1 { font-size: 34px; } .h-2 { font-size: 21px; line-height: 1.25; }
.m .h-xl { font-size: 42px; } .m .h-l { font-size: 34px; } .m .h-1 { font-size: 26px; } .m .h-2 { font-size: 20px; }
.dot { color: #FFB703; } .gold { color: #FFB703; } .cyan { color: #00D2FF; } .purple { color: #6C1FA0; }
p { margin: 0; text-wrap: pretty; }
.lead { font-size: 18px; line-height: 1.65; } .m .lead { font-size: 17px; }
.dark p { color: #B9C6D6; } .light p, .tint p, .paper p { color: #45566B; }
.stack { display: flex; flex-direction: column; gap: 18px; } .stack-s { display: flex; flex-direction: column; gap: 13px; }
.split { display: grid; grid-template-columns: 1.618fr 1fr; gap: 55px; align-items: center; }
.split.flip { grid-template-columns: 1fr 1.618fr; }
.split.even { grid-template-columns: minmax(0,1fr) minmax(0,1fr); }
.m .split, .m .split.flip, .m .split.even { grid-template-columns: 1fr; gap: 24px; }
.g2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 21px; }
.g3 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 21px; }
.g4 { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 21px; }
.g5 { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 13px; }
.m .g2, .m .g3, .m .g4 { grid-template-columns: 1fr; gap: 14px; } .m .g5 { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
.m .g2.keep { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.btns { display: flex; gap: 13px; flex-wrap: wrap; align-items: center; } .m .btns { flex-direction: column; align-items: stretch; gap: 12px; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; min-height: 44px; padding: 12px 26px; border-radius: 999px; border: 0; cursor: pointer; font-family: Syne, sans-serif; font-weight: 700; font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; text-decoration: none; transition: background 200ms cubic-bezier(0.16,1,0.3,1), color 200ms cubic-bezier(0.16,1,0.3,1), border-color 200ms cubic-bezier(0.16,1,0.3,1); box-sizing: border-box; white-space: nowrap; text-align: center; }
.m .btns .btn { width: 100%; white-space: normal; min-height: 48px; }
.btn.btn-primary { background: #FFB703; color: #0D1B2A; } .btn.btn-primary:hover { background: #00D2FF; color: #0D1B2A; }
.btn.btn-tertiary { background: transparent; color: #F8F9FA; border: 2px solid rgba(248,249,250,0.35); padding: 10px 24px; } .btn.btn-tertiary:hover { border-color: #00D2FF; color: #00D2FF; }
.light .btn.btn-tertiary, .tint .btn.btn-tertiary, .paper .btn.btn-tertiary { color: #0D1B2A; border-color: rgba(13,27,42,0.35); } .light .btn.btn-tertiary:hover, .tint .btn.btn-tertiary:hover, .paper .btn.btn-tertiary:hover { border-color: #6C1FA0; color: #6C1FA0; }
.chip { display: inline-flex; align-items: center; align-self: flex-start; background: #6C1FA0; color: #F8F9FA; font-family: Syne, sans-serif; font-weight: 700; font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; padding: 7px 14px; border-radius: 999px; white-space: nowrap; }
.chip.gold { background: #FFB703; color: #0D1B2A; }
.m .chip { white-space: normal; text-align: left; line-height: 1.4; }
.card { border-radius: 12px; padding: 28px 26px; display: flex; flex-direction: column; gap: 12px; box-sizing: border-box; transition: transform 200ms cubic-bezier(0.16,1,0.3,1), box-shadow 200ms cubic-bezier(0.16,1,0.3,1); }
.m .card { padding: 24px 22px; gap: 10px; }
.card:hover { transform: translateY(-8px); box-shadow: 0 18px 40px rgba(13,27,42,0.18); }
.dark .card { background: rgba(248,249,250,0.04); border: 1px solid rgba(0,210,255,0.35); }
.light .card, .tint .card, .paper .card { background: #FFFFFF; border: 1px solid rgba(108,31,160,0.35); }
.card.tint-cyan { border-color: rgba(0,168,204,0.45); } .card.tint-gold { border-color: rgba(255,183,3,0.5); }
.card h3 { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; line-height: 1.25; margin: 0; letter-spacing: -0.01em; }
.m .card h3 { font-size: 20px; }
.card p { font-size: 15px; line-height: 1.6; }
.card .open { font-family: Syne, sans-serif; font-weight: 700; font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; }
.stat .num { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 55px; line-height: 1; letter-spacing: -0.02em; }
.m .stat .num { font-size: 40px; }
.stat .label { font-family: Syne, sans-serif; font-weight: 600; font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase; margin-top: 10px; line-height: 1.5; }
.m .stat .label { font-size: 11px; }
.row1 .num, .row1 .label { color: #F8F9FA; } .row1 .plus { color: #FFB703; }
.row2 .num, .row2 .label { color: #FFB703; } .row2 .plus { color: #F8F9FA; }
.ice .num, .ice .label { color: #F8F9FA; } .ice .plus, .ice .dot { color: #FFB703; }
.light .stat .num, .tint .stat .num { color: #0D1B2A; } .light .stat .label, .tint .stat .label { color: #6B7A8D; }
.tier h4 { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; margin: 0 0 13px; } .m .tier h4 { font-size: 18px; margin-bottom: 10px; }
.logo-cell { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; min-height: 72px; padding: 13px 16px; border: 1px solid #DDE4EA; border-radius: 10px; background: #FFFFFF; font-family: Syne, sans-serif; font-weight: 600; font-size: 12px; letter-spacing: 0.06em; text-transform: uppercase; color: #45566B; box-sizing: border-box; }
.m .logo-cell { min-height: 60px; padding: 10px 12px; font-size: 11px; }
.logo-cell .founding { display: block; font-size: 9px; letter-spacing: 0.2em; color: #E09E00; margin-top: 4px; }
.quote { border-left: 3px solid #FFB703; padding: 8px 0 8px 21px; margin: 0; display: flex; flex-direction: column; gap: 10px; }
.quote p { font-size: 19px; line-height: 1.5; font-weight: 600; color: #0D1B2A; } .m .quote p { font-size: 17px; }
.dark .quote p { color: #F8F9FA; }
.quote cite { font-style: normal; font-family: Syne, sans-serif; font-weight: 600; font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: #6B7A8D; }
.dark .quote cite { color: #B9C6D6; }
.nav { display: flex; align-items: center; gap: 34px; min-height: 72px; padding: 0 56px; background: rgba(13,27,42,0.9); border-bottom: 1px solid rgba(0,210,255,0.12); }
.m .nav { min-height: 64px; padding: 0 20px; justify-content: space-between; gap: 12px; }
.brand { display: flex; align-items: center; gap: 12px; } .brand img { width: 34px; height: auto; display: block; } .m .brand img { width: 28px; }
.brand .wm { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 22px; letter-spacing: -0.02em; color: #F8F9FA; } .m .brand .wm { font-size: 19px; }
.nav-links { display: flex; align-items: center; gap: 24px; margin-left: auto; }
.nav-link { font-family: Syne, sans-serif; font-weight: 600; font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: #F8F9FA; padding: 8px 2px; border-bottom: 2px solid transparent; }
.nav-link:hover { color: #00D2FF; } .nav-link.on { color: #FFB703; border-bottom-color: #FFB703; }
.burger { width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(0,210,255,0.3); border-radius: 10px; }
.footer a { color: #B9C6D6; font-size: 14px; } .footer a:hover { color: #00D2FF; } .m .footer a { font-size: 15px; padding: 6px 0; }
.footer h5 { font-family: Syne, sans-serif; font-weight: 700; font-size: 12px; letter-spacing: 0.22em; text-transform: uppercase; color: #00D2FF; margin: 0 0 13px; } .m .footer h5 { font-size: 11px; margin-bottom: 8px; }
.fgrid { display: grid; grid-template-columns: 1.618fr 1fr 1fr 1fr; gap: 55px; align-items: start; }
.m .fgrid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px 16px; }
.m .fgrid > div:first-child, .m .fgrid > div.wide { grid-column: span 2; }
.fcol { display: flex; flex-direction: column; gap: 8px; } .m .fcol { gap: 0; }
.copy { border-top: 2px solid #FFB703; padding-top: 21px; text-align: center; font-family: Syne, sans-serif; font-weight: 600; font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: #6B7A8D; line-height: 1.6; }
.field { width: 100%; box-sizing: border-box; min-height: 48px; padding: 12px 16px; border-radius: 10px; border: 1px solid #DDE4EA; background: #FFFFFF; font-family: Manrope, sans-serif; font-size: 15px; color: #6B7A8D; display: flex; align-items: center; }
.field.ta { min-height: 130px; align-items: flex-start; }
.flabel { font-family: Syne, sans-serif; font-weight: 700; font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; margin: 0 0 6px; color: #0D1B2A; }
.dark .flabel { color: #00D2FF; }
.dark .field { background: rgba(248,249,250,0.05); border-color: rgba(248,249,250,0.25); color: rgba(248,249,250,0.5); }
.fgroup { display: flex; flex-direction: column; }
.list-row { display: grid; grid-template-columns: 150px 1fr auto; gap: 21px; align-items: baseline; padding: 21px 0; border-bottom: 1px solid #DDE4EA; }
.m .list-row { grid-template-columns: 1fr; gap: 6px; padding: 16px 0; }
.list-row .date { font-family: Syne, sans-serif; font-weight: 600; font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; color: #6B7A8D; }
.list-row h3 { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; margin: 0 0 4px; letter-spacing: -0.01em; line-height: 1.25; } .m .list-row h3 { font-size: 19px; }
.list-row p { font-size: 15px; }
.tags { display: flex; flex-wrap: wrap; gap: 8px; }
.tag { font-family: Syne, sans-serif; font-weight: 600; font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; border: 1px solid #DDE4EA; border-radius: 999px; padding: 7px 14px; color: #45566B; background: #FFFFFF; }
.tag.on { background: #0D1B2A; color: #F8F9FA; border-color: #0D1B2A; }
.info { display: flex; flex-direction: column; gap: 6px; padding: 21px 24px; border-radius: 12px; background: #FFFFFF; border: 1px solid #DDE4EA; }
.info .k { font-family: Syne, sans-serif; font-weight: 700; font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: #6C1FA0; }
.info .v { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 18px; color: #0D1B2A; line-height: 1.3; }
.person { display: flex; flex-direction: column; gap: 10px; padding: 24px; border-radius: 12px; background: #FFFFFF; border: 1px solid #DDE4EA; }
.avatar { width: 72px; height: 72px; border-radius: 50%; background: #0D1B2A; color: #FFB703; display: flex; align-items: center; justify-content: center; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 22px; letter-spacing: -0.02em; }
.avatar.cyan { background: #0089A8; color: #F8F9FA; } .avatar.purple { background: #6C1FA0; color: #F8F9FA; }
.person .name { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 19px; color: #0D1B2A; line-height: 1.25; }
.person .role { font-family: Syne, sans-serif; font-weight: 600; font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: #6C1FA0; }
.person p { font-size: 14px; }
.icon { width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1.5px solid rgba(108,31,160,0.45); background: rgba(108,31,160,0.06); flex: none; }
.dark .icon { border-color: rgba(0,210,255,0.45); background: rgba(0,210,255,0.06); }
.pillar { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 12px; padding: 21px 13px; border-left: 1px solid #DDE4EA; }
.pillar:first-child { border-left: 0; }
.m .pillar { border-left: 0; border-top: 1px solid #DDE4EA; padding: 21px 0; } .m .pillar:first-child { border-top: 0; }
.dark .pillar { border-left-color: rgba(248,249,250,0.14); } .m .dark .pillar, .dark.m .pillar { border-top-color: rgba(248,249,250,0.14); }
.pillar .t { font-family: Syne, sans-serif; font-weight: 800; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; }
.pillar p { font-size: 15px; line-height: 1.7; }
.hb-photo { border-radius: 12px; overflow: hidden; background: linear-gradient(160deg, #1B2A44, #0D1B2A 55%, #3B0B59); position: relative; min-height: 420px; display: flex; align-items: flex-end; }
.hb-photo img { width: 100%; height: auto; display: block; }
.diagram { position: relative; width: 560px; height: 560px; margin: 0 auto; } .m .diagram { width: 342px; height: 342px; }
.node { position: absolute; width: 96px; height: 96px; margin: -48px 0 0 -48px; border-radius: 50%; background: #FFFFFF; border: 1.5px solid rgba(108,31,160,0.45); display: flex; align-items: center; justify-content: center; text-align: center; font-family: Syne, sans-serif; font-weight: 700; font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase; color: #0D1B2A; padding: 8px; box-sizing: border-box; line-height: 1.3; }
.m .node { width: 74px; height: 74px; margin: -37px 0 0 -37px; font-size: 8px; letter-spacing: 0.08em; }
.node.core { width: 150px; height: 150px; margin: -75px 0 0 -75px; background: #0D1B2A; color: #FFB703; font-size: 14px; border: 0; box-shadow: 0 0 0 10px rgba(255,183,3,0.12); }
.m .node.core { width: 100px; height: 100px; margin: -50px 0 0 -50px; font-size: 11px; }
.marquee { background: #FFB703; color: #0D1B2A; overflow: hidden; white-space: nowrap; padding: 11px 0; }
.marquee-track { display: inline-block; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 14px; letter-spacing: 0.2em; animation: marquee 32s linear infinite; }
@keyframes marquee { from { transform: translateX(0); } to { transform: translateX(-50%); } }
@media (prefers-reduced-motion: reduce) { .marquee-track { animation: none !important; } .card, .btn { transition: none; } }
"""

NAV_ITEMS = [("About Us", "about"), ("Membership", "membership"), ("Policymakers", "policymakers"), ("Industry", "industry"), ("Events", "events"), ("Media Room", "media"), ("Resources", "resources")]

def nav(active, m):
    brand = '<div class="brand"><img src="usha-h-full-dark.svg" alt="USHA dotted-H monogram, full color on navy"><div class="wm">USHA</div></div>'
    if m:
        return f'''<div class="dark nav">{brand}<div style="display: flex; align-items: center; gap: 10px"><a class="btn btn-primary" href="#join" style="min-height: 40px; padding: 8px 16px; font-size: 12px">Join</a><div class="burger" aria-label="Open menu"><svg width="20" height="14" viewBox="0 0 20 14" fill="none" stroke="#00D2FF" stroke-width="2" stroke-linecap="round"><path d="M1 1h18M1 7h18M1 13h18"></path></svg></div></div></div>'''
    links = "".join(f'<a class="nav-link{" on" if key == active else ""}" href="#{key}">{label}</a>' for label, key in NAV_ITEMS)
    return f'<div class="dark nav">{brand}<div class="nav-links">{links}<a class="btn btn-primary" href="#join" style="margin-left: 8px; min-height: 40px; padding: 10px 22px">Join</a></div></div>'

def sec(surface, inner, extra_style=""):
    return f'<div class="{surface} sec" style="{extra_style}"><div class="wrap">{inner}</div></div>'

def head(eyebrow, title, size="h-l", extra=""):
    return f'<div class="stack-s"><p class="eyebrow">{eyebrow}</p><h2 class="display {size}">{title}</h2>{extra}</div>'

def card(chip, title, body, cls="", open_link=None):
    o = f'<span class="open">{open_link} &#9656;</span>' if open_link else ""
    c = f'<span class="chip">{chip}</span>' if chip else ""
    return f'<div class="card {cls}">{c}<h3>{title}</h3><p>{body}</p>{o}</div>'

WHY_JOIN = [
    ("Strategy", "Navigate what&rsquo;s next", "One-on-one strategy focused on the policy, market, and business priorities affecting your company."),
    ("Visibility", "Be seen by the right people", "Position your company and expertise before policymakers, industry leaders, and potential partners."),
    ("Intelligence", "See what&rsquo;s coming", "Biweekly policy reports on federal and state hydrogen and fuel cell policy."),
    ("Policy engagement", "Help shape the framework", "Bring your expertise into the policies and regulations affecting hydrogen deployment."),
    ("Business development", "Get closer to opportunity", "Tailored introductions to customers, partners, economic developers, and emerging markets."),
    ("Exclusive access", "Get in the room", "Member-only access to working groups, strategy sessions, political and investment roundtables, and USHA convenings."),
]

def join_section():
    cards = "".join(card(c, t, b) for c, t, b in WHY_JOIN)
    return sec("dark", head("Propel your business", 'Join the United States Hydrogen Alliance<span class="dot">.</span>') + f'<div class="g3">{cards}</div><div class="btns"><a class="btn btn-primary" href="#membership">Explore membership</a></div>', "")

def join_membership_variant():
    return sec("dark", f'''<div class="split">
      <div class="stack"><p class="eyebrow">People. Policy. Markets.</p><h2 class="display h-l">Your seat is at the table<span class="dot">.</span></h2>
      <p class="lead">The hydrogen economy is being shaped now, through decisions being made in statehouses, boardrooms, communities, and markets across the country. USHA membership puts your company inside that conversation, alongside the people building what comes next.</p>
      <div class="btns"><a class="btn btn-primary" href="#apply">Submit an application</a><a class="btn btn-tertiary" href="#brochure">2026 membership brochure &#9656;</a></div></div>
      <img src="usha-map-full-dark.svg" alt="USHA dotted map, full color on navy" style="width: 100%; height: auto; display: block">
    </div>''')

def newsletter():
    return sec("tint", '''<div class="split"><div class="stack-s"><p class="eyebrow">Newsletter</p><h2 class="display h-l">Stay ahead<span class="dot">.</span></h2><p class="lead">From policy shifts to market opportunities, stay ahead of what&rsquo;s moving hydrogen forward.</p></div>
      <div class="btns" style="flex-wrap: nowrap"><div class="field" style="flex: 1 1 auto">Work email</div><a class="btn btn-primary" href="#newsletter">Subscribe</a></div></div>''', "padding-top: 76px; padding-bottom: 76px")

def footer(m):
    return f'''<div class="dark footer sec" style="padding-top: 76px; padding-bottom: 34px"><div class="wrap" style="gap: 55px">
      <div class="fgrid">
        <div class="stack" style="{'align-items: center; text-align: center;' if m else ''}">
          <div class="brand" style="gap: 14px"><img src="usha-h-full-dark.svg" alt="USHA dotted-H monogram, full color on navy" style="width: 44px"><div class="wm" style="font-size: 28px">USHA</div></div>
          <p style="color: #B9C6D6; font-size: {'14px' if m else '16px'}; white-space: nowrap">Fifty states. One hydrogen economy. Built together.</p>
        </div>
        <div><h5>Alliance</h5><div class="fcol"><a href="#about">About Us</a><a href="#membership">Membership</a><a href="#contact">Contact</a></div></div>
        <div><h5>Work</h5><div class="fcol"><a href="#policymakers">Policymakers</a><a href="#industry">Industry</a><a href="#hydrogen-built">Hydrogen Built</a><a href="#events">Events</a></div></div>
        <div class="wide"><h5>Newsroom</h5><div class="fcol"><a href="#media">Media Room</a><a href="#resources">Resources</a><a href="#linkedin-usha">LinkedIn &middot; USHA</a><a href="#linkedin-convention">LinkedIn &middot; Convention</a><a href="#x">X / Twitter</a></div></div>
      </div>
      <div class="copy">&copy; 2026 United States Hydrogen Alliance &middot; 501(c)(6)</div>
    </div></div>'''

def hero(eyebrow, title, body, buttons="", right=None, extra="", surface="dark"):
    b = f'<div class="btns" style="margin-top: 8px">{buttons}</div>' if buttons else ""
    left = f'<div class="stack"><p class="eyebrow">{eyebrow}</p><h1 class="display h-xl">{title}</h1>{body}{extra}{b}</div>'
    if right is None:
        return sec(surface, left, "padding-top: 89px; padding-bottom: 89px")
    return sec(surface, f'<div class="split">{left}<div>{right}</div></div>', "padding-top: 89px; padding-bottom: 76px")

MAP_DARK = '<img src="usha-map-full-dark.svg" alt="USHA dotted map, full color on navy" style="width: 100%; height: auto; display: block; filter: drop-shadow(0 0 26px rgba(0,210,255,0.22))">'
MAP_LIGHT = '<img src="usha-map-full-light.svg" alt="USHA dotted map, full color on ice" style="width: 100%; height: auto; display: block">'
SEAL_DARK = '<img src="usha-seal-fullcolor-dark.svg" alt="USHA seal, full color on navy" style="width: 100%; max-width: 380px; height: auto; display: block; margin: 0 auto">'

TESTIMONIALS = [
    ("Without USHA, recent Utah legislation promoting hydrogen production through tax credits would not have been successful or even possible.", "Melissa Garff Ballard &middot; Utah State Representative"),
    ("An active legislative impact machine.", "Jeff Holyoak &middot; TOMCO2 Systems"),
    ("There is no price tag on what USHA has done for us.", "Carolina Ahlstrand &middot; Hycamite"),
    ("ROI within six months, and a tax incentive education we needed.", "Greg Heller &middot; HNO International"),
    ("Introductions to the stakeholders that mattered.", "Aaron Villarreal &middot; Taylor-Wharton"),
    ("Hundreds of contacts gained through membership.", "George Drake &middot; HSB"),
    ("Real policy impact.", "Tim Sasseen &middot; Ballard Power Systems"),
]

def quotes(items, dark=False):
    return "".join(f'<blockquote class="quote"><p>&ldquo;{q}&rdquo;</p><cite>{c}</cite></blockquote>' for q, c in items)

TIERS = [
    ("H2 Champions", "#E09E00", ["Air Water|Founding member", "Honda", "Nikkiso", "Pacific Clean Fuels", "Pap&eacute;", "Taylor-Wharton|Founding member", "TOMCO2 Systems|Founding member", "Total Hydrogen Solutions"]),
    ("H2 Patrons", "#6C1FA0", ["Avalon"]),
    ("H2 Proponents", "#0089A8", ["Independence Hydrogen", "Jensen Hughes", "Southwest Gas", "TLM One", "Suburban Propane", "University of Delaware", "University of Maryland", "University of Wyoming", "Virginia Tech Corporate Research Center", "Zero Emission Advisors"]),
    ("Our Allies", "#6B7A8D", ["ASU Carbon Neutral Economy", "Canadian Hydrogen Association", "H2 Mexico", "Nuclear Hydrogen Initiative"]),
]

def tiers():
    out = []
    for name, color, members in TIERS:
        cells = []
        for mbr in members:
            n, _, f = mbr.partition("|")
            cells.append(f'<div class="logo-cell">{n}{f"<span class=\"founding\">{f}</span>" if f else ""}</div>')
        out.append(f'<div class="tier"><h4 style="color: {color}">{name}</h4><div class="g5">{"".join(cells)}</div></div>')
    out.append('<p style="font-family: Syne, sans-serif; font-weight: 600; font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: #6B7A8D">Member logo artwork pending &middot; names shown as placeholders</p>')
    return "".join(out)

ICON_PATHS = {
    "people": '<path d="M8 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm8 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM2 20c0-3 3-5 6-5s6 2 6 5M12 20c0-3 3-5 6-5s4 1 4 4"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/>',
    "leaf": '<path d="M5 20c0-8 5-14 15-15-1 10-7 15-15 15Z"/><path d="M5 20c3-4 6-7 10-9"/>',
    "pin": '<path d="M12 22s7-6 7-12a7 7 0 1 0-14 0c0 6 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/>',
    "mega": '<path d="M3 10v4h3l7 4V6l-7 4H3Z"/><path d="M17 9a4 4 0 0 1 0 6"/>',
    "star": '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9L12 3Z"/>',
    "book": '<path d="M4 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4V4Z"/><path d="M20 4h-7a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h8V4Z"/>',
    "handshake": '<path d="m2 9 4-3 5 1 3 3-3 3-3-2"/><path d="m22 9-4-3-4 1"/><path d="m8 15 2 2 2-2 2 2 2-2 2 2 4-4"/>',
    "capitol": '<path d="M3 21h18M5 21V11h14v10M12 3l6 5H6l6-5ZM9 21v-6M15 21v-6M12 21v-6"/>',
    "check": '<path d="m5 12 4 4L19 6"/>',
    "map": '<path d="m3 6 6-2 6 2 6-2v14l-6 2-6-2-6 2V6Z"/><path d="M9 4v14M15 6v14"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-4 3-6 7-6s7 2 7 6"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c3 0 5 2 5 5"/>',
    "dollar": '<path d="M12 2v20M17 6.5c0-1.5-2-2.5-5-2.5S7 5 7 7s2 3 5 3 5 1 5 3-2 3-5 3-5-1-5-2.5"/>',
    "factory": '<path d="M3 21V9l5 3V9l5 3V9l5 3v9H3Z"/><path d="M8 21v-4h3v4M14 21v-4h3v4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "gavel": '<path d="m14 4 6 6M9 9l6 6M4 20l7-7M13 5l6 6-3 3-6-6 3-3Z"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 12h18"/>',
}

def icon(name, color="#6C1FA0", size=22):
    return f'<div class="icon"><svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICON_PATHS[name]}</svg></div>'

def icon_item(name, title, body, color="#6C1FA0"):
    return f'<div style="display: flex; gap: 16px; align-items: flex-start">{icon(name, color)}<div class="stack-s" style="gap: 4px"><div style="font-family: Syne, sans-serif; font-weight: 800; font-size: 13px; letter-spacing: 0.16em; text-transform: uppercase; color: {color}">{title}</div><p style="font-size: 15px">{body}</p></div></div>'

# ---------------------------------------------------------------- pages

def page_about(m):
    mission = sec("light", f'''<div class="split">
      <div class="stack"><p class="eyebrow">Our mission</p><h2 class="display h-l">Build the conditions for hydrogen to grow<span class="dot">.</span></h2>
      <p class="lead">The United States Hydrogen Alliance is a national 501(c)(6) business association working across all 50 states to shape policy, develop markets, and connect the stakeholders needed to build durable hydrogen economies.</p>
      <p>We work at the intersection of policy, markets, and people, bringing companies, policymakers, investors, and communities together around the practical conditions hydrogen needs to succeed: functional markets, sound policy, infrastructure, investment, a skilled workforce, and a shared vision that can scale with America&rsquo;s growing demand for energy, security, and economic strength.</p></div>
      <div class="stack"><p class="eyebrow">Our philosophy</p><h3 class="display h-1">The future is built together<span class="dot">.</span></h3>
      <p>The next hydrogen economy will take more than technology. It requires markets, sound policy, infrastructure, investment, a skilled workforce, strong communities, and a shared vision capable of scaling alongside America&rsquo;s growing need for energy, security, and economic prosperity.</p>
      <p>No company builds an economy alone. That&rsquo;s where USHA comes in. We connect producers, technology companies, end users, policymakers, investors, economic developers, workforce leaders, and communities, each with distinct priorities, capabilities, and interests, and bring them into alignment around a shared opportunity.</p>
      <p>By connecting these pieces, we help create an ecosystem in which policy enables investment, investment enables infrastructure, infrastructure unlocks markets, and growing markets create opportunity for the entire hydrogen value chain. That is how individual opportunity becomes a functioning hydrogen economy, and how we build one that lasts.</p></div>
    </div>''')
    approach = sec("tint", head("Our approach &amp; strategy", 'How we build<span class="dot">.</span>') + '<div class="g4">' +
        card("Gauge and anticipate", "See what&rsquo;s coming", "We track industry, market, and political shifts before they become barriers or opportunities, giving members the foresight to move early.") +
        card("Design the framework", "Design the right structure", "We work across the ecosystem to design policy and market frameworks that create the conditions for investment, deployment, and lasting hydrogen growth.", "tint-cyan") +
        card("Connect to build", "Bring the right people together", "We bring industry, policymakers, investors, communities, and market partners together around practical solutions, turning well-founded ideas into coordinated action.", "tint-gold") +
        card("Deliver", "Turn action into outcomes", "We move frameworks from strategy to execution, advancing policy, strengthening markets, and building the foundation for hydrogen economies that last.") + '</div>')
    leader = f'''<div class="person" style="flex-direction: {'column' if m else 'row'}; gap: 24px; align-items: flex-start"><div class="avatar" style="width: 96px; height: 96px; font-size: 30px; flex: none">RB</div>
      <div class="stack-s" style="gap: 8px"><div class="name" style="font-size: 26px">Roxana Bekemohammadi</div><div class="role">Founder and Executive Director</div>
      <p>Distinguished leader in the hydrogen and fuel cell industry, known for her unique experience in policy advocacy, public service, and technology commercialization.</p>
      <p style="font-size: 13px; color: #6B7A8D">[Photo and full bio from ushydrogenalliance.org/our-team]</p></div></div>'''
    team = sec("paper", head("Our leadership", 'The people at the table<span class="dot">.</span>', extra='<p class="lead" style="max-width: 62ch">Our team is composed of technical, policy, and communications experts working state by state on behalf of the membership.</p>') + leader +
        '<p style="font-family: Syne, sans-serif; font-weight: 600; font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: #6B7A8D">[Additional staff and fellows: names, titles, and photos to be supplied]</p>')
    board_people = [("AV", "Aaron Villarreal", "President", "Taylor-Wharton America &middot; Director of Sales and Global Hydrogen", ""),
        ("GO", "Gabriel Olson", "Vice President", "Pacific Clean Fuels, Inc. / Pap&eacute; Group &middot; Director, Alternative Energy and Infrastructure", "cyan"),
        ("BH", "Bobby Hunt", "Secretary", "Total Hydrogen Solutions &middot; General Manager", "purple"),
        ("TS", "Tim Sasseen", "Policy Officer", "American Honda Motor Company &middot; Manager, Hydrogen Business", ""),
        ("CP", "Cody Patrick", "Membership Recruitment", "Nikkiso &middot; Hydrogen Segment Manager", "cyan"),
        ("RM", "RJ McIntosh", "Member At-Large", "Mantle IQ &middot; Founder and CEO", "purple")]
    board_cards = "".join(f'<div class="person"><div class="avatar {c}">{i}</div><div class="name">{n}</div><div class="role">{r}</div><p>{o}</p></div>' for i, n, r, o, c in board_people)
    board = sec("paper", head("Our Board of Directors", 'Governed by the members who build<span class="dot">.</span>') + f'<div class="g3">{board_cards}</div>' +
        '<p style="font-family: Syne, sans-serif; font-weight: 600; font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: #6B7A8D">[Board photos from ushydrogenalliance.org/board-of-directors]</p>', "padding-top: 0")
    numbers = sec("dark", f'''<div class="split">
      <div class="stack"><p class="eyebrow">Our accomplishments &amp; testimonies</p><h2 class="display h-l">By the numbers<span class="dot">.</span></h2>
      <p class="lead">Hydrogen policy is being written now, and USHA is in the room where it happens. Our track record is measured in bills tracked, laws enacted, and policymakers brought into the work.</p>
      <div class="btns"><a class="btn btn-primary" href="#record">See the record</a></div></div>
      <div class="g2 keep" style="gap: 34px 21px">
        <div class="stat ice"><div class="num">1,000<span class="plus">+</span></div><div class="label">State bills tracked and analyzed</div></div>
        <div class="stat ice"><div class="num">20</div><div class="label">Bills enacted into law</div></div>
        <div class="stat ice"><div class="num">500<span class="plus">+</span></div><div class="label">Policymakers educated and engaged</div></div>
        <div class="stat ice"><div class="num">300<span class="plus">+</span></div><div class="label">Legislative and regulatory engagements</div></div>
      </div></div>''')
    record = sec("tint", head("The record speaks", 'What USHA membership has delivered<span class="dot">.</span>') + f'<div class="g2">{quotes(TESTIMONIALS)}</div>')
    initiatives = sec("light", f'''<div class="split">
      <div class="stack"><p class="eyebrow">Initiatives</p><h2 class="display h-l">Building the U.S. hydrogen economy framework<span class="dot">.</span></h2>
      <p class="lead">One state can prove an idea. Fifty states can build an economy.</p>
      <p>We develop, advance, and connect hydrogen policy across America to build a uniform, robust, and prosperous U.S. hydrogen economy.</p>
      <div class="btns"><a class="btn btn-primary" href="#hydrogen-built">Hydrogen Built</a></div></div>
      {MAP_LIGHT}</div>''')
    return [hero("About us", 'One molecule<span class="dot">.</span> Every state<span class="dot">.</span>',
        '<p class="lead">We bring together the people, policy, and markets needed to build a durable hydrogen economy across all 50 states.</p>',
        '<a class="btn btn-primary" href="#membership">Become a member</a><a class="btn btn-tertiary" href="#mission">Our mission &#9656;</a>', SEAL_DARK),
        mission, approach, team, board, numbers, record, initiatives, join_section(), newsletter()]

def page_membership(m):
    advantage = sec("light", f'''<div class="split">
      <div class="stack"><p class="eyebrow">The USHA advantage</p><h2 class="display h-l">One membership. Fifty states<span class="dot">.</span></h2>
      <p class="lead">Hydrogen markets don&rsquo;t develop in a single place. They&rsquo;re shaped by policy decisions in statehouses, investment decisions in boardrooms, and infrastructure and demand decisions across regions, industries, and communities.</p>
      <p>USHA works across all of it, giving members a national platform for engagement while building the local relationships, policy frameworks, and market conditions that determine where and how hydrogen grows. Membership connects your company to the people, information, and opportunities shaping the U.S. hydrogen economy, and puts your business in position to help build it.</p></div>
      <div class="g2" style="grid-template-columns: 1fr; gap: 14px">
        {card("50 states", "State-by-state presence", "Policy and market presence in every statehouse and region where hydrogen is being built.")}
        {card("One network", "Everyone at one table", "Industry, policymakers, economic developers, end users, investors, and communities.", "tint-cyan")}
        {card("Your business", "Built around your priorities", "Intelligence, introductions, and strategy aligned with your company&rsquo;s priorities.", "tint-gold")}
      </div></div>''')
    why = sec("tint", head("Why join", 'An advantage built around your business<span class="dot">.</span>') + '<div class="g3">' + "".join(card(c, t, b) for c, t, b in WHY_JOIN) + '</div>')
    record = sec("light", head("The record speaks", 'Don&rsquo;t take our word for it. Hear what USHA membership has delivered<span class="dot">.</span>') + f'<div class="g3">{quotes(TESTIMONIALS[1:])}</div>')
    members = sec("tint", head("The members", 'Build the hydrogen economy with us<span class="dot">.</span>', extra='''<p class="lead" style="max-width: 70ch">No company builds an economy alone. USHA brings together companies from across the hydrogen value chain and connects them with policymakers, markets, and communities.</p><p style="max-width: 70ch">Different technologies. Different business models. Different priorities. One ecosystem with more opportunity when its parts move together.</p>''') + tiers())
    who_items = [("Producers &amp; developers", "Companies producing hydrogen or developing production, storage, and distribution projects."),
        ("Technology &amp; equipment", "Electrolyzers, fuel cells, compression, storage, and the systems that put hydrogen to work."),
        ("End users &amp; offtakers", "Industrial, mobility, and power customers building demand for hydrogen."),
        ("Infrastructure &amp; energy", "Utilities, pipelines, ports, and the energy companies moving molecules to market."),
        ("Investors &amp; economic developers", "Capital, regions, and agencies turning hydrogen opportunity into projects and jobs."),
        ("Research &amp; professional services", "Universities, engineering, legal, and advisory firms supporting the value chain.")]
    who = sec("light", head("Who membership is for", 'If you&rsquo;re building hydrogen, you belong in the conversation<span class="dot">.</span>') + '<div class="g3">' + "".join(card(t, "", b).replace("<h3></h3>", "") for t, b in who_items) + '</div>')
    return [hero("Membership", 'Your business isn&rsquo;t limited to one state<span class="dot">.</span> Neither are we<span class="dot">.</span>',
        '<p class="lead">USHA membership gives hydrogen businesses a seat at every table that matters: statehouses, markets, and the rooms where the next decade of hydrogen policy is being written.</p>',
        '<a class="btn btn-primary" href="#apply">Submit an application</a><a class="btn btn-tertiary" href="#brochure">2026 membership brochure &#9656;</a>', MAP_DARK),
        advantage, why, record, members, who, join_membership_variant(), newsletter()]

def page_policymakers(m):
    hero_stats = '''<div class="g3" style="gap: 21px; margin-top: 21px">
      <div class="stat ice"><div class="num">179</div><div class="label">Policymakers attended</div></div>
      <div class="stat ice"><div class="num">41</div><div class="label">States represented</div></div>
      <div class="stat ice"><div class="num">4</div><div class="label">Conventions to date</div></div></div>'''
    coord = sec("light", f'''<div class="split flip">
      <div class="stack"><p class="eyebrow">National coordination</p><h2 class="display h-l">Policy doesn&rsquo;t have to be built in isolation<span class="dot">.</span></h2>
      <p class="lead">The Hydrogen Policy Leaders Roundtable is a national forum where state policymakers learn from one another, compare approaches, and develop practical, nonpartisan frameworks for hydrogen investment, infrastructure, workforce, and deployment.</p>
      <div class="btns"><a class="btn btn-primary" href="#roundtable">Join the Roundtable</a></div></div>
      <div class="g3" style="grid-template-columns: 1fr; gap: 14px">
        {card("Learn", "Know what&rsquo;s shaping hydrogen", "Monthly educational briefings on hydrogen markets, technologies, infrastructure, financing, workforce, and emerging policy issues.")}
        {card("Collaborate", "Learn from every state", "Connect with policymakers from across the country to exchange lessons learned, compare policy approaches, and understand how different states and regions are addressing hydrogen opportunities and challenges.", "tint-cyan")}
        {card("Build", "Turn knowledge into policy", "Apply what you learn to develop practical, nonpartisan policy frameworks that support hydrogen investment, infrastructure, workforce development, economic growth, and deployment.", "tint-gold")}
      </div></div>''')
    tools = sec("tint", f'''<div class="split flip" style="align-items: start">
      <div class="stack"><p class="eyebrow">Policy tools</p><h2 class="display h-l">Start with what already works<span class="dot">.</span></h2>
      <p class="lead">USHA maintains a working library of model legislation, enacted bills, and regulatory guidance so no state has to start from a blank page.</p></div>
      <div class="stack" style="gap: 24px">
        {icon_item("gavel", "Model legislation", "Bill language drafted from hydrogen policy that has already passed, ready to adapt to your state.")}
        {icon_item("capitol", "Enacted state policy", "Tax credits, revolving funds, permitting reforms, and workforce programs that are working today.")}
        {icon_item("book", "Policy &amp; regulatory library", "Guidebooks, factsheets, state roadmaps, and regulatory comments curated for policy staff.")}
        <a href="#resources" style="font-family: Syne, sans-serif; font-weight: 700; font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase">Access the policymaker resources &#9656;</a>
      </div></div>''')
    states_items = [("capitol", "State legislation and regulation"), ("dollar", "Incentives and financing"), ("map", "Regional coordination"), ("factory", "Permitting and infrastructure"), ("users", "Workforce development"), ("book", "Lessons learned and best practice")]
    states = sec("light", f'''<div class="split flip" style="align-items: start">
      <div class="stack"><p class="eyebrow">Fifty states, one economy</p><h2 class="display h-l">Build from the states up<span class="dot">.</span></h2>
      <p class="lead">States set the pace on hydrogen: permitting, incentives, infrastructure, and workforce are decided closer to home than Washington.</p>
      <p>USHA brings the policy expertise, market intelligence, and peer network to help each state move faster, and to align fifty state efforts into one American hydrogen economy.</p></div>
      <div class="g2" style="gap: 21px">{"".join(f'<div style="display: flex; gap: 14px; align-items: center">{icon(i)}<span style="font-family: Manrope, sans-serif; font-weight: 700; font-size: 15px; color: #0D1B2A">{t}</span></div>' for i, t in states_items)}</div>
    </div><p style="font-family: Syne, sans-serif; font-weight: 800; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; color: #6C1FA0; text-align: center">Local leadership in partnership with national coordination<span class="dot">.</span></p>''')
    topics = ["Infrastructure &amp; deployment", "Financing &amp; investment", "Energy security", "Hub integration", "Transportation", "Workforce development", "Market standardization", "Federal policy"]
    convention = sec("dark", f'''<div class="split" style="align-items: start">
      <div class="stack"><p class="eyebrow">Fourth annual convention</p><h2 class="display h-l">Build the framework<span class="dot">.</span> Align the states<span class="dot">.</span> Move the market<span class="dot">.</span></h2>
      <p style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; color: #FFB703; line-height: 1.3">Fourth Annual National Hydrogen Policy Leaders Convention</p>
      <p style="font-family: Syne, sans-serif; font-weight: 600; font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: #F8F9FA">September 8&ndash;10, 2026 &middot; Atlantic City, New Jersey</p>
      <p>Three days that bring policymakers and industry together to build practical state policy, align regional strategies, and create the frameworks hydrogen markets need in order to grow.</p>
      <div class="g2 keep" style="gap: 8px 21px">{"".join(f'<div style="display: flex; gap: 8px; align-items: center; font-size: 14px; color: #B9C6D6"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#00D2FF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 4 4L19 6"/></svg>{t}</div>' for t in topics)}</div>
      <div class="btns"><a class="btn btn-primary" href="#register">Register &middot; complimentary for policymakers</a><a class="btn btn-tertiary" href="#agenda">See the agenda &#9656;</a></div></div>
      <div class="card" style="background: #6C1FA0; border-color: #6C1FA0; padding: 34px; gap: 14px"><span class="chip gold">Government officials</span><h3 style="color: #F8F9FA">Complimentary registration for government officials</h3><p style="color: #F8F9FA">USHA covers convention registration for elected officials and their staff. [Confirm eligibility and travel support details.]</p></div>
    </div>''')
    peers = sec("light", head("A national community", 'Your peers are already at the table<span class="dot">.</span>', extra='<p class="lead" style="max-width: 62ch">Policymakers from across the country are building hydrogen policy through USHA, and comparing notes on what works.</p>') +
        f'''<div class="g4" style="gap: 21px">{"".join(f'<div class="person" style="align-items: center; text-align: center"><div class="avatar {c}">{i}</div><div class="name" style="font-size: 16px">[Policymaker name]</div><div class="role">[Office] &middot; [State]</div></div>' for i, c in [("A","") ,("B","cyan"),("C","purple"),("D",""),("E","cyan"),("F","purple"),("G",""),("H","cyan")])}</div>
        <div class="btns"><a class="btn btn-tertiary" href="#roster">See the policymaker roster &#9656;</a></div>''')
    form = sec("dark", f'''<div class="split flip" style="align-items: start">
      <div class="stack"><p class="eyebrow">Get involved</p><h2 class="display h-l">There is a seat for your state<span class="dot">.</span></h2>
      <p class="lead">Join the Hydrogen Policy Leaders Roundtable, get the publications, and put your state on the map.</p>
      <div class="btns"><a class="btn btn-tertiary" href="#register">Register for the convention &#9656;</a></div></div>
      <div class="stack" style="gap: 14px"><h3 class="display h-2" style="font-size: 24px">Join the Hydrogen Policy Leaders Roundtable</h3><p style="font-size: 14px">Request to join the national forum for state lawmakers and policymakers. A member of the USHA team will follow up with next steps.</p>
        <div class="g2 keep" style="gap: 13px"><div class="fgroup"><p class="flabel">First name</p><div class="field">&nbsp;</div></div><div class="fgroup"><p class="flabel">Last name</p><div class="field">&nbsp;</div></div></div>
        <div class="fgroup"><p class="flabel">Title / position</p><div class="field">&nbsp;</div></div>
        <div class="fgroup"><p class="flabel">Work email</p><div class="field">&nbsp;</div></div>
        <div class="g2 keep" style="gap: 13px"><div class="fgroup"><p class="flabel">State</p><div class="field">Select your state</div></div><div class="fgroup"><p class="flabel">Office type</p><div class="field">Select an option</div></div></div>
        <div class="fgroup"><p class="flabel">Message (optional)</p><div class="field ta">&nbsp;</div></div>
        <div style="display: flex; gap: 10px; align-items: flex-start; font-size: 14px; color: #B9C6D6"><div style="width: 20px; height: 20px; border: 2px solid rgba(248,249,250,0.4); border-radius: 6px; flex: none; margin-top: 2px"></div><span>Yes, I would like to receive updates and resources from USHA.</span></div>
        <div class="btns"><a class="btn btn-primary" href="#roundtable">Request to join</a></div></div>
    </div>''')
    return [hero("Policymakers", 'Shape your local hydrogen economy<span class="dot">.</span>',
        '<p class="lead">Hydrogen policy is being built state by state. USHA brings policymakers from across the country together to learn from one another, develop practical policy frameworks, and build a more coordinated American hydrogen economy.</p>',
        '<a class="btn btn-primary" href="#roundtable">Join the Policy Leaders Roundtable</a><a class="btn btn-tertiary" href="#register">Register for the convention &#9656;</a>', MAP_DARK, hero_stats),
        coord, tools, states, convention, peers, form, join_section(), newsletter()]

def page_industry(m):
    nodes = ["Policy", "Regulators", "Infrastructure", "Capital", "Technology", "End users", "Workforce", "Communities"]
    import math
    node_html = ""
    for i, n in enumerate(nodes):
        a = -math.pi / 2 + i * 2 * math.pi / len(nodes)
        x = 50 + 39 * math.cos(a); y = 50 + 39 * math.sin(a)
        node_html += f'<div class="node" style="left: {x:.1f}%; top: {y:.1f}%">{n}</div>'
    diagram = f'<div class="diagram"><div style="position: absolute; inset: 11%; border-radius: 50%; border: 1.5px dashed rgba(108,31,160,0.35)"></div><div class="node core" style="left: 50%; top: 50%">Market</div>{node_html}</div>'
    connected = sec("light", f'''<div class="split flip">
      <div class="stack"><p class="eyebrow">The hydrogen economy</p><h2 class="display h-l">Everything is connected<span class="dot">.</span></h2>
      <p class="lead">Hydrogen markets are complex and highly interconnected. Success depends on how well every part of the ecosystem works together.</p>
      <p>A market forms where policy, capital, infrastructure, technology, and demand line up. When one piece moves, the others move with it.</p></div>
      {diagram}</div>''')
    challenge = sec("tint", f'''<div class="split flip" style="align-items: start">
      <div class="stack"><p class="eyebrow">The challenge</p><h2 class="display h-l">Your company doesn&rsquo;t operate in isolation<span class="dot">.</span></h2></div>
      <div class="g3" style="grid-template-columns: 1fr; gap: 14px">
        {card("Markets", "Demand doesn&rsquo;t exist on its own", "New technologies need production capacity, customers, offtakers, infrastructure, and economic conditions capable of supporting deployment.")}
        {card("Policy", "Policy shapes markets", "Legislation, regulation, incentives, codes, and standards determine where companies can build and how quickly markets can develop.", "tint-cyan")}
        {card("Connections", "The right people change the equation", "Customers, suppliers, policymakers, economic developers, investors, infrastructure partners, and communities each control a different piece of the market.", "tint-gold")}
      </div></div>''')
    between = [("handshake", "Industry &harr; policymakers", "The state resources and relationships to build practical policy that works."), ("bolt", "Supply &harr; demand", "Connect hydrogen capabilities with the customers and applications that need them."), ("users", "Companies &harr; communities", "Create relationships that turn projects into welcomed, durable deployments."), ("map", "Industry &harr; states", "Coordinate business needs with economic development priorities across fifty states."), ("globe", "Local &harr; national", "Align local decisions with the national framework the market needs to scale.")]
    where = sec("light", head("Where USHA works", 'Between the pieces<span class="dot">.</span>', extra='<p class="lead">USHA operates at the intersections where hydrogen markets are built.</p>') +
        f'<div class="g5" style="gap: 21px">{"".join(f'<div class="pillar" style="padding: 0 13px"><div class="icon" style="width: 56px; height: 56px">{icon(i).split(">",1)[1].rsplit("</div>",1)[0]}</div><div class="t" style="color: #6C1FA0; font-size: 12px">{t}</div><p>{b}</p></div>' for i, t, b in between)}</div>')
    fifty = sec("dark", f'''<div class="split" style="align-items: start">
      <div class="stack"><p class="eyebrow">Fifty states</p><h2 class="display h-l">Fifty states change the equation<span class="dot">.</span></h2>
      <p class="lead">Hydrogen markets don&rsquo;t develop uniformly. Each state represents different resources, industries, drivers, policies, and market conditions.</p>
      <p>A national hydrogen economy requires understanding those differences and connecting them. USHA is the only hydrogen business association working state by state, and the only one connecting what each state builds into one market.</p></div>
      <div class="g3" style="gap: 13px">
        <div class="stat"><div class="num" style="color: #9D4EDD">50</div><div class="label" style="color: #9D4EDD">States</div><p style="font-size: 14px; margin-top: 8px">A policy and market presence in every one.</p></div>
        <div class="stat"><div class="num" style="color: #00D2FF">1</div><div class="label" style="color: #00D2FF">Network</div><p style="font-size: 14px; margin-top: 8px">Industry, policymakers, and partners moving together.</p></div>
        <div class="stat"><div class="num" style="color: #FFB703; font-size: 34px; line-height: 1.15">Connected markets</div><div class="label" style="color: #FFB703">The outcome</div><p style="font-size: 14px; margin-top: 8px">More opportunity. Stronger outcomes.</p></div>
      </div></div>''')
    members = sec("tint", head("The membership", 'Different businesses<span class="dot">.</span> Shared opportunity<span class="dot">.</span>') + tiers() + '<div class="btns"><a class="btn btn-tertiary" href="#members">See all members &#9656;</a></div>')
    programs = sec("light", head("Programs", 'Six ways in<span class="dot">.</span>') + '<div class="g3">' +
        card("", "Hydrogen Nation Network", "Policy development to support Hydrogen Hub implementation, and the people who make it real.", open_link="Open") +
        card("", "Events &amp; networking", "Convenings that make meaningful connections and educate a broader audience.", "tint-cyan", "Open") +
        card("", "45V tax credit campaign", "The future of the industry hangs in the balance. We are on it.", "tint-gold", "Open") +
        card("", "Job board", "Top talent, meet the companies building American hydrogen.", open_link="Open") +
        card("", "Resources", "Strategic materials for Hydrogen Hub planning and implementation.", "tint-cyan", "Open") +
        card("", "Policy Leaders Roundtable", "Non-partisan decision makers championing hydrogen policy in all 50 states.", "tint-gold", "Open") + '</div>')
    shape = sec("tint", f'''<div class="split" style="align-items: center">
      <div class="stack"><p class="eyebrow">Membership</p><h2 class="display h-l">Don&rsquo;t just watch the market develop<span class="dot">.</span> Help shape it<span class="dot">.</span></h2>
      <p class="lead">USHA membership puts your company inside the network connecting policy, markets, industry, and opportunity across all fifty states. Bring your business into the room where the hydrogen economy is being built, and we&rsquo;ll help connect it to the rest.</p></div>
      <div class="btns" style="flex-direction: column; align-items: stretch"><a class="btn btn-primary" href="#membership">Explore membership &#9656;</a><a class="btn btn-tertiary" href="#apply">Submit an application &#9656;</a></div></div>''')
    return [hero("Industry", 'Great technology needs a market<span class="dot">.</span>',
        '''<p class="lead">You can build the best electrolyzer, fuel cell, storage system, production process, infrastructure, or hydrogen project in the world. But technology alone does not create an economy.</p>
        <p>Markets require customers. Customers require reliable supply, infrastructure, pricing, and demand. Investment requires certainty. Communities need benefits. Local and national policy sets the rules for all of it.</p>
        <p style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; color: #FFB703">USHA works where those pieces meet.</p>''',
        '<a class="btn btn-primary" href="#membership">Explore membership &#9656;</a>', MAP_DARK),
        connected, challenge, where, fifty, members, programs, shape, join_section(), newsletter()]

def page_events(m):
    stats = '''<div class="stack" style="gap: 21px">
      <div class="stat ice"><div class="num">4<span class="dot">.</span></div><div class="label">Conventions to date</div></div>
      <div class="stat ice"><div class="num">41<span class="dot">.</span></div><div class="label">States represented</div></div>
      <div class="stat ice"><div class="num">179</div><div class="label">Policymakers attended</div></div></div>'''
    upcoming = sec("light", f'''<div class="card tint-gold" style="flex-direction: {'column' if m else 'row'}; align-items: {'stretch' if m else 'center'}; justify-content: space-between; gap: 34px; padding: 34px 38px">
      <div class="stack-s"><span class="chip">September 8&ndash;10, 2026 &middot; Atlantic City, NJ</span><h2 class="display h-1">Fourth Annual National Hydrogen Policy Leaders Convention<span class="dot">.</span></h2>
      <p style="font-family: Syne, sans-serif; font-weight: 600; font-size: 13px; letter-spacing: 0.06em; text-transform: uppercase; color: #0D1B2A">Build the framework. Align the states. Move the market.</p>
      <p style="font-size: 15px">Three days to build the policy framework for the year that will shape the hydrogen economy.</p></div>
      <div class="btns"><a class="btn btn-primary" href="#register">Register interest</a></div></div>''', "padding-top: 55px; padding-bottom: 34px")
    past = [("Sep 15&ndash;17, 2025", "Third Annual National Convention &middot; Denver, CO"), ("Aug 15, 2024", "Regional Convention &middot; Pennsylvania, ARCH2 and MACH2 hubs"), ("Mar 1&ndash;3, 2024", "Second Annual Convention"), ("Nov 14&ndash;16, 2022", "First Annual Convention")]
    rows = "".join(f'<div class="list-row" style="grid-template-columns: {"1fr" if m else "150px 1fr"}"><span class="date">{d}</span><h3 style="margin: 0">{t}</h3></div>' for d, t in past)
    past_sec = sec("tint", f'<p class="eyebrow">Past conventions</p><div>{rows}</div>', "padding-top: 55px; padding-bottom: 55px")
    return [hero("USHA events", 'The Alliance convenes<span class="dot">.</span>',
        '<p class="lead">Hydrogen Policy Leaders Conventions bring members, companies, and policymakers into one room, and out with one framework.</p>', "", stats),
        upcoming, past_sec, join_section(), newsletter()]

def page_media(m):
    lanes = sec("light", '<div class="g3">' + card("", "USHA in the News", "Where the Alliance shows up in the press.") + card("", "Hydrogen News", "Industry news and developments, curated weekly.", "tint-cyan") + card("", "USHA Blog", "Original writing from the Alliance.", "tint-gold") + '</div>', "padding-top: 55px; padding-bottom: 55px")
    items = [("Video", "Third Annual Convention, compilation", "Policymakers, companies, and industry leaders together in Denver."),
        ("Interview", "Roxana Bekemohammadi at World Hydrogen NA 2025", "Reading the hydrogen economy&rsquo;s sentiment, on the record."),
        ("Policy", "45V: the rules and the stakes", "The production credit regulations and the Three Pillars impact."),
        ("Interview", "Paul Mueller &middot; HNO International", "A small business making hydrogen work."),
        ("Interview", "Carolina Ahlstrand &middot; Hycamite", "An innovative approach to hydrogen production."),
        ("Education", "Hydrogen 101 &amp; facility visits", "Sessions with industry partners; on-site at MANN+HUMMEL and the BayoTech hydrogen hub.")]
    featured = sec("tint", head("Featured", 'Recent coverage<span class="dot">.</span>') + '<div class="g3">' + "".join(card(c, t, b) for c, t, b in items) + '</div>')
    press = sec("light", f'''<div class="split">
      <div class="stack"><p class="eyebrow">Press</p><h2 class="display h-l">Working on a story<span class="dot">?</span></h2>
      <p class="lead">Media inquiries, interview requests, and the press kit: marks, boilerplate, and leadership bios.</p>
      <p style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 18px; color: #0D1B2A">marketing@ushydrogenalliance.org</p>
      <div class="btns"><a class="btn btn-primary" href="#press-kit">Press kit</a><a class="btn btn-tertiary" href="#contact">Media inquiry &#9656;</a></div></div>
      {MAP_LIGHT}</div>''')
    return [hero("Media room", 'On the record<span class="dot">.</span>',
        '<p class="lead">Coverage across the hydrogen industry, policy, and the Alliance, plus original interviews and analysis.</p>', "", MAP_DARK),
        lanes, featured, press, join_section(), newsletter()]

def page_resources(m):
    tags = ["DOE", "Factsheet", "Funding", "Guidance", "Report", "State roadmap", "U.S. policy", "USHA", "International", "National strategy", "Press release", "Research"]
    tag_html = '<div class="tags"><span class="tag on">All</span>' + "".join(f'<span class="tag">{t}</span>' for t in tags) + '</div>'
    items = [("Mar 16, 2026", "Global Hydrogen Market Landscape Report", "Markets enter a period of differentiation, consolidation, and strategic positioning."),
        ("Feb 18, 2026", "National Hydrogen Policy Leaders Roundtable", "A first-of-its-kind forum coordinating hydrogen policy across states and regions."),
        ("Dec 12, 2025", "Policy Advocacy 101 Handbook", "Legislation guidance for advocacy efforts: the playbook, written down."),
        ("Oct 1, 2025", "Unlocking Geologic Hydrogen", "The new American energy gold rush."),
        ("Sep 3, 2025", "Hydrogen Technology Guidebook for Elected Officials", "Hydrogen and fuel cells can be deployed now: transportation, industry, power."),
        ("Jan 3, 2025", "Section 45V Clean Hydrogen Tax Credit Summary", "The production credit, its rules, and the USHA statement on final Treasury guidance."),
        ("Aug 14, 2025", "Policy Brief: One Big Beautiful Bill Act", "Energy tax credit changes versus Inflation Reduction Act provisions, analyzed."),
        ("Apr 15, 2025", "Technology-Neutral Tax Credits Policy Brief", "Rainey Center analysis on tax credit mechanisms."),
        ("Apr 8, 2025", "New York State Hydrogen Assessment", "Prepared by NYSERDA with NREL and E3."),
        ("Dec 20, 2024", "DOE Hydrogen Program Plan", "The foundational resource for RDD&amp;D of hydrogen technologies.")]
    rows = "".join(f'<div class="list-row" style="grid-template-columns: {"1fr" if m else "150px 1fr"}"><span class="date">{d}</span><div><h3>{t}</h3><p>{b}</p></div></div>' for d, t, b in items)
    lib = sec("light", f'{tag_html}<div>{rows}</div><div class="btns"><a class="btn btn-primary" href="#more">Load more</a></div>', "padding-top: 55px; padding-bottom: 76px")
    return [hero("Resources", 'The library<span class="dot">.</span>',
        '<p class="lead">Guidebooks, factsheets, policy briefs, and state roadmaps: everything the hydrogen economy runs on, in one place.</p>', ""),
        lib, join_section(), newsletter()]

def page_hydrogen_built(m):
    photo = '<div class="hb-photo"><img src="hb-hero.jpg" alt="Worker in a hard hat looking over a hydrogen facility at sunset"><img src="usha-map-knockout.svg" alt="" style="position: absolute; left: 6%; top: 8%; width: 60%; opacity: 0.85; filter: drop-shadow(0 0 18px rgba(0,210,255,0.35))"></div>'
    initiative = sec("light", f'''<div class="split" style="align-items: start">
      <div class="stack"><p class="eyebrow">The Hydrogen Built initiative</p><h2 class="display h-l">A national call to build the hydrogen economy<span class="dot">.</span></h2>
      <p class="lead">Hydrogen Built is USHA&rsquo;s initiative to elevate the real impact of hydrogen across America, and to empower the people, companies, and communities building it.</p>
      <p>Together, we&rsquo;re proving that hydrogen is more than a promise. It&rsquo;s already being built.</p></div>
      <div class="g2 keep" style="gap: 0">
        <div class="pillar">{icon("people")}<div class="t" style="color: #6C1FA0">People</div><p>Good jobs. Safer communities. A stronger future.</p></div>
        <div class="pillar">{icon("shield", "#0089A8")}<div class="t" style="color: #0089A8">Security</div><p>Reliable energy. Resilient supply chains. Greater independence.</p></div>
        <div class="pillar" style="border-left: 0; border-top: 1px solid #DDE4EA">{icon("chart", "#00A8CC")}<div class="t" style="color: #00A8CC">Prosperity</div><p>Investment. Innovation. Economic growth.</p></div>
        <div class="pillar" style="border-top: 1px solid #DDE4EA">{icon("leaf", "#E09E00")}<div class="t" style="color: #E09E00">Sustainability</div><p>Lower emissions. Cleaner air. A better tomorrow.</p></div>
      </div></div>''')
    building = sec("dark", f'''<div class="split" style="align-items: start">
      <div class="stack"><p class="eyebrow">What we&rsquo;re building</p><h2 class="display h-l">Hydrogen is already delivering across America<span class="dot">.</span></h2>
      <p class="lead">From production facilities and infrastructure to mobility projects and power generation, hydrogen is creating measurable impact in every region.</p></div>
      <div class="stat" style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px">{icon("pin", "#00D2FF")}<div class="num" style="color: #00D2FF">50</div><div class="label" style="color: #00D2FF">States</div><p style="font-size: 15px">Hydrogen projects, policies, and investments are taking shape.</p></div></div>
      <div class="g3" style="gap: 0">
        <div class="pillar">{icon("users", "#00D2FF")}<div class="t" style="color: #00D2FF">Good jobs</div><p>From engineering and construction to operations and manufacturing.</p></div>
        <div class="pillar">{icon("shield", "#00D2FF")}<div class="t" style="color: #00D2FF">Energy security</div><p>Diverse domestic resources. Stronger supply chains. Less reliance.</p></div>
        <div class="pillar">{icon("chart", "#FFB703")}<div class="t" style="color: #FFB703">Economic growth</div><p>Billions in investment. New industries. Stronger communities.</p></div>
      </div>''')
    involved = sec("light", f'''<div class="split even" style="align-items: start; gap: 55px">
      <div class="stack" style="gap: 24px"><p class="eyebrow">How you can get involved</p><h2 class="display h-l">Be part of what&rsquo;s Hydrogen Built<span class="dot">.</span></h2>
      <p class="lead">Add your voice, share your story, and help show the real impact of hydrogen in your state and community.</p>
      {icon_item("mega", "Share your story", "Highlight your project, innovation, or community impact.")}
      {icon_item("people", "Join the movement", "Businesses, workers, communities, and leaders, together.")}
      {icon_item("star", "Amplify the impact", "Help others see what hydrogen is making possible.")}
      <div class="btns"><a class="btn btn-primary" href="#story">Submit your story</a></div></div>
      <div class="card" style="padding: 34px; gap: 14px"><p class="eyebrow">Join the movement</p><h3 style="font-size: 28px">I stand with Hydrogen Built<span class="dot">.</span></h3><p>Add your name to show your support for hydrogen jobs, energy security, and a stronger America.</p>
        <div class="g2 keep" style="gap: 13px"><div class="fgroup"><p class="flabel">First name *</p><div class="field">&nbsp;</div></div><div class="fgroup"><p class="flabel">Last name *</p><div class="field">&nbsp;</div></div></div>
        <div class="fgroup"><p class="flabel">Organization (optional)</p><div class="field">&nbsp;</div></div>
        <div class="fgroup"><p class="flabel">Email address *</p><div class="field">&nbsp;</div></div>
        <div class="g2 keep" style="gap: 13px"><div class="fgroup"><p class="flabel">State *</p><div class="field">Select your state</div></div><div class="fgroup"><p class="flabel">I am a&hellip; *</p><div class="field">Select an option</div></div></div>
        <div style="display: flex; gap: 10px; align-items: flex-start; font-size: 14px; color: #45566B"><div style="width: 20px; height: 20px; border: 2px solid rgba(13,27,42,0.35); border-radius: 6px; flex: none; margin-top: 2px"></div><span>Yes, I would like to receive updates about the Hydrogen Built initiative and how I can get involved.</span></div>
        <div class="btns"><a class="btn btn-primary" href="#sign">Add my name</a></div>
        <div style="display: flex; flex-direction: column; align-items: center; gap: 10px; padding-top: 21px; border-top: 1px solid #DDE4EA; text-align: center"><img src="usha-h-full-light.svg" alt="USHA dotted-H monogram, full color on ice" style="width: 64px; height: auto; display: block"><p style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 18px; color: #0D1B2A">Fifty states. One hydrogen economy. Built together<span class="dot">.</span></p><p style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 18px; color: #6C1FA0">#HydrogenBuilt</p></div>
      </div></div>''')
    return [hero("Hydrogen Built", 'Hydrogen built<span class="dot">.</span> America strengthened<span class="dot">.</span>',
        '<p class="lead">Hydrogen is built in America by American workers, innovators, and communities.</p><p>It powers our economy, strengthens our energy security, and builds a cleaner, more competitive future.</p>',
        '<a class="btn btn-primary" href="#movement">Join the movement</a>', photo),
        initiative, building, involved, join_section(), newsletter()]

def page_contact(m):
    form = f'''<div class="stack" style="gap: 14px">
      <div class="g2 keep" style="gap: 13px"><div class="fgroup"><p class="flabel">First name</p><div class="field">&nbsp;</div></div><div class="fgroup"><p class="flabel">Last name</p><div class="field">&nbsp;</div></div></div>
      <div class="fgroup"><p class="flabel">Work email</p><div class="field">&nbsp;</div></div>
      <div class="fgroup"><p class="flabel">Organization</p><div class="field">&nbsp;</div></div>
      <div class="fgroup"><p class="flabel">I&rsquo;m reaching out about</p><div class="field">Select an option</div></div>
      <div class="fgroup"><p class="flabel">Message</p><div class="field ta">&nbsp;</div></div>
      <div class="btns"><a class="btn btn-primary" href="#send">Send message</a></div></div>'''
    reach = sec("light", f'''<div class="split" style="align-items: start">
      <div class="stack"><p class="eyebrow">Get in touch</p><h2 class="display h-l">We want to hear from you<span class="dot">.</span></h2>
      <p class="lead">Whether you&rsquo;re building a hydrogen business, shaping policy, developing a project, exploring membership, or looking to collaborate, we want to hear from you.</p>
      <div class="stack-s" style="gap: 21px; margin-top: 8px">
        <div><p class="eyebrow" style="margin-bottom: 4px">All inquiries</p><p style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 21px; color: #0D1B2A">marketing@ushydrogenalliance.org</p></div>
        <div><p class="eyebrow" style="margin-bottom: 4px">Membership</p><p>Ready to join? <a href="#apply">Submit an application &#9656;</a></p></div>
        <div><p class="eyebrow" style="margin-bottom: 4px">Speak at an event</p><p>Propose a session for a convention or webinar. <a href="#speak">Tell us about it &#9656;</a></p></div>
        <div><p class="eyebrow" style="margin-bottom: 4px">Media inquiries</p><p>Press requests and the press kit. <a href="#media">Media Room &#9656;</a></p></div>
      </div></div>
      {form}</div>''')
    return [hero("Contact", 'Get in the room<span class="dot">.</span>',
        '<p class="lead">One team, fifty states, and a fast reply. Tell us what you&rsquo;re building.</p>', "", MAP_DARK),
        reach, join_section(), newsletter()]

def page_member(m):
    info = '<div class="g3">' + "".join(f'<div class="info"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in [("Headquarters", "[City, State]"), ("Sector", "[Sector &middot; application]"), ("Member since", "[Year]")]) + '</div>'
    profile = sec("tint", info, "padding-top: 34px; padding-bottom: 34px")
    words = sec("light", '<div class="stack-s"><p class="eyebrow">In their words</p>' + quotes([("[Member quote about the value of USHA membership.]", "[Name] &middot; [Member company]")]) + '</div>', "padding-top: 55px; padding-bottom: 55px")
    coalition = sec("tint", f'''<div style="display: flex; flex-direction: {'column' if m else 'row'}; align-items: {'stretch' if m else 'center'}; justify-content: space-between; gap: 21px"><h2 class="display h-1">The coalition that builds<span class="dot">.</span></h2><div class="btns"><a class="btn btn-tertiary" href="#members">All members &#9656;</a><a class="btn btn-primary" href="#membership">Become a member</a></div></div>''', "padding-top: 55px; padding-bottom: 55px")
    logo_box = '<div style="background: #FFFFFF; border-radius: 12px; min-height: 240px; display: flex; align-items: center; justify-content: center; font-family: Syne, sans-serif; font-weight: 600; font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase; color: #6B7A8D">[Member logo]</div>'
    return [hero("[Membership tier]", '[Member company]<span class="dot">.</span>',
        '<p class="lead">[One-paragraph member profile: what the company builds, where it operates, and how it puts USHA policy wins to work.]</p>',
        '<a class="btn btn-primary" href="#site">Visit website</a><a class="btn btn-tertiary" href="#linkedin">LinkedIn &#9656;</a>', logo_box),
        profile, words, coalition, join_section(), newsletter()]

PAGES = {
    "About": ("about", "About Us", page_about),
    "Membership": ("membership", "Membership", page_membership),
    "Policymakers": ("policymakers", "Policymakers", page_policymakers),
    "Industry": ("industry", "Industry", page_industry),
    "Events": ("events", "Events", page_events),
    "MediaRoom": ("media", "Media Room", page_media),
    "Resources": ("resources", "Resources", page_resources),
    "HydrogenBuilt": (None, "Hydrogen Built", page_hydrogen_built),
    "Contact": (None, "Contact", page_contact),
    "MemberProfile": ("membership", "Member Profile", page_member),
}

def render(stem, m):
    key, title, fn = PAGES[stem]
    width = 390 if m else 1440
    body = nav(key, m) + "".join(fn(m)) + footer(m)
    root = f'<div class="root{" m" if m else ""}" style="display: flex; flex-direction: column; width: {width}px; background: #0D1B2A; overflow: hidden">{body}</div>'
    return f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>{CSS}</style>
</helmet>
{root}
</x-dc>
</body>
</html>
'''

if __name__ == "__main__":
    for stem in PAGES:
        for m in (False, True):
            name = f"{stem}{'Mobile' if m else ''}.dc.html"
            with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
                f.write(render(stem, m))
            print("wrote", name)
