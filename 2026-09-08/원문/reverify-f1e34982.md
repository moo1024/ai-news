# 2akouwu/reverify — Stop your AI from making things up — it proposes, deterministic tools decide, ev

- 출처: GitHub 신규 (AI 에이전트)
- 원본 링크: https://github.com/2akouwu/reverify
- 발행: 2026-09-08T10:54:37.779781+00:00
- 접근상태: 확인 완료

---

GitHub - 2akouwu/reverify: Stop your AI from making things up — it proposes, deterministic tools decide, every claim checked against ground truth with evidence. Grounded facts and context survive resets. Reverse engineering is the proving ground. MCP server + CLI. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 2akouwu
 
 / 
 
 reverify 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 215 
 
 

 
 
 
 
 
 Star
 1k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 3 


 
 
 
 
 
 
 
 
 Pull requests 
 0 


 
 
 
 
 
 
 
 
 Discussions 
 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Projects 
 


 
 
 
 
 
 
 
 
 Security and quality 
 0 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Discussions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Projects
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 83 Commits 83 Commits Folders and files Name Name Last commit message Last commit date .github .github     benchmarks benchmarks     docs docs     reverify reverify     .coderabbit.yaml .coderabbit.yaml     .gitignore .gitignore     BENCHMARK.md BENCHMARK.md     CHANGELOG.md CHANGELOG.md     CONTACT-NOTICE.md CONTACT-NOTICE.md     CONTRIBUTING.md CONTRIBUTING.md     EXAMPLE.md EXAMPLE.md     LICENSE LICENSE     OPENAI-VERIFY.txt OPENAI-VERIFY.txt     README.md README.md     ROADMAP.md ROADMAP.md     SECURITY.md SECURITY.md     pyproject.toml pyproject.toml     View all files Repository files navigation README Contributing MIT license Security More items Reverify 
 
 Stop your AI from making things up. 

 It proposes; deterministic tools check every claim against ground truth, and only what's verified counts.


 
 
 
 
 
 
 
 


 
 
 
 


 AI is confident and often wrong: it invents an API, a struct field, an offset, or what a
function does, and says it like fact. Reverify makes a deterministic tool the judge — the model
proposes a claim, the tool checks it against the actual artifact, and it comes back VERIFIED /
REFUTED with evidence . The model never gets to assert a fact on its own.

 Two things it does today:

 
 Keeps your AI honest — every structural or behavioral claim is checked against ground
truth, not trusted, and only what survives becomes a fact ( reverify verify , or the MCP
server your agent already talks to). 
 Keeps your AI's context from rotting — instead of a lossy auto-summary, reverify rollover 
hands the session off to a file and starts a fresh one, so long tasks don't drift or need
 /clear . Works in Claude Code, Codex, Gemini CLI and OpenCode. 
 
 The hardest place to prove the first point is binary reverse engineering, where hallucination is
worst — so that's where the numbers come from. On 71 real Windows system files the AI's textbook
answer was wrong 97% of the time ; reverify caught every one and never accepted a wrong
claim (0 of 71; the same gate runs in CI on Linux and macOS every push, and an independent
aarch64 run found the same) ( EXAMPLE.md , BENCHMARK.md ;
 python benchmarks/prologue_prior.py ).

 
 


 The problem 
 Language models are great at reading code and unreliable at reverse engineering. Ask a
model to reconstruct a struct or an algorithm from a binary and it will confidently invent
offsets, sizes, and behavior. In binary analysis this hallucination problem is far worse
than in source code, and "did the model just make that up?" is the single biggest blocker
to using AI for real RE.

 What Reverify does 
 Reverify pairs a language model with a deterministic, pure-Python RE toolkit and makes the
toolkit the judge. The model proposes; the tools verify. A hypothesis about a structure or an
algorithm is only reported once it has been checked against the actual bytes — disassembled,
pattern-matched, or executed in the emulator — so the output is grounded in the binary instead
of the model's imagination.

 
 Deterministic core — PE/ELF/Mach-O parsing, x86/x64/ARM/ARM64 disassembly, AOB pattern
scanning, CPU emulation, Protobuf/TLV dissection, Frida hook generation. Pure Python out of
the box; installs clean with no Ghidra. 
 Mature engines, optional — with pip install "reverify[full]" the toolkit upgrades
itself in place to capstone (disassembly), unicorn (real CPU emulation), lief 
(PE/ELF/Mach-O) and Z3 (proofs); pip install "reverify[angr]" adds angr for
function boundaries, the call graph and cross-references. Not installed? It falls back to
the pure-Python core. reverify backends shows what's active. 
 Grounded, not guessed — structural claims are verified against the binary by the tools. 
 Not only binaries — reverify equiv <reference> <candidate> --lang python (or C) runs a
candidate implementation and a reference over shared inputs and checks they agree, so an AI's
rewrite or refactor is tested, not trusted — a refutation comes back with the input and both
outputs. The same rigour, aimed at ordinary source code. 
 Agent-native — ships as an MCP server, so Claude Code, Cursor, and other agents can call
the tools directly; also a plain CLI. 
 
 
 Reverify is for authorized reverse engineering — malware analysis, CTF, interoperability
research, and software you own or are permitted to analyze. See SECURITY.md .

 
 Quick start 
 # Install the CLI + MCP server from PyPI: 
pip install reverify # pure-Python core; or "reverify[full]" for capstone+unicorn+lief 
reverify auto sample.bin --json

 # Or run straight from a checkout — pure standard library, nothing to install: 
python reverify/cli.py auto sample.bin --json
python reverify/cli.py parse-pe sample.exe --json
python reverify/cli.py disasm 90505831C0C3 --arch x86_64 
 The verification loop 
 This is what the name is about. A claim is any hypothesis about the binary; the
deterministic tools are the judge and hand back VERIFIED , REFUTED , or
 INCONCLUSIVE together with the bytes they actually observed:

 reverify verify sample.bin --claim ' { 
 "kind": "instructions", "offset": 4096, 
 "mnemonics": ["push", "mov", "sub"], "note": "function prologue" 
 } ' 
 # Check a reconstructed routine actually computes what the model claimed: 
reverify verify - --claim ' { 
 "kind": "emulate_result", "code": "b805000000b90300000001c8c3", 
 "arch": "x86", "expect_registers": {"eax": 8} 
 } ' 
 Claims can be batched from a JSON file ( --claims-file claims.json ); the CLI exits
non-zero if anything is refuted, so an agent or CI job can gate on a grounded
reconstruction. Claim kinds: bytes_at , u16_at / u32_at / u64_at (typed reads, no
endianness math), pattern_present , string_present , instructions (mnemonics and
optionally operands), emulate_result , behavior_equiv , prove_equiv , protobuf_field ,
 import_present , export_present , section_present , and the semantic kinds
 function_at , calls , references , reachable_from_entry (see
 The semantic layer ). Offsets are file offsets unless a claim says
 "space": "rva" or "va" ; the verifier translates through the section table and echoes
all three addresses in the evidence, and a refuted bytes_at reports where the expected
bytes actually are. Set "observe": true (or omit expected ) to have the tools read a
value instead of asserting one, and "depends_on": [...] so a refuted root invalidates
the claims built on it.

 Grounded means informative , not just "nothing refuted" 
 "Every claim verified" is trivially reachable: assert that the file starts with MZ and
that .text exists. So Reverify also weighs how much a verified set actually says. Each
result carries a weight — zero for claims that merely restate the fact sheet the model was
shown, for duplicates, for inline code/data that does not occur in the binary
(self-referential), and for echoes of the tools' own previous output; otherwise it is
 measured from the binary itself — how often the expected content occurs in this file and
how much entropy it has — so zero padding, a ubiquitous prologue, or a pattern that matches
everywhere weigh almost nothing even though they verify, and emulation must actually execute
non-degenerate code. A reconstruction is grounded only when nothing
is refuted and the verified weight reaches --min-information (default 1.0). This follows
the CORE refinement of FActScore: credit only claims that are factual, informative and
non-repetitive. reverify reconstruct --samples N draws several proposals per round and
lets the verifier — not the model's confidence — select among them.

 EXAMPLE.md walks through one run on kernel32.dll — the model
proposes the textbook prologue from prior, the verifier refutes it with the real
bytes, and the model corrects to grounded, with no API key and no specific model.
 BENCHMARK.md is the reproducible measurement behind the numbers above.

 Evidence, not claims 
 Everything above is checkable without trusting the author:

 
 The verifier is checked by independent judges , not by its own tests: the pure
parser against lief on real binaries, the disassembler against capstone, binutils
 objdump and hand-verified Intel vectors, the emulator against Unicorn, the semantic
engine against the export table — plus fuzzing that a malformed file never crashes the
reader and that a wrong claim is never VERIFIED. All of it runs in CI on Linux, Windows
and macOS, with and without the engines; a nightly job fuzzes 20k inputs. 
 The benchmark runs in CI on every push, on each platform's own system binaries , and
 fails the build if a single wrong claim is VERIFIED . Each run leaves a
machine-readable record — SHA-256 of every binary, verdicts, tool versions — as an
artifact; reference runs live in benchmarks/results/ , and a
third-party aarch64 replication is in BENCHMARK.md . 
 The verifier is measured like a classifier : for every claim kind, known-true and
known-false claims on real binaries give a confusion matrix — 0 false VERIFIED of 475
known-false claims, 0 known-true claims missed — gated in every CI job. 
 Every verdict carries a receipt : reverify verify --json (and re_verify_claim )
include the binary's SHA-256, the reverify version and which engines judged, so a report
can be handed over and replayed rather than believed. Releases ship with a SLSA build
provenance attestation. 
 A replication package : benchmarks/README.md — one command
per benchmark, a pinned Dockerfile, expected output, and how to submit a run; a
model-in-the-loop benchmark anyone can run against any OpenAI-compatible endpoint. 
 
 The ledger: state that survives a context reset 
 Every agent harness handles a full context window the same way — a model summarizes the
transcript, the rest is dropped, and the docs warn that repeated compactions degrade
accuracy. That loss is unavoidable for free-form conversation, because nothing in a
transcript says which parts were state and which were chatter.

 Reverify's loop can do better for itself, because it already draws that line: the only
things that matter are what the tools verified, observed, proved — and refuted .
Everything else (the model's prose, its unverified guesses) was never trusted, so dropping
it loses nothing. Since v0.8.0 exactly that state is written to disk as it happens:

 
 .reverify/ledger/<sha256>.json per binary (content-keyed, so a renamed copy shares
its ledger), checkpointed after every round — a crash, a /clear , an auto-