# makecindy/cindy — Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开

- 출처: GitHub 신규 (claude-code)
- 원본 링크: https://github.com/makecindy/cindy
- 발행: 2026-08-19T22:24:39.770046+00:00
- 접근상태: 확인 완료

---

GitHub - makecindy/cindy: Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。 · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 makecindy
 
 / 
 
 cindy 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 300 
 
 

 
 
 
 
 
 Star
 2.2k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 804 


 
 
 
 
 
 
 
 
 Pull requests 
 146 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 3,088 Commits 3,088 Commits Folders and files Name Name Last commit message Last commit date .githooks .githooks     .github .github     appicon appicon     apps apps     config config     dependency-patches dependency-patches     docs docs     i18n i18n     packages packages     prototypes prototypes     scripts scripts     tools tools     .easignore .easignore     .gitattributes .gitattributes     .gitignore .gitignore     .npmrc .npmrc     .nvmrc .nvmrc     AGENTS.md AGENTS.md     CLAUDE.md CLAUDE.md     CODE_OF_CONDUCT.en.md CODE_OF_CONDUCT.en.md     CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md     CONTRIBUTING.en.md CONTRIBUTING.en.md     CONTRIBUTING.md CONTRIBUTING.md     DCO DCO     DESIGN.md DESIGN.md     LICENSE LICENSE     NOTICE NOTICE     README.md README.md     README.zh-CN.md README.zh-CN.md     REVIEW.md REVIEW.md     SECURITY.en.md SECURITY.en.md     SECURITY.md SECURITY.md     SUPPORT.en.md SUPPORT.en.md     SUPPORT.md SUPPORT.md     package.json package.json     pnpm-lock.yaml pnpm-lock.yaml     pnpm-workspace.yaml pnpm-workspace.yaml     View all files Repository files navigation README Code of conduct Contributing Apache-2.0 license Security More items 
 


 
 English · 简体中文 


 
 
 
 
 


 
 🌐 cindy.app  ·  ⬇️ Download 


 Cindy is an open-source AI agent that works out of the box. She brings multiple
harnesses, models and tools into one agent that finishes real work in your
projects and apps. Ready from day one, yours to shape over time.

 Cindy runs locally on your own machine, using your real files and logged-in
apps. The first supported harnesses are Claude Code and Codex — more are
being added, and a native harness is in the works. Models and harnesses mix
freely and can switch mid-task while your workspace, memory, skills and tools
stay continuous; one task can even be planned, executed in parallel, and
reviewed by agents on different harness × model combos. She can drive your
browser, computer and phone, and take work from IM and schedules.

 This repository is the open-source client for Cindy — the desktop and mobile
apps plus their shared packages, organized as a pnpm monorepo.

 The client is free to use, and its source code is open under Apache-2.0. Bring
models your way: sign in to the official Cindy service (usage deducted
transparently), authorize the Claude Code / Codex Coding Plan you already
pay for and keep using it inside Cindy — no duplicate bill — connect your own
API keys, or use local models.
See cindy.app for service details,
 pricing , and downloads .

 Yours to shape 
 Open source means more than visible — it means changeable:

 
 Memory — correct her once and she does it right from then on, shared across harnesses. 
 Skills — teach a way of working once and reuse it everywhere; handing them to your team is in the making. 
 Automation — recurring work schedules itself, runs itself, reports back. 
 MCP — wire your internal tools and business systems into her reach. 
 Plugins — reshape features, UI and interactions, shared through an open marketplace (in the making) . 
 Source — audit, fork, extend, and contribute improvements back under Apache-2.0. 
 
 Ready out of the box, never boxed in — start with
 CONTRIBUTING.en.md and build Cindy with us.

 What's in this repo 
 
 
 
 Path 
 Description 
 
 
 
 
 apps/desktop 
 Electron desktop client 
 
 
 apps/mobile 
 Expo / React Native mobile client 
 
 
 packages/* 
 Shared client capabilities (auth, device-link, agent orchestration, model providers, …) 
 
 
 apps/*-bin 
 Tool binaries shipped with the desktop app; none are committed — claude-code, codex, and ripgrep are downloaded per platform by pnpm install , and the Android platform-tools binaries are fetched (pinned version, sha256-verified) before Windows packaging 
 
 
 
 Not in this repo: the backend service lives in a separate
repository and is not part of this monorepo.

 
 
 
 Mode 
 Account requirement 
 Availability 
 
 
 
 
 Hosted service 
 Cindy cloud account 
 Use Cindy's full hosted service. See pricing . 
 
 
 Skip Sign-In 
 No Cindy sign-in required 
 Choose “Skip Sign-In” on the login screen to use local agents; the app then shows the account state as “Not signed in”. Server-backed capabilities are unavailable in this state. 
 
 
 
 Prerequisites 
 
 Node.js 22.x 
 pnpm 10.x (v11 is not yet supported) 
 Git LFS 
 
 Getting started 
 Contributor setup, Git LFS, dependency updates, and access requirements are maintained in
 CONTRIBUTING.en.md .
Plugins are installed through SkillHub or manually.

 Minimal entry point:

 git clone https://github.com/makecindy/cindy.git
 cd cindy
git lfs pull
pnpm install 
 Development entry points 
 # Mainland China Cindy account 
pnpm restart:desktop:remote --region=cn

 # Global Cindy account 
pnpm restart:desktop:remote --region=global 
 Remote development uses your own Cindy cloud account and existing login state, so
you can continue existing sessions and work while developing the client. Use cn 
for Mainland China accounts and global for everyone else; do not rely
on the internal default. Full desktop, mobile, data-isolation, and validation
workflows are in CONTRIBUTING.en.md .

 “Skip Sign-In” on the login screen runs local agents without a Cindy account
(shown in the app as “Not signed in”), not a connection to a local server.
Server-backed capabilities are unavailable in this state.

 About the default servers: the client connects to Cindy's official cloud
services by default (endpoint manifests in
 config/endpoint.json and
 config/endpoint.global.json ; desktop
auto-updates also come from the official CDN). This is intentional — external
developers don't need to self-host a server: sign in with your own Cindy
account in a dev build and develop / test directly against the official
servers.

 Architecture 
 
 DESIGN.md — visual design system, color tokens, and UI conventions 
 docs/README.md — complete documentation and rules index 
 docs/auth-realm-routing.md — organization SSO region discovery and session endpoint routing 
 CONTRIBUTING.en.md — contributor setup, validation, and submission workflow 
 AGENTS.md — engineering rules, launch/runtime contracts, and module boundaries 
 docs/dev-rules/ — deep-dive architecture docs (e.g. Orca multi-agent orchestration) 
 
 Contributing 
 Contributions go through pull requests into main . Read
 CONTRIBUTING.en.md first, then use
 .github/PULL_REQUEST_TEMPLATE.md .
Every commit needs a Developer Certificate of Origin sign-off
( git commit -s ); a DCO check on each pull request enforces it, and no CLA is
required.
Please also follow CODE_OF_CONDUCT.en.md . For ordinary
usage questions, see SUPPORT.en.md ; report security issues
privately through SECURITY.en.md .

 Security 
 Never commit credentials or authorization files to the working tree. If you
discover a security issue, follow SECURITY.en.md to report it
privately rather than opening a public issue.

 Privacy & telemetry 
 Official distribution builds include TapDB 
usage analytics for product-level aggregate statistics (device / OS / app-version
metadata; associated with your account ID after sign-in). It does not collect
chat content, file content, or working-directory data. In addition, while signed
in to a cloud account the client sends an online heartbeat to Cindy services
(account ID, platform, and version only). Crash dumps stay on the local machine
and are never uploaded automatically.

 Building from source? You are not required to keep analytics:

 
 Mobile is off by default — without TapDB credentials ( clientId /
 clientToken ) injected at build time, apps/mobile/src/analytics/mobileTapdb.ts 
is a no-op; 
 Desktop can be fully stripped by removing the initTapdb() call in
 apps/desktop/src/renderer/index.tsx (implementation lives in
 apps/desktop/src/renderer/analytics/ ). 
 
 License / 许可证 
 Except as otherwise noted, the source code in this repository is licensed under
the Apache License, Version 2.0 . Individual source files do not
carry per-file license headers; the repository-root LICENSE governs.

 Model weights, datasets, prompts, trademarks, and other separately identified
materials may be subject to their own license terms and are not automatically
covered by the repository-level Apache-2.0 grant. Third-party open-source
components retain their own copyright and license. Their attribution notices and
SPDX SBOMs are managed under docs/legal/ , with artifact-specific
outputs in docs/legal/notices/ . See NOTICE 
for this project's copyright and attribution information.

 About Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。
 cindy.app Topics agent ai-agent ai-assistant android claude-code codex electron ios llm macos react-native typescript windows Resources Readme Apache-2.0 license Code of conduct Code of conduct Contributing Contributing Security policy Security policy Activity Custom properties Stars 2.2k stars Watchers 6 watching Forks 300 forks Report repository Releases Packages Used by Contributors Languages 
 




 

 

 
 

 

 
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