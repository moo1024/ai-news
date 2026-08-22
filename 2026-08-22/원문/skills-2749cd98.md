# jakubkrehel/skills — A collection of agent skills that help you build a great interface.

- 출처: GitHub 신규 (에이전트 스킬)
- 원본 링크: https://github.com/jakubkrehel/skills
- 발행: 2026-08-22T03:54:40.404536+00:00
- 접근상태: 확인 완료

---

GitHub - jakubkrehel/skills: A collection of agent skills that help you build a great interface. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 jakubkrehel
 
 / 
 
 skills 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 135 
 
 

 
 
 
 
 
 Star
 4.1k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 1 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 88 Commits 88 Commits Folders and files Name Name Last commit message Last commit date .claude-plugin .claude-plugin     skills skills     .gitattributes .gitattributes     AGENTS.md AGENTS.md     CLAUDE.md CLAUDE.md     LICENSE LICENSE     README.md README.md     opencode.json opencode.json     View all files Repository files navigation README MIT license More items 
 
 
 

 A collection of agent skills that help you build a great interface. They cover UI, typography, colors, accessibility, layout, product writing and more.

 Skills 
 
 better-interface : A cross-discipline interface review that coordinates every skill below. 
 interface-review : A user-invoked review of your uncommitted changes, current branch or a pull request against every skill below. Run it by name; it never starts on its own. 
 variant : Builds several genuinely different versions of one piece of UI behind a picker, so you can flip between them in the real page and promote the one that wins. Run it by name. 
 explain-interface : Ask how something was built. Point it at a URL or a screenshot, name the thing you're curious about, and it finds the layers behind the effect and explains what each one does. Run it by name. 
 better-ui : Design engineering details that make interfaces feel polished: border radius, shadows, animations and micro-interactions. 
 better-typography : Choosing and pairing typefaces, type scales, spacing, wrapping and truncation. 
 better-colors : Color systems: building and naming palettes, applying color with meaning, contrast and theming. 
 better-accessibility : Focus states, keyboard support, ARIA, forms, screen readers, hit areas and motion. 
 better-layout : Layout structure, grouping, alignment, reading order, progressive disclosure and adaptive breakpoints. 
 better-writing : UX writing and interface copy, from button labels to errors, settings and empty states. 
 
 Install 
 Both methods install the same skills. They differ in what you type to run one, so pick a method and use its names.

 CLI 
 Works in Claude Code, Codex, Opencode and other agents. You can choose which skills to install or install all of them.

 npx skills add jakubkrehel/skills 
 Skills installed this way keep their plain names, so the change review runs as /interface-review .

 Claude Code plugin 
 Installs every skill in this repository together and updates in place. Run these inside Claude Code:

 /plugin marketplace add jakubkrehel/skills
/plugin install interfaces@interfaces
 
 Plugin skills are namespaced under the plugin, so the change review runs as /interfaces:interface-review and variants as /interfaces:variant .

 To update later, run /plugin update interfaces@interfaces and restart.

 About A collection of agent skills that help you build a great interface.
 jakub.kr/skills Resources Readme MIT license Activity Stars 4.1k stars Watchers 19 watching Forks 135 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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