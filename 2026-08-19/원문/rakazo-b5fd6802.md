# elie222/rakazo — Open-source Grok Bot alternative. Choose your own model and sandbox.

- 출처: GitHub 신규 (AI 에이전트)
- 원본 링크: https://github.com/elie222/rakazo
- 발행: 2026-08-19T03:34:26.738684+00:00
- 접근상태: 확인 완료

---

GitHub - elie222/rakazo: Open-source Grok Bot alternative. Choose your own model and sandbox. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 elie222
 
 / 
 
 rakazo 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 107 
 
 

 
 
 
 
 
 Star
 856 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 8 


 
 
 
 
 
 
 
 
 Pull requests 
 10 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 116 Commits 116 Commits Folders and files Name Name Last commit message Last commit date .agents/ skills/ composio .agents/ skills/ composio     .github .github     apps apps     docs docs     infra infra     packages packages     scripts scripts     .dockerignore .dockerignore     .env.example .env.example     .gitignore .gitignore     .npmrc .npmrc     AGENTS.md AGENTS.md     CHANGELOG.md CHANGELOG.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     SECURITY.md SECURITY.md     SETUP_PROMPT.md SETUP_PROMPT.md     biome.json biome.json     package.json package.json     pnpm-lock.yaml pnpm-lock.yaml     pnpm-workspace.yaml pnpm-workspace.yaml     skills-lock.json skills-lock.json     tsconfig.base.json tsconfig.base.json     turbo.json turbo.json     vitest.config.ts vitest.config.ts     View all files Repository files navigation README Contributing Apache-2.0 license Security More items Rakazo 
 
 

 

 Rakazo is an open-source platform for running persistent AI teammates. It is available on the web,
as an Electron desktop app, and through an Expo mobile app. Bring your own model and computer
provider, or run the complete stack locally.

 Rakazo is in beta. Learn more at rakazo.com .

 Features 
 
 Persistent bots with their own conversations, memory, routines, and history 
 Shared Team Computers and isolated Private computers 
 Browser, terminal, file, and graphical desktop access 
 Bots that can delegate to peer bots or short-lived subagents 
 Bring-your-own model credentials through Pi 
 Optional app integrations through Composio 
 Docker, E2B, Daytona, and trusted local-computer support 
 
 Demo 
 
 
 
 
 
 demo.mp4 
 
 

 

 
 

 Stack 
 
 TypeScript 
 React 19, Vite, and Tailwind CSS 
 Electron and Expo 
 Hono and oRPC 
 PostgreSQL and Prisma 
 Better Auth 
 Graphile Worker 
 Pi 
 Docker, E2B, and Daytona 
 Composio 
 
 Quick start 
 You need Node.js 22+, pnpm 9, and Docker Desktop.

 git clone https://github.com/elie222/rakazo.git
 cd rakazo
cp .env.example .env 
 Set BETTER_AUTH_SECRET and ENCRYPTION_KEY in .env to independent, long random values. You can
also set OPENROUTER_API_KEY , or connect a supported model provider during onboarding.

 docker compose --env-file .env -f infra/compose/docker-compose.yml up postgres -d
pnpm install
pnpm db:generate
pnpm db:migrate
pnpm sandbox:build
pnpm dev 
 Open http://127.0.0.1:5173 , create an account, connect a model, and create
your first bot.

 For an agent-assisted installation, use SETUP_PROMPT.md . For deployment,
provider selection, backups, and upgrades, see the self-hosting guide .

 Desktop and mobile 
 The Electron and Expo apps are clients of the same Rakazo API used by the web app.

 With the development stack running, launch Electron with:

 pnpm --filter @rakazo/desktop dev 
 Mobile build and release instructions live in docs/mobile-release.md .

 Development 
 Rakazo is a TypeScript monorepo built with React, Electron, Expo, Hono, Postgres, Prisma, Graphile
Worker, and Pi.

 apps/ web, api, worker, desktop, mobile, and public website
packages/ domain, contracts, persistence, adapters, UI, and test tooling
infra/ local services and computer images
docs/ architecture, operations, and release guides
 
 Common checks:

 pnpm lint
pnpm check
pnpm test 
pnpm test:integration
pnpm test:e2e 
 See CONTRIBUTING.md for the development workflow and test matrix.

 Documentation 
 pnpm test # unit, property, and in-process contract tests 
pnpm test:integration # Postgres journeys, Graphile jobs, LISTEN/NOTIFY 
pnpm test:e2e # Playwright against the emulated stack 
pnpm test:e2e -- --sandbox=e2b # the same deterministic suite against real E2B 
pnpm test:e2e -- --sandbox=daytona # the same suite against real Daytona 
pnpm test:e2e -- --sandbox=box # the same suite against real Box 
pnpm test:topology # local Docker + Graphile worker recovery (needs Docker) 
pnpm test:canary # live OpenRouter / E2B / Box canaries 
 # explicit real vision-model + real E2B desktop acceptance test: 
COMPUTER_E2E_MODEL= < vision-capable-openrouter-model-id > pnpm test:computer 
 
 Self-hosting 
 Computer runtime and isolation 
 Mobile releases 
 Performance testing 
 
 Contributing 
 The Playwright workflow can also be started manually with Sandbox provider set to e2b , daytona , or box .
Those options require E2B_API_KEY , DAYTONA_API_KEY , or BOX_API_KEY , keep the deterministic scripted agent runtime, and destroy
the provider machines after the run. The default and all automatic runs remain on fake .
Contributions are welcome. Please read CONTRIBUTING.md before opening a pull
request. For security vulnerabilities, follow SECURITY.md instead of filing a public
issue.

 Rakazo is licensed under the Apache License 2.0 .

 Questions and ideas are welcome in the Rakazo Discord community .

 About Open-source Grok Bot alternative. Choose your own model and sandbox.
 rakazo.com Topics ai-agents chatgpt docker electron expo grok llm self-hosted typescript Resources Readme Apache-2.0 license Contributing Contributing Security policy Security policy Activity Stars 856 stars Watchers 6 watching Forks 107 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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