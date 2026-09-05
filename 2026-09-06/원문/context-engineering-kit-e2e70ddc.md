# Claude Code skills for advanced context engineering techniques and patterns

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://github.com/NeoLabHQ/context-engineering-kit
- 발행: 2026-09-04T22:52:14+00:00
- 접근상태: 확인 완료

---

GitHub - NeoLabHQ/context-engineering-kit: Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemini CLI, and others. Includes CodeRabbit open-source alternative. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 NeoLabHQ
 
 / 
 
 context-engineering-kit 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 155 
 
 

 
 
 
 
 
 Star
 1.6k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 6 


 
 
 
 
 
 
 
 
 Pull requests 
 3 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 master Branches Tags Go to file Code Open more actions menu Latest commit   History 410 Commits 410 Commits Folders and files Name Name Last commit message Last commit date .claude-plugin .claude-plugin     .claude .claude     .cursor .cursor     .devcontainer .devcontainer     .github/ workflows .github/ workflows     .specs .specs     agents agents     antigravity antigravity     docs docs     plugins plugins     scripts scripts     skills skills     .gitbook.yaml .gitbook.yaml     .gitignore .gitignore     CLAUDE.md CLAUDE.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     gemini-extension.json gemini-extension.json     justfile justfile     plugin.json plugin.json     View all files Repository files navigation README Contributing GPL-3.0 license More items 
 


 
 
 
 

 Advanced context engineering techniques and patterns for Claude Code, OpenCode, Cursor, Antigravity and more.

 Quick Start · Plugins · Github Action · Reference · Docs 

 
 Context Engineering Kit 
 A hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint, focused on improving agent result quality and predictability.

 The marketplace is based on prompts our company's developers have used daily for a long time, supplemented by plugins from benchmarked papers and high-quality projects.

 Key Features 
 
 Simple to Use - Easy to install and use without any dependencies. Contains automatically used skills and self-explanatory commands. 
 Token-Efficient - Carefully crafted prompts and architecture, preferring command-oriented skills with sub-agents over general information skills when possible, to minimize populating context with unnecessary information. 
 Quality-Focused - Each plugin is focused on meaningfully improving agent results in a specific area. 
 Granular - Install only the plugins you need. Each plugin loads only its specific agents, commands, and skills, without overlap or redundant skills. 
 Scientifically proven - Plugins are based on proven techniques and patterns validated by reputable benchmarks and studies. 
 Open-Standards - Skills are based on agentskills.io specification. The SDD plugin is based on the Arc42 specification standard for software development documentation. 
 
 News 
 Updates from key releases:

 
 v3.1.0: Improved Spec-Driven Development plugin generated code quality by embedding DDD/SOLID rules in the developer agent and adding a dedicated code-reviewer agent that applies functional and OOP best-practices rules together with Muda waste analysis to reduce code complexity and duplication. 
 v3.0.0: Added support for AMP and Hermes agents. Tech Stack plugin now automatically injects typescript best practices when agent reads or writes TypeScript files. 
 v2.2.0: Subagent-Driven Development plugin now works as a distilled version of SDD plugin using meta-judge and judge sub-agents for specification generation on the fly and in parallel to implementation. DDD plugin now includes Clean Architecture, DDD, SOLID, Functional Programming, and other pattern examples as rules that are automatically added to the context during code writing. 
 v2.1.0: Spec-Driven Development plugin agents include high-level code quality guidelines from DDD plugin . 
 v2.0.0: Spec-Driven Development plugin was rewritten from scratch. It is now able to produce working code in 99% of cases on real-life production projects! 
 
 Quick Start 
 Step 1: Install Marketplace and Plugins 
 
 Claude Code 
 Open Claude Code and add the Context Engineering Kit marketplace:

 /plugin marketplace add NeoLabHQ/context-engineering-kit 
 This makes all plugins available for installation, but does not load any agents or skills into your context.

 Install any plugin — for example, reflexion:

 /plugin install reflexion@NeoLabHQ/context-engineering-kit 
 Each installed plugin loads only its specific agents, commands, and skills into Claude's context.

 
 
 Gemini CLI 
 Install the extension directly from the repository:

 gemini extensions install https://github.com/NeoLabHQ/context-engineering-kit 
 Note: This installs every plugin's skills and agents as a single bundle — there's no per-plugin selection like Claude Code's. Unfortunately, Gemini CLI does not support per-plugin selection. But you can delete skills and agents that you don't need, after installation.

 
 
 Antigravity CLI 
 Install the plugin directly from the repository's antigravity/ folder — Gemini CLI is not required:

 agy plugin install https://github.com/NeoLabHQ/context-engineering-kit/antigravity 
 Note: This installs every plugin's skills and agents as a single bundle — there's no per-plugin selection like Claude Code's. Unfortunately, Antigravity CLI does not support per-plugin selection. But you can delete skills and agents that you don't need, after installation.

 
 
 Cursor, Codex, OpenCode and others 
 Run the vercel-labs/skills command in your terminal:

 npx skills add NeoLabHQ/context-engineering-kit 
 You can pick which skills to install.

 Note: Each provider uses its own agent format and npx skills does not support subagents, so this installation method won't provide the full experience.

 
 
 Alternative installation methods 
 You can use OpenSkills to install skills by running the following commands:

 npx openskills install NeoLabHQ/context-engineering-kit
npx openskills sync 
 
 Step 2: Use Plugin 
 > claude " implement user authentication " 
 # Claude implements user authentication, then you can ask it to reflect on implementation 

 > /reflect
 # It analyses results and suggests improvements 
 # If issues are obvious, it will fix them immediately 
 # If they are minor, it will suggest improvements that you can respond to 
 > fix the issues

 # If you would like to prevent issues found during reflection from appearing again, 
 # ask Claude to extract resolution strategies and save the insights to project memory 
 > /memorize 
 Alternatively, you can use the reflect word in the initial prompt:

 > claude " implement user authentication, then reflect " 
 # Claude implements user authentication, 
 # then hook automatically runs /reflect 
 In order to use this hook, you need to have bun installed. However, it is not required for the overall command.

 Documentation 
 You can find the complete Context Engineering Kit documentation here .

 However, the main plugins we recommend starting with are Subagent-Driven Development and Spec-Driven Development .

 Agent Reliability Engineering 
 The three plugins in this marketplace are designed to improve how accurately and consistently the agent follows provided instructions and to reduce hallucinations and bias toward incorrect solutions. They are not competitors but rather complementary to each other, because they allow you to balance reliability vs. token cost. Here is a high-level comparison of different agent usage approaches and the probability of receiving results that are fully accurate and include zero hallucinations, based on task complexity:

 
 
 
 Approach 
 Probability of receiving fully accurate results for the following number of changed files (p) 
 Tokens Overhead 
 What does this mean in practice 
 
 
 1-3 
 4-10 
 10-20 
 20+ 
 
 
 
 
 One-shot prompt 
 60%-80% 
 30%-50% 
 5%-30% 
 1%-20% 
 0 
 Accuracy depends on model, but with context growth LLM quality degrades exponentially 
 
 
 /reflect 
 68%-91% 
 49%-71% 
 13%-41% 
 1%-30% 
 1k-3k 
 Agent finds and fixes missed requirements on its own 
 
 
 /reflect + /memorize 
 79%-87% 
 60%-79% 
 34%-42% 
 5%-30% 
 2k-5k 
 Agent extracts repeatable mistakes and avoids them during new tasks 
 
 
 /do-and-judge 
 90% 
 83% 
 60% 
 30% 
 1.5x-3x 
 Mitigates context rot, bias, hallucinations and missed requirements using Judge sub-agent 
 
 
 /do-in-steps 
 92% 
 90% 
 71% 
 50% 
 3x-5x 
 Resolves all issues similar to /do-and-judge, but separately per file group 
 
 
 /plan-task + /implement-task 
 94% 
 93% 
 85% 
 70% 
 5x-20x 
 Performs the /do-in-steps flow, but the specification mitigates issues caused by inconsistent architecture and codebase size 
 
 
 /brainstorm + /plan-task + /implement-task 
 95% 
 95% 
 90% 
 80% 
 5x-20x 
 Brainstorming decreases the number of incorrect decisions and missed requirements 
 
 
 /plan-task + human review + /implement-task 
 99% 
 99% 
 99% 
 95% 
 5x-35x 
 Human review mitigates misunderstanding of requirements by LLM 
 
 
 
 
 Reliability metrics are based on more than year of real development usage on production projects.

 
 Plugins List 
 To view all available plugins:

 /plugin 
 
 Reflexion - Feedback and refinement loops to improve output quality. 
 Spec-Driven Development - Commands for specification-driven development, based on Continuous Learning + LLM-as-Judge + Agent Swarm. Achieves development as compilation through reliable code generation. 
 Review - Open-source and higher quality version of CodeRabbit. Includes code and PR review commands and skills using multiple specialized agents with impact/confidence filtering. Free Github Actions integration available 
 Git - Commands for commit and PR creation. 
 Test-Driven Development - Commands for test-driven development and common anti-patterns, plus skills for testing using subagents. 
 Subagent-Driven Development - Skills for subagent-driven development, which dispatches a fresh subagent for each task with code review between tasks, enabling fast iteration with quality gates. 
 Domain-Driven Development - Commands to update CLAUDE.md with best practices for domain-driven development, focused on code quality, and includes Clean Architecture, SOLID principles, and other design patterns. 
 FPF - First Principles Framework - Structured reasoning using ADI cycle (Abduction-Deduction-Induction) with knowledge layer progression. Uses workflow command pattern with fpf-agent for hypothesis generation, verification, and auditable decision-making. 
 Kaizen - Inspired by Japanese continuous improvement philosophy, Agile and Lean development practices. Commands for analysis of root causes of issues and problems, including 5 Whys, Cause and Effect Analysis, and other techniques. 
 Customaize Agent - Commands and skills for writing and refining commands, hooks, and skills for Claude Code. Includes Anthropic Best Practices and Agent Persuasion Principles that can be useful for sub-agent workflows. 
 Docs - Commands for analyzing projects, wr