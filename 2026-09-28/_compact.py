import json, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs('_정리', exist_ok=True)
d = json.load(open('_후보.json', encoding='utf-8'))
for it in d['항목']:
    raw = open(f"원문/{it['id']}.md", encoding='utf-8').read()
    parts = raw.split('\n---\n', 1)
    body = parts[1] if len(parts) > 1 else raw
    out, blank = [], 0
    for ln in (l.strip() for l in body.split('\n')):
        if not ln:
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    text = '\n'.join(out).strip()
    open(f"_정리/{it['id']}.txt", 'w', encoding='utf-8').write(text)
    print(it['id'], len(text))
