# duty1g/x64dbg-mcp-server — x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg tha

- 출처: GitHub 신규 (claude-code)
- 원본 링크: https://github.com/duty1g/x64dbg-mcp-server
- 발행: 2026-09-08T10:54:37.779781+00:00
- 접근상태: 확인 완료

---

GitHub - duty1g/x64dbg-mcp-server: x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more. Built with Zig — zero dependencies, single-binary output, cros · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 duty1g
 
 / 
 
 x64dbg-mcp-server 
 

 Public 
 


 

 
 
 
 
 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 
 

 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 194 
 
 

 
 
 
 
 
 Star
 1.9k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 0 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Projects 
 


 
 
 
 
 
 
 
 
 Security and quality 
 2 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Issues
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Projects
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 22 Commits 22 Commits Folders and files Name Name Last commit message Last commit date .github .github     src src     .gitignore .gitignore     LICENSE LICENSE     README.md README.md     SKILL.md SKILL.md     build.zig build.zig     build.zig.zon build.zig.zon     logo.png logo.png     View all files Repository files navigation README MIT license More items 

 x64dbg-MCP Server 
 MCP-powered agentic reverse engineering for x64dbg. 
 
 
 
 
 
 
 
 
 


 
 Features •
 Install •
 Usage •
 Tools •
 Configuration •
 Building •
 Structure 


 
 x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.

 Built with Zig — zero dependencies, single-binary output, cross-compiles to both x32 and x64 from any host. No .NET, no Python, no runtime — just drop the plugin into your x64dbg plugins folder and go.

 
 MCP 2024-11-05 — Streamable HTTP + SSE transports, JSON-RPC 2.0.

 
 Features 
 
 84 MCP Tools: Full debugger control — disassembly, stepping, breakpoints, memory allocation, registers, modules, threads, call stack, pattern scanning, string extraction, xrefs, symbols, bookmarks, PE analysis, OEP detection, module dumping, PEB/SEH inspection, tracing, and more. 
 22 Event Callbacks: Full debugger event coverage — init, stop, breakpoint, exception, step, attach/detach, DLL load/unload, threads, and more. 
 Zero Dependencies: Pure native plugin, no runtime or framework needed. 
 x32 and x64: Single codebase, builds both architectures from one command. 
 Dual Transport: Streamable HTTP + SSE — compatible with any MCP client (new and legacy). 
 Bearer Auth: Mandatory token authentication — auto-generated on first run, required on every request to prevent unauthorized access. 
 Config Dialog: Change IP/port/token from the Plugins menu, auto-restarts the server on save. 
 Auto-Start: MCP server starts automatically when x64dbg launches. 
 Cross-Compile: Build Windows plugins from Linux, macOS, or WSL. 
 
 Install 
 Download the latest release or build from source:

 
 Copy the contents of dist/ into your x64dbg root folder (deploys both x32 and x64) 
 Launch x64dbg 
 
 The MCP server starts automatically. Default ports:

 
 x64: 0.0.0.0:9094 
 x32: 0.0.0.0:9095 
 
 Usage 
 Add to your MCP client config ( .mcp.json , etc.):

 Streamable HTTP (recommended): 

 {
 "mcpServers" : {
 "x64dbg" : {
 "type" : " http " ,
 "url" : " http://localhost:9094/ " ,
 "headers" : {
 "Authorization" : " Bearer YOUR_TOKEN_HERE " 
 }
 }
 }
} 
 SSE (legacy clients): 

 {
 "mcpServers" : {
 "x64dbg" : {
 "type" : " sse " ,
 "url" : " http://localhost:9094/sse " ,
 "headers" : {
 "Authorization" : " Bearer YOUR_TOKEN_HERE " 
 }
 }
 }
} 
 If connecting from WSL or a remote machine, use the host's IP address and set the bind address to 0.0.0.0 in the config dialog.

 Example — AI-assisted reverse engineering session: 

 You: Load calc.exe and break at the entry point
AI: [calls LoadBinary, SetBreakpoint, run, WaitForPause]
 Loaded calc.exe, hit breakpoint at 0x7FF7A1234000 in calc.exe

You: What are the current registers?
AI: [calls GetAllRegisters]
 RAX: 0x0, RCX: 0x7FF7A1234000, RDX: 0x1, ...

You: Read 64 bytes at the current instruction pointer
AI: [calls ReadMemory]
 48 83 EC 28 E8 12 34 00 00 ...

You: Step over the next 3 instructions and show me the stack
AI: [calls StepOver x3, GetCallStack]
 Stepped to 0x7FF7A1234010, call stack: ...
 
 Tools 
 72 MCP tools covering the full x64dbg debugging workflow.

 Always available 
 
 
 
 Tool 
 Description 
 
 
 
 
 GetDebugState 
 Current debugger state, PID, instruction pointer 
 
 
 LoadBinary 
 Load an executable into the debugger 
 
 
 ExecuteDebuggerCommand 
 Run any x64dbg command 
 
 
 ListCommandsByCategory 
 List available MCP tools 
 
 
 SearchForStrings 
 Search process memory for text 
 
 
 GetEventLog 
 Last N debugger events (exceptions, breakpoints, DLL loads) 
 
 
 ClearEventLog 
 Clear the event log 
 
 
 EvalExpression 
 Evaluate any x64dbg expression (address, register, arithmetic) 
 
 
 AttachProcess 
 Attach to a running process by PID 
 
 
 Echo 
 Echo input back 
 
 
 WaitForEvent 
 Long-poll for debugger events (breakpoint, pause, resume, exception) 
 
 
 
 Requires active debug session 
 
 
 
 Tool 
 Description 
 
 
 
 
 GetCurrentAddress 
 Current EIP/RIP with label and comment 
 
 
 Disassemble 
 Disassemble N instructions at an address 
 
 
 DisassembleFunction 
 Disassemble an entire function by boundaries 
 
 
 ReadMemory 
 Hex dump of process memory 
 
 
 WaitForPause 
 Block until target pauses 
 
 
 run 
 Resume execution (F9) 
 
 
 StepInto 
 Single-step into calls (F7) 
 
 
 StepOver 
 Step over calls (F8) 
 
 
 StepOut 
 Run until return (Ctrl+F9) 
 
 
 PauseDebug 
 Pause the target (F12) 
 
 
 StopDebug 
 Terminate debug session 
 
 
 RestartDebug 
 Restart debug session 
 
 
 SetBreakpoint 
 Set INT3 breakpoint at address/symbol 
 
 
 SetHardwareBreakpoint 
 Set hardware breakpoint (DR0-DR3, read/write/execute) 
 
 
 SetConditionalBreakpoint 
 Set breakpoint with condition expression and optional log 
 
 
 EnableBreakpoint 
 Enable a breakpoint at a given address 
 
 
 DisableBreakpoint 
 Disable a breakpoint without deleting it 
 
 
 ToggleBreakpoint 
 Toggle a breakpoint between enabled and disabled 
 
 
 DeleteBreakpoint 
 Remove a breakpoint 
 
 
 DeleteAllBreakpoints 
 Remove all breakpoints (normal, hardware, memory) 
 
 
 ResetHitCount 
 Reset a breakpoint's hit counter to zero 
 
 
 ListBreakpoints 
 List all active breakpoints 
 
 
 GetAllRegisters 
 Dump all general-purpose registers 
 
 
 SetRegister 
 Set a CPU register value 
 
 
 GetCallStack 
 Current thread call stack 
 
 
 GetThreads 
 List all threads with IDs and instruction pointers 
 
 
 SwitchThread 
 Switch active thread context 
 
 
 SuspendThread 
 Suspend a thread by its thread ID 
 
 
 ResumeThread 
 Resume a suspended thread 
 
 
 ListModules 
 List loaded modules with base addresses and sizes 
 
 
 GetMemoryMap 
 Memory regions with addresses, sizes, and protection 
 
 
 GetDumpableRegions 
 List committed, readable memory regions 
 
 
 AllocateMemory 
 Allocate memory in the target process 
 
 
 FreeMemory 
 Free allocated memory in the target process 
 
 
 WriteMemToAddress 
 Patch memory with hex bytes 
 
 
 RestorePatches 
 Restore all patches to original bytes 
 
 
 Assemble 
 Assemble an instruction at an address 
 
 
 CommentOrLabelAtAddress 
 Add comment/label in disassembly 
 
 
 SetBookmark 
 Set a bookmark at an address 
 
 
 DeleteBookmark 
 Delete a bookmark 
 
 
 ListBookmarks 
 List all bookmarks 
 
 
 GetImports 
 Show module import table 
 
 
 GetExports 
 Show module export table 
 
 
 SearchSymbols 
 Search for symbols matching a pattern 
 
 
 ListSymbols 
 List exported symbols of a module 
 
 
 GetPatches 
 List all memory patches 
 
 
 FindPattern 
 Scan module memory for byte pattern with ?? wildcards 
 
 
 GetStrings 
 Extract ASCII strings from a module's memory 
 
 
 GetReferences 
 Find CALL/JMP xrefs to a target address 
 
 
 GetFunctions 
 List analyzed functions with addresses and labels 
 
 
 AnalyzeModule 
 PE structure analysis: sections, EP, image size 
 
 
 DetectOEP 
 Detect Original Entry Point for packed executables 
 
 
 DumpMemory 
 Save memory region to file on disk 
 
 
 DumpModule 
 Dump an entire module to a file 
 
 
 RunToAddress 
 Run until hitting a specific address 
 
 
 TraceInto 
 Step N instructions recording address + disassembly 
 
 
 FollowPointer 
 Dereference pointer chain N levels deep 
 
 
 WatchExpressions 
 Evaluate multiple expressions in one call 
 
 
 GetSEHChain 
 Walk Structured Exception Handler chain (x32) 
 
 
 GetPEB 
 Read Process Environment Block fields 
 
 
 GetArguments 
 Read function arguments from stack/registers 
 
 
 SetMemoryBreakpoint 
 Set memory breakpoint (read/write/execute) 
 
 
 SetExceptionBreakpoint 
 Configure exception breakpoint (break or ignore, first/second/all chance) 
 
 
 DeleteExceptionBreakpoint 
 Delete an exception breakpoint 
 
 
 AnalyzeCode 
 Run code analysis (function, module, or control flow) 
 
 
 TraceOver 
 Trace N instructions stepping over calls 
 
 
 SetBreakpointCommand 
 Set a command to execute when a breakpoint is hit 
 
 
 SetBreakpointFastResume 
 Enable/disable fast resume (auto-continue) on a breakpoint 
 
 
 SaveDatabase 
 Save the x64dbg database (.dd64/.dd32) 
 
 
 
 Configuration 
 Go to Plugins > x64dbg-MCP Server > Configure MCP Server... to change the bind address, port, and auth token.

 
 0.0.0.0 — listen on all interfaces (for WSL/remote access) 
 127.0.0.1 — local-only access 
 
 Authentication 
 A Bearer token is auto-generated on first run and required on every request. The MCP server has full debugger control and can read/write process memory — all requests without a valid token receive 401 Unauthorized . Click Generate in the config dialog to rotate the token, or Copy to copy it to clipboard. Clients must include the token as an Authorization: Bearer <token> header.

 Changes take effect immediately — the server auto-restarts on save. Config is persisted to mcp_config.json next to the x64dbg executable.

 Building 
 Requires Zig 0.16-dev or later. Builds on Windows, WSL, Linux, or macOS.

 zig build -Doptimize=ReleaseSafe --prefix dist 
 Output mirrors x64dbg's folder structure — copy the contents of dist/ into your x64dbg root to deploy both architectures at once:

 dist/
├── x32/
│ └── plugins/
│ └── x64dbg-MCP-Server.dp32
└── x64/
 └── plugins/
 └── x64dbg-MCP-Server.dp64
 
 Project Structure 
 ├── build.zig # build config — x32 + x64 cross-compilation
├── build.zig.zon # package manifest
└── src/
 ├── main.zig # plugin entry point, menu, callbacks
 ├── core/
 │ ├── bridge.zig # x64dbg SDK bindings (runtime-resolved)
 │ ├── config.zig # Win32 config dialog and persistence
 │ └── mcp_server.zig # HTTP server and JSON-RPC dispatch
 ├── mcp/
 │ ├── json.zig # JSON writer and parser helpers
 │ └── tools.zig # MCP tool definitions and handlers
 └── resou