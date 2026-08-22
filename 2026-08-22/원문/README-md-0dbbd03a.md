# Claudette: Make Claude stop talking like a BuzzFeed article

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://github.com/adnanakil/nobuzz/blob/main/README.md
- 발행: 2026-08-21T14:31:52+00:00
- 접근상태: 확인 완료

---

nobuzz/README.md at main · adnanakil/nobuzz · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 adnanakil
 
 / 
 
 nobuzz 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 2 
 
 

 
 
 
 
 
 Star
 89 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 1 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 Files Expand file tree main Breadcrumbs nobuzz / README.md Copy path Blame More file actions Blame More file actions Latest commit   History History History 54 lines (33 loc) · 3.79 KB main Breadcrumbs nobuzz / README.md Copy path Top File metadata and controls Preview Code Blame 54 lines (33 loc) · 3.79 KB Raw Copy raw file Download raw file Outline Edit and raw actions NoBuzz 
 Obviously it's common knowledge by now that Anthropic has solely trained claude on old Buzzfeed articles (explaining its love for 90s nostalgia). So Claude and I built a Claude Code skill ( /debuzz ) that takes Claude's last response and runs it through the Antigravity CLI ( agy ) to translate it from talking like a millennial clickbait to regular English. We're thinking of calling it "Claudette" but Cat Wu is famously litigious so it's definitely absolutely not called "Claudette".

 The problem 
 Claudette is our solution to Claude being a great engineer with one incurable condition: it talks like it's delivering a TED talk about its own pull request. You ask why a test is flaky and you get a "load-bearing assumption," three numbered revelations, and a solemn note that the third one is the most instructive yet . Nothing is ever just a bug. There is always a kicker.

 This skill accepts that no amount of prompting fully cures this, and does the honest thing instead: it hands the response to a different model, Gemini (remember gemini from last summer?) via Google's Antigravity CLI, whose only job is to say it like a human person. Claudette has pinky promised to print Antigravity's translation verbatim, because letting Claude "tidy up" the translation reintroduces exactly the voice being removed.

 Before / after 
 Before (Claude): 

 
 Here's where it gets interesting: the retry logic isn't just a nice-to-have — it's - the - load-bearing - assumption - of - the - entire - sync - pipeline. Three things jumped out at me, and the third one is the most instructive yet. [...] And third — and this is the kicker — the dedupe key includes a timestamp, which means retries are never actually deduplicated.

 
 After ( /debuzz , colleague mode): 

 
 The sync pipeline's retry logic has three bugs. syncQueue.ts:142 swallows ETIMEDOUT instead of re-queuing the job. The backoff caps at 2 seconds, which is too low for mobile networks. And the dedupe key includes a timestamp, so retries are never deduplicated. Fix: strip the timestamp from the key, raise the cap to 30 seconds, and re-throw the timeout error.

 
 Install 
 git clone https://github.com/adnanakil/nobuzz
mkdir -p ~ /.claude/skills
cp -r nobuzz/debuzz ~ /.claude/skills/ 
 Requirements:

 
 Claude Code 
 The Antigravity CLI ( agy ) — install with curl -fsSL https://antigravity.google/cli/install.sh | bash (macOS/Linux) or irm https://antigravity.google/cli/install.ps1 | iex (Windows), then run agy once to complete the Google Sign-In flow. 
 
 Usage 
 /debuzz [mode] [text]
 
 
 
 
 Mode 
 Audience 
 What you get 
 
 
 
 
 colleague (default) 
 An engineer 
 Same content, every file path and code block intact, zero theatrics 
 
 
 manager 
 A technical-adjacent manager 
 What happened, why it matters, what's next — about a third the length, no code 
 
 
 director 
 An executive 
 Three to five sentences: outcome, impact, ask. Assumes thirty seconds of attention 
 
 
 
 With no text argument it translates Claude's previous reply. Paste text after the mode to translate that instead. It also triggers on natural phrases like "say that in normal english."

 How it works 
 No magic. Claudette writes its previous reply to a temp file and runs agy -p "$(cat <file>) <plain-English style instructions>" — agy's headless mode doesn't read stdin and won't read files outside the project, so the text goes straight into the prompt — then prints Antigravity's output verbatim. If agy errors (usually auth), you see the actual error — Claude only offers its own rewrite as a clearly labeled fallback, because a debuzzer that quietly asks the buzzer to debuzz itself is how you end up with a load-bearing translation.

 License 
 MIT

 
 




 

 

 
 

 

 
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