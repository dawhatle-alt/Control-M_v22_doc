import re, os, pickle, json, collections, shutil

D = pickle.load(open('/home/claude/build/parsed.pkl', 'rb'))
pages, toc = D['pages'], D['toc']
OUT = '/home/claude/vault/Control-M-User-Guide-Vault'
VERSION = '9.0.27'
SOURCE = 'Control-M User Guide 9.0.27 (Self-Hosted), September 2026'

# ---------------------------------------------------------------- folders
FOLDERS = [  # (start_page, folder)
    (73, '10-Getting-Started'),
    (129, '20-Planning'),
    (174, '21-Job-Types'),
    (826, '22-Scheduling-and-Definitions'),
    (1055, '23-Planning-Utilities'),
    (1111, '30-Monitoring'),
    (1239, '31-Monitoring-Utilities'),
    (1356, '32-Control-M-AI'),
    (1375, '40-Administration'),
    (1631, '41-Reports'),
    (1651, '42-Platform-Configuration'),
    (1899, '43-System-Configuration'),
    (2036, '44-EM-Utilities'),
    (2168, '45-Server-Utilities'),
    (2377, '46-Automation-API-Admin'),
    (2424, '50-Messages'),
    (2949, '60-Plug-ins-and-Connection-Profiles'),
    (3279, '61-Application-Integrator'),
    (3381, '62-Managed-File-Transfer'),
    (3671, '63-Plug-in-Configuration'),
    (3859, '64-Integrations'),
    (4272, '65-Migration-Tools'),
    (4316, '70-Glossary'),
]
def folder_for(page):
    f = FOLDERS[0][1]
    for p, name in FOLDERS:
        if page >= p: f = name
    return f
def folder_short(f): return re.sub(r'^\d+-', '', f)

SPLIT_PAGES = 40  # level-0 notes longer than this (with children) are split into a sub-folder

# ---------------------------------------------------------------- naming
def slug(title):
    s = title.replace('/', '-').replace('\\', '-')
    s = re.sub(r'[:*?"<>|#\[\]^]', '', s)
    s = re.sub(r'[\s,]+', '-', s.strip())
    s = re.sub(r'-{2,}', '-', s).strip('-')
    return s[:120]

# ---------------------------------------------------------------- cut points
# each toc entry = start of a segment at (page, top). Segment ends at next entry.
cuts = [(t['page'], t['top']) for t in toc]
def seg_items(i):
    p0, t0 = cuts[i]
    p1, t1 = cuts[i + 1] if i + 1 < len(cuts) else (4326, 0)
    out = []
    for p in range(p0, min(p1, 4325) + 1):
        its = clean_page(p)
        for it in its:
            if p == p0 and it['top'] < t0: continue
            if p == p1 and it['top'] >= t1: continue
            out.append((p, it))
    return out

_clean_cache = {}
def clean_page(p):
    if p in _clean_cache: return _clean_cache[p]
    its = [it for it in pages.get(p, []) if it['text'].strip()]
    its = [it for it in its if not (it['top'] < 100)]                      # running header
    its = [it for it in its if not (it['size'] == 14 and it['top'] > 1100)]  # page number
    its = [it for it in its if not (it['size'] >= 27 and it['size'] not in (32, 36, 41))]  # chapter pages
    its.sort(key=lambda it: (it['top'], it['left']))
    # footnote definitions: small numeric marker at left margin, drop it and everything below
    cut = None
    for it in its:
        if it['size'] in (15, 16) and it['text'].strip().isdigit() and it['left'] <= 100 and it['top'] > 600:
            cut = it['top']; break
    if cut is not None: its = [it for it in its if it['top'] < cut]
    its = [it for it in its if not (it['size'] in (15, 16) and it['text'].strip().isdigit())]  # superscripts
    _clean_cache[p] = its
    return its

# ---------------------------------------------------------------- link targets
# page -> (note_name, heading) resolved after note assembly; collect first
def esc(t):
    t = t.replace('|', '\\|').replace('[[', '\\[\\[')
    t = re.sub(r'<(?=[A-Za-z_/])', '\\<', t)
    return t

LINKCOL = ('#00597e',)
def is_link(it): return isinstance(it['href'], int) and it['color'] in LINKCOL and re.search(r'[A-Za-z0-9]', it['text'])
def wikilink(tgt, text):
    text = text.strip()
    base = tgt.split('#')[0]
    if text == base or text == base.replace('-', ' '): return f'[[{tgt}]]'
    return f'[[{tgt}|{esc(text)}]]'
def _n(t): return re.sub(r'[^a-z0-9]', '', t.lower())
def resolve(page, text):
    cands = page_entries.get(page, [])
    nt = _n(text)
    for k in cands:
        if _n(toc[k]['title']) == nt and nt:
            nm, hd = entry_note[k]
            return nm if hd is None else f'{nm}#{hd}'
    for (hp, htop, htxt, hentry) in subheads.get(page, []):
        if _n(htxt) == nt and nt:
            nm, hd = entry_note[hentry]
            return f'{nm}#{htxt}'
    return linkmap.get(page)
def item_text(it, linkmap):
    t = it['text'].strip()
    if is_link(it):
        tgt = resolve(it['href'], t)
        if tgt: return wikilink(tgt, t)
    return esc(t)
def merge_links(items):
    """merge consecutive link items with the same href into one pseudo-item"""
    out = []
    for it in items:
        if out and is_link(it) and is_link(out[-1]) and out[-1]['href'] == it['href'] and it['kind'] == out[-1]['kind']:
            m = dict(out[-1]); m['text'] = m['text'].rstrip() + ' ' + it['text'].strip()
            m['width'] = it['left'] + it['width'] - m['left']
            out[-1] = m
        else:
            out.append(it)
    return out

def group_lines(items):
    """items: list of (page,item). Group into lines by (page, top±4). Returns list of dict."""
    lines = []
    for p, it in items:
        if lines and lines[-1]['page'] == p and abs(lines[-1]['top'] - it['top']) <= 4:
            lines[-1]['items'].append(it)
        else:
            lines.append(dict(page=p, top=it['top'], items=[it]))
    for ln in lines:
        ln['items'].sort(key=lambda x: x['left'])
        ln['items'] = merge_links(ln['items'])
        ln['left'] = ln['items'][0]['left']
        ln['size'] = max(ln['items'], key=lambda x: x['width'])['size']
        ln['kinds'] = {x['kind'] for x in ln['items']}
    return lines

def line_text(ln, linkmap):
    parts = []
    for it in ln['items']:
        if it['kind'] == 'bullet': continue
        parts.append(item_text(it, linkmap))
    t = ' '.join(parts)
    t = re.sub(r'\s+([.,;:)])', r'\1', t)
    t = re.sub(r'\(\s+', '(', t)
    return t.strip()

def code_line(ln):
    # rebuild spacing from x positions (char width ~ 10px at size 18)
    out = ''
    base = ln['items'][0]['left']
    x = base
    for it in ln['items']:
        gap = it['left'] - x
        if out == '':
            out = ' ' * max(0, int((it['left'] - 88) / 10.5))
        elif gap > 4:
            out += ' ' * max(1, int(gap / 10.5))
        out += it['text']
        x = it['left'] + it['width']
    return out.rstrip()

def render(items, linkmap, skip=None):
    """Render a segment's items (list of (page,item)) into markdown lines."""
    lines = group_lines(items)
    md = []
    i = 0
    n = len(lines)
    para = []         # accumulating body lines
    para_meta = None  # (page, top, left)
    def flush():
        nonlocal para, para_meta
        if para:
            md.append(' '.join(para)); md.append('')
        para = []; para_meta = None

    table = None      # dict(cols=[lefts], rows=[], header=[...], cur=None, maxtop)
    def flush_table():
        nonlocal table
        if table:
            if table['cur']: table['rows'].append(table['cur'])
            hdr = table['header']
            md.append('| ' + ' | '.join(hdr) + ' |')
            md.append('|' + '---|' * len(hdr))
            for row in table['rows']:
                def celltxt(parts):
                    o = []
                    for pt in parts:
                        if isinstance(pt, tuple): o.append('`' + ' '.join(pt[1]) + '`')
                        else: o.append(pt)
                    return ' '.join(o).replace(' <br>', '<br>')
                cells = [celltxt(row.get(c, [])) for c in range(len(hdr))]
                if any(c.strip() for c in cells):
                    md.append('| ' + ' | '.join(cells) + ' |')
            md.append('')
        table = None

    code = []
    def flush_code():
        nonlocal code
        if code:
            md.append('```'); md.extend(code); md.append('```'); md.append('')
        code = []

    prev_heading_top = None; prev_heading_page = None
    quote_left = None  # when inside a Note callout, lines with left >= this are quoted
    prev = None
    while i < n:
        ln = lines[i]
        sz = ln['size']; txt = line_text(ln, linkmap)
        is_code = 'code' in ln['kinds'] and all(x['kind'] in ('code', 'bullet') for x in ln['items'])
        is_bullet = 'bullet' in ln['kinds']
        first = ln['items'][0]
        # ---- table handling ----
        hdr_items = [x for x in ln['items'] if x['size'] == 20 and x['kind'] == 'text']
        if len(hdr_items) >= 2 and len(hdr_items) == len([x for x in ln['items'] if x['kind'] == 'text']):
            hdr = [esc(x['text'].strip()) for x in hdr_items]
            cols = [x['left'] for x in hdr_items]
            flush(); flush_code()
            if table and table['header'] == hdr:
                pass  # continuation on a new page: keep going
            else:
                flush_table()
                table = dict(cols=cols, header=hdr, rows=[], cur=None, maxtop=ln['top'], page=ln['page'])
            table['cols'] = cols; table['maxtop'] = ln['top']; table['page'] = ln['page']
            i += 1; continue
        if table:
            in_table = all(x['size'] in (18, 20, 16, 15, 12, 13, 9, 8, 11) for x in ln['items']) and not (sz >= 23)
            if in_table:
                newpage = ln['page'] != table['page']
                gap = ln['top'] - table['maxtop'] if not newpage else 999
                def colof(x):
                    c = 0
                    for k, cl in enumerate(table['cols']):
                        if x['left'] >= cl - 12: c = k
                    return c
                textitems = [x for x in ln['items'] if x['kind'] != 'bullet']
                has_c0 = any(colof(x) == 0 for x in textitems)
                if table['cur'] is None or newpage or (has_c0 and gap > 44):
                    if table['cur']: table['rows'].append(table['cur'])
                    table['cur'] = {}
                    table['celltop'] = {}
                # assign items to columns
                bullets = sorted(x['left'] for x in ln['items'] if x['kind'] == 'bullet')
                marked = set()
                for bl in bullets:
                    nxt = [x for x in textitems if x['left'] > bl]
                    if nxt: marked.add(id(min(nxt, key=lambda x: x['left'])))
                codebuf = None
                for x in textitems:
                    c = colof(x)
                    cell = table['cur'].setdefault(c, [])
                    if x['kind'] == 'code':
                        if codebuf and codebuf[0] == c:
                            codebuf[1].append(x['text'].strip()); continue
                        codebuf = (c, [x['text'].strip()]); cell.append(codebuf)
                        continue
                    t = item_text(x, linkmap)
                    prevtop = table['celltop'].get(c)
                    if prevtop is not None and ln['top'] - prevtop > 34: t = '<br>' + t
                    if id(x) in marked: t = '• ' + t
                    cell.append(t)
                for c in list(table['cur'].keys()):
                    for x in textitems:
                        if colof(x) == c: table['celltop'][c] = ln['top']
                if is_bullet:
                    # mark bullet within cell text
                    for x in ln['items']:
                        if x['kind'] == 'bullet': pass
                table['maxtop'] = ln['top']; table['page'] = ln['page']
                i += 1; continue
            else:
                flush_table()
        # ---- code ----
        if is_code:
            flush()
            code.append(code_line(ln)); i += 1; continue
        else:
            flush_code()
        # ---- headings ----
        if sz == 41 or sz == 36:
            flush()
            if skip and ln['page'] == skip[0] and skip[1] <= ln['top'] <= skip[1] + 50 * max(1, skip[2]):
                i += 1; continue
            # wrapped heading continuation: append to previous heading
            if md and len(md) >= 2 and md[-2].startswith('## ') and md[-1] == '' and prev_heading_top is not None and ln['top'] - prev_heading_top < 60 and ln['page'] == prev_heading_page:
                md[-2] += ' ' + txt; prev_heading_top = ln['top']; i += 1; continue
            md.append('## ' + txt); md.append('')
            prev_heading_top = ln['top']; prev_heading_page = ln['page']
            quote_left = None; i += 1; continue
        if sz in (23, 32, 27) and first['kind'] == 'text':
            flush()
            md.append('### ' + txt); md.append(''); quote_left = None; i += 1; continue
        if sz == 20 and len(ln['items']) == 1:
            flush(); md.append('**' + txt + '**'); md.append(''); i += 1; continue
        if sz == 18 and first['color'] == '#1a97c7':
            flush(); md.append('> [!' + ('warning' if 'warn' in txt.lower() else 'note') + '] ' + txt)
            quote_left = 140; i += 1; continue
        if sz == 21:  # glossary term
            flush(); md.append('### ' + txt); md.append(''); i += 1; continue
        # ---- body ----
        if quote_left and ln['left'] < quote_left:
            flush(); quote_left = None
        prefix = ''
        if is_bullet:
            b = [x for x in ln['items'] if x['kind'] == 'bullet'][0]
            prefix = ('  - ' if b['size'] <= 9 else '- ')
        if quote_left: prefix = '> ' + prefix
        newpara = (para_meta is None or is_bullet or re.match(r'^\d+\.\s', txt)
                   or ln['page'] != para_meta[0] and ln['top'] < 200 and False
                   or (ln['page'] == para_meta[0] and ln['top'] - para_meta[1] > 36)
                   or abs(ln['left'] - para_meta[2]) > 40)
        if newpara:
            flush()
            para.append(prefix + txt)
        else:
            para.append(txt)
        para_meta = (ln['page'], ln['top'], ln['left'])
        i += 1
    flush(); flush_code(); flush_table()
    # tidy
    out = []
    for l in md:
        if out and out[-1] == '' and l == '': continue
        out.append(l)
    tidy = []
    for k, l in enumerate(out):
        if l == '' and k + 1 < len(out) and tidy and re.match(r'^\s*(- |\d+\. )', out[k + 1]) and re.match(r'^\s*(- |\d+\. |> )', tidy[-1]):
            continue
        tidy.append(l)
    return tidy

# ---------------------------------------------------------------- note assembly
# Level-0 entries -> notes; children -> ## sections. Big ones split.
notes = []  # dict(name, title, folder, path, entries=[toc idx...], parent=None, page0, page1)
names_used = collections.Counter()
def uniq(base, folder):
    if names_used[base] == 0:
        names_used[base] += 1; return base
    alt = f'{base}-{folder_short(folder)}'
    if names_used[alt] == 0:
        names_used[alt] += 1; return alt
    names_used[base] += 1
    return f'{base}-{names_used[base]}'

l0 = [k for k, t in enumerate(toc) if t['level'] == 0]
for a, k in enumerate(l0):
    k_end = l0[a + 1] if a + 1 < len(l0) else len(toc)
    t = toc[k]
    p0 = t['page']; p1 = toc[k_end]['page'] if k_end < len(toc) else 4326
    children = list(range(k + 1, k_end))
    folder = folder_for(p0)
    span = p1 - p0
    if span > SPLIT_PAGES and children:
        sub = folder + '/' + slug(t['title'])
        name = uniq(slug(t['title']), folder)
        parent = dict(name=name, title=t['title'], folder=sub, entries=[k], children_notes=[], page0=p0,
                      page1=toc[children[0]]['page'], hub=True)
        notes.append(parent)
        for c in children:
            ct = toc[c]
            cn = uniq(slug(ct['title']), folder)
            cp1 = toc[c + 1]['page'] if c + 1 < len(toc) else 4326
            notes.append(dict(name=cn, title=ct['title'], folder=sub, entries=[c], page0=ct['page'], page1=cp1,
                              parent=name, hub=False))
            parent['children_notes'].append(cn)
    else:
        name = uniq(slug(t['title']), folder)
        notes.append(dict(name=name, title=t['title'], folder=folder, entries=[k] + children, page0=p0, page1=p1, hub=False))

# toc idx -> (note name, heading or None)
entry_note = {}
for nt in notes:
    for j, e in enumerate(nt['entries']):
        entry_note[e] = (nt['name'], None if j == 0 else toc[e]['title'])

# page -> link target: last toc entry starting at or before that page (top-most on that page = first)
starts = sorted(range(len(toc)), key=lambda k: (toc[k]['page'], toc[k]['top']))
page_first = {}
page_entries = collections.defaultdict(list)
for k in starts:
    page_first.setdefault(toc[k]['page'], k)
    page_entries[toc[k]['page']].append(k)
# sub-headings (size 23/32) index for finer link targets
subheads = collections.defaultdict(list)
cut_sorted = sorted(range(len(toc)), key=lambda k: (toc[k]['page'], toc[k]['top']))
import bisect
cut_keys = [(toc[k]['page'], toc[k]['top']) for k in cut_sorted]
for p in range(73, 4326):
    for it in clean_page(p):
        if it['size'] in (23, 32) and it['kind'] == 'text' and it['color'] == '#00597e':
            pos = bisect.bisect_right(cut_keys, (p, it['top'])) - 1
            if pos >= 0: subheads[p].append((p, it['top'], it['text'].strip(), cut_sorted[pos]))
linkmap = {}
last = None
for p in range(73, 4326):
    if p in page_first: last = page_first[p]
    if last is None: continue
    nm, hd = entry_note[last]
    linkmap[p] = nm if hd is None else f'{nm}#{hd}'

# ---------------------------------------------------------------- write notes
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
note_by_name = {nt['name']: nt for nt in notes}
folder_notes = collections.defaultdict(list)
inbound = collections.Counter()
seg_cache = {}

def fm(nt, extra=None):
    f = ['---', f'type: doc-topic', f'status: extracted', f'title: "{nt["title"].replace(chr(34), "")}"',
         f'product_version: "{VERSION}"', f'source: "{SOURCE}"', f'source_pages: "{nt["page0"]}-{max(nt["page0"], nt["page1"] - 1)}"',
         f'section: "{folder_short(nt["folder"].split("/")[0])}"']
    if nt.get('parent'): f.append(f'parent: "[[{nt["parent"]}]]"')
    f += ['tags:', '  - control-m', f'  - {slug(folder_short(nt["folder"].split("/")[0])).lower()}', '---', '']
    return f

for nt in notes:
    body = []
    for j, e in enumerate(nt['entries']):
        its = seg_items(e)
        seg = render(its, linkmap, skip=(toc[e]['page'], toc[e]['top'], toc[e]['nlines']))
        if j > 0:
            body.append('## ' + toc[e]['title']); body.append('')
        body.extend(seg)
    lines = fm(nt) + ['# ' + nt['title'], '']
    sec = folder_short(nt['folder'].split('/')[0])
    crumbs = f'**Section:** [[{sec}-MOC]]'
    if nt.get('parent'): crumbs += f' · **Parent:** [[{nt["parent"]}]]'
    lines.append(crumbs); lines.append('')
    if nt.get('hub'):
        lines += body
        lines += ['## Topics in this section', '']
        for cn in nt['children_notes']:
            lines.append(f'- [[{cn}]]')
        lines.append('')
    else:
        lines += body
    text = '\n'.join(lines).rstrip() + '\n'
    for _ in range(3):
        text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\] \[\[\1\|([^\]]+)\]\]', r'[[\1|\2 \3]]', text)
        text = re.sub(r'\[\[([^\]|]+)\]\] \[\[\1\|([^\]]+)\]\]', r'[[\1|\1 \2]]', text)
    text = re.sub(r'(\]\])\s+([.,;:)])', r'\1\2', text)
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', lambda m: wikilink(m.group(1), m.group(2)), text)
    for m in re.finditer(r'\[\[([^\]|#]+)', text): inbound[m.group(1)] += 1
    path = os.path.join(OUT, '10-Guide', nt['folder'], nt['name'] + '.md')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(text)
    nt['path'] = path
    folder_notes[nt['folder'].split('/')[0]].append(nt)

# ---------------------------------------------------------------- MOCs
os.makedirs(os.path.join(OUT, '00-Index'), exist_ok=True)
master = ['---', 'type: moc', 'status: extracted', 'tags:', '  - control-m', '  - moc', '---', '',
          '# Control-M User Guide 9.0.27 — Master MOC', '',
          f'Source: {SOURCE}. Every note carries `source_pages` for citation back to the PDF.', '',
          'Start here → [[About-This-Vault]] · [[Troubleshooting-Entry-Points]]', '', '## Sections', '']
for p, f in FOLDERS:
    sec = folder_short(f)
    master.append(f'- [[{sec}-MOC]] — {sec.replace("-", " ")} (pp. {p}–)')
    m = ['---', 'type: moc', 'status: extracted', f'section: "{sec}"', 'tags:', '  - control-m', '  - moc', '---', '',
         f'# {sec.replace("-", " ")} — MOC', '', 'Up: [[Control-M-Guide-MOC]]', '']
    for nt in folder_notes.get(f, []):
        if nt.get('parent'): continue
        m.append(f'- [[{nt["name"]}]] (pp. {nt["page0"]}–{max(nt["page0"], nt["page1"] - 1)})')
        if nt.get('hub'):
            for cn in nt['children_notes']:
                m.append(f'  - [[{cn}]]')
    open(os.path.join(OUT, '00-Index', f'{sec}-MOC.md'), 'w', encoding='utf-8').write('\n'.join(m) + '\n')
open(os.path.join(OUT, '00-Index', 'Control-M-Guide-MOC.md'), 'w', encoding='utf-8').write('\n'.join(master) + '\n')

json.dump(dict(notes=[{k: v for k, v in nt.items() if k != 'path'} for nt in notes], linkmap=linkmap),
          open('/home/claude/build/notes.json', 'w'))
print('notes', len(notes), 'hubs', sum(1 for n in notes if n.get('hub')))


# ---------------------------------------------------------------- split message tables into chunks
MAXROWS = 80
msg_hubs = []
for nt in [n for n in notes if n['folder'].startswith('50-Messages') and not n.get('hub')]:
    text = open(nt['path'], encoding='utf-8').read()
    lines = text.split('\n')
    # find table start
    try:
        hi = next(k for k, l in enumerate(lines) if l.startswith('| ') and lines[k + 1].startswith('|---'))
    except StopIteration:
        continue
    head, hdr, sep = lines[:hi], lines[hi], lines[hi + 1]
    rows = [l for l in lines[hi + 2:] if l.startswith('| ') and l != hdr and not l.startswith('|---')]
    chunks, cur = [], []
    for r in rows:
        m = re.match(r'\| (\d{3,6})\b', r)
        if m and len(cur) >= MAXROWS:
            chunks.append(cur); cur = []
        cur.append(r)
    if cur: chunks.append(cur)
    if len(chunks) <= 1: continue
    child_names = []
    for ci, ch in enumerate(chunks):
        ids = [re.match(r'\| (\d{3,6})\b', r).group(1) for r in ch if re.match(r'\| (\d{3,6})\b', r)]
        rng = f'{ids[0]}-{ids[-1]}' if ids and ids[0] != ids[-1] else f'part-{ci + 1}'
        cname = f'{nt["name"]}-{rng}'
        child_names.append((cname, rng, len(ids)))
        cfm = ['---', 'type: doc-messages', 'status: extracted', f'title: "{nt["title"]} {rng}"', f'product_version: "{VERSION}"',
               f'source: "{SOURCE}"', f'source_pages: "{nt["page0"]}-{nt["page1"] - 1}"', 'section: "Messages"',
               f'parent: "[[{nt["name"]}]]"', f'message_range: "{rng}"', 'tags:', '  - control-m', '  - messages', '---', '',
               f'# {nt["title"]} — {rng}', '', f'**Section:** [[Messages-MOC]] · **Parent:** [[{nt["name"]}]]', '',
               'Each row: message text (with the numeric ID) · explanation · corrective action, as printed in the guide.', '',
               hdr, sep] + ch + ['']
        open(os.path.join(os.path.dirname(nt['path']), cname + '.md'), 'w', encoding='utf-8').write('\n'.join(cfm))
    hub = head + [f'Messages are split into ranges of ~{MAXROWS} IDs. Search the ID to find the right range.', '', '## Message ranges', '']
    for cname, rng, n in child_names:
        hub.append(f'- [[{cname}]] — IDs {rng} ({n} messages)')
    open(nt['path'], 'w', encoding='utf-8').write('\n'.join(hub) + '\n')
    nt['msg_children'] = [c[0] for c in child_names]
    msg_hubs.append(nt)

# patch the Messages MOC with the ranges
mocp = os.path.join(OUT, '00-Index', 'Messages-MOC.md')
m = open(mocp, encoding='utf-8').read().rstrip('\n').split('\n')
for nt in msg_hubs:
    for k, l in enumerate(m):
        if l.strip() == f'- [[{nt["name"]}]]':
            m[k:k + 1] = [l] + [f'    - [[{c}]]' for c in nt['msg_children']]
            break
open(mocp, 'w', encoding='utf-8').write('\n'.join(m) + '\n')

# ---------------------------------------------------------------- troubleshooting entry points
KEYS = ['Health Check', 'Troubleshoot', 'Diagnostic', 'Messages', 'diag', 'ping', 'Communication', 'Ports', 'Log', 'Firewall',
        'Return Codes', 'Compare Utility', 'check_config', 'Backup and Restore', 'Disaster Recovery', 'High Availability',
        'Time Zones', 'New Day', 'Agent Management', 'Control-M/Server Management', 'Control-M/EM Management', 'Alert',
        'Archiv', 'Database Maintenance', 'Agent Utilities', 'Agent Toolbox', 'ctmag_mng_svr', 'ctm_agstat', 'Kerberos',
        'Cryptographic', 'Proxy', 'Load Balancer', 'Authentication', 'Security', 'Usage Reporting', 'ctmsys', 'ctmsec',
        'Vault', 'Startup Parameter', 'Site Settings', 'Hub Settings', 'Gateway Settings', 'File Transfer Server', 'Glossary',
        'Control-M Architecture', 'Control-M Services']
tp = ['---', 'type: moc', 'status: extracted', 'tags:', '  - control-m', '  - moc', '  - troubleshooting', '---', '',
      '# Troubleshooting Entry Points', '', 'Up: [[Control-M-Guide-MOC]]', '',
      'Curated by title keyword from the guide; the notes below are the ones a TSA most often needs mid-case.',
      'Pair with the HCU vault (archive interpretation) — this vault answers "what does the product do / what does this message mean".', '']
grouped = collections.defaultdict(list)
for nt in notes:
    if any(k.lower() in nt['title'].lower() for k in KEYS) and not nt.get('parent'):
        grouped[folder_short(nt['folder'].split('/')[0])].append(nt)
for sec in sorted(grouped, key=lambda s: [f for _, f in FOLDERS].index(next(f for _, f in FOLDERS if folder_short(f) == s))):
    tp.append(f'## {sec.replace("-", " ")}'); tp.append('')
    for nt in grouped[sec]:
        tp.append(f'- [[{nt["name"]}]]')
        if nt.get('hub'):
            for c in nt.get('msg_children', nt.get('children_notes', []))[:0]: pass
    tp.append('')
open(os.path.join(OUT, '00-Index', 'Troubleshooting-Entry-Points.md'), 'w', encoding='utf-8').write('\n'.join(tp) + '\n')

# ---------------------------------------------------------------- link check
names = set()
for root, _, files in os.walk(OUT):
    for f in files:
        if f.endswith('.md'): names.add(f[:-3])
dangling = collections.Counter()
for root, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.md'): continue
        t = open(os.path.join(root, f), encoding='utf-8').read()
        for m in re.finditer(r'\[\[([^\]|#]+)', t):
            if m.group(1) not in names: dangling[m.group(1)] += 1
print('files', len(names), 'dangling targets', len(dangling), sum(dangling.values()))
print(dangling.most_common(10))
