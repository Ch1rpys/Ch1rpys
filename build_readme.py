#!/usr/bin/env python3
"""Generate README.md for the Ch1rpys GitHub profile repository.

Keeping the generator around makes it easy to tweak wording and re-render
without hand-escaping URL query strings full of Chinese characters.
"""
from urllib.parse import quote

U = "Ch1rpys"


def q(s: str, safe: str = "") -> str:
    return quote(s, safe=safe)


# ---------------------------------------------------------------- capsule ----
def capsule(color: str, text_color: str, desc: str, text: str = "Ch1rpys",
            height: int = 240, size: int = 64, kind: str = "wave") -> str:
    # GitHub parses a <source srcset> as a comma-separated list of image
    # candidates, so a literal comma anywhere in the query string truncates the
    # URL at that point. Percent-encode every comma (and colon) to keep the
    # gradient intact.
    stops = "%2C".join(q(f"{k}:{v}") for k, v in
                       (("0", color[0]), ("50", color[1]), ("100", color[2])))
    return (
        "https://capsule-render.vercel.app/api"
        f"?type={kind}"
        f"&color={stops}"
        f"&height={height}"
        f"&text={q(text)}"
        f"&fontSize={size}"
        f"&fontColor={text_color}"
        "&animation=fadeIn"
        f"&desc={q(desc)}"
        "&descAlign=center"
        "&descSize=18"
    )


HERO_DARK = capsule(("5B21B6", "4338CA", "0E7490"), "ffffff",
                    "AI · 音游 · 内核移植")
HERO_LIGHT = capsule(("C4B5FD", "93C5FD", "67E8F9"), "312E81",
                     "AI · 音游 · 内核移植")
FOOTER = ("https://capsule-render.vercel.app/api?type=rect"
          "&color=" + "%2C".join(q(f"{k}:{v}") for k, v in
                                (("0", "5B21B6"), ("50", "4338CA"), ("100", "0E7490")))
          + "&height=90&text=Thanks+for+visiting"
          "&fontSize=28&fontColor=ffffff&animation=fadeIn")

# ----------------------------------------------------------------- typing ----
TYPE_LINES = [
    "AI 应用开发者 / 音乐游戏制作者",
    "音游《溯 Resux》核心开发 · 10minstudio",
    "开源 AI 数字分身 Mirrai — 让 TA 一直都在",
    "Linux 内核移植 — 小米平板 8 Pro",
    "Building things that sing, and kernels that boot.",
]
typing = (
    "https://readme-typing-svg.demolab.com"
    "?font=Fira+Code&weight=600&size=26&pause=1500&color=8B5CF6"
    "&center=true&vCenter=true&width=700"
    f"&lines={q(';'.join(TYPE_LINES), safe=';')}"
    "&repeat=true"
)

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
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{HERO_DARK}">
    <source media="(prefers-color-scheme: light)" srcset="{HERO_LIGHT}">
    <img alt="Ch1rpys" src="{HERO_LIGHT}">
  </picture>
</p>

<p align="center">
  <img src="{typing}" alt="Ch1rpy 的自我介绍" width="700"/>
</p>

<p align="center">
  <a href="https://github.com/{U}?tab=followers"><img src="https://img.shields.io/github/followers/{U}?label=Followers&style=for-the-badge&logo=github&color=06B6D4" alt="Followers"/></a>
  <a href="https://github.com/{U}?tab=repositories"><img src="https://img.shields.io/github/stars/{U}?label=Stars&style=for-the-badge&logo=github&color=8B5CF6" alt="Stars"/></a>
  <a href="https://ch1rpy.com"><img src="https://img.shields.io/badge/Website-Ch1rpy.com-6366F1?style=for-the-badge&logo=googlechrome" alt="Website"/></a>
  <a href="mailto:ch1rpy@163.com"><img src="https://img.shields.io/badge/Email-ch1rpy%40163.com-0EA5E9?style=for-the-badge&logo=gmail" alt="Email"/></a>
  <img src="https://komarev.com/ghpvc/?username={U}&label=Profile%20Views&color=8B5CF6&style=for-the-badge" alt="Profile views"/>
  <img src="https://img.shields.io/badge/Open%20to%20Collaboration-22C55E?style=for-the-badge" alt="Open to collaboration"/>
</p>

---

## 👋 关于我 · About Me

- 🤖 **AI 应用开发** — 用 TypeScript / Python 把大模型塞进真正能用的产品里；主力项目是开源 AI 数字分身 [Mirrai](https://github.com/{U}/Mirrai)
- 🎮 **音乐游戏** — 10minstudio 音游《溯 [Resux](https://github.com/piae-mentes-project)》核心开发，负责本体工程、制谱器与剧情编辑器；同时参与 [CyanStars](https://github.com/IPOL-Studio/CyanStars) 中文虚拟歌手同人音游企划
- 🐧 **内核移植** — 为小米平板 8 Pro 移植 Linux：主线内核补丁、驱动适配、Ubuntu 桌面集成
- 🛠️ **顺手造轮子** — [pdfcopy](https://github.com/{U}/pdfcopy)，专治 PDF 划线取词断行、混入页码和乱码
- 🌱 **正在学** — Agent 架构与推理优化、Linux 子系统、音游手感 / 节奏判定算法

> 「不在身边的时候，TA 还在这里。」 —— 这是我给 Mirrai 起的 slogan，也是这个项目的起点。

---

## 🛠️ 技术栈 · Tech Stack

<p align="center">
  <img src="{SKILL_ICONS}" alt="Tech Stack"/>
</p>

---

## 📊 数据统计 · Stats

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{stats('tokyonight')}">
    <source media="(prefers-color-scheme: light)" srcset="{stats('default')}">
    <img alt="Ch1rpys GitHub Stats" src="{stats('tokyonight')}"/>
  </picture>
  <br><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{langs('tokyonight')}">
    <source media="(prefers-color-scheme: light)" srcset="{langs('default')}">
    <img alt="Top Languages" src="{langs('tokyonight')}"/>
  </picture>
  <br><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{streak('dark')}">
    <source media="(prefers-color-scheme: light)" srcset="{streak('default')}">
    <img alt="Contribution Streak" src="{streak('dark')}"/>
  </picture>
</div>

---

## 🚀 代表项目 · Featured Projects

| 项目 | 简介 | 技术 |
| :--- | :--- | :--- |
| [**Mirrai**](https://github.com/{U}/Mirrai) · ★1.2k | 开源 AI 数字分身：上传聊天记录 → 多阶段性格蒸馏 → 7 层结构化人设 + 6 态情感状态机；12 家 LLM 提供商即插即用，数据全部本地存储，带一个别人都没有的「毕业机制」 | `TypeScript` `React` `tRPC` `Docker` `WeChaty` |
| [**pdfcopy**](https://github.com/{U}/pdfcopy) · ★3 | PDF 划线取词：跨行跨页不丢字、不带页码和 ???；纯离线、不吃 GPU、MIT 开源 | `Python` `tagged-pdf` `ToUnicode` |
| [**CyanStars**](https://github.com/IPOL-Studio/CyanStars) · ★52 | 中文虚拟歌手同人音游企划：曲谱版本管理、多媒体资源库、剧情编辑器、Malody 谱面转换 | `C#` `Unity` `Python` |
| [**Resux / 溯**](https://github.com/piae-mentes-project/piae-mentes-core) | 音游《溯》的本体工程，另有[制谱器](https://github.com/piae-mentes-project/Resux-Map-Designer)、剧情编辑器与本地化工具链 | `C#` `Unity` `Python` |
| [**linux-sm8750-piano**](https://github.com/{U}/linux-sm8750-piano) | 小米平板 8 Pro 的 Linux 移植：主线 7.2.y 内核树 + 驱动移植 + Ubuntu 桌面集成 | `C` `Linux Kernel` |

> 还有一些在做但还没开源的东西 —— AI 运维诊断平台、私有化教育云服务之类。等它们成熟了会陆续放出来。

---

## 🏢 参与的组织 · Organizations

| 组织 | 说明 |
| :--- | :--- |
| [piae-mentes-project](https://github.com/piae-mentes-project) | 10minstudio — 音游《溯 Resux》本体、制谱器与配套工具链 |
| [IPOL-Studio](https://github.com/IPOL-Studio) | CyanStars 中文虚拟歌手同人音游企划 |
| [YunYingWeb](https://github.com/YunYingWeb) | 运营中台 · ONEDUSH 制谱器 |

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

| | |
| :--- | :--- |
| 📧 **Email** | [ch1rpy@163.com](mailto:ch1rpy@163.com) |
| 🌐 **Blog** | [Ch1rpy.com](https://ch1rpy.com) |
| 🎮 **音游文档** | [CyanStars Docs](https://ipol-studio.github.io/CyanStars_Docs/) |
| 💬 **欢迎交流** | 技术讨论、谱面合作、内核移植互助、或者单纯来打个招呼都行 |

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
