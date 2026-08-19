# jdshfhds/northcinder — Buyer-run, ad-neutral shopping-agent MCP software with deterministic ranking, si

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/jdshfhds/northcinder
- 발행: 2026-08-19T03:45:28.294035+00:00
- 접근상태: 확인 완료

---

GitHub - jdshfhds/northcinder: Buyer-run, ad-neutral shopping-agent MCP software with deterministic ranking, signed purchase mandates, and a local audit trail. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 jdshfhds
 
 / 
 
 northcinder 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 4 
 
 

 
 
 
 
 
 Star
 1.2k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 0 


 
 
 
 
 
 
 
 
 Discussions 
 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Security and quality 
 0 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Discussions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 1 Commit 1 Commit Folders and files Name Name Last commit message Last commit date adapters adapters     client client     docs docs     northcinder northcinder     packages packages     patches patches     remote remote     scripts/ release scripts/ release     service service     site site     .env.example .env.example     .gitignore .gitignore     CHANGELOG.md CHANGELOG.md     CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     MANIFESTO.md MANIFESTO.md     README.md README.md     SECURITY.md SECURITY.md     SUPPORT.md SUPPORT.md     package.json package.json     pnpm-lock.yaml pnpm-lock.yaml     pnpm-workspace.yaml pnpm-workspace.yaml     tsconfig.base.json tsconfig.base.json     View all files Repository files navigation README Code of conduct Contributing MIT license Security More items NorthCinder 
 Make your shopping agent compare, explain, and ask before buying. 

 NorthCinder helps your AI agent search for products, compare them against your brief, and show why one
option ranks above another. Seller payment and affiliate data never improve a result's position.

 NorthCinder runs on your computer alongside the AI app you already use. There is no NorthCinder account or
cloud service.

 Get started 
 You need Node.js 20 or later and an AI app that supports MCP. MCP is the standard the app uses to
connect to tools running on your computer.

 npx northcinder init 
 The initializer walks you through setup and prints the configuration to add to your AI app. Once
connected, try a specific brief:

 
 Find black wool running shoes under $130. Compare price, delivery, fit, and merchant trust. Tell
me why the winner ranked first and which options were ruled out.

 
 What you get 
 
 A ranked shortlist based on the requirements and preferences in your brief. 
 Reasons for every recommendation, including tradeoffs and missing information. 
 Sponsored offers labeled and placed below organic results. 
 Merchant trust evidence and an honest report of which stores were searched. 
 A local history you can review, correct, and use to improve later searches. 
 A separate approval step before any automated checkout. 
 
 How NorthCinder works 
 
 You tell your agent what you want, what matters, and your budget. 
 NorthCinder collects candidates from the direct store connections you configured. Your agent can also pass
product details from browser tools it already controls. 
 NorthCinder checks the candidates, ranks them against your brief, and returns a shortlist with reasons
and coverage gaps. 
 If you choose to buy, NorthCinder asks you to approve the exact item, quantity, and spending limit. 
 
 Results reported from a browser are clearly marked as agent-observed. You can compare them and open
the product page, but NorthCinder will not use them for automated checkout or a background price watch
until a direct store connection confirms the offer.

 Store coverage 
 Store access varies because each platform has different rules. NorthCinder reports a store as unavailable
or blocked when it cannot search it, rather than presenting partial coverage as a complete market
search.

 
 
 
 Store 
 What works today 
 
 
 
 
 Shopify 
 Catalog search is available after additional Shopify setup. The older per-store connection is no longer current. 
 
 
 WooCommerce 
 Works with stores that expose WooCommerce's public Store API. 
 
 
 eBay 
 Native search requires approved eBay Buy API access. 
 
 
 Etsy 
 Native search requires approved Etsy app access. 
 
 
 Amazon 
 Read-only comparison can use a browser profile you control. It stops at challenges and does not check out. 
 
 
 
 When a native store connection is unavailable, your agent may still compare permitted product pages
with browser tools it already has. NorthCinder accepts only product facts needed for comparison. It does
not take over the browser or ask for cookies, page contents, passwords, one-time codes, or your AI
provider key.

 Privacy and control 
 NorthCinder is software you run. The repository owner does not operate a NorthCinder service.

 
 Your AI provider key stays in your AI app. Store logins stay with you and the store. 
 NorthCinder does not send your searches, settings, or local history to the repository owner. 
 NorthCinder never accepts raw card details. Automated checkout can use a payment token created for the purchase,
or NorthCinder can hand you a cart to finish in your own browser. 
 Search is not permission to buy. Every automated checkout needs your approval for that purchase. 
 
 Learn more 
 
 Why NorthCinder exists 
 How ranking works 
 How merchant trust works 
 Privacy and software ownership 
 Build from source or contribute 
 Report a security issue 
 
 NorthCinder is open source under the MIT License .

 About Buyer-run, ad-neutral shopping-agent MCP software with deterministic ranking, signed purchase mandates, and a local audit trail.
 Topics agentic-commerce human-in-the-loop local-first mcp mcp-server model-context-protocol privacy self-hosted shopping-agent typescript Resources Readme MIT license Code of conduct Code of conduct Contributing Contributing Security policy Security policy Activity Stars 1.2k stars Watchers 5 watching Forks 4 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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