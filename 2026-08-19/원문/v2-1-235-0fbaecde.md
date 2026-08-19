# v2.1.235

- 출처: Claude Code 릴리스
- 원본 링크: https://github.com/anthropics/claude-code/releases/tag/v2.1.235
- 발행: 2026-08-18T20:38:54+00:00
- 접근상태: 확인 완료

---

Release v2.1.235 · anthropics/claude-code · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 anthropics
 
 / 
 
 claude-code 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 22.8k 
 
 

 
 
 
 
 
 Star
 142k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 5k+ 


 
 
 
 
 
 
 
 
 Pull requests 
 729 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Security and quality 
 30 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 
 
 
 Releases 
 v2.1.235 
 
 
 
 
 
 
 
 
 v2.1.235 
 
 Latest 
 
 

 
 
 

 
 Latest 
 
 
 

 
 
 
 
 
 
 Compare 
 
 
 
 
 
 
 

 
 
 
 
 
 Choose a tag to compare
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Sorry, something went wrong. 


 
 
 
 
 Filter
 
 
 
 
 
 
 
 
 
 
 Loading 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Sorry, something went wrong. 
 
 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 
 
 No results found 
 
 
 
 View all tags 
 
 
 
 

 
 

 
 
 
 
 ashwin-ant 

 released this

 
 18 Aug 20:38
 
 

 


 
 
 
 
 
 
 v2.1.235
 
 
 
 
 
 
 
 c3d2e35 
 

 
 
 What's changed 
 
 Added an optional spellcheck setting that underlines misspelled words in the prompt input as you type, using your installed aspell , hunspell , or ispell 
 Fixed whole-prompt-cache invalidation when a language server disconnected or reconnected mid-session 
 Fixed nested markdown list items misaligning at depth 3+ and added a hanging indent to wrapped list items in the terminal UI 
 Fixed prompt input highlights (slash commands, keywords, mentions) appearing shifted by one or more characters in some multi-line prompts 
 Fixed Shift+Tab inside the permission prompt's comment field approving the edit and granting session-wide edit permission instead of closing the field 
 Fixed the Agent tool advertising a general-purpose default in sessions where that agent is unavailable: an omitted subagent_type there now gets a clear error listing the available agents 
 Fixed notebook cell delete/replace approval dialogs silently omitting the existing cell content when the notebook or cell could not be read; the dialog now says why 
 Fixed slash commands run while Claude is responding showing HTML entities instead of the actual characters 
 Fixed the prompt footer not showing the "Update installed" restart notice after a background auto-update 
 Fixed the expanded task list ( ctrl+t ) always starting collapsed when resuming or relaunching into a session that still has open tasks 
 Improved memory and CPU usage while cloud sessions such as /ultrareview or /autofix-pr run in the background — their event streams are no longer re-scanned and re-rendered on every update 
 Improved permission dialogs: display text and "don't ask again" options now always match what a grant would cover, and "don't ask again" is withheld when contents cannot be fully displayed 
 Improved the embedded grep in native macOS/Linux builds: pathological patterns now fail fast instead of exhausting memory, and -m N with -A/-C prints correct context 
 Improved the context-limit error to say when auto-compact is off and point to /config to re-enable it 
 Vim mode: NORMAL mode and cursor position are now preserved when toggling the detailed transcript (ctrl+o) or closing a panel 
 Dialogs: arrow keys and Enter pressed in quick succession now select the option you navigated to instead of the previously highlighted one 
 SendMessage now refuses messages too large for cross-session delivery up front instead of silently dropping them 
 Remote Control: claude rc now applies the same enterprise-gateway availability check as interactive startup 
 [VSCode] Fixed focus jumping between open Claude tabs on its own when a window with several Claude panels is restored or reloaded 
 
 
 
 
 
 
 
 Assets 
 12 
 
 
 
 
 
 
 
 
 Loading 
 

 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 
 

 


 
 
 --> 
 
 
 👍 
 6 
 mike1858, saita08, egoan82, Nolunga, brandaltux, and Kaushalt2004 reacted with thumbs up emoji 
 😄 
 3 
 mike1858, saita08, and Nolunga reacted with laugh emoji 
 🎉 
 5 
 mike1858, saita08, JRAVILES, thinh9e, and tareqmahmud reacted with hooray emoji 
 ❤️ 
 4 
 mike1858, saita08, sakharovmaksim, and JRAVILES reacted with heart emoji 
 🚀 
 4 
 mike1858, saita08, egoan82, and JRAVILES reacted with rocket emoji 
 👀 
 2 
 mike1858 and saita08 reacted with eyes emoji 
 
 
 
 All reactions 
 
 

 
 
 👍 
 6 reactions 
 
 
 😄 
 3 reactions 
 
 
 🎉 
 5 reactions 
 
 
 ❤️ 
 4 reactions 
 
 
 🚀 
 4 reactions 
 
 
 👀 
 2 reactions 
 
 
 
 
 
 10 people reacted 
 
 
 
 

 


 

 


 
 

 

 
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