# Show HN: Self-hosted company OS, Claude Code and Codex agents in departments

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://github.com/OtoDock/oto-dock
- 발행: 2026-09-09T17:57:55+00:00
- 접근상태: 확인 완료

---

GitHub - OtoDock/oto-dock: Your personal AI agent platform — self-hosted, BYO Claude/Codex subscription · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 OtoDock
 
 / 
 
 oto-dock 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 10 
 
 

 
 
 
 
 
 Star
 128 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 2 


 
 
 
 
 
 
 
 
 Pull requests 
 1 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 43 Commits 43 Commits Folders and files Name Name Last commit message Last commit date .github .github     audio audio     dashboard dashboard     mcps mcps     phone phone     proxy proxy     satellite satellite     scripts scripts     .dockerignore .dockerignore     .gitattributes .gitattributes     .gitignore .gitignore     CHANGELOG.md CHANGELOG.md     CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     SECURITY.md SECURITY.md     VERSIONS.md VERSIONS.md     config.env.example config.env.example     docker-compose.build.yml docker-compose.build.yml     docker-compose.phone.yml docker-compose.phone.yml     docker-compose.t1.yml docker-compose.t1.yml     docker-compose.yml docker-compose.yml     ruff.toml ruff.toml     View all files Repository files navigation README Code of conduct Contributing License Security More items 
 


 OtoDock — Collaborative Agents 

 The agentic company OS. 
 
 The brains of your company, built on Claude Code & Codex, working on your Anthropic and OpenAI subscriptions.


 
 
 
 
 
 


 
 Docs ·
 Install ·
 Features ·
 Discussions 




 
 Self-hosted · Multi-tenant by design · Fair source 

 Runs on  Claude Code · Codex · your API keys · local models 




 
 


 Dashboard highlights. The two-minute video tells the whole story. 

 If OtoDock is useful to you, a star on this repository helps other people find it.

 
 Why OtoDock 
 OtoDock acts as the brain of your company. You create powerful agents that
connect to the tools your company runs on, work in departments, delegate to
each other, and keep working on their own when no one is watching. It is
multi-tenant by design. Many people work with the same agents, and there
are four modes that decide how an agent is shared and where its work lands.
You work with your agents on your self-hosted dashboard, or you can even
give them a phone line and talk to them. All of it runs on your own
Anthropic and OpenAI subscriptions, and on local models.

 Build your own AI agents 
 Every agent gets a name and a job, like a Personal Assistant, a System Admin
or a Marketing Manager, and runs on your server. An agent is made of six
parts, and you can edit every one of them.

 
 Persona. Plain-language instructions tell the agent who it is and how
it works. 
 Memory. The agent keeps its own notes across chats. 
 Workspace. The folder where the everyday work lands. It is private for
each person, shared by the whole team, or both, depending on the agent's
mode. 
 Knowledge. Reference documents are always on hand. 
 Skills. The agent learns techniques it can apply to its work. 
 Tools. The agent uses only what it is allowed to use. 
 
 
 


 Four ways to share one agent 
 Every agent has a mode that decides how people share it.

 
 
 
 Mode 
 What it means 
 
 
 
 
 Personal only 
 A private workspace for each person. 
 
 
 Personal + shared 
 A private workspace for each person as the default, and a shared one for the team. 
 
 
 Shared + personal 
 A shared team workspace as the default for everyday work, plus a private one per person. 
 
 
 Shared only 
 Everyone shares one history and one workspace. 
 
 
 
 Everyone gets the right seat 
 Admins add each person to the agents they need.

 
 
 
 Three platform roles 
 Three roles on every agent 
 
 
 
 
 An Admin runs the platform. 
 A Manager has full control of the agent. 
 
 
 A Creator creates agents. 
 An Editor edits the shared files. 
 
 
 A Member uses the agents they are given. 
 A Viewer chats and reads the shared files. 
 
 
 
 Claude Code or Codex. Your subscription. 
 Claude Code runs on your Anthropic subscription, and Codex runs on your
ChatGPT subscription. Every user connects their own subscription. Local
models on your own hardware work as well. You pick the engine per agent,
and you can switch it per chat.

 
 


 They work while you are away 
 Agents run on any schedule, when a webhook event fires, or once at a time
you choose. They work in your workspace, where their reports, files and
updates land, and they notify you when something needs you. Notifications
come in four severities, from a quiet chime to a persistent danger alarm.
Every run is a full chat you can open, read and continue, so no one has to
be watching.

 
 


 Give an agent a phone number 
 Agents answer and place phone calls. Bring your own Twilio account, or
connect the Asterisk or FreePBX server you already run.

 
 


 Runs on your server. Works on your machines. 
 By default, all your agents run on your server, in an isolated sandbox, with
one dashboard controlling all of them. You can also pair a laptop, a
workstation or a PC running macOS, Linux or Windows with a one-line install.
The machine keeps a single outbound connection to your server, so it needs
no open ports, and its files stay in sync. The same agent then runs on that
machine with full access to it, and you work with it from the same
dashboard, anywhere. If the machine goes offline, your server takes over.

 
 


 Your own cloud of agents. 
 The two-minute video 
 
 
 
 
 
 hero-v8-web.mp4 
 
 

 

 
 

 This entire video was directed, captured and edited by an OtoDock agent.
 Watch it in full quality on otodock.io . 

 The company, running 
 
 
 
 
 
 
 Departments. Organize your agents into departments, decide who can delegate to whom, or put them in a meeting together. 
 Live dashboards. Every agent gets live dashboards, so you can manage them effortlessly. 
 
 
 
 
 
 
 Endless tools. Your agents are digital employees. They connect to endless tools, from your calendar to your smart home. 
 Documents. They edit Excel, Word and PowerPoint files right in the chat. 
 
 
 
 
 
 
 Artifacts. Agents answer with live, interactive UI, rendered right in the chat. 
 Meetings. Specialist agents discuss a topic together and converge on an answer, live in the dashboard. 
 
 
 
 
 
 
 Terminal. The Claude Code or Codex terminal opens in the dashboard, with the agent's tools already loaded. 
 Remote machines. The same agent, with all its tools and its synced workspace, runs on any machine you pair with one command, and it can use everything on that machine. 
 
 
 Locked down by default 
 Agents are powerful, so OtoDock assumes they can't be trusted. Every
server-side agent runs inside a kernel sandbox with always-on network
isolation, and you grant access one service at a time.

 
 A kernel sandbox around every agent. Each session runs in its own
mount and process namespace. Folders are mounted automatically from each
user's role per agent. 
 Network isolation. Private ranges, your LAN, and cloud metadata
endpoints are unreachable by design. MCP tools that need a local service
can be granted scoped access by the admin, per agent. 
 Secure credentials. Credentials are encrypted at rest and injected
only per session. Agents can use them, but never see them. 
 Ready for teams. SSO sign-in, two-factor auth, and per-user cost
budgets come standard, from the first install. 
 
 Read the security model → 

 Everything included 
 One platform, the whole toolkit.

 
 Memory that persists. Agents keep transparent, editable memory files,
per user and per agent. 
 Documents and files. Agents create and edit Word, Excel, PowerPoint
and PDF files, and every file opens in a live editor inside the chat. 
 Images. Agents generate and edit images in the chat, and a
professional-grade pipeline handles photo editing. 
 Video and audio. Agents generate footage and transitions, cut
timelines, add captions, voice-overs and music, transcribe audio and video
into text and subtitles, and produce speech and music of their own. 
 Web browsing. The browser tool from the community catalog lets agents
research the live web. 
 Built-in tools. Schedules, triggers, notifications, meetings,
delegation, phone calls, file transfer between agents, live charts and
mini-apps, SSH hosts, and browser and computer control on paired machines
all ship with the platform. 
 Community catalog. Ready-made agents, tools and skills install in one
click, with GitHub, Notion, Home Assistant, Nextcloud, Prometheus, UniFi
and Uptime Kuma among them, and more landing regularly. 
 Extensible by design. Any MCP tool server installs from a manifest,
and tools are assigned per agent. 
 Usage and budgets. Costs are tracked per user and per agent, with
weekly or monthly limits. 
 Team-ready security. SSO and OIDC, two-factor auth, per-agent roles,
encrypted credentials and scoped API keys come from day one. 
 
 See all features at otodock.io/features .

 Quick start 
 A Linux server with Docker is all you need (4 GB RAM minimum, see the
 sizing guide ).
Create a folder for the install, then run the script in it:

 mkdir otodock && cd otodock
curl -fsSLO https://raw.githubusercontent.com/OtoDock/oto-dock/main/scripts/install.sh
bash install.sh 
 The installer checks Docker, writes a .env with a generated database
password, handles the Ubuntu 24.04+ host step automatically when the host
needs it, downloads the release-pinned docker-compose.yml plus the
phone-service overlay, and starts the stack. Everything lands in the folder
you run it from. The script performs fresh installs only, and stops rather
than touch an existing install.

 If your users browse to the server by name or IP, set DASHBOARD_PUBLIC_URL 
in the generated .env . Behind a reverse proxy, also set TRUSTED_PROXY to
your proxy's IP
( reverse proxy & HTTPS ).
Every optional knob is documented in the
 Configuration reference ,
and the installation guide 
also covers building from source, bare-metal development, and running
behind a reverse proxy with HTTPS.

 The first five minutes 
 Open http://localhost:8400 and the setup wizard greets you. Create the
owner account, and OtoDock installs the Personal Assistant for you, with the
tools it needs. Connect your Claude or ChatGPT subscription under Setup,
AI Engines, and the banner that reminds you goes away. Open the Personal
Assistant from the Agents page and send it your first message. Its reply
streams in live, with every tool call and every file it creates
( First run ). From there
you add agents from the community catalog or build your own, and you add
the people who will work with them.

 How it fits together 
 dashboard/ React dashboard — chat, agents, tasks, files, admin
 proxy/ Platform core (FastAPI) — sessions, security, scheduling,
 the agent sandbox, and the WebSocket hub th