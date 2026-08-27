# AMAP-ML/LongHorizon-Harness — The long-horizon computer-use harness. Run AI agents across desktop apps and the

- 출처: GitHub 신규 (claude-code)
- 원본 링크: https://github.com/AMAP-ML/LongHorizon-Harness
- 발행: 2026-08-27T22:24:38.380645+00:00
- 접근상태: 확인 완료

---

GitHub - AMAP-ML/LongHorizon-Harness: The long-horizon computer-use harness. Run AI agents across desktop apps and the CLI for extended periods while preserving task state and making reliable progress on complex workflows. Features fresh-context execution, durable verified state, independent auditing, recoverable progress, and native Claude Code / Codex / OpenClaw integration. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 AMAP-ML
 
 / 
 
 LongHorizon-Harness 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 137 
 
 

 
 
 
 
 
 Star
 1.3k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 14 


 
 
 
 
 
 
 
 
 Pull requests 
 19 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 40 Commits 40 Commits Folders and files Name Name Last commit message Last commit date .github/ workflows .github/ workflows     assets assets     eval eval     frontend frontend     src/ lh_harness src/ lh_harness     tests tests     .gitignore .gitignore     LICENSE LICENSE     README.md README.md     README.zh-CN.md README.zh-CN.md     pyproject.toml pyproject.toml     View all files Repository files navigation README MIT license More items 
 LongHorizon-Harness 
 Loop Engineering for Computer-Use Agents 
 Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. Keep it working across desktop apps and the terminal for dozens of hours. 

 Plan → act → verify → checkpoint or recover → repeat — until the work is actually done. 

 
 
 
 
 
 
 


 
 
 

 Usage · The Loop · Computer Use · Results · Project Website · 简体中文 



 
 
 
 The model determines what an agent can do in one round. LongHorizon-Harness engineers the loop around it: what to do next, how to verify the result in the real computer, what progress to preserve, and how to continue after failure or context refresh. 

 
 A Loop Engineering system for Claude Code, Codex, OpenCode, and DeepSeek Harness. One-command install, ready to run. 

 LongHorizon-Harness turns existing agents into long-running computer-use systems. Across desktop apps and the terminal CLI, it continuously recovers the goal and verified state, selects the next bounded step, executes it with a fresh context, checks the actual result, and then checkpoints accepted progress or feeds failure evidence into the next round. It does not train a new model or replace an existing agent; it provides the durable execution loop around one.

 ✨ News 
 
 [v0.1.7 · 2026-08-20] A finished run is no longer a dead end: the workbench is now a conversation. Read the reply, type a follow-up, and the run continues on its own round ledger instead of replanning from scratch. A message you send mid-round is claimed by the very next round, so stopping and continuing never drops it. Also adds --reasoning-effort for every role (with --manager-reasoning-effort and friends to override one), forwarded to whichever backend exposes it. The transcript now reads in strict chronological order, and a graceful stop escalates to a force stop only when a worker ignores it. 
 [v0.1.6 · 2026-08-15] Added OpenCode CLI support. LongHorizon-Harness can now run opencode run prompt as --agent opencode , with role-scoped read/write permissions, OpenCode API endpoint overrides, normalized JSON results, and CLI/config/doctor integration. The Web workbench can select OpenCode Harness and its model independently for each role. 
 [v0.1.5 · 2026-08-14] Added phase-1 DeepSeek Harness CLI support. LongHorizon-Harness can now run dsh --profile headless as --agent deepseek_harness , with an isolated DSH_HOME , role-scoped read/write permissions, DeepSeek API endpoint overrides, normalized JSONL results, and CLI/config/doctor integration. The Web workbench can select DeepSeek Harness and its model independently for each role. GUI computer-use and MCP support will follow in a later phase; see the CLI setup . 
 [v0.1.4 · 2026-08-11] The new Dashboard has landed: a React/FastAPI workbench you can drive entirely from the browser. Start a task, choose a backend and model per role, answer approvals, send an instruction mid-run, and stop or restart a run. Launch it with lh-harness web ; see Run a task in the browser . 
 [2026-08-10] Added the Terminal-Bench 2.1 evaluation. 
 [v0.1.3 · 2026-08-07] Every run now ends with a plain-language reply that answers your task from the verified state alone. Tasks act on the directory you launched from by default, and the console reports each round as it happens. 
 [2026-08-06] LongHorizon-Harness reaches #1 on the Hugging Face Daily Papers weekly ranking . 
 [v0.1.2 · 2026-08-06] Adds unified computer-use plugin management, stronger auditor read-only checks and role isolation, reliable process cleanup, and expanded doctor diagnostics. See Manage computer-use plugins . 
 
 
 🚀 We’re iterating rapidly. Stay tuned!

 
 Video Demo 
 
 
 
 
 
 promotional_video_1440p.mp4 
 
 

 

 
 

 Open the promotional video (1440p MP4) 

 Loop Engineering for real computer environments. 
 Give LongHorizon-Harness an outcome. It repeatedly turns the remaining work into a bounded step, performs that step on the right computer surface, checks what actually happened, and carries the verified result into the next round.

 
 
 
 flowchart LR
 S["Original goal +<br/>verified state"] --> P["Plan the next<br/>bounded step"]
 P --> A["Act in a desktop app or CLI<br/>with fresh context"]
 A --> V["Verify files, UI, logs, and tests<br/>in the real environment"]
 V -->|Pass| C["Checkpoint<br/>verified progress"]
 V -->|Fail| R["Record evidence<br/>and recover"]
 C --> D{"Task complete?"}
 R --> S
 D -->|No| S
 D -->|Yes| F["Verified result"]
 
 
 
 
 
 
 
 
 Loading 
 
 
 

 This is Loop Engineering : designing the execution, verification, correction, and recovery loop around the agent — not just the prompt for a single turn.

 One loop. Three focused responsibilities. 
 The roles are implementation boundaries inside the loop, not three agents independently growing their own versions of the task.

 
 
 
 Loop responsibility 
 Role 
 What it owns 
 
 
 
 
 🧭 State and next step 
 Manager 
 Rebuilds each round from the original goal, verified progress, failure evidence, and remaining work 
 
 
 ⚡ Action 
 Executor 
 Starts with a fresh context and completes one clearly defined step in a desktop app or the CLI 
 
 
 🔍 Ground truth 
 Auditor 
 Independently inspects the actual files, interfaces, logs, and tests instead of trusting the Executor's claim 
 
 
 
 Only results that pass independent verification become trusted task state. A rejected result remains evidence, not progress. When a context is refreshed, an action fails, or a deliverable does not pass inspection, the next round starts from the original goal and the last verified checkpoint, then continues from what remains.

 Desktop apps and CLI. One continuous task. 
 LongHorizon-Harness supports both GUI and CLI workflows.

 
 
 
 🖥️ Operate the desktop 
 ⌨️ Work in the terminal 
 
 
 
 
 🌐 Click, type, scroll, and browse 
 💻 Write and modify code 
 
 
 📊 Operate spreadsheets 
 ▶️ Run commands and scripts 
 
 
 📄 Edit documents 
 📦 Install dependencies and environments 
 
 
 🎨 Use design software 
 🔧 Configure and debug systems 
 
 
 🧊 Operate 3D tools 
 📁 Process files and data 
 
 
 
 One task can begin in a browser, move to the command line for data processing, continue in desktop software to produce an artifact, and return to the terminal for validation or debugging. The goal, progress, and evidence remain under the same state-management system throughout.

 Any model. Any agent backend. 
 LongHorizon-Harness is not tied to a specific model or agent backend. Existing models and agents connect through configuration without changing their original workflows.

 
 
 
 
 Layer 
 Supported choices 
 
 
 
 
 🧠 
 Models 
 Claude, GPT, Qwen, and other models exposed by an agent backend 
 
 
 🤖 
 Agent backends 
 Claude Code, Codex CLI, OpenCode, DeepSeek Harness ( dsh , CLI-only in phase 1), and custom AgentAdapter implementations 
 
 
 🎛️ 
 Role assignment 
 The Manager, Executor, and Auditor can each use a different model or backend 
 
 
 🖥️ 
 Execution environments 
 Local, with a pluggable Environment protocol 
 
 
 
 A lightweight AgentAdapter preserves each agent's native execution loop while LongHorizon-Harness coordinates role boundaries, verified task state, and cross-round progress around it.

 Use one model for all three roles, or combine different models and backends to balance quality, speed, and cost.

 Hundreds of real tasks. Measured gains. 
 LongHorizon-Harness is not demonstrated only on a handful of carefully selected success cases.

 We ran it on hundreds of complex tasks across GUI, CLI, and mixed computer environments:

 
 
 
 Task domain 
 What the tasks involve 
 
 
 
 
 🌐 Web Frontend 
 Developing, fixing, and validating websites and web applications through browser interaction, developer tools, and code changes 
 
 
 📊 Data Analysis & Visualization 
 Processing data, producing charts and dashboards, and checking analytical results and visual deliverables 
 
 
 🛠️ Operations & Debugging 
 Investigating logs, networks, performance, and service failures; configuring, diagnosing, and repairing systems 
 
 
 🎨 Design & Image Processing 
 Editing visual assets, matching design references, processing images, and verifying final visual quality 
 
 
 🎮 Games & Interaction 
 Building, operating, and debugging games or interactive applications; checking interaction logic and runtime behavior 
 
 
 📄 Documents & Presentations 
 Editing documents and slide decks, including content, formatting, references, layout, and final delivery 
 
 
 🧊 Spatial Reasoning 
 Completing tasks involving spatial relationships, geometry, precise placement, and 3D operations 
 
 
 🖥️ Desktop & System Settings 
 Operating desktop applications, files, and system settings across multi-application workflows 
 
 
 🔬 Research & Education 
 Completing literature research, coursework, teaching materials, forms, and research-support workflows 
 
 
 🎬 Creative Production 
 Producing presentations, video, audio, and other media while coordinating assets across tools 
 
 
 ⚙️ Engineering & Computing 
 Using CAD, EDA, scientific software, development tools, and cloud or DevOps toolchains 
 
 
 🎫 Personal Services 
 Handling event ticketing, everyday services, games, and visual-search workflows 
 
 
 🏛️ Administration & Compliance 
 Completing office, legal, policy-sensitive form, institutional, and safety-aware submission workflows 
 
 
 💼 Business & Finance 
 Handling market analysis, procurement, loans, sales, reimbursements, and cross-application enterprise workflows 
 
 
 🏥 Healthcare 
 Completing medical quality-control, insurance, immunization, and structured health-form workflows 
 
 
 
 Same model. Same execution backend. Only the harness changes. 
 
 
 
 ~50% → ~80% 
 GUI + CLI completion 

 WeaveBench 
 
 
 3×