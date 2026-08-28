# 0xsline/awesome-deepseek-harness — DeepSeek Harness (DSH) ecosystem: curated plugins, tools, and infrastructure fro

- 출처: GitHub 신규 (MCP 서버)
- 원본 링크: https://github.com/0xsline/awesome-deepseek-harness
- 발행: 2026-08-28T22:24:35.418829+00:00
- 접근상태: 확인 완료

---

GitHub - 0xsline/awesome-deepseek-harness: DeepSeek Harness (DSH) ecosystem: curated plugins, tools, and infrastructure from dsh-external/hub and the public dsh-plugin topic. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 0xsline
 
 / 
 
 awesome-deepseek-harness 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 342 
 
 

 
 
 
 
 
 Star
 932 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 7 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 1,092 Commits 1,092 Commits Folders and files Name Name Last commit message Last commit date .github/ workflows .github/ workflows     assets assets     scripts scripts     .gitignore .gitignore     CATALOG.md CATALOG.md     LICENSE LICENSE     README.md README.md     README.zh-CN.md README.zh-CN.md     contributing.md contributing.md     View all files Repository files navigation README Contributing CC0-1.0 license More items 
 English   |  
 简体中文 




 
 
 
 Awesome DeepSeek Harness 

 
 Install    
 Contribution guide    
 DeepSeek Docs    
 Public plugin topic    
 Issues    
 完整目录    




 
 Curated DeepSeek Harness (DSH) ecosystem: plugins, tools & infrastructure. Sources: dsh-external/hub catalog and the public GitHub dsh-plugin topic. 





> Note: the GitHub [`dsh-plugin` topic]( https://github.com/topics/dsh-plugin ) is public; some `dsh-external` repository links may still require org access.
 Contents 
 
 Install 
 Core & Bundles 
 Agents & Orchestration 
 Context & Search 
 Memory & Knowledge 
 Input & Editing 
 UI, Themes & Interaction 
 Dashboards & Session UX 
 IDE & Clients 
 Browser & Remote 
 Models & Inference 
 Git & Engineering 
 Security & Governance 
 Output & Deliverables 
 Office & Documents 
 Notifications & Channels 
 Fun & Lifestyle 
 Plugin Ecosystem & Development 
 Runtime & Operations 
 Domain & Specialist Skills 
 Tools & Utilities 
 Related 
 Thanks 
 
 Install 
 Install the official runtime with Node.js:

 npx @deepseek-ai/dsh web 
 Install an external profile bundle with pnpm on your PATH :

 dsh plugin --profile web add " github:owner/repo#ref " 
 dsh plugin forwards package operations to pnpm, so npm, Git/GitHub, local path, file: and link: package specs are supported. Only packages declaring dsh.bundle.patch become active profile layers; plain dependencies remain installed but inactive. Restart dsh --profile web after installing or updating a bundle.

 The former &path: sub-path and Repository Plugin installation forms are not part of the current official bundle flow; use an installable package that declares dsh.bundle.patch .

 Management panel: Settings → Plugins.

 Core & Bundles 
 
 DeepSeek Harness Ultimate - Community-maintained reproducible profile installer: deduplicated defaults across coding, workflow, reliability and productivity; full commit-SHA pins, permissive-license audit, pre/post dependency checks, optional sensitive integrations, and beginner guides in 20 languages for Windows, macOS and Linux. 
 dsh-deepresearch - DeepResearch plugin (cordis). 
 dsh-plan-execute - Dual-model plan/execute routing: planner model thinks, executor model acts. 
 dsh-toolkit - Zero-dependency tool suite (calculator/csv/diff/encoding/json/markdown/regex/time). 
 dsh-deep-research - Adaptive deep-research orchestrator (workflow engine). 
 dsh-101 - DSH documentation reading mode. 
 dsh-client-ui-plan-execute - Web Settings row for plan/execute model routing. 
 dsh_workflow - Dynamic workflow for DSH (placeholder). 
 dsh-equip-engine - Task-driven plugin equip engine: dual retrieval (curated rules + LLM semantic), combo scoring (synergy/conflict/cost/trust), conflict detection and install-command export. 
 dsh-claude-move - Four-source migration wizard: move Claude Code, Codex, OpenCode and Hermes sessions, memories, skills, instructions and slash commands into DSH (approval-gated, idempotent, resumable sessions). 
 dsh-skill-mover - One-click skill migration into DSH: scans 14 agent platforms (Cursor, Claude Code, Codex, Hermes, Trae, Qoder...) plus the shared ~/.agents layer, merges same-name skills, dedupes symlinks and rolls back safely. 
 gewu-tools - Model-agnostic visual-inspection pipeline for text-only agents: page-by-page HTML screenshots plus a ready-made vision-subagent briefing contract (gewu_prep), then source-code truth verification of every finding (gewu_locate); validated on mimo-v2.5 & qwen3.7-plus. 
 dsh-plugin-hub - DSH plugin manager & marketplace: one-click enable/disable, multi-source market, static index (500+ plugins / 300 skills), skill install/disable, suite one-click assembly, one-click framework upgrade (online install + auto-rollback). 
 
 Agents & Orchestration 
 
 dsh-todo-guard - Reliable todo panel that survives restarts (official panel only re-renders on write — fixed via projection pre-warm) with three-state completion verification: evidence exists → verified, fake evidence → blocked, no evidence → unverified badge; settings toggle to fall back to official behavior. 
 fakechris/dsh-track - Embedded task-management engine for DSH: decision-point protocol, idea capture wall, Linear-shaped issue store with an evidence-driven lifecycle. 
 dsh-dual-model-eval - Runs one coding prompt across multiple configured models in isolated Git worktrees, streams side-by-side tool traces and results, and commits the candidate the user adopts for later rounds. 
 dsh-agent-arena - Compares coding agents in isolated Git worktrees with deterministic validation, scoring, and explicit winner application. 
 xiehuan123/coding-coach - Coding Coach: 35-skill bundle plus a full agent preset for non-developers (8-stage idea-to-launch pipeline; engineering/product/UI skills). 
 dsh-collaboration - Multi-agent collaboration suite: user-configured specialist roster, persistent on-demand dispatch (team_call/team_message/team_status/team_close), clone instances, star-topology relay, model comparison and a multimodal vision bridge. 
 dsh-plans - Planning-first agent preset: research repository changes into traceable Markdown plans, refine them through reviewer/criticizer subagent rounds, then execute as a DSH goal with a verifier checklist. 
 dsh-agent-team-gui - Persistent multi-model squads managed in Settings and selected in the Composer; the lead Agent dynamically plans bounded DAG runs with optional review/repair, while Run Center reports DSH's official provider-reported Token usage. 
 DSH Automation Center - Workspace automation center for scheduled Agent runs: each execution starts a fresh Result Session with persistent audit history; stock DSH uses a Conversation tab, while compatible Shell slots enable a global page. 
 Knotline - Visual DSH project map for composing persistent agent workflows from requests, agents, skills, backlogs, approval pools, and scheduled triggers. 
 cleverer-dsh - Execution-discipline suite for DSH with identical-retry interception, forced reflection, todo enforcement, memory deduplication, and experience-to-skill promotion (11 plugins + 6 skills). 
 february2015/dsh-taskswarm - DSH port of TaskPlane: dependency-ordered waves run in parallel git-worktree lanes, with task packets, cross-model review, and crash recovery. 
 hongyue0721/dsh-kimicode-swarm - Kimi Code Swarm-style batch parallel subagent dispatch: a swarm_batch tool fans independent subtasks out to real subagents with two-stage adaptive concurrency (ramp-up plus collision-driven exponential backoff, auto shrink/recover), an in-chat live progress stream (SSE), and resume_agent_ids continuation. 
 timwhitez/dsh-self-evolving - Evidence-first, crash-resumable self-evolution engine for DSH: generates bounded Cordis plugin candidates, admits them through a one-shot real Loader, evaluates with Harbor, and journals an auditable lineage. 
 Saktawdi/dsh-ha-orchestrator - Model high-availability failover (quarantine, circuit breaking, probe recovery) plus subagent orchestration (fanout/pipeline/supervisor) with a bilingual settings UI. 
 dsh-background-agents - Durable background child agents on the official subagent seam: start from any session, watch progress in the Web UI sidebar, message and interrupt any time, with per-child tool scoping, persona and delegation-depth caps. 
 zoahdev/dsh-kirocrew - Bridge a DSH agent to a persistent, self-evolving KiroCrew development workspace over ACP (JSON-RPC 2.0 over stdio) via a single kiro_send tool. 
 bpc-oss/dsh-routed-subagent - Run a one-shot subagent fully mounted on any agent preset from any session, with per-call model/provider override, model pre-check, and external CLI engines (codex / claude / codebuddy) with background jobs, live progress, kill, and continuable sessions. 
 bpc-oss/dsh-fork-to-preset - Fork any session into a different agent preset from the conversation header: a preset picker creates a new child session mounted on the chosen preset, inheriting the source session's completed turns. 
 qwert702/dsh-commander - Commander mode for DSH Web: inject protocol briefs into the session title bar, parse task blocks from model replies and auto-execute them, separating strategy from execution; activated via a badge button. 
 
 Context & Search 
 
 zoahdev/dsh-github-intelligence - Read-only developer-intelligence tools across 16 ecosystems (GitHub, GitLab, Gitee, npm, PyPI, crates.io, Docker Hub, Hugging Face, Hacker News, Stack Overflow, Reddit, dev.to, RubyGems, NuGet, Go, ArXiv) with TTL caching and no API key. 
 dsh-hacker-news - Live Hacker News feeds, item threads, Algolia search, and user profiles for DeepSeek Harness. 
 dsh-minimal-first-turn - Minimal-compatible first-turn conditioning for Web root sessions: restricts the prompt and tool catalog to persistent bash and str_replace_editor, then restores the selected preset after the first tool call or reply; includes a persistent composer toggle. 
 xiehuan123/dsh-deepread - DeepRead: deep-reading assistant with five modes (quick/deep/knowledge-map/Feynman reading/book), batch comparison, budget preflight, transparent background-job progress, WeChat links, local PDF (pure-JS extractor), optional MD/FreeMind/HTML export. 
 dsh-context - Context insight panel: see what the model's context window is made of and how it evolves — composition vs. window size, per-request history, compression/injection events, and per-message token stats. 
 dsh-bookmarks - Bookmark finalized assistant replies with notes and tags; a cross-session center with search, tag filter, session jump and one-click Markdown export (Alt+B toggles the panel). 
 billion-context-dsh - Model-driven context compression (ACP) for DeepSeek Harness, ported from billion-context-pi; the model decides when and what to compress. 
 qwert702/dsh-context-compressor - Context compression for small models: compresses tool output and conversation history to a few sentences, freeing context for the actual task; continues in a fresh session automatically. 
 dsh-scope - Context lens: per-session KV cache hit rate and token composition, plus a GitHub-style usage heatma