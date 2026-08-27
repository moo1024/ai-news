# CEO fired developers to make room for AI. Developers create open source AI CEO

- 출처: Hacker News
- 원본 링크: https://github.com/SenteLabsAI/OpenExecutive
- 발행: 2026-08-27T01:46:22+00:00
- 접근상태: 확인 완료

---

GitHub - SenteLabsAI/OpenExecutive: AI-powered virtual executive team — a single coherent executive persona backed by 8 specialist Claude agents (FastAPI + Next.js). · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 SenteLabsAI
 
 / 
 
 OpenExecutive 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 96 
 
 

 
 
 
 
 
 Star
 1.5k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 3 


 
 
 
 
 
 
 
 
 Pull requests 
 11 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 16 Commits 16 Commits Folders and files Name Name Last commit message Last commit date .claude .claude     .github .github     .vscode .vscode     docker docker     docs docs     evals evals     fixtures fixtures     packages packages     scripts scripts     .dockerignore .dockerignore     .env.example .env.example     .gitignore .gitignore     CHANGELOG.md CHANGELOG.md     CLAUDE.md CLAUDE.md     LICENSE LICENSE     Makefile Makefile     README.md README.md     SECURITY.md SECURITY.md     fly.api.qa.toml fly.api.qa.toml     fly.api.toml fly.api.toml     fly.honcho.toml fly.honcho.toml     fly.ui.qa.toml fly.ui.qa.toml     fly.ui.toml fly.ui.toml     View all files Repository files navigation README Code of conduct Contributing License Security More items Open Executive 
 
 
 
 

 An AI system that acts as your company's virtual executive team — a senior advisor with Harvard MBA-level knowledge, customized for your specific business.

 Demo 
 

 A walkthrough of Open Executive in action — watch on YouTube .

 What It Does 
 Developed by sentelabs.ai Open Executive provides a single coherent executive voice backed by eight specialist AI agents:

 
 Chief Strategy Officer — competitive analysis, M&A, market positioning, OKRs 
 Chief Financial Officer — financial modeling, fundraising, unit economics, cash flow 
 Chief HR/People Officer — hiring, compensation, performance, culture 
 General Counsel — contracts, IP, employment law basics, compliance 
 Chief Operating Officer — process design, vendor management, operational scaling 
 Chief Marketing Officer — GTM strategy, brand, communications, PR 
 Chief Product Officer — roadmap, prioritization, product strategy 
 Board Communications Director — board decks, investor relations, governance 
 
 All responses come from one consistent executive voice. The internal agent architecture is never exposed to the user. Beyond Q&A, the system maintains episodic memory of past decisions and initiatives across sessions, and a built-in scheduler can proactively surface follow-ups and time-sensitive actions.

 Architecture 
 User message
 ↓
Executive Orchestrator (claude-sonnet-4-6)
 ↓ tool use → parallel specialist calls
CSO / CFO / CHRO / GC / COO / CMO / CPO / Board
 ↓ each specialist retrieves relevant context from ChromaDB
Built-in MBA knowledge + Your company documents
 ↓
Synthesized executive response
 
 Knowledge — Two retrieval layers per specialist call: (1) built-in MBA-level Markdown ( knowledge/builtin/ , git-tracked) seeded into ChromaDB at startup, and (2) your uploaded company documents chunked and stored in a separate company_docs collection. RAG context is injected into the user turn, never the cached system prompt.

 Episodic memory — After every response, a background claude-haiku-4-5 pass extracts key decisions, initiatives, and advice into SQLite. The next session opens with a <past_decisions> block so the Executive remembers what it recommended last month.

 Scheduler — A built-in job runner claims due actions via UPDATE … RETURNING to prevent double-firing. The API must run as a single instance; do not horizontally scale it without gating the scheduler first.

 Prompt caching — The system prompt is structured so the Executive persona, company profile, and knowledge index are cached separately (up to 85% cache hit rate after the first few turns). No dynamic content ever goes in a cached block.

 See docs/architecture.md for the full design.

 Tech Stack 
 
 
 
 Layer 
 Choice 
 
 
 
 
 LLM backbone 
 Anthropic Claude API 
 
 
 Default model 
 claude-sonnet-4-6 (Executive + most specialists) 
 
 
 Deep reasoning 
 claude-opus-4-7 (CSO, CFO, GC, Board — with extended thinking) 
 
 
 Backend 
 Python 3.11 + FastAPI 
 
 
 Package manager 
 uv 
 
 
 Vector store 
 ChromaDB (local, embedded) 
 
 
 Episodic memory 
 SQLite 
 
 
 Web UI 
 Next.js 15 (App Router) + Tailwind 
 
 
 License 
 Apache 2.0 
 
 
 
 Repo Layout 
 openexecutive/
├── packages/
│ ├── core/
│ │ └── openexecutive/
│ │ ├── orchestrator/ # Executive persona + routing loop
│ │ ├── agents/ # 8 specialist agents
│ │ ├── knowledge/ # ChromaDB store + RAG pipeline
│ │ ├── memory/ # Company profile + episodic memory
│ │ ├── onboarding/ # Wizard state machine + profile builder
│ │ ├── prompts/ # Persona + domain prompts + cache manager
│ │ ├── api/ # FastAPI app + routes
│ │ ├── integrations/ # Slack, Email, Telegram, Google Chat, Discord
│ │ ├── scheduler/ # Background job runner (single-instance)
│ │ ├── alerts/ # Proactive alert system
│ │ ├── audit/ # Audit logging
│ │ ├── architecture/ # Internal architecture utilities
│ │ ├── workflows/ # Multi-step workflow definitions
│ │ └── cli.py # Click CLI
│ └── ui/ # Next.js 15 web UI
├── evals/ # Eval scenarios + LLM-as-judge runner
├── fixtures/ # Demo company fixtures (profiles, docs, rosters)
├── scripts/ # Operator scripts (Fly secrets, Google auth)
├── docker/ # Dockerfile(s) + docker-compose.yml
├── fly.api.toml / fly.ui.toml # Fly.io configs — dev API + UI apps
├── fly.api.qa.toml / fly.ui.qa.toml # Fly.io configs — QA API + UI apps
├── fly.honcho.toml # Fly.io config — Honcho memory app (optional)
└── docs/ # Architecture + deployment docs
 
 Quick Start 
 # Clone the repo 
git clone https://github.com/SenteLabsAI/OpenExecutive.git
 cd OpenExecutive

 # Set your Anthropic API key 
cp .env.example .env
 # Edit .env and add ANTHROPIC_API_KEY=sk-ant-... 

 # Start everything 
make dev 
 Open http://localhost:3000 to start chatting with your executive. The API runs on port 8000 and the UI on 3000.

 
 First run: requires Python 3.11+ and Node 22+. The initial uv sync pulls heavy
ML dependencies (ChromaDB + sentence-transformers/PyTorch), and the first boot
downloads a small embedding model (~90 MB) to build the local vector index — so the
first make dev takes a few minutes before the app is ready. Subsequent starts are fast.

 
 For contributors not using make : 

 cd packages/core
uv sync
 source .venv/bin/activate
uvicorn openexecutive.api.main:app --reload --port 8000

 # In a second terminal 
 cd packages/ui && npm install && npm run dev 
 Run the Discord Bot 
 
 Create a Discord application at https://discord.com/developers/applications 
 Enable the Message Content privileged intent (Bot → Privileged Gateway Intents) 
 Invite the bot with bot + applications.commands scopes 
 Set env vars in .env : DISCORD_BOT_TOKEN , DISCORD_APP_ID , DISCORD_GUILD_IDS 
 Run the API normally — the bot starts as part of the FastAPI lifespan when DISCORD_BOT_TOKEN is set: 
 
 make dev 
 The bot is embedded in the API process (alongside the email poller, scheduler, and resumer) so it shares the same SQLite database and ChromaDB vector store under /data in production. Skip the token to disable.

 For iterating on bot-only code without restarting the API, make discord runs the bot as a standalone process against the same local DB.

 Users can DM the bot, @mention it in a channel (replies in a thread), or use /ask and /today slash commands. Slash commands sync to DISCORD_GUILD_IDS instantly on startup; leave blank for global registration (up to 1-hour propagation delay).

 Deploying to production 
 Just set the secrets on the existing API app — no new Fly app required:

 flyctl secrets set -a openexec-api-dev \
 DISCORD_BOT_TOKEN=... \
 DISCORD_APP_ID=... \
 DISCORD_GUILD_IDS=... 
 Discord user access is managed via the /people UI — add a Person row with discord_user_id set.

 The machine restarts and the bot starts on the next lifespan boot. To disable in prod: flyctl secrets unset -a openexec-api-dev DISCORD_BOT_TOKEN .

 Onboarding Your Company 
 The first time you visit the app, you'll be guided through a wizard to set up your company profile:

 
 Company basics (name, industry, stage, team size) 
 Business model and revenue 
 Competitive landscape 
 Strategic priorities 
 Culture and values 
 Optional: financial position, document upload 
 
 After onboarding, the Executive will reference your specific company context in every response.

 Interfaces 
 
 
 
 Interface 
 How to Use 
 
 
 
 
 Web UI 
 http://localhost:3000 
 
 
 Slack 
 Mention @OpenExecutive or DM the app 
 
 
 Email 
 CC or email the configured address (IMAP/SMTP poller) 
 
 
 Telegram 
 Message the configured bot 
 
 
 Google Chat 
 Mention the app in a space 
 
 
 Discord 
 DM the bot, @mention it in a channel, or use /ask / /today slash commands 
 
 
 CLI 
 openexecutive chat 
 
 
 
 Document Upload 
 Upload your pitch deck, financial model, strategy docs, or any company documents via the web UI or API. The Executive will reference them when relevant.

 # Via CLI 
openexecutive upload deck.pdf model.xlsx strategy.md

 # Via API 
curl -X POST http://localhost:8000/documents \
 -F " file=@deck.pdf " \
 -F " domain=strategy " 
 Deployment (Fly.io) 
 Two environments, each a separate set of Fly apps, driven by branch:

 
 
 
 Environment 
 Trigger 
 Workflow 
 Apps 
 
 
 
 
 dev 
 push/merge to main (continuous) 
 .github/workflows/deploy.yml 
 openexec-api-dev , openexec-ui-dev 
 
 
 qa 
 push/merge to qa (deliberate promotion) 
 .github/workflows/deploy-qa.yml 
 openexec-api-qa , openexec-ui-qa 
 
 
 
 Both workflows use dorny/paths-filter to deploy only the changed app (API, UI, or both). QA is a stable twin of dev — same image and runtime, only the app name differs ( fly.api.qa.toml / fly.ui.qa.toml ) — so it lags main and stays vetted. An optional Honcho memory app ( fly.honcho.toml ) deploys independently.

 Topology 
 
 
 
 App 
 Purpose 
 State 
 
 
 
 
 openexec-api-{dev,qa} 
 FastAPI + scheduler 
 Persistent volume executive_data at /data 
 
 
 openexec-ui-{dev,qa} 
 Next.js 15 
 Stateless 
 
 
 openexec-honcho-dev 
 Honcho per-person memory (optional) 
 Postgres-backed 
 
 
 
 
 ⚠️ Single-instance only : The scheduler claims rows via UPDATE … RETURNING . Running two API machines would double-fire scheduled actions. max_machines_running = 1 is set in fly.api.toml / fly.api.qa.toml — do not override it.

 
 Required GitHub Actions secrets 
 Deploys authenticate with per-app Fly deploy tokens stored as repo (or org) Actions secrets. Generate each with flyctl tokens create deploy -a <app> -x 999999h :

 
 
 
 Secret 
 App 
 Used by 
 
 
 
 
 FLY_API_TOKEN_API 
 openexec-api-dev 
 dev 
 
 
 FLY_API_TOKEN_UI 
 openexec-ui-dev 
 dev 
 
 
 FLY_API_TOKEN_HO