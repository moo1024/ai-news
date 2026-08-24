# A Claude Code skill that recovers export-blocked Kindle highlights

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://github.com/l3a0/claude-plugins
- 발행: 2026-08-24T19:32:18+00:00
- 접근상태: 확인 완료

---

GitHub - l3a0/claude-plugins: l3a0's Claude Code plugin marketplace — kindle-highlights: verbatim Kindle highlight extraction with truncation recovery · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 l3a0
 
 / 
 
 claude-plugins 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 1 
 
 

 
 
 
 
 
 Star
 11 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 7 Commits 7 Commits Folders and files Name Name Last commit message Last commit date .claude-plugin .claude-plugin     blog blog     skills/ kindle-highlights skills/ kindle-highlights     LICENSE LICENSE     README.md README.md     View all files Repository files navigation README MIT license More items l3a0's Claude Code plugins 
 A personal collection of Claude Code skills, published as a single
plugin under the l3a0 namespace. This repo is both the plugin and its own marketplace.

 I write about how these tools get built — and about technology, business, and finance — at
 baowebdev.substack.com .

 Install 
 claude plugin marketplace add l3a0/claude-plugins
claude plugin install l3a0@l3a0 
 Skills are invoked as /l3a0:<skill-name> (the bare /<skill-name> also works while no other
installed command claims the name), and Claude auto-invokes them when a request matches a
skill's description.

 Skills 
 kindle-highlights 
 Export a heavily-highlighted book from Amazon's notebook page and some highlights come back
cut off mid-sentence, while others come back as a bare location number with no text at all,
under this notice:

 
 "Some highlights have been hidden or truncated due to export limits."

 
 Those are your own notes, in your own account, capped by a budget Amazon doesn't document and
you can't raise. This skill gets them back: it extracts every highlight for a book from the
Kindle notebook ( read.amazon.com/notebook ) into one combined, verbatim, location-cited 
Markdown file — including the highlights the export limit truncates or hides entirely, which
are recovered from the Mac Kindle app's synced annotation positions plus the Cloud Reader's
rendered pages.

 Proven on four real books: 2,432 highlights extracted, 815 of them export-blocked (454
truncated + 361 fully hidden) — every one recovered , with recovered text landing within a
couple of characters of the Kindle app's own position ruler (median residual 0–1). Every
gotcha in the skill was earned by real debugging across those runs.
The build story — why the export limit exists, the three unlocks that beat it, and what a
library of exports becomes — is written up in
 How to Take Back Your Kindle Highlights ,
also published on Substack .

 Scope: this exports your own highlights from your own Amazon account, by driving your
own logged-in browser session and reading files the Kindle app stores on your Mac. The output
is for your personal notes — book text is copyrighted, so keep extracted notes private.

 Prerequisites (macOS only) 
 The pipeline is macOS-only three times over: browser control runs over AppleScript, OCR uses
Apple's Vision framework, and highlight positions come from the Mac Kindle app's data files.

 
 Claude Desktop with the "Control Chrome" extension — Anthropic's browser-control MCP,
installed in one click from Claude Desktop → Settings → Extensions. It is the skill's
verified path for executing JavaScript in your real Chrome (any browser MCP that can run JS
in the tab can substitute). It requires a Chrome setting:
Chrome menu bar → View → Developer → Allow JavaScript from Apple Events → check →
quit and relaunch Chrome. 
 Google Chrome , signed in to your Amazon account (the skill drives
 read.amazon.com ). 
 The current Mac Kindle app (App Store; bundle id com.amazon.Lassen — not the classic
Kindle.app), signed in to the same Amazon account, with the book downloaded. Its synced
annotation database provides exact highlight extents with no export limit. 
 Xcode Command Line Tools ( xcode-select --install ) — the bulk-recovery path compiles a
small Swift OCR helper ( swiftc ) that uses Apple Vision. 
 python3 — builds the final Markdown and runs a localhost receiver
( 127.0.0.1:8931 ) that the reader page POSTs captures to. 
 
 What it does, briefly 
 
 Scrapes all highlights from the notebook page DOM to JSON (verbatim typography preserved). 
 Reads exact character-precise highlight positions from the Kindle app's SQLite database —
including highlights the web export hides completely. 
 For blocked text, captures the Cloud Reader's rendered pages via canvas (no OS screenshots
needed), OCRs them locally with Apple Vision (zero tokens), and cuts the text to the known
positions. 
 Emits one Markdown file with ### Location N sections, blockquoted verbatim text, and
flags for anything recovered or approximate, then runs a QA pass. 
 
 License 
 MIT 

 About l3a0's Claude Code plugin marketplace — kindle-highlights: verbatim Kindle highlight extraction with truncation recovery
 Topics ai-agents claude claude-code claude-plugin data-ownership kindle kindle-highlights note-taking ocr pkm Resources Readme MIT license Activity Stars 11 stars Watchers 0 watching Forks 1 fork Report repository Releases Packages Used by Contributors Languages 
 




 

 

 
 

 

 
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