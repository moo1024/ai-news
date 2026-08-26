# Leonxlnx/unlazy — Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a t

- 출처: GitHub 신규 (claude-code)
- 원본 링크: https://github.com/Leonxlnx/unlazy
- 발행: 2026-08-26T03:54:38.294674+00:00
- 접근상태: 확인 완료

---

GitHub - Leonxlnx/unlazy: Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf the full time budget of the whole task, so effort multiplies with depth. Grounded in 2025-2026 research on model laziness, underthinking and premature completion. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 Leonxlnx
 
 / 
 
 unlazy 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 139 
 
 

 
 
 
 
 
 Star
 2.4k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 42 Commits 42 Commits Folders and files Name Name Last commit message Last commit date .github/ workflows .github/ workflows     agents agents     references references     research research     scripts scripts     templates templates     tests tests     .gitignore .gitignore     CHANGELOG.md CHANGELOG.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     README.md README.md     SECURITY.md SECURITY.md     SKILL.md SKILL.md     package.json package.json     View all files Repository files navigation README Contributing MIT license Security More items 
 unlazy 
 Completion discipline for substantial AI-agent work, backed by runnable gates. 

 Write the acceptance ledger first. Execute reviewed checks. Reverify returned work. Report only what the evidence supports.

 Quick start | Gate contract | Orchestration | Security | Research 

 
 Version status 
 The current source targets 2.1.0 . It is not identified here as a tagged GitHub release. Pin an exact commit when you need an immutable installation. See CHANGELOG.md for the unreleased change set.

 Install 
 Use the skills CLI for supported agents:

 npx skills add Leonxlnx/unlazy
 
 Add -g for a user-level install or --all for every detected agent.

 Manual locations:

 Claude Code: ~/.claude/skills/unlazy
Codex CLI: ~/.codex/skills/unlazy
 
 Clone the repository into the relevant directory. Invoke it as /unlazy where slash skills are supported, $unlazy in Codex, or by a natural-language trigger from the skill description.

 The core is SKILL.md . The checker and optional hook require Node 16 or newer and use no third-party runtime packages.

 Quick start 
 Ask for substantial work with an explicit trigger:

 /unlazy tree 5 refactor the payment module and verify every migration path
 
 For a solo task, copy templates/gates-leaf.md to GATES.md , replace every placeholder, and inspect it without executing commands:

 node <path-to-skill>/scripts/gate-check.mjs --status GATES.md
 
 --status is the only mode that is always non-executing. On a new oracle with no exact approval record, a normal run prints its resolved command, expectation, working directory, shell, and PATH without executing it:

 node <path-to-skill>/scripts/gate-check.mjs GATES.md
 
 Do not treat normal mode as a permanent dry run: once the exact oracle is approved, normal mode can execute it.

 CHECK: lines are shell code. After reading every command and called script, approve and run the ledger:

 node <path-to-skill>/scripts/gate-check.mjs --approve GATES.md
 
 Re-run all runnable gates, including gates already marked complete:

 node <path-to-skill>/scripts/gate-check.mjs --reverify GATES.md
 
 Use --help for the complete current CLI.

 The gate contract 
 # Gates: pricing behavior 

 - [ ] G1: pricing fixtures render the expected tiers
 CHECK: node scripts/verify-pricing.mjs
 EXPECT: pricing verification passed
 EVIDENCE: pending

 - [ ] G2: checkout integration succeeds from its package
 CHECK: node scripts/verify-checkout.mjs
 EXPECT: checkout verification passed
 CWD: packages/checkout
 EVIDENCE: pending 
 A runnable gate passes only when its process exits 0 and EXPECT: matches combined output. Evidence records the resolved shell, resolved working directory, exit status, a short PATH fingerprint, the match result, and a SHA-256/byte-count fingerprint of successful output. Raw successful output is neither echoed nor persisted. The pre-execution transcript shows the resolved PATH , capped for display. Old evidence is not re-execution; parent verification uses --reverify .

 The parser rejects zero-gate ledgers, duplicate ids, incomplete runnable gates, invalid expectations, and abandonment with a missing reason or unknown gate id. It ignores fenced examples, preserves CRLF or LF when updating, and inserts a missing evidence line when needed. A valid abandonment is terminal handoff rather than success: the checker exits 1 with HANDOFF REQUIRED , and Stop allows exit while reporting qualified ids.

 The checker can prove only the command oracle you declare. It cannot infer that an English title and arbitrary shell code mean the same thing. Good gates therefore:

 
 read the artifact or service named by the outcome 
 print a success-only marker after all assertions pass 
 test an absence check against a known positive control 
 measure supplied figures instead of copying them into EXPECT: 
 review consequential manual outcomes with evidence proportional to risk 
 
 Use the advisory, non-executing scripts/gate-lint.mjs to catch mechanically weak ledger patterns; add --strict when warnings should fail. Full specification: references/gates.md .

 Shell and PATH 
 The checker uses --shell first, then UNLAZY_SHELL , then Node's platform default shell. That default is /bin/sh on Unix and process.env.ComSpec on Windows with the platform fallback. Checks inherit the launch environment, including PATH .

 This matters on Windows: a checker launched from Git Bash can see Unix-like tools that the same checker launched from PowerShell does not. --shell changes the interpreter; it does not install grep , tail , tr , or other external programs. Portable examples call repository-owned Node scripts.

 Parent re-verification should use the same declared shell and required toolchain. A shell or PATH mismatch is a failed verification to resolve, not successful evidence.

 Security boundary 
 Approval records live under ~/.unlazy/approved by default. UNLAZY_APPROVAL_DIR may select another owner-private real directory, but its canonical target must remain outside the checked repository. Symlinked stores and linked, replaced, or non-private records fail closed. Each record is specific to the absolute ledger and gate, exact CHECK: and EXPECT: , resolved CWD: and shell, timeout, output and regex limits, regex worker limits, platform, and full inherited PATH . Editing any bound input requires approval again.

 Approval is consent, not a sandbox. Approval storage is a canonical, owner-private directory outside the repository; records are accepted only as single-link private regular files. Approval does not hash called scripts, fixtures, dependencies, or other transitive inputs, and --status /Stop do not revalidate old evidence. Reinspect changed dependencies and run --reverify ; see SECURITY.md for the bounded digest pattern when user-designed dependency identity is needed. Checks run with ambient filesystem, environment, credential, and network access. Scopes and ownership leases coordinate cooperating processes but do not restrict what a process can read or write.

 Orchestration and parallel work 
 For work that needs fresh contexts, create one scoped pipeline under .unlazy/<scope>/ :

 .unlazy/<scope>/PLAN.md
.unlazy/<scope>/GATES.md
.unlazy/<scope>/gates/leaf-*.md
.unlazy/<scope>/gates/node-*.md
 
 The driver rereads the current request and maintains a revisioned contract inventory that maps each independently required outcome or acceptance-changing constraint to an owner and observation. It fixes interfaces, dependencies, conventions, and file ownership before dispatch. Leaves use declared WAITING , READY , IN-FLIGHT , VERIFIED , or ABANDONED states. Branches use OPEN , VERIFIED , or ABANDONED .

 Ready leaves may run together only after each declares complete, disjoint, repository-relative OWNS: paths and claims them:

 node <path-to-skill>/scripts/gate-check.mjs --scope api --leaf leaf-1.2.1 --claim
 
 Lease matching is conservative and may reject a safe-looking pair. It is a coordination guard, not write isolation. Use separate worktrees for colliding worktree-local output, and configure separate cache locations when cache writes can conflict.

 Dispatch is rolling: when a verified leaf unblocks another, start the newly ready leaf without waiting for unrelated work. Gate checks remain sequential by default. --jobs <N> , where N is an integer from 1 through 64, is an opt-in rolling limit for independent checks and keeps reporting in ledger order.

 For every independent READY set, open a native launch wave, record each host agent handle, and seal before the first wait. If a partial launch cannot recover, use the audited abandon --reason transition; never invent a handle or delete state. Read references/method.md , references/orchestration.md , references/dispatch.md , and references/parallel.md before parallel fan-out.

 gate-check.mjs --scope <id> reduces the scope's ledgers and dispatch waves together. It prints ALL MET only when every gate is met and every wave is complete; an abandoned wave remains a non-successful HANDOFF REQUIRED outcome.

 Optional Claude Code Stop hook 
 The hook scans the current session's resolved ledger and dispatch state and returns Claude Code's documented top-level decision: "block" response while gates remain unmet or launch waves remain incomplete. It does not execute checks. Its own session-keyed progress guard releases after six consecutive blocks without semantic gate/dispatch progress; metadata-only edits do not reset it. Abandonment stays visible as an explicit bounded handoff in pure, mixed-blocking, and final-release messages, without echoing free-form reasons.

 Install only with the user's consent:

 node <path-to-skill>/scripts/install-hooks.mjs
node <path-to-skill>/scripts/install-hooks.mjs --scope api
node <path-to-skill>/scripts/install-hooks.mjs --uninstall
 
 Default installation writes .claude/settings.local.json . Keep that file, .unlazy/ , and .unlazy-hook-state.json in the project's ignore rules. --shared writes absolute Node and hook-script paths into project settings, so it is usually not portable and can expose local directory names. --global writes the current user's Claude settings.

 The installer preserves unrelated hooks, refuses malformed settings shapes, and identifies moved unlazy entries without depending on the install directory name. It writes settings atomically and creates <settings-file>.unlazy.bak beside an existing settings file before replacing it.

 What 2.1.0 changes 
 The unreleased 2.1.0 source integrates the useful parts of community PRs while repairing their edge cases:

 
 strict shared ledger parsing and explicit named-file targeting 
 --reverify , explicit --approve , and fail-closed exit-plus-EXPECT success 
 --shell and UNLAZY_SHELL , with pre-execution PATH disclosure and resolved shell, CWD, exit, match, and successful-outpu