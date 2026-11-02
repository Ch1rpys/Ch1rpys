#!/usr/bin/env python3
"""Generate the dark cyber hero banner for the Ch1rpys profile README.

GitHub strips every colour/background style from README HTML, so the only way
to get a dark, neon look is to author the banner as an SVG image and host it
in this repo. Keeping the generator around makes the layout tweakable.
"""
import pathlib

W, H = 1200, 420

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
CJK = "'PingFang SC','Microsoft YaHei','Noto Sans CJK SC','Hiragino Sans GB',sans-serif"

CYAN = "#22d3ee"
VIOLET = "#a855f7"
TEXT = "#e2e8f0"
DIM = "#64748b"

# --------------------------------------------------------------- piano strip --
# 14 white keys starting at C. Black keys follow the usual 2-3 grouping.
WHITE_PITCHES = "CDEFGAB CDEFGAB".replace(" ", "")
WHITE_W = 31
WHITE_H = 118
BLACK_W = 18
BLACK_H = 72


def piano_svg(x0: int, y0: int, lit: int = 3) -> str:
    """A keyboard drawn the way a real one reads: white keys sit flush
    together (only hairline separators), black keys overlap them."""
    parts = []
    # white keys: flush, separated by a 1px darker line
    for i in range(len(WHITE_PITCHES)):
        x = x0 + i * WHITE_W
        parts.append(
            f'<rect x="{x}" y="{y0}" width="{WHITE_W}" height="{WHITE_H}" '
            f'fill="#e8eefc"/>'
        )
        parts.append(
            f'<rect x="{x + WHITE_W - 1}" y="{y0}" width="1" height="{WHITE_H}" '
            f'fill="#94a3b8" opacity="0.55"/>'
        )
    # black keys: overlapping the boundary between two white keys
    for i, p in enumerate(WHITE_PITCHES):
        if p in "CDFGA":
            cx = x0 + (i + 1) * WHITE_W - BLACK_W / 2
            parts.append(
                f'<rect x="{cx:.1f}" y="{y0}" width="{BLACK_W}" height="{BLACK_H}" '
                f'rx="2" fill="#080d18" stroke="#1e293b" stroke-width="1"/>'
            )
    # one key lit up in neon
    lx = x0 + lit * WHITE_W
    parts.append(
        f'<rect x="{lx}" y="{y0}" width="{WHITE_W - 1}" height="{WHITE_H}" '
        f'fill="url(#neon)" opacity="0.9"/>'
    )
    return "".join(parts)


def build() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img"
     aria-label="Ch1rpys — AI 应用开发 / 音乐游戏 / Linux 内核移植">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0" stop-color="#0c1222"/>
      <stop offset="0.55" stop-color="#080d18"/>
      <stop offset="1" stop-color="#04060c"/>
    </linearGradient>

    <linearGradient id="neon" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}"/>
      <stop offset="0.55" stop-color="#818cf8"/>
      <stop offset="1" stop-color="{VIOLET}"/>
    </linearGradient>

    <radialGradient id="halo" cx="0.18" cy="0.42" r="0.62">
      <stop offset="0" stop-color="{CYAN}" stop-opacity="0.16"/>
      <stop offset="0.55" stop-color="#6366f1" stop-opacity="0.05"/>
      <stop offset="1" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>

    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#16213a" stroke-width="1"/>
    </pattern>

    <filter id="glow" x="-40%" y="-80%" width="180%" height="260%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="11" result="blur"/>
      <feFlood flood-color="{CYAN}" flood-opacity="0.5" result="col"/>
      <feComposite in="col" in2="blur" operator="in" result="g"/>
      <feMerge>
        <feMergeNode in="g"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="9"/>
    </filter>
  </defs>

  <!-- backdrop -->
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.32"/>
  <rect width="{W}" height="{H}" fill="url(#halo)"/>

  <!-- neon top rail -->
  <rect x="0" y="0" width="{W}" height="3" fill="url(#neon)" opacity="0.9"/>
  <rect x="0" y="3" width="{W}" height="16" fill="url(#neon)" opacity="0.13" filter="url(#soft)"/>

  <!-- HUD corner brackets -->
  <g fill="none" stroke="{CYAN}" stroke-width="2" opacity="0.5">
    <path d="M34 40h46M34 40v34"/>
    <path d="M{W-34} {H-40}h-46M{W-34} {H-40}v-34"/>
  </g>

  <!-- terminal prompt -->
  <text x="70" y="118" font-family="{MONO}" font-size="21" fill="{CYAN}">$</text>
  <text x="96" y="118" font-family="{MONO}" font-size="21" fill="{DIM}">ssh ch1rpy@github</text>

  <!-- name -->
  <text x="66" y="232" font-family="{MONO}" font-size="96" font-weight="700"
        fill="{TEXT}" filter="url(#glow)" letter-spacing="-1">Ch1rpys</text>

  <!-- neon underline -->
  <rect x="70" y="256" width="248" height="3" fill="url(#neon)"/>

  <!-- tagline -->
  <text x="70" y="300" font-family="{CJK}" font-size="25" fill="#cbd5e1">AI 应用开发 · 音乐游戏 · Linux 内核移植</text>

  <!-- footer line -->
  <text x="70" y="352" font-family="{MONO}" font-size="16" fill="#475569">10minstudio · IPOL-Studio · piae-mentes-project</text>

  <!-- piano strip -->
  {piano_svg(700, 250, lit=3)}

  <!-- scanlines -->
  <g opacity="0.028">
    {"".join(f'<rect x="0" y="{y}" width="{W}" height="1" fill="#7dd3fc"/>' for y in range(0, H, 5))}
  </g>
</svg>
"""


def build_footer() -> str:
    """A slim dark sign-off bar that matches the hero's palette."""
    w, h = 1200, 96
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"
     viewBox="0 0 {w} {h}" role="img" aria-label="Thanks for visiting">
  <defs>
    <linearGradient id="neon2" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}"/>
      <stop offset="0.55" stop-color="#818cf8"/>
      <stop offset="1" stop-color="{VIOLET}"/>
    </linearGradient>
    <pattern id="grid2" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#16213a" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="{w}" height="{h}" fill="#080d18"/>
  <rect width="{w}" height="{h}" fill="url(#grid2)" opacity="0.3"/>
  <rect x="0" y="0" width="{w}" height="2" fill="url(#neon2)" opacity="0.85"/>
  <rect x="0" y="{h - 1}" width="{w}" height="1" fill="#1e293b"/>

  <text x="{w / 2 - 132}" y="{h / 2 + 9}" font-family="{MONO}" font-size="21"
        fill="{CYAN}">❯</text>
  <text x="{w / 2 - 96}" y="{h / 2 + 9}" font-family="{MONO}" font-size="21"
        fill="#94a3b8">thanks for visiting</text>
  <text x="{w / 2 + 152}" y="{h / 2 + 9}" font-family="{MONO}" font-size="21"
        fill="#475569">_</text>
</svg>
"""


if __name__ == "__main__":
    # 目录名带版本号：raw.githubusercontent 的 CDN 按路径缓存且忽略查询参数，
    # 改图时换一个目录才能确保访客拿到新文件。
    base = pathlib.Path(__file__).with_name("assets") / "v2"
    base.mkdir(parents=True, exist_ok=True)
    for name, svg in (("hero.svg", build()), ("footer.svg", build_footer())):
        path = base / name
        path.write_text(svg, encoding="utf-8")
        print(f"wrote {path} ({path.stat().st_size} bytes)")
