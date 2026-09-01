import os

IDS = [
    "2094840179676660097-7e04f323",
    "codex-libreoffice-123fd05b",
    "v2-1-257-f415247f",
    "2094885578173260259-e4c6db82",
    "claude-fable-and-mythos-5-1-c3eef50e",
    "44-on-arc-1-44526c12",
    "introducing-agentic-video-in-gemini-9658836c",
    "2094840182457422260-4bd15ae5",
    "zitron-56a6fd93",
    "3mui4h3h76223-2c859b04",
    "dwarf-fortress-creator-says-the-industry-d1bfe22b",
    "3mugm575l4s2v-f9a92e9f",
]

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "원문")
dst = os.path.join(base, "_정리본문")
os.makedirs(dst, exist_ok=True)

for i in IDS:
    text = open(os.path.join(src, i + ".md"), encoding="utf-8").read()
    sep = "\n---\n"
    body = text.split(sep, 1)[1] if sep in text else text
    out = []
    for line in body.split("\n"):
        line = line.strip()
        if line == "":
            if out and out[-1] == "":
                continue
            out.append("")
        else:
            out.append(line)
    s = "\n".join(out).strip()
    open(os.path.join(dst, i + ".txt"), "w", encoding="utf-8").write(s)
    print(i, len(s), s.count("\n") + 1)
