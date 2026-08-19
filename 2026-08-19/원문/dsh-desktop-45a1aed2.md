# dataelement/dsh-desktop — DeepSeek Harness Desktop

- 출처: GitHub 신규 (AI 에이전트)
- 원본 링크: https://github.com/dataelement/dsh-desktop
- 발행: 2026-08-19T03:34:26.738684+00:00
- 접근상태: 확인 완료

---

GitHub - dataelement/dsh-desktop: DeepSeek Harness Desktop · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 dataelement
 
 / 
 
 dsh-desktop 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 86 
 
 

 
 
 
 
 
 Star
 959 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 27 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 116 Commits 116 Commits Folders and files Name Name Last commit message Last commit date .github/ workflows .github/ workflows     build build     docs docs     packages/ dsh-desktop-market-installer packages/ dsh-desktop-market-installer     patches patches     scripts scripts     src src     test test     .gitattributes .gitattributes     .gitignore .gitignore     LICENSE LICENSE     README.md README.md     README.zh.md README.zh.md     electron-builder.dev.cjs electron-builder.dev.cjs     electron.vite.config.ts electron.vite.config.ts     package-lock.json package-lock.json     package.json package.json     tsconfig.json tsconfig.json     tsconfig.node.json tsconfig.node.json     View all files Repository files navigation README MIT license More items 
 
 DSH Desktop
 
 
 A local-first, cross-platform desktop shell for
 DeepSeek Harness .


 
 English · 简体中文 


 
 
 
 


 

 Beyond official DeepSeek models, DSH Desktop supports mainstream third-party model providers—with more DSH-powered desktop experiences coming soon. 

 DSH Desktop packages the local DeepSeek Harness web experience as a desktop application. It launches a local Harness instance automatically, manages a random loopback port, persists profiles, plugins, and sessions, and opens the full interface as soon as Harness is ready. Project workspaces are added and managed entirely in the Harness interface.

 Important
 DSH Desktop is currently an early preview and depends on the rapidly evolving @deepseek-ai/dsh@0.1.0-rc.7 . macOS releases are code-signed and notarized by Apple; current installers are distributed through the official website.

 
 Download 
 Download DSH Desktop for macOS and Windows from the official website .

 Installed macOS and Windows builds check for updates automatically after startup and every six hours. Updates download in the background and prompt you to restart when they are ready. You can also choose Check for Updates… from the application menu.

 Community 
 
 Scan the QR code below with WeChat to join the DSH Desktop community group.

 

 Prefer Discord? Join the DSH Desktop Discord community .


 Why this project exists 
 DeepSeek Harness already provides a complete agent runtime and Web UI. DSH Desktop does not reimplement Harness; it supplies the host capabilities needed for a desktop product:

 
 Run without manually starting a CLI or managing local ports 
 Create an application-owned Harness launch directory automatically at startup 
 Add and manage project workspaces through Harness's built-in directory picker 
 Manage the Harness child process, readiness checks, logs, and shutdown in one place 
 Store profiles, plugins, and sessions outside the application installation directory so upgrades do not remove user data 
 Provide packaging entry points for macOS and Windows 
 
 Features 
 
 Opens directly into Harness without an additional landing page 
 Starts without an initial directory prompt by creating and reusing an internal launch directory 
 Offers retry, log viewing, and exit actions when Harness fails to start 
 Provides Harness menu actions for restarting the child process and viewing its log 
 Gracefully terminates the Harness child process when the desktop app exits 
 Listens only on a random 127.0.0.1 port for each launch 
 Removes Node.js privileges from the renderer and enables contextIsolation , sandboxing, and navigation restrictions 
 Uses the DSH brand logo consistently in the desktop window and Harness sidebar 
 Imports and exports complete custom Agent presets as portable .dshpreset packages , with conflict checks and a trust warning before installation 
 Includes a production DSH app icon in macOS ICNS and Windows ICO formats 
 
 Friends 
 dsh-market — the DeepSeek Harness plugin market: browse and search 900+ community plugins, preview screenshots, and install, update, enable or disable plugins, or switch themes with one click. Most plugins take effect instantly without a restart.

 Quick start 
 Requirements 
 
 Node.js 22 or later 
 npm 
 macOS on Apple Silicon or Intel, or Windows x64 
 
 Local development 
 git clone https://github.com/dataelement/dsh-desktop.git
 cd dsh-desktop
npm install
npm run dev 
 npm install runs patch-package to reapply DSH Desktop's model-provider onboarding, preset package transfer, and sidebar branding, installs the brand asset, and then installs the Electron runtime.

 Quality checks 
 npm test 
npm run typecheck
npm run build 
 Packaging 
 # Generate unsigned DMG and ZIP artifacts for the current Mac architecture 
npm run package:mac

 # Run each command on a Mac or CI runner with the matching architecture 
npm run package:mac:arm64
npm run package:mac:x64

 # Generate NSIS and Portable artifacts on a Windows x64 machine or runner 
npm run package:win 
 Harness includes architecture-specific native modules. Dependencies must be reinstalled and built on the matching platform for macOS ARM64, macOS Intel, and Windows x64. The architecture-specific scripts validate the current platform/arch before packaging to prevent artifacts that appear successful but are missing native dependencies.

 Runtime architecture 
 DSH Desktop (Electron Main)
├── Application-owned launch directory
├── Harness child-process lifecycle
├── Random loopback port and readiness checks
├── Native logging and recovery actions
└── Hardened BrowserWindow
 └── http://127.0.0.1:<random> DeepSeek Harness Web UI

Electron userData
├── launch-root/
├── logs/harness.log
└── harness/
 ├── profiles/
 ├── sessions/
 └── Plugins and user data
 
 Harness runs in a separate Electron Node child process. The --expose-internals permission required by Cordis HMR is granted only to that child process and never to the web renderer.

 Project structure 
 src/main/ Electron main process, windows, and Harness lifecycle
src/shared/ Shared runtime types
patches/ Reproducible UI customizations for the pinned DSH version
scripts/ Brand-asset installation and target-platform packaging checks
test/ Settings, runtime, security, and provider coverage tests
build/ Application icon assets
 
 Current validation status 
 
 macOS Apple Silicon: development workflow, real Harness startup, DMG packaging, code signing, Apple notarization, and mounted artifact verified 
 macOS Intel: packaging configuration and platform checks provided; runtime verification still requires an Intel Mac or runner 
 Windows x64: NSIS/Portable configuration and platform checks provided; runtime verification still requires a Windows runner 
 Windows ARM64: not currently supported 
 Automatic updates: not yet integrated 
 
 Upstream version and patches 
 The project currently pins @deepseek-ai/dsh@0.1.0-rc.7 . The initial provider list and desktop preset-transfer surface are captured with patch-package under patches/ rather than relying on untracked changes in node_modules .

 When upgrading DSH:

 
 Verify the upstream Settings, Credentials, and Provider Directory contracts. 
 Reapply or rewrite the customized onboarding interface. 
 Regenerate the patch. 
 Run regression checks against a real Harness startup and provider configuration flow. 
 
 Contributing 
 Issues and pull requests are welcome. Before submitting a change, run at least:

 npm test 
npm run typecheck
npm run build 
 Never include real API keys in issues, logs, screenshots, or test data.

 License 
 This project is open source under the MIT License .

 DeepSeek Harness and its dependencies remain subject to their respective upstream licenses and trademark policies. DSH Desktop is an independent community desktop wrapper.

 About DeepSeek Harness Desktop
 dshdesktop.com Topics ai-agents deepseek desktop dsh-plugins Resources Readme MIT license Activity Custom properties Stars 959 stars Watchers 24 watching Forks 86 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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