# miuuyy/codex-chatgpt-web — Use ChatGPT Web (including Pro) as a native model in the Codex app — with contex

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/miuuyy/codex-chatgpt-web
- 발행: 2026-08-23T22:24:09.085719+00:00
- 접근상태: 확인 완료

---

GitHub - miuuyy/codex-chatgpt-web: Use ChatGPT Web (including Pro) as a native model in the Codex app — with context, tools, streaming and images beyond Codex usage limits. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 miuuyy
 
 / 
 
 codex-chatgpt-web 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 177 
 
 

 
 
 
 
 
 Star
 1.4k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 9 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 201 Commits 201 Commits Folders and files Name Name Last commit message Last commit date .github .github     LICENSES LICENSES     assets assets     docs docs     launcher launcher     scripts scripts     src src     tests tests     .gitignore .gitignore     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     README.zh-CN.md README.zh-CN.md     SECURITY.md SECURITY.md     bun.lock bun.lock     package.json package.json     tsconfig.json tsconfig.json     View all files Repository files navigation README Contributing MIT license Security More items ChatGPT Web for Codex 
 
 Use ChatGPT Web (including Pro) as native Codex models. 

 Change the model tier, save your workflow.


 
 English · 简体中文 


 
 
 
 
 
 
 


 Free and Go accounts get ChatGPT Web — Luna in Codex's native model picker. Accounts that
expose the reasoning selector keep Instant , Medium , High , Extra High , and Pro as
their subscription allows. The bridge sends the current compiled Codex task context to a fresh
ChatGPT Temporary Chat, attaches images, and streams visible reasoning, tool activity, and Markdown
back into the same Codex task.

 
 


 Codex task ──Responses + SSE──▶ codex-chatgpt-web ──embedded browser──▶ ChatGPT
 ▲ │ │
 └──────── native UI, context, images, tracing, and tool lifecycle ──────┘
 
 Codex keeps the native task, context lifecycle, UI, and tool harness. The local Responses bridge
routes only the selected model turn through a fresh ChatGPT Temporary Chat; in full mode, MCP
connects ChatGPT back to the tools of that same Codex task.

 Tip
 I also built ChatGPT Persona Voice , a local
app that changes the ChatGPT/Codex voice in near real time. It never touches your account, browser
session, or ChatGPT requests, so using it carries no account-blocking risk. If you like my work,
give it a try.

 
 Highlights 
 
 A polished cross-platform launcher. One command installs the native macOS, Windows, or Linux
app. It keeps sign-in orchestration, setup, smoke testing, MCP guidance, runtime health, and local
logs in one place, while the embedded browser lets you watch every ChatGPT turn as it happens. Up
to five task-bound browser tabs can run in parallel; the cap avoids excessive parallel account
traffic. 
 ChatGPT is the selected model. It runs as a native Codex model, not as a tool called by
another host model. The original model picker, task lifecycle, streaming, tracing, and tool UI
remain intact. 
 Local-first task sessions. Codex remains the source of truth for task history on your
computer. Every browser turn starts in a fresh ChatGPT Temporary Chat and receives the current
compiled context. Measured browser ceilings trigger compaction, while Luna carries completed
state through an adaptive rolling checkpoint. Browser chats are never reused across tasks or
added to normal ChatGPT history. 
 The full Codex harness over MCP. In Full mode, every effort available to the signed-in account—
Luna, Instant, Medium, High, Extra High, and Pro—can use the active Codex task's filesystem,
shell, images, approvals, and configured tools/apps through the same turn-bound MCP capability.
Calls and real results stay inside the same browser response; nothing is simulated as text. 
 No Pro exception. Pro follows exactly the same MCP, context, image, tracing, tool-round,
browser-ceiling, and compaction contracts as every other effort. There are no effort-specific MCP
exclusions. Browser-only mode remains read-only for every route. 
 Fail-closed with an explicit release gate. UI drift and missing capabilities produce explicit
errors rather than silent fallbacks. Account-bound model selection, long context, images,
streaming, compaction, native tool rounds, cancellation, and Pro are covered by the documented
 release validation , separately from package smoke. 
 
 Temporary Chat is a ChatGPT privacy mode, not anonymity or local-only inference: prompts are still
processed by OpenAI and are subject to the account's settings and OpenAI's
 Temporary Chat policy . This project
is unofficial; users remain responsible for complying with applicable OpenAI terms and workspace
policies.

 Quick start 
 Install or update the desktop launcher. To update or repair an existing installation, quit the
launcher and run the same command again; it replaces the application and embedded runtime while
preserving the ChatGPT profile and launcher configuration.

 macOS or Linux 

 curl -fsSL https://github.com/miuuyy/codex-chatgpt-web/releases/latest/download/install-launcher.sh | sh 
 Windows PowerShell 

 irm https: // github.com / miuuyy / codex - chatgpt - web / releases / latest / download / install-launcher.ps1 | iex 
 Then complete the three checks in the app:

 
 Sign in directly in the launcher's embedded ChatGPT browser. Login pages and identity-provider
windows stay inside the same launcher-owned private browser profile; no session is copied between
browsers. 
 Run the browser smoke test. 
 Press Install models , restart Codex once, and select a ChatGPT Web — … model. 
 
 The launcher detects the current account's ChatGPT controls during setup: Free/Go accounts expose
only Luna, while Pro appears only when the signed-in account exposes it. The separate MCP page
is optional and guides the full-harness setup without terminal commands.

 The packaged launcher keeps sign-in and ChatGPT model turns in its embedded browser. It needs no
model API key, installed Chrome/Chromium, system Node/Bun, or project-managed browser download.

 Run from source 

 git clone https://github.com/miuuyy/codex-chatgpt-web.git && \
 cd codex-chatgpt-web && \
bun run app 
 This source path requires Bun 1.4.0. The command installs locked dependencies and opens the app.

 Modes 
 
 
 
 Mode 
 Models 
 Local Codex tools 
 Extra setup 
 
 
 
 
 Browser-only 
 Free/Go: Luna; Plus: Instant–High; Pro: adds Extra High and Pro 
 No; Codex shows a warning 
 None 
 
 
 Full harness 
 Free/Go: Luna; Plus: Instant–High; Pro: adds Extra High and Pro 
 Yes for every listed effort, including Pro 
 OpenAI tunnel + ChatGPT connector 
 
 
 
 Every picker entry has one fixed ChatGPT mode. Codex still displays its built-in Effort and Speed
rows, but changing them cannot silently change the selected browser model. In Full mode every
available effort receives the same turn-bound MCP capability. Pro has no separate restriction or
reduced tool contract.

 Full harness 
 Full mode connects ChatGPT's tool calls back to the current Codex task through the official
 OpenAI tunnel-client . The tunnel is outbound: it does
not expose a public IP, open an inbound port, or require router forwarding.

 Warning
 Create a new connector named Codex Native2 and set its permissions to
 Allow all actions . Do not rename, refresh, or reuse an older Codex Native connector:
ChatGPT caches the public MCP contract by connector identity, and Allow low-risk actions 
blocks commands and patches before they reach the Codex harness.

 
 
 Finish the required launcher setup. 
 Open MCP in the launcher. Create the Tunnel and a regular API key on the same OpenAI account
that will use the ChatGPT connector; creating the key is free and does not consume model API
credits. 
 Paste the Tunnel ID and API key, then press Connect harness . 
 Enable Developer Mode in ChatGPT settings. Create a new connector using Tunnel , select
that exact Tunnel, set Authentication to None , and name it exactly Codex Native2 . 
 If an older Codex Native connector exists, leave it untouched. Do not rename or refresh it:
ChatGPT caches the public MCP contract by connector identity, and this release uses a new direct
turn-token contract. Under Permissions on Codex Native2 , choose Allow all actions ;
 Allow low-risk actions blocks commands and patches before they reach this runtime. The outer
Codex harness still enforces its sandbox and approvals. 
 Run Verify runtime . It selects Codex Native2 exactly. If only Codex Native is found,
verification fails with an explicit migration error instead of accepting the legacy connector. 
 
 Write/modify actions also require the ChatGPT workspace and its administrator policy to permit
them. See
 developer mode and MCP apps .
Unexpected approval prompts fail closed unless --auto-approve-tool-calls is explicitly enabled;
that option clicks Allow once , never a permanent grant.

 Operations 
 Use Activity for structured local logs and Settings → Run doctor for end-to-end health
checks. Use Settings → Cancel retained browser turn if a stopped task leaves ChatGPT working,
and Settings → Remove Codex integration before deleting the launcher so the previous Codex
route is restored.

 Browser turn diagnostics save bounded JSON state at each checkpoint. Screenshots are captured for
stalled and failed turns, where the visible UI is needed to diagnose DOM drift without slowing every
successful step. Set CODEX_CHATGPT_WEB_BROWSER_DIAGNOSTICS=1 before starting the runtime to also
capture a screenshot at every checkpoint during an investigation.

 Subagent protocol is an explicit installation setting. New installs use Compatibility V1 : it
enables multi_agent , disables the global multi_agent_v2 override, and
restores the user's previous feature lines on disconnect or uninstall. It also raises
 [agents].max_depth to at least 2 while active so Web children can spawn Web grandchildren, then
restores the prior value. This is the universal cross-backend surface: native and Web parents can
delegate to Web children without opaque V2 payloads, and targeted waits can observe a child that
completed before the parent began waiting. Web parents expose wait_agent as explicit 10-second
polls so one long wait cannot occupy the connector's MCP channel and block the child's own tools.
 Native remains an advanced opt-in that preserves
Codex's own feature settings and supports plaintext Web-to-Web V2 delegation. Switch deliberately,
then restart Codex and start a new task because an existing task cannot change protocol in place:

 codex-chatgpt-web subagents status
codex-chatgpt-web subagents compatibility-v1
codex-chatgpt-web subagents native 
 Limitations and security 
 
 This is unofficial browser automation, not an OpenAI API. ChatGPT UI changes can break selectors;
drift fails explicitly instead of silently switching model or transport. 
 ChatGPT's account-specific composer ceilings are smaller than some underlying model windows.
The measured boundaries and requirements for a larg