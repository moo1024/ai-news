# 0.151.0

- 출처: Codex 릴리스
- 원본 링크: https://github.com/openai/codex/releases/tag/rust-v0.151.0
- 발행: 2026-08-29T09:57:02+00:00
- 접근상태: 확인 완료

---

Release 0.151.0 · openai/codex · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 openai
 
 / 
 
 codex 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 18.3k 
 
 

 
 
 
 
 
 Star
 120k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 5k+ 


 
 
 
 
 
 
 
 
 Pull requests 
 170 


 
 
 
 
 
 
 
 
 Discussions 
 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Security and quality 
 1 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Discussions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 
 
 
 Releases 
 rust-v0.151.0 
 
 
 
 
 
 
 
 
 0.151.0 
 
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
 
 
 
 

 
 

 
 
 
 
 github-actions 

 released this

 
 29 Aug 09:55
 
 

 
 
 ·
 
 68 commits
 
 to main
 since this release
 


 
 
 
 
 
 
 rust-v0.151.0
 
 
 
 
 
 
 
 78c2908 
 

 
 
 New Features 
 
 Added a configurable grace period for discovering tools from optional MCP servers. ( #41199 ) 
 Extensions can now inspect or replace MCP tool results before they reach the model. ( #41202 ) 
 Plugin catalogs now combine per-repository configuration and report invalid project marketplaces without hiding valid plugins. ( #41208 ) 
 
 Bug Fixes 
 
 Preserved restored permission profiles across TUI turns and prevented /cd from weakening sandbox restrictions. ( #41192 ) 
 Kept tool availability and reasoning effort correct when switching models or falling back to another model. ( #41195 , #41206 ) 
 Improved remote sandbox enforcement using the executor’s actual home directory, operating system, and path conventions. ( #41196 , #41204 , #41207 , #41209 ) 
 Preserved structured MCP tool and resource errors in app-server responses. ( #41196 ) 
 Counted nested subagent token usage toward root goal budgets. ( #41183 ) 
 Prevented stale Guardian classifications from authorizing actions after permission state changes. ( #41196 ) 
 
 Chores 
 
 Added telemetry for escalated stdin reviews and remote executor MCP discovery. ( #41189 , #41205 ) 
 Stabilized Guardian WebSocket and core fixture tests under slow or highly concurrent CI. ( #41191 , #41194 ) 
 
 Changelog 
 Full Changelog: rust-v0.150.0...rust-v0.151.0 

 
 #41183 Account subagent token usage toward root goals @copyberry 
 #41189 Instrument stdin review size checks @copyberry 
 #41191 Stabilize Guardian WebSocket tests @copyberry 
 #41192 Preserve restored permission profiles in TUI sessions @copyberry 
 #41193 Report affected capabilities from remote plugin syncs @copyberry 
 #41194 Harden core test fixture startup assertions @copyberry 
 #41195 Finalize model-specific tool plans in ToolRouter @copyberry 
 #41196 Improve sandboxing, MCP errors, and cached approvals @copyberry 
 #41199 Make the optional MCP startup grace configurable @copyberry 
 #41202 Let extensions process MCP tool results @copyberry 
 #41204 Propagate executor home directories into sandbox contexts @copyberry 
 #41205 Track executor MCP discovery telemetry @copyberry 
 #41206 Make Ultra reasoning fallback model-aware @copyberry 
 #41207 Propagate executor OS into turn environments @copyberry 
 #41208 Honor per-repository plugin configuration in catalog requests @copyberry 
 #41209 Align deny-read matching with executor path semantics @copyberry 
 
 
 
 Contributors 
 
 
 
 
 
 
 

 
 copyberry
 

 

 
 
 
 
 Assets 
 162 
 
 
 
 
 
 
 
 
 Loading 
 

 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 
 

 


 
 
 --> 
 
 
 👍 
 4 
 felipeadeildo, Yuruzuu, Flower-fertilizer, and teamchat538-coder reacted with thumbs up emoji 
 
 
 
 All reactions 
 
 

 
 
 👍 
 4 reactions 
 
 
 
 
 
 4 people reacted 
 
 
 
 

 


 

 


 
 

 

 
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