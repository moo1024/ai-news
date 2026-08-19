# mikehasa/agentacct — See what your coding agents did and what it cost. Breaks each task down into wor

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/mikehasa/agentacct
- 발행: 2026-08-19T03:34:26.738684+00:00
- 접근상태: 확인 완료

---

GitHub - mikehasa/agentacct: See what your coding agents did and what it cost. Breaks each task down into work steps — tools used, files changed, tests run, time and tokens spent. Local-first dashboard for Claude Code, Codex, OpenCode, and more. No login, no telemetry. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 mikehasa
 
 / 
 
 agentacct 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 69 
 
 

 
 
 
 
 
 Star
 609 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 0 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Projects 
 


 
 
 
 
 
 
 
 
 Security and quality 
 0 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Projects
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 113 Commits 113 Commits Folders and files Name Name Last commit message Last commit date .github .github     apps/ agentacct apps/ agentacct     benchmarks benchmarks     contrib/ swiftbar contrib/ swiftbar     docs docs     examples examples     integrations/ hermes/ agentacct-workflow integrations/ hermes/ agentacct-workflow     packaging packaging     scripts scripts     src/ agentacct src/ agentacct     tests tests     .env.example .env.example     .gitignore .gitignore     CHANGELOG.md CHANGELOG.md     CONTRIBUTING.md CONTRIBUTING.md     INSTALL.md INSTALL.md     LICENSE LICENSE     MANIFEST.in MANIFEST.in     README.md README.md     SECURITY.md SECURITY.md     pyproject.toml pyproject.toml     uv.lock uv.lock     View all files Repository files navigation README Contributing MIT license Security More items agentacct 
 
 
 
 

 See what your coding agents actually did — and whether you can trust it — across Claude Code, Codex, OpenCode, and Hermes, without any of it leaving your machine. 

 agentacct is local-first Agent Work Intelligence for coding agents. It reads the session logs your agents already write on disk — Claude Code, Codex, OpenCode, and Hermes — joins them with the work each session records as it goes, and turns the result into one honest Work Receipt per task: what it did (the commands it ran, the files it touched, the tools it used), what it cost, and how well that is actually proven. See it in the macOS app , a live terminal dashboard ( agentacct tui ), or over a local JSON API. No browser tab, no server, no account.

 

 Private by design. Everything stays on your machine: state is plain local files, nothing binds a network port, and there is no phone-home telemetry, no account, no cloud sync. agentacct never stores or requests a provider API key.

 Screenshots show a synthetic demo workspace; your own dashboard renders your machine's real local data. 

 What you get 
 The same Task-primary view of your agents' work in the macOS app, in agentacct tui (a live terminal dashboard), and over a local JSON API — everything at a glance across all four agents:

 

 
 
 One Work Receipt per task — what it did, and whether you can trust it. Every task rolls up into eight questions a reviewer needs: what it was, who ran it, the actions it took (the commands it ran and the files it touched — read straight from each agent's own store), the cost, the evidence (how much of the work carries a real passing check), the outcome, the gaps, and per-field provenance — each fact labelled with where it came from (a client hook, a transcript scan, the agent's MCP records, CI). It keeps two things deliberately separate: what a human or agent says happened, and how well that is actually proven — an agent reporting "done" never raises the evidence bar. Read one in the app (above), or with agentacct receipt <task> .

 
 
 Honest usage and cost — per agent, model, and day. Tokens read from the clients' own local session files and labeled client_reported ; costs are clearly marked pricing-table estimates, never invoices.

 

 
 
 The work, not just the tokens. Every session rolls up its recorded work steps and machine checks — a passing test is Verified evidence, an agent's own claim stays labeled Agent reported . Open a task to see each step, its status ( in progress / handed off / done / blocked ), and its check results with exit codes.

 
 
 Attribution you can trust. Every join between usage and recorded work carries a confidence label ( exact / high / medium / low ). Missing attribution beats wrong attribution: when agentacct cannot prove a link, it shows the gap instead of a guess.

 
 
 What a task cost your plan (beta). agentacct estimates what fraction of your weekly Claude plan each task consumed — a plan column on the home panel and the sessions list, and an ≈ X% of your weekly plan line on the session detail. This is the number the raw token count can't give you: different models burn the plan at very different rates, so agentacct learns the rate from your own recorded limit history and shows a figure only once it can calibrate to your account — until then it says it's still calibrating, rather than showing a guess. Always labeled an estimate.

 
 
 Install 
 The macOS app — no Python required 
 The signed, notarized macOS app bundles everything. Download the .dmg from the latest release , drag agentacct to Applications, and open it — on first launch it installs the bundled CLI, instruments the coding agents it finds, and shows your Work Receipts in a native window. Requires macOS 14+.

 The CLI 
 Requires Python >= 3.11 on macOS or Linux; Windows is supported only via WSL.

 pipx install agentacct
agentacct onboard # once per machine (global by default) 
agentacct tui # the live terminal dashboard 
 No pipx yet? Install it first with brew install pipx (macOS) or python3 -m pip install --user pipx — or skip pipx entirely and use uv tool install agentacct . See INSTALL.md for a plain- venv fallback.

 onboard installs agentacct once per machine (global by default, writing zero files into your repo): it detects your local coding-agent logs, sets up a global store, and runs a first usage sync. Then run agentacct tui for the live terminal dashboard (onboarding also starts the managed background sync plus a local JSON API on http://127.0.0.1:8765 — the machine-readable lane native shells and scripts poll). Open a new agent session in any repo — MCP servers and hooks bind at session start, so the session that ran onboarding cannot become the first recorded Task. (Prefer a per-repo install? Run agentacct onboard --scope project instead.)

 Let your coding agent install it 
 Paste this into your coding agent:

 Install and set up agentacct — a local-first tool that reads my
coding-agent logs read-only and shows honest token usage and cost.

Run `pipx install agentacct`
(or `pipx install git+https://github.com/mikehasa/agentacct`),
then `agentacct onboard` (installs once per machine, global by default, zero
files written into the repo), then tell me to run `agentacct tui`.

Observe-only: never store, request, or echo any API key; all state stays local
on this machine. Don't modify my global client config without showing the exact
command first.
 
 The agent then follows INSTALL.md , the canonical runbook: the global install, the manual per-client setup, and the full per-client capability matrix. agentacct setup prompt --agent <client> prints the same prompt.

 Want to look around before touching your real data? agentacct demo runs a safe local walkthrough in a throwaway temporary store — no provider keys, no paid API calls.

 The managed runtime is controlled with agentacct start / status / stop / repair ; all state lives in the global store (by default ~/.local/state/agentacct/state ; older global stores under ~/.agent-sentinel-global/state are still recognized). A --scope project install keeps its state in the repo's .agent-sentinel/ directory instead (gitignored; the directory keeps its pre-rename spelling for data compatibility).

 Uninstall 
 agentacct stop # stop the managed sync + local API (owned processes only) 
agentacct uninstall-autostart # only if you installed autostart 
pipx uninstall agentacct 
 Then remove what onboarding added. For a global install (the default): delete the global store ( ~/.local/state/agentacct/state — keep it if you want the history) and the agentacct entries in your user config ( ~/.claude.json , the merged blocks in ~/.claude/settings.json , the ~/.claude/hooks/ wrapper, and ~/.codex/config.toml ). For a --scope project install: delete that repo's .agent-sentinel/ directory (that project's local ledger) and the agentacct entries onboarding added to .mcp.json / .claude/settings.local.json / ~/.codex/config.toml . If you installed the standing instruction block, remove it first with agentacct setup instructions --agent <client> --user --remove .

 The terminal dashboard 
 Prefer the terminal? agentacct tui is the full dashboard in your shell — usage windows, provider rate-limit bars with reset countdowns, and your recent sessions across every agent. Press s to drill into the sessions, u for the usage screen, t for a task's Work Receipt, p to save a shareable snapshot of the current view (an SVG that renders anywhere), q to quit.

 

 What it is honest about 
 agentacct is early alpha, and it would rather show you a gap than a guess:

 
 No hosted anything. No hosted dashboard, no phone-home telemetry, no automatic cloud account sync. agentacct can receive telemetry locally when you explicitly point an OTLP exporter at it. 
 Estimates are labeled as estimates. There is no exact Claude Code/Codex subscription invoice access; costs come from a local pricing table and are labeled accordingly. See docs/usage-truth-table.md for what each path can and cannot prove. 
 No silent monitoring. agentacct only reads the local session files of detected clients and never watches unrelated processes started outside agentacct/integrations. Hard stops apply only to runs agentacct itself launched or the opt-in proxy path. 
 Support is per-capability, not per-logo. Claude Code, Codex, and OpenCode carry a full Work Receipt today — usage, cost, and the actions each session took (commands, edited files, tools); OpenCode also contributes independent exit-code checks. Hermes has a live usage path plus a narrower capture surface; OpenClaw and Cursor are usage-focused and explicitly scoped. How each fact is captured differs honestly — a live hook, or a scan of the client's own store — and the Receipt says which. Every per-client claim is pinned in the capability matrix in INSTALL.md and docs/reference.md , and agentacct capabilities agents prints the same truth for your machine. 
 
 Interfaces may change while agentacct is alpha.

 How it works 
 agentacct keeps two evidence streams separate and joins them on real client ids instead of guessing:

 
 Usage truth comes from the client's own local session files: imported tokens are labeled client_reported , and costs are pricing-table estimates — never provider invoices. 
 Work meaning comes from the sections and events the agent records over MCP while it works ( agentacct_record_section , agentacct_record_machine_check ), plus machine checks like test runs. 
 The join links the two through session/transcript ids and labels every attribution exact , high , medium , or low . Claude Code binds real 