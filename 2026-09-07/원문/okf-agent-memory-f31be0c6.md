# OKF Agent Memory – Git-native persistent memory for AI coding agents

- 출처: Hacker News
- 원본 링크: https://github.com/okf-memory/okf-agent-memory
- 발행: 2026-09-05T22:15:52+00:00
- 접근상태: 확인 완료

---

GitHub - okf-memory/okf-agent-memory: Git-native persistent memory for AI coding agents. Implements Google OKF v0.2 with sub-300µs in-memory BM25 search, embedded MCP server, and progressive disclosure. Slashes token bloat by 80% with zero external databases or dependencies. Built in pure Go. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 okf-memory
 
 / 
 
 okf-agent-memory 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 16 
 
 

 
 
 
 
 
 Star
 340 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 3 Commits 3 Commits Folders and files Name Name Last commit message Last commit date .agents/ skills/ okf-memory .agents/ skills/ okf-memory     .github .github     benchmarks benchmarks     cmd cmd     docs docs     examples examples     knowledge knowledge     packaging/ homebrew packaging/ homebrew     pkg/ okf pkg/ okf     .gitignore .gitignore     AGENTS.md AGENTS.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     Makefile Makefile     README.md README.md     SECURITY.md SECURITY.md     go.mod go.mod     View all files Repository files navigation README Contributing MIT license Security More items OKF Agent Memory 
 
 A Domain-Neutral, Git-Native Persistent Project Memory for AI Agents based on the Open Knowledge Format (OKF) v0.2. 

 
 
 
 
 

 
 🌟 Overview 
 Conversations with AI agents reset when context windows close. Valuable architectural decisions, domain discoveries, and operational facts are lost unless stored persistently.

 OKF Agent Memory provides a standardized, vendor-neutral memory layer that lives directly in your repository ( knowledge/ ) as plain Markdown files with YAML frontmatter. It bridges the gap between unstructured ad-hoc markdown files ( CLAUDE.md , AGENTS.md ) and complex, black-box vector databases.

 
 
 
 flowchart TD
 L1["1. OKF v0.2 Specification<br/>(Normative Markdown & YAML Format)"]
 L2["2. Agent Memory Convention<br/>(Behavioral Rules: Search, Review, Trust)"]
 L3["3. Agent Skill<br/>(LLM Prompts & Operational Workflows)"]
 L4["4. Tooling Layer: Go Library & CLI<br/>(Deterministic Parsing, Validation, Search, MCP)"]
 L5["5. Project Knowledge Corpus<br/>(knowledge/ OKF Bundle)"]

 L1 --> L2
 L2 --> L3
 L3 --> L4
 L4 --> L5
 
 
 
 
 
 
 
 
 Loading 
 
 
 

 
 ⚡ Key Highlights 
 
 Blazing Fast Performance (<300µs Search, ~4ms Graph Validation) : In-memory BM25 retrieval and bundle validation execute in microseconds without VM spin-up or network roundtrips. 
 100% Git-Native & Zero Vendor Lock-in : Everything is version-controlled plain text. Inspect, audit, and review your agent's memory using standard git diff and git log . No external database required. 
 Zero API Costs for Memory Retrieval : Local lexical BM25 indexing eliminates recurring vector embedding API costs and network roundtrips. 
 Built on Google OKF v0.2 : Uses the open standard format for agent knowledge with full support for provenance ( sources ), trust tiers ( generated vs. verified ), and lifecycle metadata ( status , stale_after ). 
 Solves Context Bloat & Memory Rot : Employs Progressive Disclosure (hierarchical index.md files and link graphs) so agents only load the exact concepts they need. 
 Search-Before-Write Principle : Mandates querying existing memory before authoring, preventing concept duplication and hallucinated divergence. 
 Zero-Dependency Go Toolchain : Single binary with zero external dependencies , sub-5ms CLI startup time, and a built-in Model Context Protocol (MCP) server ( okf mcp ). 
 Truly Domain-Neutral : Designed for Software Engineering, Coaching, Scientific Research, Literature Reviews, and Operations. 
 
 
 📊 Performance Benchmarks 
 Built in Go with zero external dependencies, okf is engineered for high-frequency agent tool calling loops:

 
 
 
 Benchmark Metric 
 Python / Vector DB Runtimes (Mem0, Letta) 
 Deno / Node.js Tooling 
 OKF Agent Memory (Go) 
 
 
 
 
 Concept Search Latency 
 150ms – 800ms (Embedding API + Vector DB) 
 40ms – 120ms 
 < 300 µs (Microseconds, In-Memory BM25) 
 
 
 Full Corpus Parse & Graph Validation 
 200ms – 1.5s 
 80ms – 250ms 
 ~4.0 ms (50+ concepts, bidirectional graph) 
 
 
 Process Cold-Start Overhead 
 250ms – 600ms (Python VM boot) 
 80ms – 180ms (V8 / Deno boot) 
 < 4 ms (Compiled Single Binary) 
 
 
 Retrieval Cost per 1,000 Queries 
 ~$0.10 – $0.50 (Embedding tokens) 
 $0.00 
 $0.00 (Zero API cost, fully local) 
 
 
 Memory Footprint (RSS) 
 ~120 MB – 350 MB 
 ~60 MB – 140 MB 
 < 15 MB 
 
 
 
 Tip
 Reproduce Locally with your own LLM : We provide an automated benchmark runner in pure Go to verify Time-To-First-Token (TTFT) speedups and -80% token reduction on your local hardware (LM Studio / Ollama with Gemma, Qwen, Llama). Run make benchmark or explore the Progressive Disclosure Benchmark Suite .

 
 
 🚀 Quickstart 
 1. Build the Tooling 
 Clone the repository and compile the standalone okf executable:

 make build 
 This generates the standalone binary at bin/okf .

 2. Basic CLI Commands 
 # Validate bundle conformance, graph connectivity, and description drift 
./bin/okf validate knowledge --strict --drift

 # Search concepts via in-memory BM25 scoring 
./bin/okf search " architecture layers " knowledge

 # Inspect a concept and its relationships (with --json support) 
./bin/okf show architecture/layers knowledge --json

 # Create a new concept with automated log.md and index.md bookkeeping 
./bin/okf create decisions/auth-flow knowledge \
 --type Decision \
 --title " OAuth2 Authorization Flow " \
 --desc " Standardized on PKCE for client authentication. " 

 # Update an existing concept 
./bin/okf update decisions/auth-flow knowledge \
 --desc " Updated OAuth2 PKCE token refresh interval. " 

 # Bootstrap full agent memory stack into any target project 
./bin/okf bootstrap /path/to/project --name " My Project " 

 # Initialize only a bare OKF bundle in any directory 
./bin/okf init my-project/knowledge 
 3. Bootstrapping Agent Memory in Any Project 
 Scaffold the complete OKF Agent Memory architecture into any new or existing repository with a single command:

 # Bootstrap full memory stack into target project 
./bin/okf bootstrap /path/to/my-project --name " My Service " 
 This automatically sets up:

 
 knowledge/ — OKF v0.2 compliant persistent memory bundle ( index.md , log.md ) 
 .agents/skills/okf-memory/ — Embedded agent skill definition and capability guides 
 AGENTS.md — Project-tailored operating instructions for AI coding agents 
 Makefile — Convenience tasks for validation ( make validate ) and search ( make search q="..." ) 
 
 4. Running as an MCP Server 
 okf ships with a native Model Context Protocol (MCP) server over stdio to seamlessly connect with Claude Code, Cursor, Codex, and other agent platforms:

 ./bin/okf mcp knowledge 
 Example MCP Configuration ( claude_desktop_config.json or Cursor): 
 {
 "mcpServers" : {
 "okf-memory" : {
 "command" : " /path/to/okf-agent-memory/bin/okf " ,
 "args" : [ " mcp " , " /path/to/project/knowledge " ]
 }
 }
} 
 
 📂 Repository Structure 
 okf-agent-memory/
├── benchmarks/ # Progressive disclosure benchmark suite & hardware test data
│ ├── data/ # Monolith docs vs OKF bundle test fixtures
│ └── results/ # Reproducible benchmark logs across 8+ local & cloud LLMs
├── cmd/
│ ├── okf/ # Standalone CLI and embedded MCP server (`stdio`)
│ └── okf-benchmark/ # Automated benchmark runner for LLM TTFT & token measurements
├── docs/ # Guides, specifications, architecture & release playbook
│ ├── AGENT_TESTING.md # Multi-agent testing, prompt scenarios & compatibility matrix
│ ├── ALTERNATIVES.md # Comparison against Mem0, Letta, and ad-hoc markdown
│ ├── CLI.md # Complete command-line & MCP tool reference
│ ├── CONVENTION.md # OKF Agent Memory Convention v0.1
│ ├── GETTING_STARTED.md # Comprehensive onboarding guide
│ ├── OKF-COMPATIBILITY.md# OKF v0.2 spec compatibility analysis
│ ├── RELEASE_PLAYBOOK.md # Automated release process & version tagging
│ ├── ROADMAP.md # Project roadmap & milestones
│ └── SECURITY.md # Data governance, secret prevention & PII rules
├── examples/ # Domain-neutral reference OKF v0.2 bundles
│ ├── books/ # Literature & cognitive science knowledge bundle
│ ├── coaching/ # Executive coaching & client session bundle
│ └── software/ # Microservices architecture & ADR bundle
├── knowledge/ # Project's own OKF v0.2 persistent memory bundle
│ ├── index.md # Root progressive disclosure index (okf_version: "0.2")
│ ├── log.md # Dated change log (ISO 8601 YYYY-MM-DD)
│ ├── project/ # Overview & value propositions
│ ├── architecture/ # 5-tier architecture & tooling decisions
│ ├── convention/ # Principles & lifecycle workflows
│ └── roadmap/ # Milestones
├── packaging/ # Distribution packaging
│ └── homebrew/ # Official Homebrew formula & tap instructions
├── pkg/okf/ # Zero-dependency Go core library (parser, validator, BM25, MCP, bootstrap)
├── AGENTS.md # Operating instructions for AI coding agents
├── CONTRIBUTING.md # Contribution guidelines & development workflow
├── Makefile # Build, test, lint, validation & release targets
├── LICENSE # MIT License
├── README.md # Main repository documentation
└── SECURITY.md # Security policy & reporting guidelines
 
 
 🧪 Testing & Verification 
 Run the full test suite and validate the repository's self-documenting knowledge bundle:

 make check 
 
 📖 Further Documentation 
 
 Getting Started Guide — Comprehensive onboarding guide for agents and humans. 
 CLI & MCP Reference — Complete command-line and protocol tools reference. 
 Contributing Guide — Development setup, quality gates, and pull request standards. 
 Security & Privacy Guidelines — Data governance, secret prevention, and PII protection rules. 
 Multi-Agent Testing & Evaluation — Test scenarios, compatibility matrix, and benchmarks. 
 OKF Agent Memory Convention v0.1 — Behavioral rules and lifecycle specification. 
 Project Roadmap & Milestones — Phased development plan. 
 Release Playbook — Versioning, CI/CD pipeline, and distribution procedures. 
 OKF v0.2 Compatibility Matrix — Specification validation analysis. 
 Why OKF Agent Memory? — Detailed value proposition & differentiators. 
 Alternatives & Ecosystem Comparison — Comparison with Mem0, Letta, and ad-hoc markdown files. 
 
 
 📄 License 
 MIT License. See LICENSE for details.

 About Git-native persistent memory for AI coding agents. Implements Google OKF v0.2 with sub-300µs in-memory BM25 search, embedded MCP server, and progressive disclosure. Slashes token bloat by 80% with zero external databases or dependencies. Built in pure Go.
 Resources Readme MIT license Contributing Contributing Security policy Security policy Activity Custom properties Stars 340 stars Watchers 1 watching Forks 16 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
 Footer 

 


 
 
 
 
 
 
 
 
