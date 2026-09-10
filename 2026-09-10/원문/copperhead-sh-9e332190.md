# Show HN: Copperhead – Cursor for circuit boards

- 출처: Hacker News
- 원본 링크: https://copperhead.sh/
- 발행: 2026-09-08T13:26:45+00:00
- 접근상태: 확인 완료

---

copperhead. Cursor for circuit boards. copperhead copperhead Research Pricing Blog Docs Careers Sign in 221 Let's talk New Hardware as fast as software Cursor for circuit boards . Copperhead is an open-source AI engineering platform that helps hardware teams design, verify and ship circuit boards.
 Start building Read the docs $ npm i -g copperhead Replay copperhead v0.8.1 claude via flag · kicad-cli 9.0.4 ~/hardware/open-key   ❯ $ add a USB-C power input to the key   ▸ read_file docs/POWER.md (48 lines) ▸ list_nets 41 nets, no VBUS, no CC1/CC2 ▸ validate_change add-usb-c-power valid, edit tools unlocked ✓ propose: add-usb-c-power validated, edit tools unlocked ▸ edit_file hardware/open-key.kicad_sch: USB-C receptacle, 2x 5.1k CC pulldowns ▸ edit_file docs/POWER.md: VBUS budget, 5 V at 1.5 A ✓ edit: 2 files, 5 anchored regions ▸ run_erc clean, 0 violations ▸ check_drift docs match schematic ✓ verify: ERC clean, no drift ▸ record_decision DECISIONS.md +1 · CHANGELOG.md +1 ✓ remember: decision + changelog recorded turn 1/40 · 900 in / 120 out · 0s 1s 2s 3s 4s 5s 6s 7s 8s 9s 10s 11s 12s 13s 14s 15s 16s 17s · drafting the power proposal turn 2/40 · 4.2k in / 800 out · 0s 1s 2s 3s 4s 5s 6s 7s 8s 9s 10s 11s 12s 13s 14s 15s 16s 17s · placing the receptacle turn 3/40 · 9.1k in / 1.5k out · 0s 1s 2s 3s 4s 5s 6s 7s 8s 9s 10s 11s 12s 13s 14s 15s 16s 17s · running ERC turn 4/40 · 11.8k in / 1.9k out · 0s 1s 2s 3s 4s 5s 6s 7s 8s 9s 10s 11s 12s 13s 14s 15s 16s 17s · writing the decision log done · verified erc · committed 3f2c9a1 · 17s · 12.3k tokens 221 GitHub stars 513 installs / month 
 Backed by
 Microsoft for Startups Google for Startups Activate Clerk Supabase Google Workspace Sarvam AI Hugging Face Microsoft for Startups Google for Startups Activate Clerk Supabase Google Workspace Sarvam AI Hugging Face Proven on copper Proven on real copper. Open Telegraph: pocket-size ESP32-S3 Morse key, built end to end with this workflow. Every decision, every check, every file is public.
 Read the build story Browse the repo 
 How it works Eight stages, start to finish. You write the brief. copperhead runs the stages in order, each one its own agent run. A stage has to leave its artifact on disk before the next starts. If a gate fails, the run stops there.
 in brief.md 
 what you want, written in your own words
 01 spec docs/SPEC.md 
 gate a budgets section, actually filled in
 02 architecture docs/SUBSYSTEMS.md 
 gate real reasoning under every subsystem
 03 parts docs/BOM.md 
 gate part numbers chosen against datasheets
 04 schematic design.kicad_sch 
 gate symbols placed, docs agree, ERC clean
 05 layout design.kicad_pcb 
 gate footprints on the board, DRC clean
 06 outputs gerbers / drill / STEP 
 gate gerbers actually on disk
 07 firmware firmware/ / pins.h 
 gate sources on disk, pins from the pinout
 08 dev plan docs/DEVPLAN.md 
 gate a written bring-up and test plan
 out a design package
 gerbers, firmware, docs. One commit per stage.
 Every hop is a gate: no real work on disk, no commit . Copper border: verified by KiCad itself, ERC and DRC clean . Read the long version, one stage at a time Pricing Pay to not run it yourself. copperhead is open core. The CLI is free and always will be, and it does the real work on its own. You pay to host it, to work as a team or to give an auditor what they ask for.
 Talk to sales CLI Free Apache-2.0, forever
 Design on your own, on your own machine.
 Get started Includes:
 The full agent: do, create, init, check, watch Bring your own Claude or GPT-5 key Runs on your KiCad files, in your own git repo Plain markdown, JSON and KiCad output. No lock-in. Runs locally, never metered Community support Most popular Cloud $49 per user / month Free for open hardware repos
 Hosted runs on private repos, with a web viewer.
 Let's talk Everything in CLI, plus:
 Hosted runs, no local setup, from anywhere Private repositories Web viewer: chat, live schematic and board render, ERC/DRC status Run history and shareable check reports One-click gerber, DXF/STEP, render and BOM export BYO key, or managed inference with 200 credits a seat Team $49 per user / month + $199 / mo platform
 Cloud, with governance and CI for a whole team.
 Let's talk Everything in Cloud, plus:
 CI bot: run check as a required PR status check Shared, versioned constraint libraries across the org SSO / SAML, role management, central billing Managed credits pooled across the team Shared run history Enterprise Custom annual Self-hosted, built for procurement, one price a year.
 Talk to sales Everything in Team, plus:
 Self-hosted or VPC, so design data never leaves your network Altium support beyond KiCad RBAC, security review, dedicated support and an SLA An audit trail your compliance team can hand over Flat annual license, no per-run metering FAQ Questions, before you ask them. What is copperhead? An open source AI agent that designs, documents and verifies printed circuit boards. You describe a change or hand it a product brief, and it edits your real KiCad files, updates every document that references them, and runs KiCad's own checks until they pass. Longer introduction here .
 What problem does it actually solve? Drift. A hardware design spreads one decision across a schematic, a bill of materials, a power budget and several documents, and nothing breaks when they fall out of sync. The inconsistency is found at bring-up, and a respin costs 5,000 to 50,000 dollars and six to eight weeks. The full argument is here .
 What do I need installed? Node 20 or newer, KiCad with kicad-cli on your path and a model API key of your own. Then npm i -g copperhead .
 Does it work on a design that already exists? That is the main case. Point it at a KiCad repository, run copperhead init and start asking for changes. It can also run the full pipeline from a written brief with copperhead create , but iterating on real designs is what it is best at.
 What will it refuse to do? It refuses to run on a dirty git tree, refuses to edit any design file before a validated change proposal exists and refuses changes that break a budget or constraint you have documented, citing the line it would violate. It also never invents a part number it cannot justify from a datasheet.
 Will it rewrite my whole schematic? No. Edits are surgical changes to the KiCad s-expression source, so your diffs stay small and reviewable and untouched parts of the file stay byte-identical. A tool that regenerates the file to move one net has made its own work impossible to review.
 9 more questions 
 Start building Never ship a board your docs no longer describe. copperhead is open source and free to use. Install once, describe the board you want in a short brief.md and run create .
 
copperhead create --brief brief.md" aria-label="Copy to clipboard" hidden data-astro-cid-wfdy3gt7> $ npm i -g copperhead
 $ export ANTHROPIC_API_KEY=<api-key>
 $ copperhead create --brief brief.md
 brief.md # Pocket Bluetooth speaker 
 
 A palm-size Bluetooth speaker that plays for a day on one charge. 
 
 - ESP32, Bluetooth audio (A2DP sink) 
 - 3 W class-D amp into a 4 Ω driver 
 - Li-Po cell, USB-C charging 
 - Standby current budget: 100 µA Circuit boards, designed by an agent. Open source, verified against KiCad and built by people who still solder.
 Product Quickstart Pricing Docs Open Telegraph Resources Blog FAQ Stats Status llms.txt Built on KiCad OpenSpec Company chouhan.ai Careers Contact Connect © 2026 · copperhead · Software Apache-2.0 · Hardware CERN-OHL-S v2.0 
 copperhead .