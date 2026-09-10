# totec448-spec/chat-on-steroids — Cross-platform local MCP capabilities for ChatGPT with Chrome integration, Goal,

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/totec448-spec/chat-on-steroids
- 발행: 2026-09-10T22:30:10.227035+00:00
- 접근상태: 확인 완료

---

GitHub - totec448-spec/chat-on-steroids: Cross-platform local MCP capabilities for ChatGPT with Chrome integration, Goal, Compact & Resume, and durable multi-agent workflows. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 totec448-spec
 
 / 
 
 chat-on-steroids 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 237 
 
 

 
 
 
 
 
 Star
 1.7k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 24 


 
 
 
 
 
 
 
 
 Pull requests 
 14 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 112 Commits 112 Commits Folders and files Name Name Last commit message Last commit date .githooks .githooks     .github .github     artwork artwork     docs docs     extension extension     native native     scripts scripts     src src     test test     .gitattributes .gitattributes     .gitignore .gitignore     AGENTS.md AGENTS.md     CHANGELOG.md CHANGELOG.md     CLAUDE.md CLAUDE.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     SECURITY.md SECURITY.md     THIRD-PARTY-NOTICES.txt THIRD-PARTY-NOTICES.txt     electron-builder.yml electron-builder.yml     electron.vite.config.ts electron.vite.config.ts     package-lock.json package-lock.json     package.json package.json     tsconfig.json tsconfig.json     vitest.config.ts vitest.config.ts     View all files Repository files navigation README Contributing MIT license Security More items Important
 2.0.8 — Darkex by dark tibo — needs its matching companion extension. Reload the unpacked extension after updating.
Model discovery now reads your account's native picker state across languages and nested version menus.
See Browser behavior for tab reuse, Browser only and native file attachments.

 
 
 
 Chat On Steroids 
 ChatGPT, with hands on your computer. 

 A desktop chat workspace and local MCP server for ChatGPT: project folders, images, plans, worker chats, and tools to read, patch and run code. Keep a local transcript and choose how the next instruction arrives.

 
 Download the latest release 
 · Quick start 
 · Tools 
 · Security 
 · Changelog 
 

 
 
 


 
 


 Screenshots of the app with private conversation and folder details redacted. Chat history loads in small chunks as you scroll upward. Image attachments stay visible as thumbnails, and delivery controls sit below their messages.

 Why this exists 
 ChatGPT is a good engineer trapped in a text box. Developer mode lets it call MCP servers, but most servers give it one narrow API. This one gives it a workbench.

 
 Codex-grade tools. apply_patch , exec_command and write_stdin are ports of the tool contracts OpenAI's Codex CLI uses, so the model already knows how to hold them. Multi-file patches are preflighted before anything is written. Commands run as real processes with interactive stdin, output budgets and background results it can collect later. 
 Sub agents inside ChatGPT. One prime chat can spawn worker chats, hand them tasks, read their reports and wake them again later. Workers are ordinary ChatGPT conversations in your own browser, brokered by the app, so you can watch every one of them. 
 Sessions that outlive the context window. Every tool call is recorded locally with its real result. When a chat gets heavy, Compact & Resume asks it for a handoff brief, opens a fresh chat and moves the same local session across. The new chat can query everything the old one did. 
 Plans, Goal and Loop. Split a request into editable tasks or generate follow-ups through a separate ChatGPT helper or the API. Astra can receive the next task through session_finish in the same turn, without opening another model turn. 
 External MCP plugins. Settings → Plugins installs integrations such as Blender MCP, Playwright, Memory and Web Fetch behind a separate Chat On Steroids Plugins connector. Enable individual tools, import MCPB bundles or connect custom local/remote servers. Setup and supported sources . External servers run with their own OS/service permissions, outside CoS's approved-folder sandbox. 
 You stay the permission boundary. Only the folders you approve are visible. Each capability is a switch. Read-only mode is a single kill switch. Nothing runs on this machine that you did not turn on. 
 
 It runs in the tray, hosts no model of its own, and works with the ChatGPT you already use in the browser.

 Download 
 
 
 
 Platform 
 x64 
 ARM64 
 
 
 
 
 Windows 
 Installer 
 Installer 
 
 
 macOS 
 DMG · ZIP 
 DMG · ZIP 
 
 
 Linux 
 AppImage · DEB 
 AppImage · DEB 
 
 
 
 Every package ships with matching native dependencies, a pinned tunnel-client , ripgrep and the Chrome extension for that CPU. A standalone extension zip is attached for manual installs, and SHA256SUMS.txt lists every hash.

 Windows and AppImage installs check GitHub for a newer release on start and every six hours, download it, verify its checksum and apply it when you quit or choose Install update . Staged downloads are revalidated before installation. macOS and DEB installs link to the release page for manual installation.

 Debian and Ubuntu: prefer the DEB. The AppImage uses electron-builder's static launcher. On a host that disables unprivileged user namespaces, that launcher can fall back to starting Chromium with --no-sandbox so the app still opens. If you do not want that fallback, use the DEB.

 The builds are not publisher-signed yet , and macOS builds are not notarized. SmartScreen, Gatekeeper or your browser will warn. Verify the hash first, then use the normal "run anyway" path, or build from source .

 Get-FileHash .\ Chat-On-Steroids-Setup-x64.exe - Algorithm SHA256 # Windows 
 shasum -a 256 Chat-On-Steroids-macOS-arm64.dmg # macOS 
sha256sum Chat-On-Steroids-Linux-x64.AppImage # Linux 
 
 This is a beta with real permissions. A fresh install starts with Core capabilities on except opt-in ChatGPT file saving, read-only mode off, multi-agent mode on with two workers, and, on Windows, the Desktop permissions on. On macOS the Desktop permissions start off; enable them in Settings → Workspace , then grant Screen Recording and Accessibility in System Settings. Linux has Core tools but no Desktop computer-control backend. Review folder access before connecting: exec_command runs programs as your logged-in user.

 
 Requirements 
 
 Windows 10/11 , macOS 13 Ventura or newer , or a current desktop Linux , on x64 or ARM64 matching the build you downloaded. 
 Chrome 116 or newer , or a current Microsoft Edge with the companion extension. Without it you still get the MCP tools, but not session attribution, Compact & Resume, worker chats or the Goal loop. 
 
 Using Edge? Choose Settings → Browser & history → ChatGPT browser → Microsoft Edge . Install the companion and sign in to ChatGPT in that browser's active profile ( edge://extensions for Edge). This choice controls app-originated launches, including startup model discovery; already connected tabs and source-tab continuations keep their browser. Older configurations retain Chrome. If the selected browser is missing or cannot start, the app reports an error instead of opening a different browser. The setting chooses a browser family, not a particular profile.

 
 Linux: a Secret Service keyring such as GNOME Keyring or KWallet. The app refuses Electron's unencrypted basic_text fallback for stored keys. 
 A ChatGPT workspace with Developer mode and custom MCP apps. OpenAI currently documents full MCP support, including write actions, as a beta for Business, Enterprise and Edu, with Pro limited to read and fetch. Business needs an admin to enable it. Check OpenAI's Developer mode and MCP apps page if your workspace looks different. 
 An OpenRouter API key (or your own OpenAI-compatible endpoint) only if you select the API source for plans, Goal or Loop. The default ChatGPT helper source uses your connected browser session. 
 
 Use a normal ChatGPT conversation with the custom app enabled. OpenAI's built-in Agent mode does not use custom apps.

 Quick start 
 
 Install the build for your CPU and open Chat On Steroids. It lives in the tray or menu bar. 
 Open Settings → Workspace , review permissions and approve a project folder. Press Add , or drop the folder onto the Folders card. 
 Create an OpenAI Secure MCP Tunnel and a restricted API key, then press Connect . Details below. 
 In ChatGPT on the web, enable Developer mode and create the Core app from the tunnel. On Windows, create the Desktop app too if you left screen and input control on; on macOS, if you switched them on. 
 Press Open extension folder , open chrome://extensions , enable Developer mode, choose Load unpacked and select that folder. Pairing is automatic. 
 
 Settings → Setup marks each hop done only once the app has actually seen traffic on it. Back in chat, select a project and model, write a message, or choose Create plan from the gear. Images can be attached or dropped into the composer.

 OpenAI Secure MCP Tunnel (recommended) 
 
 In Platform → Tunnels , create a tunnel in the same workspace you use in ChatGPT and copy its id ( tunnel_… ). 
 In Platform → API keys , create a Restricted key with only Tunnels: Read and Tunnels: Use . 
 Paste both into the Setup tab and press Connect . 
 In ChatGPT, enable Developer mode under Settings → Apps → Advanced settings and create a custom app of type Tunnel . Review the discovered actions and enable it. 
 
 Core and the optional Desktop surface (Windows and macOS) use separate tunnel ids, because ChatGPT treats each custom app as one endpoint. Release builds bundle a checksum-verified tunnel-client ; a path you set explicitly wins over it, and PATH is only a fallback.

 Other tunnels 
 Cloudflare quick tunnel: press Connect , copy the URL and use it as the MCP server URL in ChatGPT. The random path in that URL is the secret. It changes on every restart.

 Your own HTTPS tunnel: point it at the loopback URL the app shows and give ChatGPT the public equivalent, secret path included.

 Permission changes take effect locally immediately. Schema changes schedule a separate connector refresh; if that refresh fails, refresh the custom app in ChatGPT. ChatGPT may keep an older reviewed action list until it refreshes.

 What ChatGPT gets 
 
 
 
 Connector 
 Tools 
 What they do 
 
 
 
 
 Core (all platforms) 
 read , view_image , find , apply_patch , exec_command , write_stdin , download_artifact , session , agents 
 Bounded reads and search inside approved folders, preflighted multi-file patches, shell commands and interactive terminals, saving ChatGPT-generated files, lookups into the recorded session, and worker chat control 
 
 
 Desktop (Windows, and macOS when switched on) 
 observe , computer 
 Screenshots, window and control inspection, mouse, keyboard and clipboard 
 
 
 
 The live tool list follows your settings: find is the no-shell search fallback and steps aside when commands are enabled. Enabling Session finish adds the Astra-only session_finish tool. Revoking a permission takes effect immediately, even while ChatGPT still shows the old schema. The full contra