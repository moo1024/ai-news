# CopilotKit/OpenBot — Open-source AI coworkers that each get a computer of their own: a browser, files

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/CopilotKit/OpenBot
- 발행: 2026-08-20T22:24:11.655602+00:00
- 접근상태: 확인 완료

---

GitHub - CopilotKit/OpenBot: Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 CopilotKit
 
 / 
 
 OpenBot 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 160 
 
 

 
 
 
 
 
 Star
 1.6k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 13 


 
 
 
 
 
 
 
 
 Pull requests 
 19 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Projects 
 


 
 
 
 
 
 
 
 
 Wiki 
 


 
 
 
 
 
 
 
 
 Security and quality 
 0 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Projects
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Wiki
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 23 Commits 23 Commits Folders and files Name Name Last commit message Last commit date .claude/ skills .claude/ skills     .github .github     agent-bot agent-bot     agent-computer agent-computer     agent-langgraph agent-langgraph     app app     assets assets     docs docs     examples examples     scripts scripts     server server     shared shared     spire spire     supervisor supervisor     tests tests     worker worker     .env.example .env.example     .gitattributes .gitattributes     .gitignore .gitignore     LICENSE LICENSE     README.md README.md     biome.json biome.json     bun.lock bun.lock     bunfig.toml bunfig.toml     docker-compose.yml docker-compose.yml     package.json package.json     renovate.json renovate.json     tsconfig.base.json tsconfig.base.json     View all files Repository files navigation README MIT license More items 
 OpenBot 
 AI coworkers you can hand real work to, and actually trust with the access. Each gets a computer of its own: a real browser with its own logins, its own files, and only the tools you grant. Every action decided before it happens and recorded after.

 copilotkit.ai/openbot · Quick start · Features · Bring your own agent · Architecture · Docs 

 
 
 
 

 
 
 
 
 
 
 demo-openbot.mp4 
 
 

 

 
 

 
 Bring any AG-UI agent, written on a framework or by hand, and it arrives as a
coworker with a channel of its own. Watch it work on its own screen, take the
wheel when it reaches something it should not do alone, then hand it back. It
answers with components rather than only prose, and the whole thing runs on
your own machine.

 
 
 Alpha, and under active development. OpenBot is early. Expect rough edges and bugs, and expect things to move. Issues and pull requests are welcome.

 
 
 Runs on your machine. Everything below is written for a laptop. Out of the box OpenBot runs with OPENBOT_DEV_NO_AUTH , which skips signing in and admits every request as one administrator. Google sign-in can be wired up instead.

 
 What it is 
 An agent platform that runs inside your own infrastructure. Docker Compose brings up every part of it, the data sits in your PostgreSQL, and the model is yours to choose: no model ships in the box, and an administrator supplies the credential, which is encrypted at rest and never logged.

 Three coworkers ship in the example package, and they are configuration rather than code: General Assistant for everyday work, Knowledge for company questions, Risk Analyst for risk and compliance. Add your own by editing agents.yaml or from /agents in the UI.

 Anything a Bot does to a computer, a file, an MCP server or a component goes through one gateway that decides and records it. That is the difference between an agent that can use your tools and an agent you can let near them.

 More at copilotkit.ai/openbot .

 Built on AG-UI 
 A Bot is any endpoint speaking AG-UI , the open protocol for agent-to-user interaction, so OpenBot is not tied to a framework and neither are you. Agents built with LangGraph, Mastra, CrewAI, Pydantic AI, Google ADK or written by hand all arrive the same way, and the governance rides the protocol rather than the framework.

 
 
 
 
 Requirements 
 
 Docker, for PostgreSQL, browser computers, the supervisor, and the shipped Bots. 
 Bun 1.3+, for the app and API server. 
 A CopilotKit Intelligence project and license. A free plan is available, and Intelligence can be self-hosted. 
 A model key. The proof-of-concept Bot uses OpenAI; the LangGraph Bot can use OpenAI, Anthropic, or Google. 
 
 Quick start 
 
 
 Create .env :

 cp .env.example .env 
 
 
 Get CopilotKit Intelligence credentials:

 npx --yes copilotkit@latest login
npx --yes copilotkit@latest project select 
npx --yes copilotkit@latest license --write 
 Put the cpk-... runtime key from project select in .env as
 INTELLIGENCE_API_KEY . license --write writes
 COPILOTKIT_LICENSE_TOKEN into the existing .env .

 
 
 Fill the remaining required values:

 
 OPENAI_API_KEY 
 
 Keep the managed Intelligence URLs from .env.example unless you run Intelligence yourself. The example KEY_ENCRYPTION_KEY is public and fine locally; generate your own with:

 openssl rand -base64 32 
 
 
 Install and run:

 bun install
bash scripts/start.sh 
 
 
 Open http://localhost:3010 .

 
 
 scripts/start.sh starts Docker services, applies migrations, starts the API server on port 3001, starts the app on port 3010, and checks that the services answer their own health routes before printing next steps.

 Try it 
 
 Open /bot and ask: Open news.ycombinator.com and tell me the top story. 
 Ask the Bot to fill out https://httpbin.org/forms/post , then inspect /admin/audit . 
 Open /admin/boundaries , add a deny rule or preset, and retry the same browser action. 
 Create a coworker from /agents , give it a standing role, and start a channel with it. 
 
 Main surfaces 
 
 
 
 Route 
 Purpose 
 
 
 
 
 / 
 Start and browse channels. 
 
 
 /agents 
 Create, edit, duplicate, hide, delete, and launch coworkers. 
 
 
 /channel/:id 
 Converse with one coworker and view its live screen/profile panel. 
 
 
 /bot 
 Direct chat with a Bot; ?agent=<id> selects one. 
 
 
 /skills 
 Create and enable personal skills. 
 
 
 /settings 
 User preferences. 
 
 
 /admin/connectors 
 Configure deployment knowledge sources. 
 
 
 /admin/credentials 
 Store write-only encrypted credentials. 
 
 
 /admin/computers 
 View, stop, and reset Bot computers. 
 
 
 /admin/boundaries 
 Configure browser/file/MCP action policy. 
 
 
 /admin/components 
 Publish components and govern which Bots may use them. 
 
 
 /admin/playground 
 Draft and publish sandboxed components in the browser. 
 
 
 /admin/plugins 
 Configure MCP servers, MCP grants, and deployment skills. 
 
 
 /admin/audit 
 Review permitted, refused, and failed actions. 
 
 
 
 Features 
 
 A computer per Bot : the supervisor gives each Bot its own container, its own /workspace volume and its own browser profile. Set COMPUTER_RUNTIME=runsc to run them under gVisor where the host supports it. 
 The gateway is the only way in : it resolves the target from a server-held snapshot, evaluates the policy, writes the audit row, and only then calls the computer. There is no path that acts without the record existing first. 
 CEL policy, fail closed : rules can inspect tool.name , intent , bot.id , actor.id , page.url , page.host , element.* , key , file.* and mcp.* . Deny is evaluated before allow, a missing policy permits nothing, and a broken rule refuses rather than opens. 
 Take the wheel : a Bot that hits a login wall or a 2FA prompt asks for help. Control is handed over in the same panel and recorded as computer.help_requested , computer.control_taken and computer.control_released . While a person is driving, Bot actions are refused rather than queued. 
 Secrets never enter the transcript : the trail records that a secret was requested and how long it was, not what it said. 
 Bring your own agent : any AG-UI endpoint is a Bot, on a framework or hand written. Endpoints are validated with the same target checks used for browser navigation, and an auth header is stored write-only. 
 Components instead of prose : compiled React components live in app/src/components/gallery/ , sandboxed ones are authored in /admin/playground and published with no deployment. Every call asks the server whether the component exists, is published, and is not withheld from that Bot. Data functions are granted per component. 
 Governed MCP : a curated catalogue ships for Atlassian, Box, Slack, Salesforce and ServiceNow. Custom servers must pass URL checks, and any tool not positively classified as a read is treated as a write. 
 Skills are instructions, not capabilities : personal skills attach only to Bots their author owns, deployment skills are admin-owned, and both are invoked with / in the composer. 
 An audit trail you can read : /admin/audit lists what was permitted, what was refused and what failed, and every refusal carries the rule that caused it. 
 Credentials encrypted at rest : stored through /admin/credentials , never returned by an API, and redacted from audit events. 
 Loopback by default : computers bind to 127.0.0.1 and require a per-container token, so nothing reaches a logged-in browser by knowing its port. 
 Durable threads and memory : conversations survive restarts through CopilotKit Intelligence, and each deployment stamps the threads it owns. 
 
 Bring your own agent 
 Any AG-UI endpoint can be a Bot.

 From /agents , create a coworker with:

 
 name, title, and role description; 
 private or public visibility; 
 optional AG-UI endpoint; 
 optional write-only authorization header. 
 
 The server validates agent endpoints with the same target checks used for browser navigation. If no custom endpoint is set, product-created coworkers use MANAGED_AGENT_AG_UI_URL .

 Tenant package agents are declared in agents.yaml as either:

 
 built-in , with a system prompt; or 
 remote-ag-ui , with an endpoint. 
 
 See docs/configuration.md and docs/coworkers.md .

 Configuration 
 .env.example is the source template. The API server refuses to start without:

 
 DATABASE_URL 
 KEY_ENCRYPTION_KEY 
 MANAGED_AGENT_AG_UI_URL 
 INTELLIGENCE_API_URL 
 INTELLIGENCE_GATEWAY_WS_URL 
 INTELLIGENCE_API_KEY 
 COPILOTKIT_LICENSE_TOKEN 
 
 Settings worth knowing:

 
 
 
 Variable 
 Use 
 
 
 
 
 OPENBOT_DEV_NO_AUTH 
 Admits every request as one administrator. How OpenBot runs today. 
 
 
 OPENAI_BASE_URL 
 Answers the OpenAI-shaped calls from somewhere else: a gateway, a proxy. 
 
 
 ANTHROPIC_BASE_URL , GOOGLE_GENERATIVE_AI_BASE_URL 
 The same, for those two APIs. 
 
 
 COMPUTER_TOKEN 
 Secret every Bot computer request must present. start.sh sets one. 
 
 
 SUPERVISOR_TOKEN 
 Secret the supervisor requires. start.sh sets one. 
 
 
 COMPUTER_SUPERVISOR_URL 
 Gives each Bot a computer of its own instead of one shared computer. 
 
 
 COMPUTER_RUNTIME 
 Set to runsc to run computers under gVisor, where the host has it. 
 
 
 AGENT_COMPUTER_POLICY 
 JSON action policy. Malformed JSON stops server startup. 
 
 
 AGENT_COMPUTER_ALLOW_PRIVATE_HOSTS 
 Lets a Bot reach this machine's own services. 
 
 
 TENANT_PACKAGE_DIR 
 Directory containing tenant YAML. Defaults to ../examples/fintech . 
 
 
 DEPLOYMENT_ID 
 Names this deployment when 