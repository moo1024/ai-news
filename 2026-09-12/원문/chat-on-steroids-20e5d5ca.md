# totec448-spec/chat-on-steroids — Cross-platform local MCP capabilities for ChatGPT with Chrome integration, Goal,

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/totec448-spec/chat-on-steroids
- 발행: 2026-09-12T10:54:37.403848+00:00
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
 241 
 
 

 
 
 
 
 
 Star
 1.7k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 35 


 
 
 
 
 
 
 
 
 Pull requests 
 19 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 120 Commits 120 Commits Folders and files Name Name Last commit message Last commit date .githooks .githooks     .github .github     artwork artwork     docs docs     extension extension     native native     scripts scripts     src src     test test     .gitattributes .gitattributes     .gitignore .gitignore     AGENTS.md AGENTS.md     CHANGELOG.md CHANGELOG.md     CLAUDE.md CLAUDE.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     SECURITY.md SECURITY.md     THIRD-PARTY-NOTICES.txt THIRD-PARTY-NOTICES.txt     electron-builder.yml electron-builder.yml     electron.vite.config.ts electron.vite.config.ts     package-lock.json package-lock.json     package.json package.json     tsconfig.json tsconfig.json     vitest.config.ts vitest.config.ts     View all files Repository files navigation README Contributing MIT license Security More items 

 
  
  
 


 All downloads 



 

 Get started  ·  Watch the demo  ·  What’s new 



 Code. Delegate. Keep going. 
 Work on the real project. Let ChatGPT read and edit files, run tests, keep terminals open and use your desktop. Follow the actual tool results as they arrive.

 Give it a team. Split independent jobs across workers, then bring their results back. Workers keep their context, so the next task can pick up where they left off.

 Stay in control of long tasks. Send a correction while work runs. Goal follows unfinished work; Loop keeps working within your brief. Compact & Resume carries the session and worker history into a fresh chat.

 Uses your ChatGPT conversation. Does not consume Codex quota. 
 Your account’s model availability, usage and context limits still apply. 



 Get started 
 
 Install CoS and approve your project folder in Settings → Workspace . 
 Connect Core through Settings → Setup and add it in ChatGPT’s Developer mode. Tunnel setup → 
 Load the companion extension. Click Open extension folder , then Load unpacked in Chrome’s extension settings. Pairing is automatic. 
 Choose a model, write your task and send. 
 
 
 Requirements & installation notes 
 Windows 10/11, macOS 13 Ventura or newer , or a current desktop Linux. Chrome 116+ or current Edge, plus a ChatGPT account/workspace with Developer mode and custom MCP apps. Check account availability .

 
 Unsigned beta: Windows is not publisher-signed; macOS is unsigned and unnotarized. Verify the package against the release checksums. 
 Linux: a Secret Service keyring is required. Prefer the DEB; when unprivileged user namespaces are disabled, the AppImage launcher can fall back to --no-sandbox . 
 Permissions: choose your approved folders and review capabilities before connecting. Fresh installs enable Core capabilities and two workers; Windows also enables Desktop permissions. Shell commands run with your normal user privileges. 
 After updating: reload the companion extension and refresh the CoS apps in ChatGPT when prompted. 
 
 
 
 More screenshots 
 

 

 

 


 
 Setup & help  ·  Plugins  ·  Contribute  ·  Security  ·  MIT license 

 Not affiliated with or endorsed by OpenAI. ChatGPT and Codex are OpenAI trademarks. 

 About Cross-platform local MCP capabilities for ChatGPT with Chrome integration, Goal, Compact & Resume, and durable multi-agent workflows.
 Topics automation chatgpt chrome-extension electron linux local-first macos mcp multi-agent windows Resources Readme MIT license Contributing Contributing Security policy Security policy Activity Stars 1.7k stars Watchers 6 watching Forks 241 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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