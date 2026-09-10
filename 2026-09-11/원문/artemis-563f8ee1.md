# google/artemis — ARTEMIS turns natural-language instructions into reliable Android automation. It

- 출처: GitHub 신규 (claude-code)
- 원본 링크: https://github.com/google/artemis
- 발행: 2026-09-10T22:30:10.227035+00:00
- 접근상태: 확인 완료

---

GitHub - google/artemis: ARTEMIS turns natural-language instructions into reliable Android automation. It automates end-to-end workflows, captures logs, and integrates seamlessly with AI coding assistants such as Antigravity, Codex, and Claude Code. It also achieves 99%+ success rate on AndroidWorld Benchmark. Created by Google's Pixel-Test-Engineering (PTE) Fusion team. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 google
 
 / 
 
 artemis 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 133 
 
 

 
 
 
 
 
 Star
 1.5k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 3 


 
 
 
 
 
 
 
 
 Pull requests 
 7 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 110 Commits 110 Commits Folders and files Name Name Last commit message Last commit date .github/ workflows .github/ workflows     apps apps     artemis artemis     config config     docs/ assets docs/ assets     mcp_server mcp_server     packages packages     playground/ artemis_container playground/ artemis_container     scripts scripts     tests tests     .dockerignore .dockerignore     .env.example .env.example     .gitignore .gitignore     .pre-commit-config.yaml .pre-commit-config.yaml     .quality-baseline.json .quality-baseline.json     CONTRIBUTING.md CONTRIBUTING.md     Dockerfile Dockerfile     LICENSE LICENSE     Makefile Makefile     README.md README.md     README_CN.md README_CN.md     pyproject.toml pyproject.toml     pyright-core.json pyright-core.json     setup.py setup.py     start.bat start.bat     start.sh start.sh     uv.lock uv.lock     View all files Repository files navigation README Code of conduct Contributing Apache-2.0 license Security More items 
 


 
 Let AI assistants and test suites use real phones like a human. 


 
 English •
 中文文档 •
 Workflow Showcase •
 Quick Start •
 MCP for IDEs •
 Benchmarks •
 Discord Community 


 
 
 
 
 
 



 
 
 

 Live Demo: Setup driving routes and calculate total durations in Google Maps, then open YouTube to play a Coldplay song. 


 Key Highlights 
 
 Cross-App Automation : Executes testing workflows and everyday tasks on Android from natural language instructions. 
 Multimodal Targeting : Uses element indices when available, with coordinate and visual locating fallbacks for custom interfaces. 
 IDE Diagnostics : Model Context Protocol (MCP) integration lets Antigravity, Claude Code, and Windsurf drive test devices and collect Logcat output and screenshots. 
 Flash Execution : A reactive observe-and-act loop with asynchronous history summaries, typically 3–5s per step . 
 Pro Exploration : Checks targets before individual actions and returns blocked actions to the Operator for recovery. Supports long-running exploratory and stability tests. 
 AndroidWorld Results : 99%+ task completion on Google Research's AndroidWorld benchmark (100+ multi-step tasks). 
 
 

 Antigravity × ARTEMIS: Autonomous Testing Workflow 
 Antigravity uses ARTEMIS through MCP to turn a test request into a plan, device execution, and a diagnostic report:

 
 
 
 1. Prompt Input (Task Dispatch) 

 Describe your test scenario and target metrics in Antigravity 


 
 
 
 2. Test Plan Generation 

 Formulates a step-by-step test plan & architecture for review 


 
 
 
 
 
 3. Autonomous Test Execution 

 Drives real device, navigates UI, and profiles performance 


 
 
 
 4. Final Report 

 Delivers structured audit findings, metric tables, and raw datasets 


 
 
 
 
 

 Quick Start 
 Ensure an Android device (with USB Debugging enabled) or emulator is connected. The one-click startup script will automatically:

 
 Install System Toolchains : Detect and auto-install ADB, scrcpy, FFmpeg, and Python ( uv ) dependencies. 
 Mount Global MCP Server & AI Agent Rules : Prompt to automatically install global MCP configurations and the Artemis Mobile Testing Mindset ( rules.md ) into your AI IDEs ( Antigravity , Cursor , Claude Code , Codex , Windsurf , VS Code , Cline/Roo , OpenClaw ). 
 
 macOS and Linux 
 # 1. Clone repo & navigate to directory 
git clone https://github.com/google/artemis.git && cd artemis

 # 2. One-click launch 
./start.sh 
 Windows PowerShell 
 # 1. Clone repo & navigate to directory 
git clone https: // github.com / google / artemis.git
cd artemis

 # 2. One-click launch 
.\ start.bat 
 
 PowerShell does not search the current directory for executable scripts by default, so use .\start.bat without a trailing \ . In Command Prompt (CMD), use start.bat instead.

 
 
 Tip : Opens http://localhost:8000 in your default browser with a device connection wizard, live screen mirroring, prompt sandbox, and execution replays. You can also run directly from CLI: uv run artemis run "Open Settings, find Battery and tell me current level" --profile flash .

 
 
 

 
 MCP Setup for Codex / Antigravity / Claude Code / Windsurf (Click to expand) 


 ARTEMIS includes a native Model Context Protocol (MCP) server. Connect your real phone directly into AI IDEs:

 1. One-Click Auto Install (Recommended) 
 Running ./start.sh (macOS/Linux) or .\start.bat (Windows PowerShell) will prompt you to configure global MCP and testing rules for detected IDEs (or you can install/update anytime later manually using the commands below):

 # Auto-install MCP server & global rules for Antigravity / Jetski: 
uv run artemis mcp --install antigravity

 # Or install for all supported AI IDEs (including Codex): 
uv run artemis mcp --install all 
 
 Tip : You can also configure MCP interactively during first-time setup via uv run artemis init .
 Pro Tip : If you want to use the artemis command globally without uv run in any directory, run uv tool install -e . once in the project root.

 
 2. Manual Configuration (Optional) 
 If you prefer to configure manually, run uv run artemis mcp --generate-config <client> (for example, codex or antigravity ) to output the appropriate TOML or JSON snippet. Replace /path/to/artemis with your actual repo path and point command to your .venv Python executable:

 
 Codex ( ~/.codex/config.toml ): 
 
 [ mcp_servers . artemis ]
 command = " /path/to/artemis/.venv/bin/python " 
 args = [ " -m " , " mcp_server " ]
 cwd = " /path/to/artemis " 

[ mcp_servers . artemis . env ]
 PYTHONUNBUFFERED = " 1 " 
 PYTHONPATH = " /path/to/artemis " 
 
 Antigravity ( ~/.gemini/jetski/mcp_config.json ): 
 
 {
 "mcpServers" : {
 "artemis" : {
 "command" : " /path/to/artemis/.venv/bin/python " ,
 "args" : [ " -m " , " mcp_server " ],
 "cwd" : " /path/to/artemis " ,
 "env" : {
 "PYTHONUNBUFFERED" : " 1 " 
 },
 "tools" : {
 "mobile_run_task" : { "eager" : true },
 "mobile_manage_task" : { "eager" : true },
 "mobile_get_device_state" : { "eager" : true },
 "mobile_inspect_trace" : { "eager" : true },
 "mobile_diagnose" : { "eager" : true }
 }
 }
 }
} 
 
 Claude Desktop ( claude_desktop_config.json ): 
 
 {
 "mcpServers" : {
 "artemis" : {
 "command" : " /path/to/artemis/.venv/bin/python " ,
 "args" : [ " -m " , " mcp_server " ],
 "cwd" : " /path/to/artemis " 
 }
 }
} 
 3. Mount Behavioral Rules for AI Agents (Highly Recommended) 
 To ensure your AI coding assistant acts with the rigor of a senior mobile test engineer and never hallucinates UI interactions, we provide a dedicated testing mindset rules file at mcp_server/rules.md (covering Active Exploration before coding , Flash vs. Pro routing strategy , Latency & Timing compensation , and the "Dynamic-First, Coordinate-Fallback" locator pattern ).

 You can mount or copy mcp_server/rules.md into your AI IDE's rule configuration:

 
 Antigravity : Add the contents of rules.md to your Workspace Rules, Global Rules settings, or agent instructions. 
 Claude Code : Run artemis mcp --install claude to install the rules to ~/.claude/rules/artemis.md (install to exactly one location — Claude Code loads both ~/.claude/CLAUDE.md and ~/.claude/rules/*.md , so duplicating the rules wastes context). 
 Cursor : Copy the contents into .cursorrules or create a rule file at .cursor/rules/artemis.mdc . 
 Codex : Add the contents to ~/.codex/AGENTS.md (or the active AGENTS.override.md ). 
 Windsurf / OpenClaw : Add the rules to your workspace rules or global system prompts. 
 
 
 For more details on the testing mindset and MCP architecture, see the MCP Server README .

 
 4. Prompt Your Phone in the IDE Chat 
 In Codex, Antigravity, or Claude Code, simply prompt:

 
 "Build the latest changes into an APK, install it on the connected device, open the login screen with a test account, verify if there are any unexpected popups after login, and return screenshots of the final page." 

 
 
 

 
 Python SDK Integration (Click to expand) 


 Install the zero-runtime-dependency client on the development machine. ADB,
agents, models, and image processing remain on the device host:

 uv add " artemis-client @ git+https://github.com/google/artemis.git#subdirectory=packages/artemis-client " 
 import asyncio 
 from artemis_client import ArtemisClient 


 async def main ():
 client = ArtemisClient (
 "http://artemis-host:8000" ,
 device_serial = "emulator-5554" , # optional: target specific device serial 
 default_profile = "flash" , # "flash" (fast reactive) or "pro" (deep reasoning) 
 )

 result = await client . run (
 "Open System Settings, go to 'Battery', verify battery percentage is displayed, and check for any crash dialogs." ,
 )

 assert result . succeeded , f"Test failed: { result . error or result . status } " 
 print ( f"✅ Test Passed! Device: { result . device_serial } | Trace ID: { result . trace_id } " )


 if __name__ == "__main__" :
 asyncio . run ( main ()) 
 
 Usage Modes 
 
 
 

 Console Overview : ① View Switcher (Home / Workspace) · ② Model & Replay (Flash/Pro status & video replay) · ③ Live Agent Stream (Action perception, target coordinates & structured results) · ④ Prompt Dock (Natural language dispatch) · ⑤ Task Queue & Dashboard (Lifecycle & history) 


 
 Web Visual Test Console ( uv run artemis ui ) : Real-time screen projection and interactive panel, supporting natural language test dispatch, live reasoning telemetry, action trajectories, and execution replay; manage server lifecycle anytime from any terminal using uv run artemis restart , uv run artemis stop , and uv run artemis status ; 
 MCP Server : Connects Antigravity, Claude Code, Windsurf , and other MCP clients to real devices for bug reproduction and test execution; 
 Developer CLI ( uv run artemis run ) : Direct terminal execution for automated test cases, exploratory stability inspection, or AndroidWorld benchmarks with high-fidelity structured terminal output; 
 Python SDK : Integrates as a standard Python library into existing automated testing frameworks (e.g., pytest) or CI/CD pipelines with strongly typed Pydantic structured outputs and assertion support. 
 
 

 Benchmarks: AndroidWorld (SOTA 99%+) 
 Artemis achieved a 99%+ completion rate on AndroidWorld , 