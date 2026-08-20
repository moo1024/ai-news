# Tiger3807861189/J-Space-Cognition-Suite-V3.6 — J-Space Cognition Suite V3.6 - AI cognitive-enhancement Skills based on Anthropi

- 출처: GitHub 신규 (claude-code)
- 원본 링크: https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6
- 발행: 2026-08-20T22:24:11.655602+00:00
- 접근상태: 확인 완료

---

GitHub - Tiger3807861189/J-Space-Cognition-Suite-V3.6: J-Space Cognition Suite V3.6 - AI cognitive-enhancement Skills based on Anthropic's J-space global workspace research. | 哔哩哔哩：Tiger380 (UID 3494375382321675) — https://space.bilibili.com/3494375382321675 · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 Tiger3807861189
 
 / 
 
 J-Space-Cognition-Suite-V3.6 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 205 
 
 

 
 
 
 
 
 Star
 3k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 33 


 
 
 
 
 
 
 
 
 Pull requests 
 5 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 80 Commits 80 Commits Folders and files Name Name Last commit message Last commit date .github/ workflows .github/ workflows     j-space j-space     tests tests     .gitignore .gitignore     CITATION.cff CITATION.cff     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     README.zh-CN.md README.zh-CN.md     THIRD_PARTY_NOTICES.md THIRD_PARTY_NOTICES.md     View all files Repository files navigation README Contributing Apache-2.0 license More items J-Space Cognition Suite V3.6 
 简体中文 

 

 J-Space Cognition Suite is a model-agnostic inference-time control system for deep reasoning, long-horizon work, tool use, verification, and recovery.

 It is packaged as a Skill for cross-platform use, selective loading, and low-friction integration.

 The suite organizes an agent's accessible working representations into a deliberately managed workspace. It operates through a single entry, nine selectively loaded modules, three supporting references, and an optional standard-library controller for durable task state.

 J-Space operates at inference time. Model weights and training remain unchanged.

 Quick start 
 Option A — manual installation 
 
 
 Download or clone this repository.

 
 
 Locate the user-level Skills directory used by your AI host.

 
 
 Copy the complete j-space/ directory into it so that the installed entry is <skills-directory>/j-space/SKILL.md .

 
 
 Run the integrity check with an available Python 3 interpreter:

 <python-command> <skills-directory>/j-space/scripts/verify_suite.py
 
 Replace <python-command> with the Python 3 command available on the host, commonly python , python3 , or py -3 .

 
 
 Reload the host if it discovers Skills at startup.

 
 
 
 
 The directory must remain intact because SKILL.md routes to relative paths under modules/ , references/ , and scripts/ .

 
 
 The repository-level LICENSE and THIRD_PARTY_NOTICES.md remain part of the distribution.

 
 
 Include copies of both when redistributing j-space/ as a standalone package.

 
 
 Option B — ask an AI agent to install it 
 Copy the following prompt into an agent that can access files and this repository:

 Install J-Space Cognition Suite from
https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6 into this environment's user-level Skills directory.

First inspect the host configuration or documentation to locate the correct Skills directory. Install the complete j-space/ directory as j-space/, preserving SKILL.md, modules/, references/, and scripts/. If a j-space target already exists, compare it and ask before replacing anything. Run scripts/verify_suite.py with an available Python 3 interpreter after installation.

When finished, report the installed path and verification result, then tell me how this host invokes the Skill. Briefly explain fast, full, and loop, and explain that the optional controller records long-task state rather than choosing solutions. If this host has no native Skill loader, explain the selective system/developer-instruction integration instead of reporting an installation.
 
 Use it 
 Invoke the Skill through the mechanism provided by your host—such as its Skill picker,
 /j-space , $j-space , or a direct request:

 Use j-space for this task. Audit this repository, preserve its architecture,
verify every finding, and keep the work consistent across all affected files.
 
 The entry gate selects the lightest suitable pass automatically.

 Operating modes 
 
 
 
 Pass 
 Suitable work 
 What loads 
 
 
 
 
 fast 
 One step, or a result checkable in one glance 
 Nothing extra 
 
 
 full 
 Several dependent steps and one bounded deliverable 
 One or two relevant modules; ship before delivery 
 
 
 loop 
 Multiple stages, files, turns, tools, or persistent state 
 Ledger, seams, checkpoints, register audit, and recovery 
 
 
 
 A request for brevity changes the outer response length while verification remains aligned with the task's floor. Short work stays light; long work receives durable state only when it needs it.

 Core mechanisms 
 
 
 
 Mechanism 
 Function 
 
 
 
 
 Selective workspace loading 
 Keeps one or two load-bearing ideas active and externalizes the rest 
 
 
 Broadcast hub 
 Gives dependent branches one shared source for names, values, constraints, and style anchors 
 
 
 Dense Track 
 Carries long internal chains in compact, decodable notation before returning to clean outer language 
 
 
 Bridge-before-conclusion reasoning 
 Makes required intermediates explicit before a conclusion consumes them 
 
 
 Metacognitive control 
 Routes confidence, inconsistency, and failure signals into a concrete next action 
 
 
 Empirical escape and verification 
 Converts stalled derivation into bounded tests with a named verifier and coverage 
 
 
 First-person agency and functional echo 
 Uses I , we , let's , and we need to bind workspace state to later actions and checks 
 
 
 
 The mechanisms are selectively loaded. They are not a fixed checklist for every request.

 Optional controller 
 j-space/scripts/jspace.py externalizes loop state into
 .jspace/ in the current task workspace. Invoke it by its resolved Skill path while keeping the task workspace as the current directory.

 
 
 
 Command 
 Purpose 
 
 
 
 
 note --goal "..." --next "..." 
 Open the ledger and define done plus the first action 
 
 
 note --next "..." 
 Replace the single next action after a checkpoint or seam 
 
 
 note --core "..." 
 Record a hub entry 
 
 
 note --core "..." --core-slot 1 
 Swap a selected live hub entry 
 
 
 note --check "..." --by "..." 
 Append a checkpoint with verifier and coverage 
 
 
 note --open "..." --settled-by "..." 
 Record a question and what would settle it 
 
 
 note --close N --check "..." --by "..." 
 Close question N against a new recorded checkpoint 
 
 
 seam 
 Re-read current state and report recent movement 
 
 
 ship FILE 
 Inspect outgoing text for register leakage and failure signatures 
 
 
 resume 
 Reload the premise, invariants, and full ledger after a long gap 
 
 
 
 <python-command> <skill-root>/scripts/jspace.py note --goal "what done means" --next "first action"
<python-command> <skill-root>/scripts/jspace.py note --close 1 --check "what now holds" --by "verifier and coverage"
<python-command> <skill-root>/scripts/jspace.py seam
<python-command> <skill-root>/scripts/jspace.py ship OUTPUT_FILE
<python-command> <skill-root>/scripts/jspace.py resume
 
 The controller records and reports state. Solution choice remains with the model. It uses the Python standard library and writes working state only under the task's .jspace/ directory.

 Generic model integration 
 An environment with a native Skill loader can install j-space/ directly. For a chat or API environment, provide j-space/SKILL.md as a system- or developer-level instruction and expose modules/ and references/ through file or retrieval tools.

 Selected files should be retrieved on demand. Selective loading is part of the operating design.

 Benchmarks 
 All values use the native score of the corresponding benchmark; higher is better. — means that no result is reported. HLE is separated into no-tool and tool-enabled conditions.

 Evaluation context 
 The J-Space evaluations on DeepSeek were configured with reference to the official DeepSeek Harness minimal-mode setup, with max reasoning effort, temperature = 1.0 , and top_p = 0.95 . J-Space participated across the inference-time workflow through workspace routing, state continuity,
verification, and recovery.

 Results were collected within the project's available evaluation environment. Hardware conditions, process isolation, tool availability, and information-access boundaries form part of that context. J-Space tends to encourage more initiative and goal-directed exploration, making accessible artifacts and execution traces relevant to observed outcomes.

 The table presents project-level benchmark records under these conditions. Comparator values retain the evaluation contexts published by their respective providers, and score variation across environments and harness configurations is expected. Source records include the DeepSeek V4-Flash-0731 model card , Z.ai 's GLM-5.3 release-evaluation record, the Kimi-K3 model card , and Anthropic's Claude Fable 5 & Claude Mythos 5 System Card , which also reports its named comparator conditions.

 Model comparison 
 
 
 
 Benchmark 
 DeepSeek V4-Flash-0731 
 DeepSeek V4-Flash-0731 + J-Space V3.6 
 GLM-5.3 
 Kimi-K3 
 Opus-4.8 
 Fable 5 (w/ fallback) 
 
 
 
 
 HLE (w/o tools) 
 37.8 
 45.5 
 — 
 43.5 
 49.8 
 53.3 
 
 
 HLE (w/ tools) 
 51.5 
 60.6 
 62.5 
 56.0 
 57.9 
 63.0 
 
 
 Terminal Bench 2.1 
 82.7 
 87.1 
 88.2 
 88.3 
 85.0 
 88.0 
 
 
 NL2Repo 
 54.2 
 70.2 
 58.0 
 58.0 
 69.7 
 — 
 
 
 CyberGym 
 76.7 
 81.7 
 84.5 
 80.0 
 78.3 
 83.1 
 
 
 DeepSWE 
 54.4 
 67.4 
 66.9 
 67.5 
 58.0 
 70.0 
 
 
 Toolathlon-Verified 
 70.3 
 77.7 
 73.0 
 76.5 
 76.2 
 77.9 
 
 
 Agents' Last Exam 
 25.2 
 30.1 
 28.5 
 27.6 
 25.7 
 23.8 
 
 
 AutomationBench (Public) 
 25.1 
 31.7 
 48.2 
 30.8 
 27.2 
 29.1 
 
 
 
 Efficiency 
 These task-level indices retain the same task and model conditions and each records one evaluation run. Control is the matched baseline; J-Space is the corresponding suite-assisted condition. Speed is benchmark score divided by elapsed time, where higher is better. Token cost is consumed tokens divided by benchmark score, where lower is better. Elapsed time and token count use fixed, uniform scaling coefficients across both conditions. The coefficients affect the displayed scale while the within-metric improvement ratio remains comparable.

 
 
 
 Metric 
 Control 
 J-Space 
 Improvement 
 
 
 
 
 Speed (score/time; higher is better) 
 0.43 
 1.09 
 2.53× 
 
 
 Token cost (tokens/score; lower is better) 
 2.63 
 1.19 
 2.21× 
 
 
 
 Related evaluation material:
 DeepSeek V4 × J-Space Capability Realization Report .

 Cross-model compatibility 
 The operating effects have been reproduced across the DeepSeek, Qwen, GLM, GPT, and Claude model families. Effect size varies with base capability, context policy, tool harness, sampling configuration, and benchmark implementation.

 The portable unit is the protocol: workspace loading, selective routing, state externalization, verification, and recovery. It is independent of a vendor-specific tokenizer or model API.

 Project structure 
 J-Space-