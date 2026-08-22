# Show HN: Proliferate- open-source, self-hostable Codex for any coding agent

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://github.com/proliferate-ai/proliferate
- 발행: 2026-08-21T16:47:15+00:00
- 접근상태: 확인 완료

---

GitHub - proliferate-ai/proliferate: The open-source AI IDE for Claude Code, Codex, OpenCode, and more. Run agents in parallel, locally or in the cloud, and build reusable workflows. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 proliferate-ai
 
 / 
 
 proliferate 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 52 
 
 

 
 
 
 
 
 Star
 246 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 28 


 
 
 
 
 
 
 
 
 Pull requests 
 63 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 2,904 Commits 2,904 Commits Folders and files Name Name Last commit message Last commit date .auth-env .auth-env     .claude/ skills/ ui-conformance-review .claude/ skills/ ui-conformance-review     .design-sync .design-sync     .github .github     adrs adrs     anyharness anyharness     apps apps     assets/ readme assets/ readme     catalogs catalogs     cloud cloud     delivery delivery     fixtures/ contracts fixtures/ contracts     guides guides     install install     lints lints     scripts scripts     server server     specs specs     tests tests     .gitattributes .gitattributes     .gitignore .gitignore     .vercelignore .vercelignore     AGENTS.md AGENTS.md     ARCHITECTURE.md ARCHITECTURE.md     CLAUDE.md CLAUDE.md     CONTRIBUTING.md CONTRIBUTING.md     Cargo.lock Cargo.lock     Cargo.toml Cargo.toml     Cross.toml Cross.toml     LICENSE LICENSE     Makefile Makefile     README.md README.md     SECURITY.md SECURITY.md     THIRD_PARTY_NOTICES.md THIRD_PARTY_NOTICES.md     VERSION VERSION     package.json package.json     pnpm-lock.yaml pnpm-lock.yaml     pnpm-workspace.yaml pnpm-workspace.yaml     vercel.json vercel.json     View all files Repository files navigation README Contributing AGPL-3.0 license Security More items 
 
 
 
 
 


 The open-source AI IDE 
 
 
 
 
 
 
 




 Run Claude Code, Codex, OpenCode, Grok, and any other coding agent in parallel, in one workspace.

Each task gets an isolated git worktree for its branch, terminal, conversation, and review state.



 
 Download for macOS 
  • 
 Documentation 
  • 
 Changelog 
  • 
 Discord 


 
 
 Features 
 
 🤖 Native harnesses - Claude Code, Codex, OpenCode, Cursor, Grok, and more 
 🌳 Worktree workspaces - an isolated branch and working directory for every task 
 🔀 Parallel agents - run agents side by side in the same workspace, each on its own task 
 🪆 Subagents - agents delegate scoped work to child agents and pick the results back up when they finish 
 🧩 Integrations - MCPs, skills, Computer Use, Browser Use, and custom tools, configured once and shared by every agent 
 ⏰ Workflows - recurring and event-driven agent runs: nightly review passes, triage on alerts, dependency bumps 
 
 Supported agents 
 Proliferate runs each agent through its native harness.

 
 
 
 

 Claude 
 
 
 
 
 
 

 Codex 
 
 
 

 OpenCode 
 
 
 
 
 
 

 Cursor 
 
 
 
 
 
 

 Grok 
 
 
 
 Self-hosting 
 The full Proliferate control plane is self-hostable. Start with the
 deployment docs , which cover Docker,
AWS, GCP, Azure, Kubernetes, and air-gapped operation.

 
 Docker Compose: self-hosted-deploy.md 
runs Caddy, Postgres, and the API, with bootstrap and update scripts 
 AWS (one-click): self-hosted-aws.md 
is a CloudFormation wrapper that provisions the stack on EC2 
 Configuration: server/deploy/.env.production.example 
documents every required and optional setting 
 
 Point the desktop app at your control plane by following
 configure desktop .
 Open an issue or ask in
 Discord if you hit problems, and see
 SECURITY.md for reporting vulnerabilities.

 
 Run from source 


 Requirements:

 
 Rust stable 
 Node.js 22+ 
 pnpm 
 
 Run the desktop app with the bundled local AnyHarness runtime:

 make install
make dev-local 
 Local full-stack development additionally requires Python 3.12+, uv , and
Docker for the local control plane database. Use named dev profiles when
multiple worktrees run at the same time.

 make server-install
make setup PROFILE=main
make build # first clean worktree, or after generated/Rust/frontend artifacts change 
make dev-list
make run PROFILE=main 
 See dev profiles for profile state, ports,
generated Tauri config, and app labels.

 
 Community 
 Join our community on Discord !

 Contributing 
 Contributing? See the Contribution Guide .

 License 
 AGPL-3.0 

 About The open-source AI IDE for Claude Code, Codex, OpenCode, and more. Run agents in parallel, locally or in the cloud, and build reusable workflows.
 proliferate.com/docs Resources Readme AGPL-3.0 license Contributing Contributing Security policy Security policy Activity Custom properties Stars 246 stars Watchers 0 watching Forks 52 forks Report repository Releases Packages Used by Contributors Languages 
 




 

 

 
 

 

 
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