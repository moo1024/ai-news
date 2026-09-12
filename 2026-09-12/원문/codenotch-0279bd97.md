# vinzdg/codenotch — A macOS app that pins usage limits from Claude Code, Cursor, Codex, and Antigrav

- 출처: GitHub 신규 (claude-code)
- 원본 링크: https://github.com/vinzdg/codenotch
- 발행: 2026-09-12T10:54:37.403848+00:00
- 접근상태: 확인 완료

---

GitHub - vinzdg/codenotch: A macOS app that pins usage limits from Claude Code, Cursor, Codex, and Antigravity to a screen edge. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 vinzdg
 
 / 
 
 codenotch 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 233 
 
 

 
 
 
 
 
 Star
 1.5k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 24 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 276 Commits 276 Commits Folders and files Name Name Last commit message Last commit date .github .github     Scripts Scripts     Sources Sources     Tests Tests     docs docs     site site     windows windows     .gitignore .gitignore     CONTRIBUTING.md CONTRIBUTING.md     LICENSE LICENSE     Makefile Makefile     README.md README.md     TASKS.md TASKS.md     project.yml project.yml     View all files Repository files navigation README Contributing MIT license More items 
 

 
 
 
 

 A macOS app that pins a small black notch to a screen edge, showing how much
of each coding assistant's usage limit you have burned — and whether it is
still working, done, or waiting on you. 

 

 
 Hover a ring for its limit windows and when they reset. Claude's ring shows the
same current session window Claude Code's own /usage leads with, so the
two never disagree.

 Download 
 

 That button is the disk image itself, not the page it sits on — the asset is
named Codenotch.dmg in every release, so releases/latest/download/ always
resolves to the newest one and the link never needs updating. Signed,
notarized, and updating itself from then on. Take this one unless you have a
reason not to; the release page has the notes.

 To try unreleased main without an Xcode install, the preview
build is rebuilt from every commit, and the
Package workflow keeps a per-commit disk image on each of its
 runs . Neither is notarized — they are
ad-hoc signed, because the Developer ID certificate exists on one machine — so
macOS quarantines the download. Clear the flag once, after dragging the app to
Applications:

 xattr -dr com.apple.quarantine /Applications/Codenotch.app 
 If macOS says the app is damaged , that is the quarantine flag rather than a bad download — run the command above.

 Universal binary. macOS 15 or later. To build and install a copy from source
instead, see Building .

 Windows 
 A Windows port — Rust/Tauri 2, same design and providers — lives in windows/ .

 What it reads 
 
 
 
 Provider 
 Source 
 How 
 
 
 
 
 Claude Code 
 official 
 Claude Desktop's own cached usage response, where Desktop is running and signed into the same account. Then Claude Code's own /usage , asked of the installed claude . Then the OAuth token in the login keychain, against the endpoint that command uses. 
 
 
 Cursor 
 official 
 The editor's signed-in session in its local SQLite state, or the cursor-agent login in the keychain — no separate sign-in. 
 
 
 Codex 
 official 
 ChatGPT's usage endpoint, using the local Codex sign-in. Shows the 5-hour and weekly limits when available. 
 
 
 DeepSeek Platform 
 derived from official Platform responses 
 Explicit sign-in in Codenotch's own WKWebView, then the Platform account summary and API-key/model usage endpoints. Shows funded/spent balance, 30-day tokens/cost, requests and API-key count. 
 
 
 Antigravity 
 official where licensed, otherwise a request count 
 Antigravity's local language server first, then Google's quota endpoint; a plain count when neither will answer for the account. 
 
 
 GLM 
 official 
 Z.ai's Coding Plan monitor endpoint, with a key borrowed from whichever coding tool already holds one — Claude Code's settings.json , ZCode, or OpenCode. 
 
 
 Ollama (Local) 
 local runtime 
 Automatically detected local models, RAM/VRAM, unload time and context. Optional response capture adds thinking and generation speed. 
 
 
 LM Studio 
 local runtime 
 Loaded models from LM Studio's own listing, what each one is doing (prompt, generating, queue) from its SDK socket, and speed, context use and tokens per day from its server log. No relay needed. 
 
 
 Grok 
 official 
 The Grok CLI session in ~/.grok/auth.json , against the same credits billing endpoint /usage uses. 
 
 
 OpenCode 
 official 
 The Go plan's official usage endpoint, with the opencode-go key OpenCode itself stores on sign-in. 
 
 
 Command Code 
 official 
 The GOAT plan's /alpha billing endpoints, with the key the Command Code app writes to ~/.commandcode/auth.json . 
 
 
 GitHub Copilot 
 official 
 GitHub's Copilot quota endpoint, authenticated with the GitHub CLI session already on the Mac ( gh auth login ). 
 
 
 Kimi 
 official 
 The Kimi Code CLI session in ~/.kimi-code/credentials/kimi-code.json , against the same /usages endpoint the CLI's /usage asks. Shows the 5-hour rate window and the weekly quota. 
 
 
 
 Most providers borrow a credential or session from a tool already on your Mac.
DeepSeek is the explicit browser-login exception: it never reads a browser's
cookies or credentials, and only makes requests after you choose Sign in to
DeepSeek from Codenotch.
Ollama Cloud accepts an API key in Settings. Switching a provider off stops its
usage polling and forgets its readings; borrowed accounts stay signed in to
the tools that own them.

 Local Ollama is detected automatically. Configure its address or stop monitoring in Settings → Ollama .
Each loaded model gets a notch cell; reorder or hide it in Settings → Accounts .
Hover for RAM/VRAM, unload time, context limit and quantization.

 For generation speed ( tok/s ) and live Thinking , enable Measure speed and thinking 
in Settings → Ollama, keep Codenotch open and connect through its local relay:

 OLLAMA_HOST=http://127.0.0.1:11435 ollama run gemma4:e4b --think 
 Speed updates after completed native Ollama responses; thinking requires streamed
reasoning. Direct requests to Ollama's default port ( 11434 ) only provide model
detection. Monitoring never initiates inference or saves prompts, reasoning or replies.
See Ollama details .

 Local LM Studio is detected automatically on the port LM Studio's own settings name
(1234 unless you moved it). Configure the address or stop monitoring in Settings → LM Studio .
Each loaded language model gets a notch cell; embedding models are left out. The cell shows the
last response's tok/s and its ring fills with how much of the loaded context the last
request used. A white arc turns while the model reads a prompt or generates, and becomes a ring
of dots when requests are queued behind it. Hover for context used, tokens and requests today,
reasoning share, speculative-decoding acceptance, model size, quantization and context limit.

 Nothing has to be pointed at Codenotch: what a model is doing comes from LM Studio's SDK socket
on the same port (the one lms ps uses), and speed and tokens come from ~/.lmstudio/server-logs ,
which LM Studio writes for every request from any client. Only counts and timings are read from
those files, never a prompt or a reply. Responses through the OpenAI-compatible endpoint carry no
clock, so their speed is timed from the generating phase and marked ~ . If LM Studio's server is
set to require an API token, paste one in Settings → LM Studio (or export LM_API_TOKEN ); without
one, requests are sent with no Authorization header at all.
See LM Studio details .

 Settings lists the connected providers in the order the notch draws them, and
you can drag one by its handle to move it. The order is remembered across
launches. A provider you switch back on joins the end of that list rather than
reclaiming an older position, so nothing you cannot currently see jumps ahead
of something you placed deliberately.

 It also answers "is it still working?" — a thin arc spins inside a
provider's ring while a session is busy, and becomes a pulsing amber ring when
one is blocked waiting on you. Hover for every live session by name, where it
is running, and what it wants.

 Two Claude Code logins are two rings. Anyone who keeps a work account apart with
 CLAUDE_CONFIG_DIR=~/.claude-work claude gets a Claude (work) ring beside the
personal one, with its own limits, its own sessions and its own row in Settings.
Any ~/.claude-<slug> directory Claude Code has run against is found at launch;
the default ~/.claude always comes first, the rest in alphabetical order, so the
rings never swap places.

 Codex accounts work the same way: ~/.codex stays the Codex ring, and each
used ~/.codex-<slug> directory adds a Codex (slug) ring with its own limits,
activity and Settings row. Profiles are discovered at launch, default first,
then alphabetically. To connect a second account, sign in through Codex CLI
using a separate home directory:

 mkdir -p " $HOME /.codex-work " 
CODEX_HOME= " $HOME /.codex-work " codex -c ' cli_auth_credentials_store="file" ' login 
 Choose the second account during sign-in, then restart Codenotch. Run that
account's CLI sessions with CODEX_HOME="$HOME/.codex-work" codex as well.
Repeat with another name, such as .codex-personal , for more accounts.
Settings shows each account's email and profile directory; each ring can be
reordered or switched off independently. Switching one off forgets only its
Codenotch readings and leaves the Codex login intact.

 Codenotch reads each profile's auth.json ; keychain-only or API-key-only
logins cannot provide these ChatGPT account limits. It never copies, refreshes
or writes Codex credentials. If a login expires, use that profile's Codex CLI
to renew it. Directories outside the ~/.codex-<slug> convention are not
discovered automatically, and adding a profile requires restarting Codenotch,
just as it does for Claude.

 When a session ends 
 The notch opens itself for five seconds when an agent stops working, or stops
to ask you something, and sounds the system alert. Clicking it while it is open
brings that session's application to the front.

 The app, not the tab. A session publishes its pid and nothing else — no window,
no tab, no tty — so the app is found by walking up the process tree from the
agent to whatever launched it. Choosing the tab inside that app needs the
terminal's own scripting interface, and there is no general one: Terminal.app
and iTerm2 can match a tab by tty, Warp and Ghostty publish no scripting
dictionary at all. So the app is raised for everybody and the tooltip names the
session, which leaves the last hop one keystroke rather than working for two
terminals and silently doing nothing in a third.

 Both halves switch off separately in Settings, because they fail differently:
the peek is no use behind a full-screen window, and the sound is no use in a
meeting. Each of the two events — finished, and waiting on you — picks its own
sound there, with a preview button beside it.

 The sound is played as a file on the ordinary output rather than handed to
 NSSound as a system alert. A system alert goes through the interface
sound-effects channel, which System Settings → Sound can switch off — and on a
Mac where it is off, NSSound.play() rep