# Appllama/appllama-skills — A builder, not just a researcher. Agent skills that turn top-grossing app patter

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/Appllama/appllama-skills
- 발행: 2026-09-10T12:22:47.260202+00:00
- 접근상태: 확인 완료

---

GitHub - Appllama/appllama-skills: A builder, not just a researcher. Agent skills that turn top-grossing app patterns into native-quality mobile screens. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 Appllama
 
 / 
 
 appllama-skills 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 71 
 
 

 
 
 
 
 
 Star
 1.3k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 0 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 10 Commits 10 Commits Folders and files Name Name Last commit message Last commit date .claude-plugin .claude-plugin     .cursor-plugin .cursor-plugin     skills skills     .gitignore .gitignore     .mcp.json .mcp.json     LICENSE LICENSE     README.md README.md     mcp.json mcp.json     View all files Repository files navigation README MIT license More items 
 
 
 
 
 
 


 A builder, not just a researcher. 
 
 Agent skills that make AI agents genuinely good at building mobile apps —

 studied against the top-grossing apps, finished to a simulator-verified bar.


 
 
 
 


 
 appllama.io ·
 MCP ·
 X ·
 LinkedIn ·
 Product Hunt 


 
 Appllama is the design library of top-grossing mobile
apps — their real screens, flows, and UI patterns, with revenue and download
context. These skills turn that library into an agent's working method:
study every screen of the apps that already win, extract the category's
design language, then build screens that hold up next to them.

 The skills 
 
 
 
 Skill 
 What it does 
 
 
 
 
 appllama-usage 
 The research engine: how to use the Appllama MCP like a design director — the full tool map, and the playbooks for building an app from scratch, improving an existing screen, and flow & element research. 
 
 
 appllama-app-design-skill 
 The build bar: native-feeling Expo / React Native screens — Apple HIG fidelity, semantic colors, native controls, anti-slop discipline, navigation that behaves (push vs replace, sheets and overlays, the one-way doors where back must not exist), a strict motion bar (should it animate at all, springs that carry the finger's velocity, nothing on the JS thread), generated image assets, and a full-motion simulator loop (whole flows recorded and scrubbed frame by frame, not screenshots). 
 
 
 
 They are designed as a pair: usage decides what to study, design 
decides how to build, and both insist the loop only ends in a simulator
with a screen you can't fault.

 Install 
 One command, from your project root — works with Claude Code, Cursor,
Codex, and 70+ other agents :

 npx skills@latest add appllama/appllama-skills 
 Variations:

 # install for specific agents, no prompts 
npx skills@latest add appllama/appllama-skills -a claude-code -a cursor -y

 # install user-wide instead of per-project 
npx skills@latest add appllama/appllama-skills -g 
 Only want the app design skill? 
 appllama-app-design-skill stands on its own — the native-quality build
bar, anti-slop discipline, and the full-motion simulator loop work with or
without the Appllama MCP connected:

 npx skills@latest add appllama/appllama-skills --skill appllama-app-design-skill 
 (The same --skill flag installs only appllama-usage if you want just the
research engine.)

 
 Manual install 
 Skills are plain directories — copy them into your agent's skills folder
( .claude/skills/ per project, ~/.claude/skills/ user-wide, or your
harness's equivalent):

 git clone https://github.com/appllama/appllama-skills
cp -r appllama-skills/skills/ * ~ /.claude/skills/ 
 
 Connect the Appllama MCP 
 appllama-usage runs on the Appllama MCP; appllama-app-design-skill is
sharper with it connected. The endpoint:

 https://mcp.appllama.io/mcp
 
 Add it as a custom connector in Claude, Cursor, Codex, or any MCP client
and approve the connection with your Appllama account. MCP access is part
of Pro ; credits reset in full on the 1st of
each month. Every call spends one credit — get_credits is always free.

 Try it 
 With the MCP connected and the skills installed, ask your agent:

 
 Build me a habit tracker. Study the top-grossing habit apps first and
don't stop until every screen survives the simulator comparison.

 
 
 Make this screen better. (paste a screenshot, code, or a "Copy Screen
ID" ref from appllama.io) 

 
 
 How do the best fitness apps structure onboarding — how long, what does
each step earn, and where does the paywall sit?

 
 
 Wire up the checkout flow. Decide which screens push, which present as
sheets, and make sure nobody can go back into the paywall after paying.

 
 
 Review the animations in this app — what should be deleted, what's on the
wrong thread, what's missing velocity — and give me the plan.

 
 License 
 MIT . The Appllama name, llama, and logo are trademarks of
Antmind Ventures Private Limited — the license does not grant rights to
use them.

 
 
 Built by Appllama — the design library of top-grossing apps.

 X ·
 LinkedIn ·
 Product Hunt 


 About A builder, not just a researcher. Agent skills that turn top-grossing app patterns into native-quality mobile screens.
 appllama.io/mcp Topics agent-skills ai-agents claude claude-code claude-code-skill claude-skills codex codex-skill cursor design-system expo mcp mobile-app-development mobile-design mobile-ui model-context-protocol react-native skills ui-design Resources Readme MIT license Activity Custom properties Stars 1.3k stars Watchers 0 watching Forks 71 forks Report repository Releases Packages Contributors 
 




 

 

 
 

 

 
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