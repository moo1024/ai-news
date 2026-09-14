# Vincentwei1021/anything2explainer — Topic in, narrated explainer video out. A Claude Code / Codex skill that turns a

- 출처: GitHub 신규 (AI 에이전트)
- 원본 링크: https://github.com/Vincentwei1021/anything2explainer
- 발행: 2026-09-14T22:24:46.559913+00:00
- 접근상태: 확인 완료

---

GitHub - Vincentwei1021/anything2explainer: Topic in, narrated explainer video out. A Claude Code / Codex skill that turns any topic into a black-canvas motion-graphics explainer video with TTS voiceover, subtitles and a chapter progress bar. Chinese or English; every frame drawn in code with Remotion. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 Vincentwei1021
 
 / 
 
 anything2explainer 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 219 
 
 

 
 
 
 
 
 Star
 1.3k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 20 Commits 20 Commits Folders and files Name Name Last commit message Last commit date examples examples     reference reference     template template     .gitignore .gitignore     CITATION.cff CITATION.cff     LICENSE LICENSE     README.md README.md     README_ZH.md README_ZH.md     SKILL.md SKILL.md     View all files Repository files navigation README License More items anything2explainer 
 
 
 
 

 English | 简体中文 

 Topic in, narrated explainer video out. anything2explainer is a Claude Code / Codex skill that turns any topic into a black-canvas motion-graphics explainer video with TTS voiceover, subtitles and a chapter progress bar, in Chinese or English. Every frame is drawn in code with Remotion (React + TypeScript). No stock footage, no generative video model, no frames lifted from anyone else's work.

 It is not a CLI. What ships here is the whole method an AI coding agent needs to finish the film: a compilable Remotion template, a primitives and lighting library, tooling for voiceover / storyboard / rendering / quantitative QC, written style and motion specs, a multi-agent division-of-labour protocol, and one complete reference film as the quality bar.

 English cut — RAG & Knowledge Bases , 5′02″, 44 lines / 785 words, voiced by kokoro-82m am_liam at natural speed:

 
 
 
 
 
 rag_en_v4_under10mb.mp4 
 
 

 

 
 

 Chinese cut — RAG 与知识库 v2, 4′54″, 44 lines / 1490 characters, dot-field backdrop ( bg: 'dots' ), voiced through the bring-your-own-TTS path (Volcengine TTS 2.0 + forced alignment):

 
 
 
 
 
 rag_zh2d_v1_under10mb.mp4 
 
 

 

 
 

 Both cuts share one storyboard and 44 shots; the English cut re-times every shot to the English voiceover. The full paper trail of the original Chinese cut (4′35″, star-field backdrop, 8 build agents in parallel for 40 minutes, two QC rounds) lives in examples/rag/ (research → narration → storyboard → shot source → QC reports → delivery notes); rendered frames are in examples/rag/frames/ .

 What it does 
 
 Input : a topic ("explain vector databases"), or an article / document you want turned into a video. You also pick the length and the language. 
 Output : a 1280×720 H.264 MP4 with synchronized voiceover, word-boundary-aligned subtitles, chapter cards, a top HUD and a bottom chapter progress bar, plus the full paper trail (research doc with sources, narration, storyboard, per-shot source code, QC reports). 
 How : the agent researches the topic with sources, writes the narration, generates the voiceover and frame-accurate timeline, storyboards every shot, then dispatches parallel build agents that write one Remotion component per shot. QC agents review the rendered frames against written criteria before delivery. 
 Time : roughly 1 to 3 hours of wall clock depending on length, most of it agents building shots in parallel. You are consulted at exactly four checkpoints. 
 
 Output spec 
 
 
 
 
 
 
 
 
 
 Frame / rate 
 1280×720 @ 30fps, H.264 
 
 
 Length 
 your call (see table below); 2–8 minutes all work 
 
 
 Language 
 Chinese or English ( lang in src/config.ts ); typography, subtitle budgets and TTS switch with it 
 
 
 Look 
 black canvas with one of two backdrops, star field + fog gradient or dot-field wave ( bg in src/config.ts ; the dot-field wave is ported from video-talkcraft); white line art + purple accents; ultra-bold headline type 
 
 
 Persistent layers 
 44px white-on-black-stroke subtitles, bottom chapter progress bar, top capsule HUD, optional pipeline rail 
 
 
 Voiceover 
 Chinese: edge-tts zh-CN-YunxiNeural (Yunxi, male). English: kokoro-82m am_liam (Liam, male). Or bring your own TTS / finished audio 
 
 
 
 Length drives how much ground the film covers, and the size of the whole pipeline:

 
 
 
 Length 
 Chinese chars 
 English words 
 Lines / shots 
 Build agents 
 Wall clock 
 Disk 
 
 
 
 
 2–3 min 
 700–950 
 280–420 
 24–32 
 4–6 
 ≈1 h 
 ≈2 GB 
 
 
 3–5 min (reference tier) 
 1200–1500 
 420–700 
 40–50 
 8 
 ≈2 h 
 ≈2 GB 
 
 
 5–8 min 
 1800–2400 
 700–1150 
 60–80 
 10–14 
 ≈2–3 h 
 ≈3 GB 
 
 
 
 Chapter count is not tied to length. One chapter that goes deep or several short ones both work; the progress bar splits evenly across however many chapters the narration declares.

 Install 
 git clone https://github.com/Vincentwei1021/anything2explainer.git
ln -s " $PWD /anything2explainer " ~ /.claude/skills/anything2explainer # Claude Code 
ln -s " $PWD /anything2explainer " ~ /.codex/skills/anything2explainer # Codex 
 Dependencies:

 # Node ≥18 (the template's npm install pulls remotion 4.0.507 / react 19) 
brew install ffmpeg # frame extraction / transcoding, required 

python3 -m venv ~ /.venvs/a2e && source ~ /.venvs/a2e/bin/activate
pip install ' edge-tts==7.2.8 ' numpy pillow scipy # pin edge-tts: it tracks a Microsoft endpoint and breaks across upgrades (7.2.0+ needs word boundaries requested explicitly; the script does) 

 # only needed for English narration (kokoro-82m runs locally) 
pip install kokoro soundfile && brew install espeak-ng 
 scipy is only used by the QC script frame_metrics.py . The shell scripts are zsh + Python 3, developed and verified on macOS; Linux should work, Windows is untested.

 Linux / Raspberry Pi (ARM) 
 Verified on a Raspberry Pi 5 (ARM64, Python 3.13). Three things differ from macOS:

 sudo apt install zsh espeak-ng # scripts are #!/bin/zsh; espeak-ng for kokoro/piper G2P 

 # Remotion has no linux-arm64 headless browser → point it at system Chromium: 
sudo apt install chromium # or chromium-browser 
 export REMOTION_BROWSER_EXECUTABLE=/usr/bin/chromium # read by template/remotion.config.ts (no-op on macOS) 
 TTS on Linux/ARM. kokoro (the default English engine) is hard to install on ARM/Python 3.13 (it pins an old numpy and pulls spaCy → blis, which lack aarch64 wheels). Two local engines that install cleanly instead — pass one via TTS_ENGINE :

 # kokoro_onnx — natural voice, onnxruntime (no torch/spaCy). Download model + voices from 
 # github.com/thewh1teagle/kokoro-onnx releases (kokoro-v1.0.onnx, voices-v1.0.bin) 
pip install kokoro-onnx
TTS_ENGINE=kokoro_onnx KOKORO_ONNX_MODEL=…/kokoro-v1.0.onnx KOKORO_ONNX_VOICES=…/voices-v1.0.bin \
 KOKORO_ONNX_VOICE=am_michael python3 scripts/tts_build.py

 # piper — fastest local, robotic; a Pi-native fallback. Voice .onnx from github.com/rhasspy/piper 
pip install piper-tts
TTS_ENGINE=piper PIPER_MODEL=…/en_US-ryan-medium.onnx python3 scripts/tts_build.py 
 The edge engine (natural, free, word-boundary timing) also works on Linux and needs no local model — it's a cloud call to Microsoft: TTS_ENGINE=edge VOICE=en-US-AndrewNeural python3 scripts/tts_build.py .

 Usage 
 In Claude Code or Codex, just say what you want. The skill triggers itself:

 
 Make me an explainer video about vector databases.

 
 
 讲一下向量数据库，做成一条讲解视频

 
 It then walks the 9 stages in SKILL.md :

 
 Scaffold the Remotion project from the template. 
 Research (1 agent): a sourced research doc with a list of numbers and analogies, every item with a URL. 
 Narration & timeline : the script, then TTS voiceover with per-word boundaries turned into a frame-accurate timeline and subtitle table. 
 Storyboard : one line per shot with frame range, beat, visuals, motion, hero element and lighting. 
 Overlays & primitives : title, chapter cards, HUD, pipeline rail, plus 2–5 topic-specific icons. 
 Pilot (1 agent): the first shot group, then a 30-second cut for you to judge the look. 
 Parallel build : the remaining groups, 5–7 shots per agent, each writing pure-function Remotion components. 
 Render the full film and run quantitative frame metrics. 
 QC & fixes : one QC agent per chapter, fix agents per group, re-verification, then delivery notes. 
 
 You can also drive the template by hand:

 template/scripts/new_project.sh ~ /work/my-video myslug
 cd ~ /work/my-video
 # 1. research/调研.md 2. script/narration.txt → python3 scripts/tts_build.py 
 # 3. script/storyboard_src.md → python3 scripts/render_storyboard.py 4. edit src/config.ts 
 # 5. src/shots/G1..Gn 6. scripts/preview.sh 30 (first 30 seconds) 
 # 7. VER=v1 scripts/render.sh + python3 scripts/frame_metrics.py 8. QC → fix → v2/v3 
 Four checkpoints 
 The run stops and waits for you at exactly four points instead of ploughing through (details in SKILL.md ):

 
 Length and language : before the script is written. Length decides the line count, shot count and how many agents run in parallel, i.e. how much the film can actually cover; language flips lang in src/config.ts , which drives typography, subtitle budgets and the default voice. 
 Narration sign-off : before voiceover. Once locked, frame numbers are hard-coded into every shot; changing one word re-times the whole film. This is the cheapest place to intervene. 
 Voiceover : before TTS runs you get asked whether you have a preferred engine. If not, defaults apply (edge-tts Yunxi for Chinese, kokoro-82m Liam for English). You can also hand over finished audio and fill the per-line timeline yourself. 
 First 30 seconds : only the first build group is done, then 30 seconds get rendered for you to judge the look. Fixing the style here costs one group; after the full render it costs every group. 
 
 How it compares 
 
 
 
 Tool class 
 What it produces 
 Where anything2explainer differs 
 
 
 
 
 Generative video models (Sora, Veo, Runway) 
 Footage synthesized from a prompt 
 Deterministic code, not pixels. Every number on screen traces to a source URL, and any frame can be fixed by editing one shot file 
 
 
 Avatar / presenter tools (HeyGen, Synthesia) 
 A digital presenter reading a script 
 No presenter. Motion-graphics diagrams that show the mechanism, with the narration driving the visuals 
 
 
 Remotion or Motion Canvas by hand 
 A programmable video canvas 
 Ships the method on top of the canvas: research → narration → storyboard → parallel build → QC, with style specs, motion vocabulary and a reference film to match 
 
 
 Manim 
 Python mathematical animations 
 An agent-driven end-to-end pipeline with TTS-aligned subtitles, chapters and QC; React / TypeScript rather than Python 
 
 
 
 FAQ 
 Which AI coding agents does it work with? 
It is written for Claude Code and Codex, and those two are what it has been run with. The skill itself is plain Markdown plus a Remotion project, so any agent that reads SKILL.md -style skill folders and can run shell commands should be able to 