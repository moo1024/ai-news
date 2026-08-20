# cinderline/northcinder — Buyer-run, ad-neutral shopping-agent MCP software with deterministic ranking, si

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/cinderline/northcinder
- 발행: 2026-08-20T22:24:11.655602+00:00
- 접근상태: 확인 완료

---

GitHub - cinderline/northcinder: Buyer-run, ad-neutral shopping-agent MCP software with deterministic ranking, signed purchase mandates, and a local audit trail. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 cinderline
 
 / 
 
 northcinder 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 5 
 
 

 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 2 Commits 2 Commits Folders and files Name Name Last commit message Last commit date .github .github     adapters adapters     client client     docs docs     northcinder northcinder     packages packages     patches patches     remote remote     scripts/ release scripts/ release     service service     site site     .env.example .env.example     .gitignore .gitignore     CHANGELOG.md CHANGELOG.md     CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     MANIFESTO.md MANIFESTO.md     README.md README.md     SECURITY.md SECURITY.md     SUPPORT.md SUPPORT.md     package.json package.json     pnpm-lock.yaml pnpm-lock.yaml     pnpm-workspace.yaml pnpm-workspace.yaml     tsconfig.base.json tsconfig.base.json     View all files Repository files navigation README Code of conduct Contributing MIT license Security More items NorthCinder 
 Make your shopping agent compare, explain, and ask before buying. 

 NorthCinder is an open-source MCP server that helps an AI agent compare products against your brief. It
returns a ranked shortlist with reasons, reports which stores it could and could not search, and requires a
separate approval before checkout. Seller payment and affiliate data never improve a result's position.

 NorthCinder is software you run. It works on your computer alongside the AI app you already use. The
repository owner does not operate a NorthCinder service. There is no NorthCinder account, hosted control
plane, or telemetry service.

 Get started 
 You need Node.js 20 or later and an AI app that supports MCP.

 npx northcinder init 
 The initializer walks you through local setup and prints the MCP configuration for your AI app. After you
connect it, try a specific brief:

 
 Find black wool running shoes under $130. Compare price, delivery, fit, and merchant trust. Tell me why
the winner ranked first and which options were ruled out.

 
 What you get 
 NorthCinder's response includes:

 
 the offers that matched the required criteria; 
 the score and machine-readable reasons for each recommendation; 
 rejected offers and the requirement each one missed; 
 merchant-trust evidence and missing evidence; 
 a store-by-store coverage report; and 
 sponsorship and source labels that remain attached to every offer. 
 
 The contract you can inspect 
 
 
 
 Concern 
 NorthCinder's rule 
 Evidence 
 
 
 
 
 Ranking 
 Buyer criteria determine the order. Seller payment is not an input. 
 Ranking specification and ranking source 
 
 
 Sponsored offers 
 Labeled sponsored offers remain below every organic result. 
 Neutrality audit 
 
 
 Coverage 
 Unavailable and unconfigured stores stay visible in the response. 
 Adapter contract 
 
 
 Merchant trust 
 Every merchant carries explicit evidence or an honest unknown state. 
 Trust specification 
 
 
 Checkout 
 A signed, single-use mandate binds the exact offer, quantity, and spending cap. 
 Checkout package 
 
 
 Audit 
 Recommendations, approvals, and checkout attempts are written to a local audit trail. 
 Client source 
 
 
 
 The client reruns the deterministic ranking over the service-disclosed inputs. This verifies the order it
received; it does not prove that an upstream catalog was complete or that every store-supplied fact was true.

 How NorthCinder works 
 
 
 
 flowchart LR
 A["Your AI app"] -->|MCP| C["NorthCinder client"]
 C --> S["Buyer-run search service"]
 S --> D["Configured store adapters"]
 S --> C
 C --> R["Local reranking and reasons"]
 C --> L["Local audit trail"]
 C --> P["Buyer approval"]
 P -->|signed single-use mandate| X["Checkout rail or cart handoff"]
 
 
 
 
 
 
 
 
 Loading 
 
 
 

 The repository owner is not in this runtime path. You run the client and aggregation engine, choose the
store connections, and keep the local configuration and audit data.

 Store coverage 
 Store access varies because each platform has different rules. NorthCinder reports a store as unavailable
or blocked when it cannot search it instead of presenting partial coverage as a complete market search.

 
 
 
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
 
 
 
 When a native store connection is unavailable, your agent may still compare permitted product pages with
browser tools it already controls. NorthCinder accepts normalized product facts, not cookies, raw HTML,
screenshots, page instructions, passwords, one-time codes, or your AI-provider key. Agent-observed offers
must be confirmed by a native adapter or merchant protocol before automated checkout or an unattended watch.

 Privacy and purchase control 
 
 Your AI-provider key stays in your AI app. Store credentials stay with you and the store. 
 NorthCinder does not send your searches, settings, or local history to the repository owner. 
 Raw card details are rejected. Automated rails use opaque delegated payment tokens when available. 
 Search and price watches are not permission to buy. Every automated checkout needs approval for that
specific purchase. 
 The approval mandate is single use and protected by a cross-process nonce ledger. 
 
 Read privacy and software ownership and the security policy for
the complete boundary.

 Project status 
 northcinder 0.1.2 is the initial public release. The repository includes offline build, typecheck, test,
dependency, secret, packaging, and public-surface checks. Fixture and harness coverage does not prove current
third-party credentials, production access to every store, or a completed real purchase. Read the relevant
adapter documentation before relying on a specific integration.

 The package is not yet listed in the official MCP Registry, and the marketing site in this repository has
not been published at a canonical production origin.

 Build from source 
 This is a pnpm workspace. Product packages require Node.js 20 or later; the private site workspace requires
Node.js 22.12 or later.

 corepack pnpm install --frozen-lockfile
corepack pnpm build 
 Then run the local initializer from the checkout:

 node northcinder/bin/northcinder.js init 
 Contributors can find the full release-verification commands in CONTRIBUTING.md .

 Contributing and support 
 
 Read CONTRIBUTING.md before proposing a change. 
 Use GitHub Issues for reproducible bugs and focused work. 
 Use GitHub Discussions for questions and open-ended ideas. 
 Report vulnerabilities through GitHub private vulnerability reporting , not a public issue. 
 
 NorthCinder is open source under the MIT License .

 About Buyer-run, ad-neutral shopping-agent MCP software with deterministic ranking, signed purchase mandates, and a local audit trail.
 Topics agentic-commerce human-in-the-loop local-first mcp mcp-server model-context-protocol privacy self-hosted shopping-agent typescript Resources Readme MIT license Code of conduct Code of conduct Contributing Contributing Security policy Security policy Activity Stars 1.2k stars Watchers 5 watching Forks 5 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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