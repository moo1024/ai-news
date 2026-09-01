# Show HN: SlideOps – slides from a repo that flag when they drift from the code

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://github.com/glukicov/slideops
- 발행: 2026-08-31T12:15:10+00:00
- 접근상태: 확인 완료

---

GitHub - glukicov/slideops: Turn a repository into a slide deck that tells you when it stops matching the code · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 glukicov
 
 / 
 
 slideops 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 2 
 
 

 
 
 
 
 
 Star
 30 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 0 


 
 
 
 
 
 
 
 
 Discussions 
 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Security and quality 
 0 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Discussions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 30 Commits 30 Commits Folders and files Name Name Last commit message Last commit date .claude-plugin .claude-plugin     .github .github     docs docs     scripts scripts     skills skills     tests tests     .gitignore .gitignore     .pre-commit-config.yaml .pre-commit-config.yaml     .python-version .python-version     AGENTS.md AGENTS.md     CHANGELOG.md CHANGELOG.md     CLAUDE.md CLAUDE.md     CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     SECURITY.md SECURITY.md     install.sh install.sh     pyproject.toml pyproject.toml     uv.lock uv.lock     View all files Repository files navigation README Code of conduct Contributing MIT license Security More items 
 Generate a deck from your code in minutes. Find out in milliseconds when it stops being true. Then rebuild only the slides that drifted. 
 
 
 
 
 
 
 

 Install · Use · Features · Docs · Demo deck · Why 

 
 

 The demo deck is 17 slides about SlideOps, built by SlideOps: open the
 HTML or the
 PDF . 

 Writing documentation isn't the bottleneck any more. Keeping it true is. The deck that said
we run two database migrations still says two, a year after we started running ten 😅.

 SlideOps is a pair of Agent Skills for Claude Code
and compatible coding agents. It treats a generated document the way you'd treat generated
code: it's built from a source, and it records which source it came from.

 The reasoning behind it is written up in
 Your documentation is a build artifact. Start treating it like one .

 

 Press Esc in any deck for the overview grid. 

 Install 
 Claude Code. This repo is its own marketplace, so two lines are the whole setup, and
it's the only install that keeps itself up to date:

 /plugin marketplace add glukicov/slideops
/plugin install slideops@slideops
 
 Any agent with the skills CLI , in one line:

 npx skills add glukicov/slideops 
 Codex, Copilot CLI, OpenCode , or a plain checkout:

 git clone https://github.com/glukicov/slideops && cd slideops
./install.sh 
 All four agents read SKILL.md and nothing needs porting between them. For the symlink and
snapshot installs, the per-agent table and how updates reach you, see
 docs/install.md .

 Note
 Third-party marketplaces have auto-update off by default . Turn it on once in
 /plugin → Marketplaces , or new versions only arrive when you run
 /plugin marketplace update slideops by hand.

 
 Use 
 Open a repository and say:

 Tip

 💬 make slides about this repo 
 
 SlideOps scans the repo first, then asks one compact set of questions: which topic (it
proposes concrete candidates it found, each with a "why now"), audience, length, theme and
extras. You get an outline to approve before it writes any HTML.

 If you already know what you want, skip the intake:

 Note

 💬 deep dive on the auth subsystem, Ledger Dark theme, 15 slides, with a PDF 
 
 Prefer a document to a deck? Since v1.1.0 the same mechanism writes Markdown:

 Tip

 💬 write markdown docs for the sync subsystem 
 
 You get a single .md that renders on GitHub, with every quoted snippet carrying an
invisible citation comment ( <!-- slideops data-src="app/main.py:40-58" data-sha256="a1b2c3d4e5f6" --> ) above its fence, Mermaid diagrams as native fences, and
the build commit stamped on line 1. The same check.py sweep verifies docs and decks
together, and the same --json repair brief lets an agent regenerate only the sections
that drifted. PDF export mirrors the deck path with a verified, print-paginated export.

 Months later, in the same repository:

 Important

 💬 is the architecture deck still accurate? 
 
 The agent sweeps the deck folder and triages by status. It re-quotes whatever merely moved,
and flags the slides whose claim might no longer hold. It repairs what drifted instead of
regenerating the deck, so the pacing and narrative you signed off on the first time survive.

 Features 
 
 
 Freshness checking. scripts/check.py sweeps a whole docs/slides/ folder and
reports which slides cite code that has changed, moved or vanished since the deck was
built, then suggests the fix or hands an agent a JSON repair brief. No model, no network,
no tokens: standard library Python, and it runs in milliseconds.

 
 
 Markdown docs with the same guarantee. The .md carrier uses HTML comments instead
of attributes, headings instead of slide numbers, and shares every status, the sweep,
and the repair brief with decks. The worked example is
 skill-demo.md , checked by this repo's CI.

 
 
 One self-contained file per deck. No build step, no CDN, works offline, attaches to
an email.

 
 
 Navigation: arrow keys, click-to-advance, URL hash deep links, an Esc-toggled
overview grid, and speaker notes on N (never visible in screenshots or exports).

 
 
 13 slide patterns: title, agenda, section divider, prose + cards, reference table,
before/after code, annotated snippet (half and full width), flow diagram, lane
comparison, image + caption, chat bubbles, closing.

 
 
 4 themes, one block each. Every color derives from a single :root token block via
 color-mix() , so switching theme is one replacement: Ledger Light (default),
 Ledger Dark , Midnight , Graphite . Or point it at a brand's real CSS values and
map those onto the token roles.

 
 
 
 Ledger Light (default) 
 Ledger Dark 
 
 
 
 
 
 
 
 
 Same deck, same markup, same content. 
 One :root block apart. 
 
 
 
 
 
 Mermaid diagrams pre-rendered to inline SVG at build time and themed from the deck's
own tokens, so the deck stays dependency-free.

 
 
 Verified PDF export. The companion skill renders the finished PDF back to images and
checks the pages, because a PDF can have the right page count and still hand you blank
images.

 
 
 Documentation 
 
 
 
 Page 
 What's in it 
 
 
 
 
 📦  Install 
 Every install path, all four agents, updating, requirements, what gets installed 
 
 
 🔎  Freshness 
 Citations, the status table, the cost model, where to automate, the accuracy contract, what never reaches a slide 
 
 
 🛠️  Development 
 Working on this repository: the gate, CI guards, generated artifacts, releasing 
 
 
 📋  Changelog 
 What changed in each release 
 
 
 
 Inside the skill, skills/slideops/references/ holds the specifications the agent reads:
freshness, automation, style, themes, diagrams and verification.

 Credits 
 Prior art worth knowing: frontend-slides 
for visual-first theme selection, and
 presentation-skills for pioneering the
render-then-look visual QA loop that SlideOps also relies on. What SlideOps adds is the
 Ops half: content grounded in a repository, and a cheap way to ask later whether it still
holds.

 Licence 
 MIT. See LICENSE . Use it, fork it, ship it commercially; attribution is the only
condition. The decks you generate are your own content either way.

 


 Install · Docs · Changelog · Releases 

 Built with SlideOps, about SlideOps. If a slide in this repo ever stops matching the code, check.py says so. 

 
 About Turn a repository into a slide deck that tells you when it stops matching the code
 medium.com/@lukicov/your-documentation-is-a-build-artifact-start-treating-it-like-one-ab48df61b1e0 Topics agent-skills claude-code claude-skills developer-tools docs-as-code documentation presentations slides Resources Readme MIT license Code of conduct Code of conduct Contributing Contributing Security policy Security policy Activity Stars 30 stars Watchers 1 watching Forks 2 forks Report repository Releases Packages Used by Contributors Languages 
 




 

 

 
 

 

 
 Footer 

 


 
 
 
 
 
 
 
 
 © 2026 GitHub, Inc.
 
 

 
 Footer navigation 

 


 
 Terms 
 

 
 Privacy 
 


 
 Security 
 

 
 Status 
 

 
 Community 
 

 
 Docs 
 

 
 Contact 
 

 
 
 
 
 Manage cookies
 
 
 

 
 
 
 Do not share my personal information
 
 
 

 
 
 
 



 




 
 
 
 
 
 
 
 
 
 You can’t perform that action at this time.