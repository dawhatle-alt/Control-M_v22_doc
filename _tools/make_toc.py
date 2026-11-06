"""Parse the printed table of contents (pdftotext -bbox-layout output) into toc.json = [[indent, title, page], ...]"""
import re, html, json, sys
src = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/toc.html'
txt = open(src).read()
entries = []
for pm in re.finditer(r'<page .*?</page>', txt, re.S):
    lines = []
    for lm in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)"[^>]*>(.*?)</line>', pm.group(0), re.S):
        x = float(lm.group(1)); y = round(float(lm.group(2)), 1)
        words = [html.unescape(w) for w in re.findall(r'<word[^>]*>(.*?)</word>', lm.group(3))]
        lines.append((x, y, ' '.join(words)))
    nums = {y: int(t) for x, y, t in lines if x > 500 and re.fullmatch(r'\d+', t)}
    for x, y, t in [(x, y, t) for x, y, t in lines if x < 500 and t not in ('Control-M Self-Hosted', 'Table of Contents')]:
        cand = [(abs(y - yy), p) for yy, p in nums.items() if abs(y - yy) < 3]
        entries.append([round((x - 58.5) / 12), t, min(cand)[1] if cand else None])
# repair wrapped titles whose page number got glued to the text
fixed, i = [], 0
while i < len(entries):
    lvl, t, p = entries[i]
    m = re.match(r'^(.*?)(\d{3,4})$', t)
    if p is None and m and i + 1 < len(entries) and entries[i + 1][2] is None:
        fixed.append([lvl, m.group(1).strip(), int(m.group(2))]); i += 2; continue
    fixed.append([lvl, t, p]); i += 1
json.dump(fixed, open('toc.json', 'w'))
print(len(fixed), 'entries')
