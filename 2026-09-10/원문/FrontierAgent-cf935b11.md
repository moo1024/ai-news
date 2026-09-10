# ApodexAI/FrontierAgent — 🧩 FrontierAgent, our agent framework, open-sourced alongside it — native command

- 출처: GitHub 신규 (AI 에이전트)
- 원본 링크: https://github.com/ApodexAI/FrontierAgent
- 발행: 2026-09-10T03:54:46.057681+00:00
- 접근상태: 확인 완료

---

GitHub - ApodexAI/FrontierAgent: 🧩 FrontierAgent, our agent framework, open-sourced alongside it — native command-line TUI, ReAct and Agent Team modes, one command on macOS and Linux, no preinstall, no hard Docker dependency. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 ApodexAI
 
 / 
 
 FrontierAgent 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 171 
 
 

 
 
 
 
 
 Star
 2.5k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 6 


 
 
 
 
 
 
 
 
 Pull requests 
 6 


 
 
 
 
 
 
 
 
 Discussions 
 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Projects 
 


 
 
 
 
 
 
 
 
 Security and quality 
 0 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Discussions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Projects
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 66 Commits 66 Commits Folders and files Name Name Last commit message Last commit date .github/ workflows .github/ workflows     apodex apodex     assets assets     benchmarks benchmarks     config config     deploy deploy     docker docker     docs docs     frontier_agent frontier_agent     plugins plugins     scripts scripts     tests tests     tools tools     workflows workflows     .dockerignore .dockerignore     .env.example .env.example     .env.sglang.example .env.sglang.example     .env.transformers.example .env.transformers.example     .gitignore .gitignore     .python-version .python-version     CHANGELOG.md CHANGELOG.md     CONTRIBUTING.md CONTRIBUTING.md     Dockerfile Dockerfile     LICENSE LICENSE     README.md README.md     SECURITY.md SECURITY.md     compose.dev.yaml compose.dev.yaml     compose.network.yaml compose.network.yaml     compose.sglang.yaml compose.sglang.yaml     compose.transformers.yaml compose.transformers.yaml     compose.yaml compose.yaml     package-lock.json package-lock.json     pyproject.toml pyproject.toml     pyrightconfig.json pyrightconfig.json     uv.lock uv.lock     View all files Repository files navigation README Contributing Apache-2.0 license Security More items 
 
 
 
 
 


 
 
 
 
 

 
 
 
 
 


 
 Tech Blog ·
 Tech Report 


 FrontierAgent 
 FrontierAgent is an open-source agent runtime, terminal product, and evaluation
suite for long-horizon research and file-based work. The frontier-agent TUI
ships two native workflows:

 
 ReAct — one stateful agent researches, reads files, writes deliverables,
runs commands, and iterates in a task-scoped sandbox. 
 Agent Team — a coordinator maintains a task board, delegates independent
work to parallel sub-agents, collects their reports, and synthesizes the result. 
 
 The same workflow engine powers the benchmark runner used to evaluate Apodex
models. The framework, tools, workflows, and evaluation layer remain separate,
so each can be reused independently.

 Important

 🚀 Try FrontierAgent on the Apodex API — free for the next two weeks! 
 No model hosting required. Get an API key, connect to the OpenAI-compatible
Apodex-1.1 endpoint, and start running FrontierAgent in minutes.

 → Start building for free at platform.apodex.ai 

 ⏳ This is a limited-time offer—come try it and let us know what you build!

 
 New here? Use the documentation index to find the right
installation, SGLang, workflow, evaluation, or developer guide.

 
 


 Highlights 
 
 Native Agent Team workflow. The coordinator decomposes the request,
dispatches bounded parallel assignments, receives structured reports, and can
use an optional fast reporter for final evidence review. 
 Task Board. Agent Team's add_task and update_task events appear live in
the TUI sidebar with pending, active, completed, blocked, and cancelled state. 
 Sandboxed file work. Shell and file tools share one task-scoped filesystem:
 /inputs is read-only, /workspace is working state, and /outputs contains
persistent deliverables. Authorization and sandbox failures are fail-closed. 
 Asynchronous intervention. Type while an agent is running to queue a new
instruction. It is injected at the next safe turn boundary without discarding
the active run. In Agent Team mode it steers the coordinator; already-running
sub-agents are allowed to finish. 
 Transparent deliverables. On macOS/Docker, /outputs maps to
 .apodex/runs/<session-id>/outputs on the host. The same run directory also
contains its checkpoint, trace, engine log, and trajectories. 
 Approval, trace, and recovery. Mutating operations show a diff and require
approval unless --yes is enabled. Sessions are checkpointed, every action is
traced locally, /revert restores session changes, and --resume continues a
saved run. 
 Evaluation included. The subprocess runner supports research and
file-grounded benchmarks, deterministic artifact collection, concurrency,
progress inspection, and rerunning individual failures. 
 
 
 


 Conceptual Agent Team workflow, from task delegation and asynchronous report collection to verification and final synthesis. 

 How it fits together 
 
 
 
 flowchart LR
 U["User / benchmark task"] --> TUI["TUI or subprocess runner"]
 TUI --> R["Stateful ReAct"]
 TUI --> C["Agent Team coordinator"]
 C --> B["Task board"]
 B --> S1["Sub-agent 1"]
 B --> S2["Sub-agent 2"]
 B --> SN["Sub-agent N"]
 R --> FS["Task sandbox"]
 S1 --> FS
 S2 --> FS
 SN --> FS
 FS --> I["/inputs (read-only)"]
 FS --> W["/workspace (working files)"]
 FS --> O["/outputs (deliverables)"]
 S1 --> C
 S2 --> C
 SN --> C
 C --> A["Final answer / report"]
 R --> A
 
 
 
 
 
 
 
 
 Loading 
 
 
 

 The repository boundaries are intentional:

 frontier_agent/ generic loop, scheduling, registries, AgentBus, observers
plugins/tools/ web, shell, file, sandbox, and team tool implementations
workflows/ ReAct and Agent Team pipelines, profiles, prompts, observers
apodex/ terminal CLI/TUI, approvals, sessions, traces, and Docker path
benchmarks/ public harness plus bundled FrontierSearchBench/FrontierChallenge
 
 More detail: framework architecture ,
 Agent Team , and
 Stateful ReAct . See
 run artifacts and timestamps for the on-disk layout.

 Quick start 
 Requirements: Git, Python 3.12, uv , and an
OpenAI-compatible model endpoint. Docker is optional.

 git clone https://github.com/ApodexAI/FrontierAgent.git
 cd FrontierAgent

uv sync --python 3.12 --extra dev
cp .env.example .env 
 Add your endpoint to .env :

 OPENAI_API_KEY = your-key 
 OPENAI_BASE_URL = https://your-openai-compatible-endpoint/v1 
 OPENAI_MODEL = your-model-name 

 # Optional web research tools 
 SERPER_API_KEY = 
 JINA_API_KEY = 
 Start the TUI:

 # Stateful single-agent workflow 
uv run frontier-agent --mode react --cwd /path/to/project

 # Coordinator plus parallel sub-agents 
uv run frontier-agent --mode agent_team --cwd /path/to/project 
 uv sync above installs the lightweight terminal runtime. Scientific and
document packages are intentionally optional in native mode; the agent installs
only what a task actually needs into <project>/.apodex/runtime/native . The
 apodex command is retained as a compatibility alias.

 Prefer a script that does all of the above? ./scripts/run-macos.sh and
 ./scripts/run-linux.sh set up a hosted-endpoint install, and
 ./scripts/run-linux-gpu.sh --install-system-deps --setup-only prepares a native,
isolated SGLang environment on a Linux NVIDIA GPU. The step-by-step equivalent is
the endpoint quickstart 
( 中文教程 ), which requires neither
model self-hosting nor Docker.

 Local SGLang serving is pinned to reviewed NVIDIA driver / CUDA / SGLang tracks,
and a mismatch surfaces late as opaque CUDA or Triton kernel errors during model
load. Confirm your nvidia-smi driver against the
 GPU compatibility matrix before choosing an
image tag or native pin. The GPU helper selects a reviewed userspace track from
the host driver, but never installs or replaces the driver itself.

 Deployment model 
 The operating system, FrontierAgent runtime, and model runtime are independent
choices. “NVIDIA” describes the local model service, not how the agent itself
runs. Unsure which applies to your machine or GPU provider? Start with the
 installation chooser .

 
 
 
 Environment 
 FrontierAgent runtime 
 Model endpoint 
 Start here 
 
 
 
 
 macOS 
 native or Docker Desktop 
 hosted or another OpenAI-compatible endpoint 
 macOS 
 
 
 Linux host/VM 
 native (default), bubblewrap, or Docker 
 hosted, native SGLang, or Docker SGLang 
 Linux 
 
 
 managed Linux GPU container 
 native inside the provider container 
 custom GPU image or native SGLang 
 GPU platforms 
 
 
 Windows 
 WSL2, treated as Linux 
 hosted or a WSL2-reachable endpoint 
 Linux/WSL2 
 
 
 
 Chinese-speaking macOS users can use the
 macOS 中文安装与一键启动指南 .

 Containers and local models 
 Pre-built linux/amd64 and linux/arm64 images are published to the GitHub
Container Registry, so no local Python environment is needed:

 cp .env.example .env
docker compose run --rm agent 
 
 Run FrontierAgent in Docker — Compose, image
pinning, direct docker run , and EC2/ECS deployment. 
 Docker SGLang on a Linux NVIDIA host — two
containers on one network; SGLang owns the GPU. 
 Native SGLang without nested Docker —
for managed GPU environments that forbid a nested daemon. 
 SGLang configuration reference — every .env.sglang 
variable, token-budget invariants, and tuning order. Production 35B templates
for RTX 4090, RTX 5090, and two-GPU hosts live under config/sglang/ . 
 
 Using the TUI 
 Run without a task for an interactive session, or pass one and stay in the
session for follow-ups:

 uv run frontier-agent --mode agent_team --cwd /repo \
 " Research the alternatives, verify the evidence, and write a report " 

 # One-shot, line mode, or resume a saved session 
uv run frontier-agent --mode react --cwd /repo -p " explain src/main.py " 
uv run frontier-agent --mode agent_team --no-tui " compare these implementations " 
uv run frontier-agent --resume

 # Attach read-only documents before the TUI starts (repeatable) 
uv run frontier-agent --mode react --cwd /repo \
 --input ~ /Downloads/claim.pdf --input ~ /Desktop/photo.jpg 
 The sidebar carries the plan/task board, live tool activity, deliverables, and a
session-scoped diff. While a workflow is busy, typing a follow-up queues it for
the next safe turn boundary rather than interrupting the run.

 For the four sidebar tabs, previews, approvals, attachments, clipboard support,
keys, and Agent Team live steering, see the
 TUI user guide 
( 中文使用教程 ). The full slash-command, option,
and theming reference is apodex/README.md .

 Workflow modes 
 
 
 
 Mode 
 Best for 
 Execution model 
 
 
 
 
 react 
 focused research, repository analysis, document/file work 
 one stateful agent using the tui workflow profile 
 
 
 agent_team 
 broad questions that benefit from decomposition and parallel investigation 
 coordinator, persistent task board, bounded parallel sub-agents, report collection, synthesis 
 
 
 
 Agent Team parallelism is additional to benchmark concurrency. When evaluating,
start with --concurrency 1 ; total simultaneous model calls can approach runner
concurrency multiplied by the team spawn limit.

 Set SWARM_NO_WEB=1 to disable Agent Team web tools or REACT_NO_WEB=1 for
closed-b