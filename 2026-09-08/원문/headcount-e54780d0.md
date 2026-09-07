# cbrock84/headcount — An agent organization for Claude Code, structured as a company — 15+ departments

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/cbrock84/headcount
- 발행: 2026-09-07T22:24:38.821148+00:00
- 접근상태: 확인 완료

---

GitHub - cbrock84/headcount: An agent organization for Claude Code, structured as a company — 15+ departments, 125+ skills, each independently installable. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 cbrock84
 
 / 
 
 headcount 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 204 
 
 

 
 
 
 
 
 Star
 1.3k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 1 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 72 Commits 72 Commits Folders and files Name Name Last commit message Last commit date .claude-plugin .claude-plugin     .claude/ agents .claude/ agents     .github/ workflows .github/ workflows     docs docs     plugins plugins     scripts scripts     .gitattributes .gitattributes     .gitignore .gitignore     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     View all files Repository files navigation README Contributing MIT license More items headcount 
 Add a department, not a prompt. 

 
 
 
 
 
 


 
 
 
 
 
 
 


 
 Open the interactive org chart — search every skill, open a department, jump to the source.


 An agent organization for Claude Code , structured as a company:
a chief executive over 16 departments, 172 skills in total.

 Every department is an independently installable plugin, so a project loads only the functions it
needs rather than all of them at once.

 Install 
 /plugin marketplace add cbrock84/headcount
/plugin install security@headcount
 
 Install as many departments as the project needs. Skills are addressed as department:skill —
 security:threat-modeling , finance:unit-economics — so names never collide.

 Use 
 Skills load themselves when a request matches. Ask a question in the department's territory and the
right specialist engages:

 
 
 
 You ask 
 What loads 
 
 
 
 
 "why isn't this landing page converting?" 
 demand-generation:landing-page-cro-expert 
 
 
 "review this design before we build it" 
 security:threat-modeling 
 
 
 "can we afford this hire?" 
 finance:unit-economics 
 
 
 "our growth has stalled" 
 executive:business-growth-consultant 
 
 
 
 Invoke one directly by name when you want a specific lens: /finance:financial-modeling .

 New to this? docs/GETTING-STARTED.md covers which departments to
install first, the three ways to invoke a skill, and what reviewer-class departments do
differently.

 Eleven situations that cross departments — a SOC 2 demand from an enterprise prospect, a link
down between two sites, a renewal that auto-renewed because nobody owned the date — are worked
through end to end in docs/USE-CASES.md , including what comes back and
where a reviewer-class department stops the work rather than adding an opinion.

 Each department also ships an agent charter in .claude/agents/ , so a department can be delegated
to as a subagent with its own exclusive write surface.

 Departments 
 
 Office of the CEO (Chief Executive) — 7 skills 
 
 
 
 Skill 
 What it does 
 
 
 
 
 agent-hierarchy 
 Designs orchestrator-and-subagent hierarchies for a repository — splitting agents by exclusive write surface, pairing every producer with an independent auditor, an…. 
 
 
 ai-research-analyst 
 Produces executive-level research — market sizing, competitor mapping, trend analysis, and strategic intelligence — grounded in cited sources with the confidence in…. 
 
 
 business-growth-consultant 
 Finds the single constraint currently limiting a business's growth and the highest-leverage moves against it, rather than producing a list of everything that could…. 
 
 
 ceo-advisor 
 Pressure-tests a decision, plan, or idea before it is committed to — surfacing the assumption it rests on, the case against it, and what would have to be true for i…. 
 
 
 chief-executive 
 Sets direction, allocates capital and attention, and makes the calls no one else can make. 
 
 
 fundraising-and-investor-relations 
 Raises capital and manages the relationship afterward — deciding how much and why, understanding what dilution and preferences actually cost, running a process with…. 
 
 
 saas-idea-validator 
 Evaluates a software or startup idea against problem, market, competition, monetization, defensibility, and execution, and returns a verdict rather than encourageme…. 
 
 
 
 
 
 Technology (CTO / CIO) — 19 skills 
 
 
 
 Skill 
 What it does 
 
 
 
 
 ai-workflow-architect 
 Designs AI systems, automations, and agent workflows for a business — identifying which manual work is worth automating, how to structure the system, which tools fi…. 
 
 
 api-design 
 Designs interfaces that survive their consumers — resource modeling, errors, versioning, pagination, and compatibility. 
 
 
 branch-and-worktree-workflow 
 Isolates feature work in its own branch or worktree and integrates it cleanly when done. 
 
 
 chief-technology-officer 
 Owns architecture, engineering delivery, infrastructure, data platform, and internal systems. 
 
 
 cloud-infrastructure 
 Designs and runs cloud infrastructure — environments, infrastructure as code, networking and isolation, scaling, and cost. 
 
 
 code-review 
 Conducts and responds to code review — reviewing a change for correctness, design, and risk, and evaluating review feedback received on your own work. 
 
 
 completion-verification 
 Verifies that work is actually complete before it is claimed to be — running the checks, reading the output, and confirming the original request was satisfied rathe…. 
 
 
 data-migration 
 Moves data from one system to another without losing it or corrupting it — profiling the source before mapping, deciding between big-bang and parallel-run cutover,…. 
 
 
 implementation-planning 
 Turns a spec or requirement into a written plan a separate session or agent can execute, then drives that plan through review checkpoints. 
 
 
 observability-and-reliability 
 Makes systems debuggable and reliably operable — instrumentation, alerting that is worth waking for, service objectives, and learning from failure. 
 
 
 parallel-agent-delivery 
 Splits work across multiple agents or sessions running at once, keeping their surfaces disjoint so results merge cleanly. 
 
 
 prompt-optimizer 
 Turns rough intent or a weak prompt into a reliable one — diagnosing why output is inconsistent, restructuring the instruction, and adapting it across models. 
 
 
 release-and-deployment 
 Ships changes safely and often — pipelines, deployment strategies, feature flags, rollback, and database changes. 
 
 
 skill-authoring 
 Writes and revises agent skills so they trigger at the right moments and give usable instruction when they do. 
 
 
 solution-architecture 
 Designs system structure and makes architectural decisions defensible — boundaries, coupling, trade-offs, and recording why. 
 
 
 solution-exploration 
 Explores the problem and the range of possible approaches before any code is written — clarifying what is actually being asked, surfacing options with their tradeof…. 
 
 
 systematic-debugging 
 Finds the root cause of a bug, test failure, or unexpected behavior before proposing any fix. 
 
 
 technical-debt-management 
 Makes technical debt visible and decidable — distinguishing real debt from mess, quantifying its cost, and arguing for remediation in business terms. 
 
 
 test-driven-development 
 Drives implementation by writing a failing test first, then the smallest code that passes it. 
 
 
 
 
 
 Security (CISO) — 8 skills · **reviewer-class** 
 
 
 
 Skill 
 What it does 
 
 
 
 
 access-and-identity 
 Designs and audits who can reach what — authentication, authorization models, privileged access, service credentials, and joiner-mover-leaver process. 
 
 
 chief-information-security-officer 
 Owns the security posture of the organization — architecture, program strategy, risk acceptance, incident command, and the authority to stop work that creates unacc…. 
 
 
 data-protection-and-encryption 
 Protects data itself rather than the systems around it — classifying what you hold, encrypting in transit and at rest and understanding what each actually defends a…. 
 
 
 detection-and-monitoring 
 Builds the capability to notice an attack in progress — deciding what to log and retain, centralizing it somewhere tamper-resistant, writing detections that fire on…. 
 
 
 incident-response 
 Runs a security incident from detection to closure — triage, containment, investigation, communication, and the review afterward. 
 
 
 security-architecture-review 
 Reviews a design or change for security before it ships — authentication and authorization, data handling, secrets, dependencies, and the secure-development practic…. 
 
 
 threat-modeling 
 Identifies what could go wrong in a system before it is built or changed — the assets worth attacking, the entry points, the trust boundaries, and the controls that…. 
 
 
 vulnerability-management 
 Runs the loop from discovering a weakness to confirming it is fixed — scanning, triage, prioritization by real exploitability, remediation tracking, and patch policy. 
 
 
 
 
 
 IT Operations (CIO) — 12 skills 
 
 
 
 Skill 
 What it does 
 
 
 
 
 backup-and-recovery 
 Protects and restores data — backup coverage and scope, retention, immutability against ransomware, and proving restores actually work. 
 
 
 chief-information-officer 
 The CIO's remit — running the technology the company works on, service quality, IT spend, and the boundary with product engineering. 
 
 
 cloud-administration 
 Administers the cloud the company runs on rather than the one it sells — tenant and subscription structure, the SaaS estate and who owns each app, identity as the r…. 
 
 
 collaboration-platform-administration 
 Administers the email, chat, meeting and file-sharing platform the organization runs on — tenant and domain configuration, mail authentication and routing, phishing…. 
 
 
 endpoint-management 
 Manages laptops, desktops and mobile devices — enrollment, configuration, patching, software distribution, and lost or compromised devices. 
 
 
 identity-lifecycle-administration 
 Executes joiner, mover and leaver processes — provisioning, group membership, access changes on role change, and complete deprovisioning. 
 
 
 it-asset-management 
 Tracks hardware and software assets through their life — procurement, ownership, licensing, refresh, and disposal. 
 
 
 network-administration 
 Designs and operates the corporate network — segmentation, remote access, wireless, DNS and addressing, and diagnosing network problems. 
 
 
 service-desk 
 Runs the IT service desk — intake, triage, prioritization, escalation, knowledge, and the metrics that improve service rather than distort it. 
 
 
 systems-administration 
 Runs servers and corporate systems — patching, configuration baselines, change control, capacity, and the routine that prevents incidents. 
 
 
 telephony-and-conferencing 
 Runs voice and meeting infrastructure — phone systems and numbers, emergency calling obligations, conference rooms and their AV, call recording and its