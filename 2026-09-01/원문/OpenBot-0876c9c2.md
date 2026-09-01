# CopilotKit/OpenBot — Open-source AI coworkers that each get a computer of their own: a browser, files

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/CopilotKit/OpenBot
- 발행: 2026-09-01T03:54:36.330680+00:00
- 접근상태: 확인 완료

---

GitHub - CopilotKit/OpenBot: Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
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
 452 
 
 

 
 
 
 
 
 Star
 3.6k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 6 


 
 
 
 
 
 
 
 
 Pull requests 
 8 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 178 Commits 178 Commits Folders and files Name Name Last commit message Last commit date .claude/ skills .claude/ skills     .github .github     agent-bot agent-bot     agent-computer agent-computer     agent-langgraph agent-langgraph     app app     assets assets     charts/ openbot charts/ openbot     docker/ s6 docker/ s6     docs docs     examples examples     scripts scripts     server server     shared shared     spire spire     supervisor supervisor     tests tests     worker worker     .dockerignore .dockerignore     .env.example .env.example     .gitattributes .gitattributes     .gitignore .gitignore     CHANGELOG.md CHANGELOG.md     Dockerfile Dockerfile     LICENSE LICENSE     README.md README.md     biome.json biome.json     bun.lock bun.lock     bunfig.toml bunfig.toml     docker-compose.yml docker-compose.yml     package.json package.json     prompt.txt prompt.txt     renovate.json renovate.json     tsconfig.base.json tsconfig.base.json     View all files Repository files navigation README MIT license More items 
 OpenBot 
 AI coworkers you can hand real work to, and actually trust with the access. Each gets a computer of its own: a real browser with its own logins, its own files, and only the tools you grant. Every action decided before it happens and recorded after.

 copilotkit.ai/openbot · Quick start · Features · Bring your own agent · Architecture · Docs 

 
 
 
 

 
 
 
 
 
 
 demo-openbot.mp4 
 
 

 

 
 

 
 Bring any AG-UI agent, written on a framework or by hand, and it arrives as a
coworker with a channel of its own. Watch it work on its own screen, take the
wheel when it reaches something it should not do alone, then hand it back. It
answers with components rather than only prose, and the whole thing runs on
your own machine.

 
 
 A template, not a product. OpenBot is meant to be cloned and made your own. There is no hosted version to sign up for, and nothing here is published as a package to depend on: every workspace in this repository is private. You take the repository, replace the example tenant package under examples/ with your own coworkers, channels and skills, and run it. Everything below describes a starting point, not a finished thing somebody operates for you.

 
 
 Alpha, and under active development. OpenBot is early. Expect rough edges and bugs, and expect things to move. Issues and pull requests are welcome.

 
 
 Runs on your machine. Everything below is written for a laptop. .env.example carries OPENBOT_SINGLE_USER=true , which admits every request as one administrator, so a fresh clone reaches the product without registering an OAuth client first. Sign-in turns that off, and is required before anybody else can reach the deployment.

 
 What it is 
 An agent platform that runs inside your own infrastructure. Docker Compose brings up every part of it, the data sits in your PostgreSQL, and the model is yours to choose: no model ships in the box, and an administrator supplies the credential, which is encrypted at rest and never logged.

 Three coworkers ship in the example package, and they are configuration rather than code: General Assistant for everyday work, Knowledge for company questions, Risk Analyst for risk and compliance. Add your own by editing agents.yaml or from /agents in the UI.

 Anything a Bot does to a computer, a file, an MCP server or a component goes through one gateway that decides and records it. That is the difference between an agent that can use your tools and an agent you can let near them.

 More at copilotkit.ai/openbot .

 Built on AG-UI 
 A Bot is any endpoint speaking AG-UI , the open protocol for agent-to-user interaction, so OpenBot is not tied to a framework and neither are you. Agents built with LangGraph, Mastra, CrewAI, Pydantic AI, Google ADK or written by hand all arrive the same way, and the governance rides the protocol rather than the framework.

 
 
 
 
 Requirements 
 
 Docker, for PostgreSQL and the shipped Bots. 
 Bun 1.3+, for the app and API server. 
 A CopilotKit Intelligence project and license. A free plan is available, and Intelligence can be self-hosted. 
 A model key. The proof-of-concept Bot uses OpenAI; the LangGraph Bot can use OpenAI, Anthropic, or Google. 
 
 Quick start 
 
 Setting up with an AI assistant? Paste prompt.txt into it first. It carries the
same steps as below plus the things that are easy to get wrong: which of the ten blank keys in
 .env.example are actually yours to fill (three), which the start script generates for you, and
what each start-up refusal means. Every claim in it is checked against this repository.

 
 
 
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

 Deploy it 
 One image carries the app, the API, the browser the Bots drive, and optionally PostgreSQL. Same
 .env , no Kubernetes.

 docker build -t openbot . 
docker run -p 3001:3001 --env-file .env \
 -e EMBEDDED_POSTGRES=on -v openbot-data:/var/lib/postgresql openbot 
 Leave EMBEDDED_POSTGRES off and set DATABASE_URL to point at a database you already run.
 docs/deployment.md has the minimum sizes, the platform notes, and how it behaves behind more than one replica.

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
 Converse with one coworker, watch its screen, and see what it ran. 
 
 
 /bot 
 Direct chat with a Bot; ?agent=<id> selects one. 
 
 
 /skills 
 Create and enable personal skills. 
 
 
 /settings 
 User preferences. 
 
 
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
 A shell, not just a browser : a Bot can run a command in its workspace, install what it needs, and process a file it saved. Through the same gate as everything else, so a rule can refuse a shell outright or refuse particular commands, and the command is on the record either way. The command inherits PATH, locale, terminal and proxy variables, not the rest of the deployment's environment. 
 The gateway is the only way in : it resolves the target from a server-held snapshot, evaluates the policy, writes the audit row, and only then calls the computer. There is no path that acts without the record existing first. 
 CEL policy, fail closed : rules can inspect tool.name , intent , bot.id , actor.id , page.url , page.host , element.* , key , file.* and mcp.* . Deny is evaluated before allow, a missing policy permits nothing, and a broken rule refuses rather than opens. 
 Watch what it is doing : the screen shows what a Bot is looking at, and the Activity tab beside it shows what it ran, read and saved, with the output. A command line in the transcript opens to the same thing. A saved file shows its path and size, never its contents. 
 Take the wheel : a Bot that hits a login wall or a 2FA prompt asks for help. Control is handed over in the same panel and recorded as computer.help_requested , computer.control_taken and computer.control_released . While a person is driving, Bot actions are refused rather than queued. 
 Secrets never enter the transcript : the trail records that a secret was requested and how long it was, not what it said. 
 Bring your own agent : any AG-UI endpoint is a Bot, on a framework or hand-written. Endpoints are validated with the same target checks used for browser navigation, and an auth header is stored write-only. 
 Components instead of prose : compiled React components live in app/src/components/gallery/ , sandboxed ones are authored in /admin/playground and published with no deployment. Every call asks the server whether the component exists, is published, and is not withheld from that Bot. Data functions are granted per component. 
 Governed MCP : Google Drive and Notion ship in the catalogue, reached as the person asking. The catalogue carries only vendors this deployment stands behind, so adding one is a review of that vendor. Custom servers must pass URL checks; unknown tools and custom-server tools are treated as writes, and a catalogue tool the server advertises but does not name as a write classifies as a read. A Bot is told which connectors exist here and which it holds, so it says it has not been granted one rather than browsing to the vendor's website. 
 Skills are instructions, not capabilities : personal skills attach only to Bots their author owns, deployment skills are admin-owned, and both are invoked with / in the composer. 
 Sign in with wh