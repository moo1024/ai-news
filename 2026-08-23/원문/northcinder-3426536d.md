# cinderline/northcinder — Open-source MCP server for comparing products and asking the buyer before purcha

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/cinderline/northcinder
- 발행: 2026-08-22T22:24:14.869265+00:00
- 접근상태: 확인 완료

---

GitHub - cinderline/northcinder: Open-source MCP server for comparing products and asking the buyer before purchase. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
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
 6 
 
 

 
 
 
 
 
 Star
 1.2k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 2 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 6 Commits 6 Commits Folders and files Name Name Last commit message Last commit date .github .github     adapters adapters     client client     docs docs     northcinder northcinder     packages packages     patches patches     remote remote     scripts/ release scripts/ release     service service     site site     .env.example .env.example     .gitignore .gitignore     CHANGELOG.md CHANGELOG.md     CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     MANIFESTO.md MANIFESTO.md     README.md README.md     SECURITY.md SECURITY.md     SUPPORT.md SUPPORT.md     package.json package.json     pnpm-lock.yaml pnpm-lock.yaml     pnpm-workspace.yaml pnpm-workspace.yaml     tsconfig.base.json tsconfig.base.json     View all files Repository files navigation README Code of conduct Contributing MIT license Security More items NorthCinder 
 Your shopping agent should work for you. 

 AI agents are starting to do more than answer shopping questions. Soon they will decide which products people see and, in some cases, buy on their behalf.

 Big marketplaces are building the easiest version of this: an agent that searches one catalog and steers the buyer toward that platform's checkout. That may be convenient, but it is not independent advice. The marketplace still decides what can be seen and makes money when the agent closes the sale.

 NorthCinder takes a different approach. It compares products from the sources you choose and shows where its facts came from. Before it buys anything, it asks for your approval. NorthCinder is software you run alongside your AI app.

 The repository owner does not operate a NorthCinder service. There is no NorthCinder account or cloud service.

 Get started 
 You need Node.js 20 or later and an MCP-capable AI app.

 npx northcinder init 
 The command saves your configuration on your computer and prints the MCP entry for your AI app. Local mode is keyless. It runs the MCP server and search engine together in one process, using a temporary loopback port.

 Once connected, try a real shopping brief:

 
 Find black wool running shoes under $130. Compare price, delivery, fit, and merchant trust. Tell me why the winner ranked first and which options were ruled out.

 
 What a result looks like 
 NorthCinder does not pretend there is one universal "best" product. It normally shows no more than three useful choices: the strongest fit, a lower-risk option, and a cheaper or meaningfully different option when one exists.

 Each result explains why it ranked where it did. You can also inspect the other finalists, rejected offers, and facts that could not be verified.

 Research before recommendation 
 Product research gets messy quickly. Model names overlap, sellers copy one another, and a polished product page can hide the one detail that makes an item wrong for the buyer.

 NorthCinder includes separate research guides for products and sellers. Before doing the research, the MCP host should:

 
 Read northcinder://research/product or northcinder://research/seller . 
 Call create_research_plan with the actual request and exact subject. 
 Follow the returned checklist with the research tools it already controls. 
 
 If the sources disagree or do not identify the exact product or seller, the result stays provisional. Research can decide whether an offer is ready to compare, but it cannot add ranking points.

 No host and model combination is currently qualified for routine research use. Treat every research result as provisional until the buyer checks its identity, sources, conflicts, and unknowns.

 Buying stays a separate decision 
 A recommendation is not permission to buy. Every checkout needs a fresh approval for one exact offer and one unit. The signed approval includes the merchant, variant, price, known total, and spending cap. It can be used once.

 NorthCinder rejects raw card details. A supported automated checkout can use an opaque payment token, or NorthCinder can hand the buyer a cart link to finish in their own browser.

 Order outcomes stay local and only attach to the purchase they belong to. NorthCinder does not silently rewrite the buyer's profile, and its reminders only send notifications.

 Rules you can inspect 
 Seller payment never improves ranking. Sponsored offers stay labeled and below organic results. Missing store coverage stays visible, and unknown seller history remains unknown instead of being guessed safe or unsafe.

 NorthCinder reruns the ranking locally and writes recommendations, approvals, and checkout attempts to a local audit log. The ranking specification , trust specification , neutrality audit , and checkout package contain the details.

 These checks cover the offers NorthCinder received, not the completeness or truth of a store's catalog.

 How NorthCinder works 
 Your AI app talks to NorthCinder over MCP. NorthCinder runs the search engine locally, checks the ranking before returning it, and keeps the audit log and purchase approvals on your computer. You choose the store connections. The repository owner is not part of this path.

 Store coverage 
 Store access varies, and NorthCinder says when a store was unavailable or not configured. It does not present a partial search as though it covered the whole market.

 Built-in adapters cover Shopify , WooCommerce , eBay , Etsy , and read-only Amazon comparison.

 If a native connection is missing, the AI app can keep researching with its own browser or search tools. NorthCinder accepts product facts, not cookies, raw pages, passwords, or page instructions. A native connection must confirm the exact offer before checkout or an unattended watch.

 Self-hosted engine 
 Most people should use local mode. If you choose to run the engine separately, set NORTHCINDER_API_KEYS on the service and configure the client with NORTHCINDER_SERVICE_URL and the matching NORTHCINDER_CLIENT_KEY bearer credential. Non-loopback bearer connections must use HTTPS.

 Privacy 
 
 NorthCinder never needs your AI provider key. It stays in your AI app. Store credentials stay with you and the store. 
 NorthCinder does not send your searches, settings, or local history to the repository owner. 
 Raw card details are rejected rather than stored or forwarded. 
 Starting a search or price watch does not give NorthCinder permission to buy anything. 
 
 Read privacy and software ownership and the security policy for the full boundary.

 Build from source 
 This is a pnpm workspace. Product packages need Node.js 20 or later. The private site workspace needs Node.js 22.12 or later.

 corepack pnpm install --frozen-lockfile
corepack pnpm build
node northcinder/bin/northcinder.js init 
 The full release checks are documented in CONTRIBUTING.md .

 Contributing and support 
 
 Use GitHub Issues for reproducible bugs and focused proposals. 
 Use GitHub Discussions for questions and early ideas. 
 Report vulnerabilities through GitHub private vulnerability reporting , not a public issue. 
 
 NorthCinder is open source under the MIT License .

 About Open-source MCP server for comparing products and asking the buyer before purchase.
 Topics agentic-commerce human-in-the-loop local-first mcp mcp-server model-context-protocol privacy self-hosted shopping-agent typescript Resources Readme MIT license Code of conduct Code of conduct Contributing Contributing Security policy Security policy Activity Stars 1.2k stars Watchers 5 watching Forks 6 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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