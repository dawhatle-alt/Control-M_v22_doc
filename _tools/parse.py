import re, html, json, pickle, collections

xml = open('/home/claude/full.xml', encoding='utf-8', errors='replace').read()
fonts = {}
for m in re.finditer(r'<fontspec id="(\d+)" size="(\d+)" family="([^"]*)" color="(#[0-9a-f]+)"', xml):
    fam = m.group(3).split('+')[-1]
    kind = 'code' if ('Consolas' in fam or 'Courier' in fam) else ('bullet' if 'Wingdings' in fam else 'text')
    fonts[m.group(1)] = (int(m.group(2)), m.group(4), kind)

pages = {}
for pm in re.finditer(r'<page number="(\d+)"[^>]*>(.*?)</page>', xml, re.S):
    n = int(pm.group(1))
    items = []
    for tm in re.finditer(r'<text top="(\d+)" left="(\d+)" width="(\d+)" height="(\d+)" font="(\d+)">(.*?)</text>', pm.group(2), re.S):
        raw = tm.group(6)
        href = None
        am = re.search(r'<a href="([^"]*)">', raw)
        if am:
            h = am.group(1)
            pm2 = re.match(r'full\.html#(\d+)', h)
            href = int(pm2.group(1)) if pm2 else 'ext'
        text = html.unescape(re.sub(r'<[^>]+>', '', raw)).replace('\xa0', ' ')
        size, color, kind = fonts[tm.group(5)]
        items.append(dict(top=int(tm.group(1)), left=int(tm.group(2)), width=int(tm.group(3)),
                          height=int(tm.group(4)), size=size, color=color, kind=kind, text=text, href=href))
    pages[n] = items

# --- locate TOC headings in page items ---
toc = json.load(open('/home/claude/toc.json'))
def norm(s): return re.sub(r'\s+', ' ', s).strip().lower()

located = []
miss = []
for idx, (lvl, title, pg) in enumerate(toc):
    want = 41 if lvl == 0 else 36
    items = [it for it in pages.get(pg, []) if it['size'] in (41, 36) and it['top'] > 100]
    items.sort(key=lambda it: it['top'])
    found = None
    # try single and multi-line concatenations
    for i in range(len(items)):
        acc = ''
        for j in range(i, min(i + 4, len(items))):
            if items[j]['size'] != items[i]['size']:
                break
            acc = (acc + ' ' + items[j]['text']).strip()
            if norm(acc) == norm(title):
                found = (items[i]['top'], items[i]['size'], j - i + 1)
                break
        if found: break
    if found is None:
        # fallback: any heading on that page with matching prefix
        for it in items:
            if norm(title).startswith(norm(it['text'])[:30]) and len(it['text']) > 8:
                found = (it['top'], it['size'], 1); break
    if found is None:
        miss.append((idx, title, pg))
        found = (0, want, 0)
    located.append(dict(idx=idx, level=lvl, title=title, page=pg, top=found[0], size=found[1], nlines=found[2]))

print('toc', len(toc), 'missed', len(miss))
for m in miss[:20]: print(m)
pickle.dump(dict(pages=pages, toc=located), open('/home/claude/build/parsed.pkl', 'wb'))
