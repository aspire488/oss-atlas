#!/usr/bin/env python3
"""Generate self-contained SVG dashboard cards for OSS Atlas."""
from __future__ import annotations
import json, os, urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "contributions.json"
OUT = ROOT / "assets" / "dashboard"
OUT.mkdir(parents=True, exist_ok=True)

BG="#0d1117"; PANEL="#161b22"; TEXT="#f0f6fc"; MUTED="#8b949e"
BLUE="#70a5fd"; GREEN="#3fb950"; ORANGE="#d29922"; RED="#f85149"; PURPLE="#bc8cff"

def load():
    return json.loads(DATA.read_text(encoding="utf-8"))

def svg(title, subtitle, body, width=1200, height=520):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" rx="24" fill="{BG}"/>
<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="24" fill="none" stroke="#30363d"/>
<text x="48" y="62" fill="{TEXT}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="30" font-weight="700">{escape(title)}</text>
<text x="48" y="94" fill="{MUTED}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="16">{escape(subtitle)}</text>
{body}
</svg>'''

def card(x,y,w,h,label,value,accent=BLUE):
    return f'''<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{PANEL}" stroke="#30363d"/>
<rect x="{x}" y="{y}" width="5" height="{h}" rx="3" fill="{accent}"/>
<text x="{x+24}" y="{y+36}" fill="{MUTED}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="14">{escape(label)}</text>
<text x="{x+24}" y="{y+82}" fill="{TEXT}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="34" font-weight="700">{escape(str(value))}</text>'''

def write(name,text):
    (OUT/name).write_text(text,encoding="utf-8")

def action_health():
    token=os.getenv("GITHUB_TOKEN")
    if not token: return []
    req=urllib.request.Request("https://api.github.com/repos/aspire488/oss-atlas/actions/runs?per_page=12",
        headers={"Authorization":f"Bearer {token}","Accept":"application/vnd.github+json","User-Agent":"oss-atlas-dashboard"})
    try:
        with urllib.request.urlopen(req,timeout=10) as r: return json.load(r).get("workflow_runs",[])
    except Exception: return []

d=load(); items=d["contributions"]; counts=Counter(x["status"] for x in items)
total=len(items); merged=counts["merged"]; open_up=counts["open_upstream"]; open_fork=counts["open_fork"]; closed=counts["closed"]
repos=Counter(x["repository"] for x in items); now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

write("overview.svg",svg("OSS Atlas · Engineering Overview",
 f"External OSS work · observed {d.get('observed_at','unknown')} · generated {now}",
 card(48,132,250,125,"External PRs",total)+card(318,132,250,125,"Merged upstream",merged,GREEN)+
 card(588,132,250,125,"Open upstream",open_up,BLUE)+card(858,132,250,125,"Fork-side",open_fork,PURPLE)+
 card(48,285,250,125,"Closed",closed,ORANGE)+card(318,285,250,125,"Repositories",len(repos),BLUE)+
 card(588,285,250,125,"Upstream share",f"{merged/total*100:.0f}%" if total else "0%",GREEN)+
 card(858,285,250,125,"Evidence model","4-stage",PURPLE)+
 f'<text x="48" y="468" fill="{MUTED}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15">Observed → Implemented → Verified → Documented</text>'))

labels=[("Merged upstream",merged,GREEN),("Open upstream",open_up,BLUE),("Open fork-side",open_fork,PURPLE),("Closed",closed,ORANGE)]
barmax=max([v for _,v,_ in labels]+[1]); bars=[]
for i,(label,value,color) in enumerate(labels):
    y=145+i*78; bw=760*value/barmax
    bars.append(f'<text x="48" y="{y+18}" fill="{TEXT}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15">{escape(label)}</text><rect x="48" y="{y+30}" width="760" height="22" rx="11" fill="#21262d"/><rect x="48" y="{y+30}" width="{bw:.1f}" height="22" rx="11" fill="{color}"/><text x="835" y="{y+48}" fill="{TEXT}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="18" font-weight="700">{value}</text>')
write("status.svg",svg("OSS Atlas · Contribution State",f"{total} tracked external PRs","".join(bars),1000,500))

top=repos.most_common(8); maxv=max([v for _,v in top]+[1]); repo_bars=[]
for i,(repo,value) in enumerate(top):
    y=130+i*43; bw=700*value/maxv
    repo_bars.append(f'<text x="48" y="{y+18}" fill="{TEXT}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="14">{escape(repo[:32])}</text><rect x="290" y="{y+5}" width="700" height="20" rx="10" fill="#21262d"/><rect x="290" y="{y+5}" width="{bw:.1f}" height="20" rx="10" fill="{BLUE}"/><text x="1010" y="{y+21}" fill="{TEXT}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15">{value}</text>')
write("repositories.svg",svg("OSS Atlas · Repository Concentration","Repositories with the most tracked contribution records","".join(repo_bars),1100,500))

runs=action_health(); success=sum(1 for r in runs if r.get("conclusion")=="success"); failure=sum(1 for r in runs if r.get("conclusion")=="failure"); other=len(runs)-success-failure
write("actions.svg",svg("OSS Atlas · GitHub Actions Health","Recent workflow-run outcomes · refreshed automatically",
 card(48,145,300,150,"Recent runs",len(runs),BLUE)+card(368,145,300,150,"Successful",success,GREEN)+
 card(688,145,300,150,"Failed",failure,RED if failure else GREEN)+
 f'<text x="48" y="355" fill="{MUTED}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15">Other / in progress: {other}</text>'+
 f'<text x="48" y="395" fill="{MUTED}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15">Workflows: Atlas CI · OSS Atlas Audit · Dashboard</text>',1040,470))
