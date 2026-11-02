#!/usr/bin/env python3
"""Generate README.md for the Ch1rpys GitHub profile repository.

Keeping the generator around makes it easy to tweak wording and re-render
without hand-escaping URL query strings full of Chinese characters.
"""
from urllib.parse import quote

U = "Ch1rpys"


def q(s: str, safe: str = "") -> str:
    return quote(s, safe=safe)


# ----------------------------------------------------------------- assets ----
# 横幅 SVG 直接存在本仓库里，不再依赖 capsule-render 这类第三方图床：
# 那些服务一旦不可用，页面最显眼的位置就空一块。
# assets/banner.svg（浅色）、banner-dark.svg（深色）、footer.svg
# 资源放在 assets/<版本>/ 下。raw.githubusercontent 的 CDN 按路径缓存并忽略
# 查询参数，所以改图必须换目录名（v2 → v3），只改内容会一直发旧图。
ASSETS = f"https://raw.githubusercontent.com/{U}/{U}/main/assets/v2"
HERO = f"{ASSETS}/hero.svg"
FOOTER = f"{ASSETS}/footer.svg"

# ----------------------------------------------------------------- typing ----
TYPE_LINES = [
    "$ AI 应用开发者 / 音乐游戏制作者",
    "$ 音游《溯 Resux》核心开发 · 10minstudio",
    "$ 开源 AI 数字分身 Mirrai — 让 TA 一直都在",
    "$ Linux 内核移植 — 小米平板 8 Pro",
    "$ Building things that sing, and kernels that boot.",
]
def typing_svg(color: str) -> str:
    return (
        "https://readme-typing-svg.demolab.com"
        f"?font=Fira+Code&weight=600&size=26&pause=1500&color={color}"
        "&center=true&vCenter=true&width=700"
        f"&lines={q(';'.join(TYPE_LINES), safe=';')}"
        "&repeat=true"
    )


typing_dark = typing_svg("22D3EE")    # 霓虹青，深色主题
typing_light = typing_svg("7C3AED")   # 紫罗兰，浅色主题下才看得清

# ------------------------------------------------------------------ stats ----
def stats(theme: str) -> str:
    return (
        "https://github-readme-stats-fast.vercel.app/api"
        f"?username={U}&show_icons=true&hide_border=true&theme={theme}"
        "&rank_icon=github&include_all_commits=true&line_height=28"
    )


def langs(theme: str) -> str:
    return (
        "https://github-readme-stats-fast.vercel.app/api/top-langs"
        f"?username={U}&layout=compact&hide_border=true&theme={theme}&langs_count=8"
    )


def streak(theme: str) -> str:
    return (
        "https://streak-stats.demolab.com"
        f"?user={U}&theme={theme}&hide_border=true&border_radius=10&date_format=Y-m-d"
    )


SNAKE = f"https://raw.githubusercontent.com/{U}/{U}/output/github-contribution-grid-snake.svg"
SNAKE_DARK = f"https://raw.githubusercontent.com/{U}/{U}/output/github-contribution-grid-snake-dark.svg"

# ------------------------------------------------------------------ icons ----
# 只留真正在用的技术，别把仓库里出现过的依赖都算进来。
SKILL_ICONS = (
    "https://skillicons.dev/icons?i="
    "typescript,python,cs,linux,unity,react,figma"
)


README = f"""<p align="center">
  <img src="{HERO}" alt="Ch1rpys — AI 应用开发 / 音乐游戏 / Linux 内核移植"/>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{typing_dark}">
    <source media="(prefers-color-scheme: light)" srcset="{typing_light}">
    <img src="{typing_light}" alt="Ch1rpy 的自我介绍" width="660"/>
  </picture>
</p>

<p align="center">
  <a href="https://github.com/{U}?tab=repositories"><img src="https://img.shields.io/github/stars/{U}?label=Stars&style=flat-square&logo=github&color=8B5CF6" alt="Stars"/></a>
  <a href="https://github.com/{U}?tab=followers"><img src="https://img.shields.io/github/followers/{U}?label=Followers&style=flat-square&logo=github&color=8B5CF6" alt="Followers"/></a>
  <a href="https://ch1rpy.com"><img src="https://img.shields.io/badge/Website-Ch1rpy.com-8B5CF6?style=flat-square&logo=googlechrome" alt="Website"/></a>
  <a href="mailto:ch1rpy@163.com"><img src="https://img.shields.io/badge/Mail-ch1rpy%40163.com-8B5CF6?style=flat-square&logo=gmail" alt="Email"/></a>
  <img src="https://komarev.com/ghpvc/?username={U}&label=Views&color=8B5CF6&style=flat-square" alt="Profile views"/>
</p>

---

## 👋 关于我 · About

- 🤖 **AI 应用开发** — 用 TypeScript / Python 把大模型塞进真正能用的产品里
- 🎮 **音乐游戏** — 10minstudio 音游《溯 Resux》核心开发；参与 CyanStars 中文虚拟歌手同人音游企划
- 🐧 **内核移植** — 为小米平板 8 Pro 移植 Linux：主线内核补丁、驱动适配、Ubuntu 桌面集成

<p align="center">
  <img src="{SKILL_ICONS}" alt="Tech Stack"/>
</p>

---

## 🚀 项目 · Projects

```text
❯ mirrai — 开源 AI 数字分身
  上传聊天记录 → 多阶段性格蒸馏 → 7 层结构化人设 + 6 态情感状态机
  12 家 LLM 提供商即插即用 · 数据全部本地存储 · 带一个「毕业机制」
  TypeScript · React · tRPC · Docker · WeChaty
```

**[Mirrai](https://github.com/{U}/Mirrai)** ★1.2k · [Releases](https://github.com/{U}/Mirrai/releases) · [Issues](https://github.com/{U}/Mirrai/issues)

```text
❯ resux / cyanstars — 音乐游戏
  《溯 Resux》本体工程与制谱器（10minstudio）· CyanStars 中文虚拟歌手同人音游企划
  曲谱版本管理 · 剧情编辑器 · Malody 谱面转换 · 本地化工具链
  C# · Unity · Python
```

**[Resux](https://github.com/piae-mentes-project)** · **[CyanStars](https://github.com/IPOL-Studio/CyanStars)** ★52 · **[音游文档](https://ipol-studio.github.io/CyanStars_Docs/)**

```text
❯ linux-sm8750-piano — 内核移植
  小米平板 8 Pro 的 Linux 移植：主线 7.2.y 内核树 + 驱动移植 + Ubuntu 桌面集成
  C · Linux Kernel
```

**[linux-sm8750-piano](https://github.com/{U}/linux-sm8750-piano)** · **[xiaomipad-8pro-mainline](https://github.com/{U}/xiaomipad-8pro-mainline)**

```text
❯ pdfcopy — 顺手造轮子
  PDF 划线取词：跨行跨页不丢字、不带页码和 ???；纯离线、不吃 GPU
  Python · tagged-pdf · ToUnicode
```

**[pdfcopy](https://github.com/{U}/pdfcopy)** ★3 · [在线体验](https://ch1rpy2613--pdfcopy.modal.run)

> 还有一些在做但还没开源的东西 —— AI 运维诊断平台、私有化教育云服务之类。等它们成熟了会陆续放出来。

---

## 📊 数据 · Stats

<table>
<tr>
<td width="52%" valign="top">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{stats('tokyonight')}">
    <source media="(prefers-color-scheme: light)" srcset="{stats('default')}">
    <img alt="Ch1rpys GitHub Stats" src="{stats('tokyonight')}"/>
  </picture>
  <br><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{streak('dark')}">
    <source media="(prefers-color-scheme: light)" srcset="{streak('default')}">
    <img alt="Contribution Streak" src="{streak('dark')}"/>
  </picture>
</td>
<td width="48%" valign="top">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{langs('tokyonight')}">
    <source media="(prefers-color-scheme: light)" srcset="{langs('default')}">
    <img alt="Top Languages" src="{langs('tokyonight')}"/>
  </picture>
  <br><br>
  <b>组织 · Organizations</b><br>
  <a href="https://github.com/piae-mentes-project">piae-mentes-project</a> — 音游《溯 Resux》<br>
  <a href="https://github.com/IPOL-Studio">IPOL-Studio</a> — CyanStars 企划<br>
  <a href="https://github.com/YunYingWeb">YunYingWeb</a> — 运营中台
</td>
</tr>
</table>

---

## 🐍 贡献 · Contributions

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{SNAKE_DARK}">
    <source media="(prefers-color-scheme: light)" srcset="{SNAKE}">
    <img alt="Contribution Snake" src="{SNAKE}"/>
  </picture>
</div>

---

## 📬 联系 · Contact

```text
❯ contact
  mail    ch1rpy@163.com
  web     ch1rpy.com
  docs    ipol-studio.github.io/CyanStars_Docs
```

**[邮件](mailto:ch1rpy@163.com)** · **[博客](https://ch1rpy.com)** · **[CyanStars 文档](https://ipol-studio.github.io/CyanStars_Docs/)**

技术讨论、谱面合作、内核移植互助、或者单纯来打个招呼都行。

---

<p align="center">
  <img src="{FOOTER}" alt="Thanks for visiting"/>
</p>

<p align="center">
  Made with ☕ and 🎹 by <a href="https://github.com/{U}">Ch1rpys</a>
</p>
"""

if __name__ == "__main__":
    import pathlib
    import re

    # Guard: a literal comma in a <source srcset> makes GitHub truncate the URL
    # at the comma (it parses srcset as a comma-separated candidate list).
    for srcset in re.findall(r"<source[^>]*srcset=\"([^\"]+)\"", README):
        if "," in srcset:
            raise SystemExit(f"literal comma in srcset, GitHub will truncate it:\n{srcset}")

    out = pathlib.Path(__file__).with_name("README.md")
    out.write_text(README, encoding="utf-8")
    print(f"wrote {out} ({len(README)} chars)")
