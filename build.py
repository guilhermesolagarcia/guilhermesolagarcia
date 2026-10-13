"""Gera os SVGs do README de perfil em duas versões (dark/light)."""
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

THEMES = {
    "dark": dict(bg="#0B0D10", panel="#12161B", line="#232A33", text="#E8ECF1",
                 mute="#7D8794", accent="#C8F135", accent2="#5EEAD4"),
    "light": dict(bg="#F6F7F4", panel="#FFFFFF", line="#E2E5E0", text="#14181D",
                  mute="#66707C", accent="#4F7A00", accent2="#0F766E"),
}

MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace"
SANS = "'Inter','Segoe UI',Helvetica,Arial,sans-serif"


def header(t):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-labelledby="t d">
  <title id="t">Guilherme Sola Garcia</title>
  <desc id="d">Desenvolvedor frontend que entende UX. Motion, 3D na web e mobile. Último semestre de ADS na FIAP, São Paulo.</desc>
  <style>
    .mono {{ font-family: {MONO}; }}
    .sans {{ font-family: {SANS}; }}
    .in {{ animation: up .7s cubic-bezier(.32,.72,0,1) backwards; }}
    .d1 {{ animation-delay: .15s }} .d2 {{ animation-delay: .45s }} .d3 {{ animation-delay: .75s }}
    .d4 {{ animation-delay: 1.05s }} .d5 {{ animation-delay: 1.35s }}
    .cursor {{ animation: blink 1.05s steps(1) infinite; }}
    .scan {{ animation: scan 6s cubic-bezier(.65,0,.35,1) infinite; }}
    @keyframes up {{ from {{ opacity: 0; transform: translateY(14px) }} to {{ opacity: 1; transform: none }} }}
    @keyframes blink {{ 50% {{ opacity: 0 }} }}
    @keyframes scan {{ 0% {{ transform: translateX(-260px) }} 60%,100% {{ transform: translateX(1260px) }} }}
    @media (prefers-reduced-motion: reduce) {{ .in, .cursor {{ animation: none }} .scan {{ display: none }} }}
  </style>
  <defs>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M24 0H0V24" fill="none" stroke="{t['line']}" stroke-width="1"/>
    </pattern>
    <linearGradient id="fade" x1="0" x2="1">
      <stop offset="0" stop-color="{t['bg']}" stop-opacity="0"/>
      <stop offset="1" stop-color="{t['bg']}"/>
    </linearGradient>
    <linearGradient id="beam" x1="0" x2="1">
      <stop offset="0" stop-color="{t['accent']}" stop-opacity="0"/>
      <stop offset=".5" stop-color="{t['accent']}" stop-opacity=".9"/>
      <stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="win"><rect x="1" y="1" width="1198" height="418" rx="18"/></clipPath>
  </defs>

  <g clip-path="url(#win)">
    <rect width="1200" height="420" fill="{t['bg']}"/>
    <rect x="640" width="560" height="420" fill="url(#grid)" opacity=".55"/>
    <rect x="640" width="560" height="420" fill="url(#fade)" transform="rotate(180 920 210)"/>

    <!-- barra da janela -->
    <rect width="1200" height="44" fill="{t['panel']}"/>
    <line x1="0" y1="44" x2="1200" y2="44" stroke="{t['line']}"/>
    <circle cx="26" cy="22" r="6" fill="{t['line']}"/><circle cx="46" cy="22" r="6" fill="{t['line']}"/><circle cx="66" cy="22" r="6" fill="{t['line']}"/>
    <text x="600" y="27" text-anchor="middle" class="mono" font-size="13" fill="{t['mute']}">sola@fiap: ~ — man sola</text>
    <rect class="scan" x="0" y="43" width="240" height="2" fill="url(#beam)"/>

    <!-- conteúdo -->
    <text class="mono in d1" x="64" y="104" font-size="16" fill="{t['mute']}"><tspan fill="{t['accent']}">$</tspan> man sola <tspan class="cursor" fill="{t['accent']}">█</tspan></text>

    <text class="mono in d2" x="64" y="146" font-size="13" letter-spacing="3" fill="{t['accent2']}">SOLA(1) · PRODUCT REQUIREMENTS</text>
    <text class="sans in d2" x="60" y="222" font-size="76" font-weight="800" letter-spacing="-3" fill="{t['text']}">Guilherme Sola<tspan fill="{t['accent']}">.</tspan></text>

    <text class="sans in d3" x="64" y="270" font-size="22" fill="{t['text']}" fill-opacity=".86">Dev frontend que entende UX. Interfaces que se movem <tspan font-style="italic">com motivo</tspan>.</text>

    <g class="mono in d4" font-size="14" fill="{t['mute']}">
      <text x="64" y="326"><tspan fill="{t['accent']}">--motion</tspan>  GSAP · Three.js · R3F</text>
      <text x="380" y="326"><tspan fill="{t['accent']}">--mobile</tspan>  React Native · Expo</text>
      <text x="690" y="326"><tspan fill="{t['accent']}">--ux</tspan>  decide antes de codar</text>
    </g>

    <g class="in d5">
      <rect x="64" y="358" width="10" height="10" rx="5" fill="{t['accent']}"/>
      <text class="mono" x="84" y="368" font-size="13" fill="{t['mute']}">ADS · FIAP · último semestre  ·  São Paulo, BR</text>
    </g>

    <!-- monograma -->
    <g transform="translate(980 200)" class="in d3">
      <circle r="118" fill="none" stroke="{t['line']}" stroke-width="1.5"/>
      <circle r="86" fill="none" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4 8">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="40s" repeatCount="indefinite"/>
      </circle>
      <text text-anchor="middle" y="24" class="sans" font-size="72" font-weight="800" letter-spacing="-4" fill="{t['text']}">gs</text>
      <circle cx="44" cy="20" r="6" fill="{t['accent']}"/>
    </g>
  </g>
  <rect x=".5" y=".5" width="1199" height="419" rx="18" fill="none" stroke="{t['line']}"/>
</svg>"""


def divider(t, num, label):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="56" viewBox="0 0 1200 56" role="img" aria-label="{num} {label}">
  <text x="0" y="36" font-family="{MONO}" font-size="15" fill="{t['accent']}">{num}</text>
  <text x="44" y="36" font-family="{MONO}" font-size="15" letter-spacing="4" fill="{t['text']}">{label.upper()}</text>
  <line x1="{60 + len(label) * 13.5}" y1="31" x2="1200" y2="31" stroke="{t['line']}" stroke-width="1.5"/>
</svg>"""


def kura(t):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-label="KURA × Clyvo Vet — apps mobile de clínica e tutor">
  <rect width="1200" height="675" fill="{t['bg']}"/>
  <defs><pattern id="g" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{t['line']}"/></pattern></defs>
  <rect width="1200" height="675" fill="url(#g)" opacity=".6"/>
  <g font-family="{SANS}">
    <text x="80" y="150" font-family="{MONO}" font-size="20" letter-spacing="4" fill="{t['accent2']}">CHALLENGE FIAP 2026 × CLYVO VET</text>
    <text x="76" y="260" font-size="120" font-weight="800" letter-spacing="-5" fill="{t['text']}">KURA<tspan fill="{t['accent']}">.</tspan></text>
    <text x="80" y="320" font-size="30" fill="{t['text']}" fill-opacity=".8">O cuidado registrado.</text>
    <text x="80" y="540" font-family="{MONO}" font-size="20" fill="{t['mute']}"><tspan fill="{t['accent']}">role</tspan>  mobile + ux</text>
  </g>
  <!-- dois celulares -->
  <g transform="translate(720 90)">
    <rect width="190" height="390" rx="30" fill="{t['panel']}" stroke="{t['line']}" stroke-width="2"/>
    <rect x="20" y="40" width="150" height="16" rx="8" fill="{t['accent']}"/>
    <rect x="20" y="76" width="110" height="10" rx="5" fill="{t['line']}"/>
    <rect x="20" y="110" width="150" height="70" rx="14" fill="{t['line']}" opacity=".7"/>
    <rect x="20" y="194" width="150" height="70" rx="14" fill="{t['line']}" opacity=".7"/>
    <rect x="20" y="278" width="150" height="70" rx="14" fill="{t['line']}" opacity=".7"/>
    <text x="95" y="430" text-anchor="middle" font-family="{MONO}" font-size="16" fill="{t['mute']}">clínica</text>
  </g>
  <g transform="translate(940 150)">
    <rect width="190" height="390" rx="30" fill="{t['panel']}" stroke="{t['line']}" stroke-width="2"/>
    <circle cx="95" cy="100" r="44" fill="{t['accent2']}" opacity=".85"/>
    <rect x="40" y="170" width="110" height="14" rx="7" fill="{t['text']}" opacity=".8"/>
    <rect x="55" y="196" width="80" height="10" rx="5" fill="{t['line']}"/>
    <rect x="20" y="240" width="70" height="70" rx="14" fill="{t['line']}" opacity=".7"/>
    <rect x="100" y="240" width="70" height="70" rx="14" fill="{t['accent']}" opacity=".9"/>
    <text x="95" y="430" text-anchor="middle" font-family="{MONO}" font-size="16" fill="{t['mute']}">tutor</text>
  </g>
</svg>"""


def footer(t):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="80" viewBox="0 0 1200 80" role="img" aria-label="SOLA(1) · São Paulo, BR · 2026">
  <line x1="0" y1="20" x2="1200" y2="20" stroke="{t['line']}" stroke-width="1.5"/>
  <g font-family="{MONO}" font-size="14" fill="{t['mute']}">
    <text x="0" y="60">SOLA(1)</text>
    <text x="600" y="60" text-anchor="middle">feito à mão · São Paulo, BR</text>
    <text x="1200" y="60" text-anchor="end">2026<tspan fill="{t['accent']}"> ●</tspan></text>
  </g>
</svg>"""


SECTIONS = [("01", "problem"), ("02", "principles"), ("03", "shipped"),
            ("04", "scope"), ("05", "non-goals"), ("06", "roadmap"), ("07", "see also")]

for name, t in THEMES.items():
    (OUT / f"header-{name}.svg").write_text(header(t), encoding="utf-8")
    (OUT / f"kura-{name}.svg").write_text(kura(t), encoding="utf-8")
    (OUT / f"footer-{name}.svg").write_text(footer(t), encoding="utf-8")
    for num, label in SECTIONS:
        slug = label.replace(" ", "-")
        (OUT / f"{num}-{slug}-{name}.svg").write_text(divider(t, num, label), encoding="utf-8")

print("ok", len(list(OUT.glob("*.svg"))), "svgs")
