# Alisa0808/vox-director — Turn one topic into a finished Vox-style paper-collage explainer/ad video — auto

- 출처: GitHub 신규 (에이전트 스킬)
- 원본 링크: https://github.com/Alisa0808/vox-director
- 발행: 2026-08-19T03:45:28.294035+00:00
- 접근상태: 확인 완료

---

GitHub - Alisa0808/vox-director: Turn one topic into a finished Vox-style paper-collage explainer/ad video — automated end to end on Atlas Cloud + ffmpeg. An agent skill. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 Alisa0808
 
 / 
 
 vox-director 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 194 
 
 

 
 
 
 
 
 Star
 1.4k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 0 


 
 
 
 
 
 
 
 
 Pull requests 
 1 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 29 Commits 29 Commits Folders and files Name Name Last commit message Last commit date assets assets     examples examples     references references     scripts scripts     .gitignore .gitignore     AGENTS.md AGENTS.md     LICENSE LICENSE     README.md README.md     README.zh.md README.zh.md     SKILL.md SKILL.md     SKILL.zh.md SKILL.zh.md     llms.txt llms.txt     package.json package.json     vox-director.skill vox-director.skill     View all files Repository files navigation README MIT license More items English · 简体中文 

 🎬 Vox Director 
 Turn one topic into a finished Vox-style paper-collage explainer / ad video — script, collage keyframes, motion, voice-over, music and captions, all automated. 

 An agent skill that runs end to end on the Atlas Cloud API + local ffmpeg , usable by any coding agent (Claude Code, Codex, etc.). You give it a one-line topic; it gives you an mp4 .

 

 
 
 
 
 
 
 showcase-tang.mp4 
 
 

 

 
 

 ▶ "The evolution of Chinese civilization" · 30s 

 
 
 
 
 
 
 
 
 
 Football history · 60s 
 Mexican street food · 60s 
 A brief history of money · 60s 
 Silicon Valley history · 60s 
 
 
 ▶ more films — click any thumbnail to play 

 
 What it is 
 The look is the modern editorial paper-collage popularized by Vox explainers: hand-cut paper cut-outs, torn edges, tape, halftone dots, newspaper clippings, bold flat color per beat, big cut-out headlines — brought to life with motion, a narrator, music and captions.

 How it works 
 One topic flows through one script per stage, all driven by a single beats.json per project:

 topic
 │
 ├─ 1. beat map pick a narrative arc → write beats.json ◀── GATE 1: you approve the beat map
 ├─ 2. style bake-off render the same beat in 3–4 themes ◀── GATE 2: you pick the look by eye
 ├─ 3. keyframes one collage poster per beat (nano-banana-2)
 ├─ 4. motion animate each poster (gemini-omni-flash i2v)
 ├─ 5. voice + music one narrator (xai/tts) + BGM (minimax/music)
 ├─ 6. assemble ffmpeg: concat, duck music under VO, burn captions + watermark
 └─ final.mp4
 
 That flow is B-roll — a topic in, everything generated. Two more input modalities reuse the same engine:

 
 A-roll — you already have a talking-head video. It is ASR-segmented into beats and re-styled into the collage look, keeping the real face, lip-sync and gestures frame-for-frame ( gemini-omni-flash/video-edit , auto-retrying on seedance-2.0/reference-to-video ). 
 C-roll — you have one still photo (a selfie, a product shot). The subject is cut out as a photographic sticker — never redrawn — and each beat's poster is generated around it ( nano-banana-2/edit ). The narration can be cloned into the subject's own voice. 
 
 Two ideas make or break the result, and the skill is built around both:

 
 The look is born in the image step. Each beat is a finished collage poster . All the collage DNA (torn paper, cut-outs, halftone, headline text) lives in that image — if the poster isn't a rich collage, nothing downstream saves it. 
 The motion is added after. By default an AI video model animates the whole poster (the "living poster" path). For dramatic piece-by-piece assembly, an optional local keyframe engine cuts the poster into parts and drives them frame-by-frame (no content filters, pixel-exact — great for real people). 
 
 Two human decision gates keep you in control (approve the beat map; pick the style); everything else is automated.

 Models (verified on Atlas Cloud) 
 
 
 
 Job 
 Model 
 
 
 
 
 Keyframe / collage poster 
 google/nano-banana-2/text-to-image 
 
 
 Animate (non-real content) 
 google/gemini-omni-flash/image-to-video 
 
 
 Animate ( real people / brands ) 
 kwaivgi/kling-video-o3-pro/image-to-video 
 
 
 Re-style a talking-head (A-roll) 
 google/gemini-omni-flash/video-edit 
 
 
 Anchor a photo in the collage (C-roll) 
 google/nano-banana-2/edit 
 
 
 Narration 
 xai/tts-v1 
 
 
 Narration in a real person's voice 
 bytedance/seed-audio-1.0 (voice cloning) 
 
 
 Music 
 minimax/music-2.6 
 
 
 Cut out an element (advanced path) 
 youchuan/v8.1/remove-background 
 
 
 
 Model IDs drift — the skill fetches the live list from GET https://api.atlascloud.ai/api/v1/models before running.

 Install 
 This is an agent skill — it works with any coding agent that can read a workflow and run scripts (Claude Code, Codex, …). Claude Code auto-discovers it as a skill; other agents read AGENTS.md → SKILL.md .

 Option A — from this repo: 

 git clone https://github.com/Alisa0808/vox-director.git ~ /.claude/skills/vox-director 
 Option B — from the packaged skill: download vox-director.skill and install it via your Claude skills UI.

 Then set your Atlas Cloud API key (get one at atlascloud.ai/console/api-keys ):

 export ATLASCLOUD_API_KEY= " sk-... " 
 Quick start 
 Just ask your coding agent, with the skill installed:

 
 "Make me a Vox-style collage video introducing Mexican street food — English, 16:9, 15 seconds." 

 
 The agent will draft a beat map for your approval, run a style bake-off for you to pick from, then generate keyframes → motion → voice → music and assemble out/<project>/final.mp4 .

 Requirements 
 
 A coding agent — Claude Code, Codex, or similar 
 Atlas Cloud API key 
 ffmpeg + ffprobe ( brew install ffmpeg ) 
 Python 3 with Pillow ( pip install pillow ) — for caption/watermark overlays 
 
 What's in the box 
 SKILL.md the skill (English) — the workflow the agent follows
SKILL.zh.md the same skill in Chinese
AGENTS.md entry point for non-Claude agents (Codex, …)
references/ the creative engine
 prompt-guide.md the LOOK layer — prompt structures, vocab & 9 theme presets
 beat-layer.md 14 narrative arcs + hook/pacing + shot patterns
 voices.md xai/tts voice roster — pick a voice_id per language/tone
 models-and-gotchas.md every API / ffmpeg gotcha, already solved
 local-engine.md the advanced element-level motion engine
scripts/ one script per pipeline stage
examples/ ready-to-run beats.json examples
assets/ the showcase film
 
 Credits 
 Built by @alisaqqt — follow for more agent-skill experiments.

 Inspired by the collage-ad workflows of Stav Zilber , rom1trs and Higgsfield , and by Vox 's explainer visual language.

 Built end to end on Atlas Cloud — one prompt, one film.

 License 
 MIT © 2026 Alisa Qian

 About Turn one topic into a finished Vox-style paper-collage explainer/ad video — automated end to end on Atlas Cloud + ffmpeg. An agent skill.
 Topics ai ai-video claude-code claude-skill collage-video dsh-plugin explainer-video ffmpeg generative-ai llm motion-graphics python text-to-video tts video video-generation vox Resources Readme MIT license Activity Stars 1.4k stars Watchers 8 watching Forks 194 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
 Footer 

 


 
 
 
 
 
 
 
 
 © 2026 GitHub, Inc.
 
 

 
 Footer navigation 

 


 
 Terms 
 

 
 Privacy 
 

 
 Security 
 

 
 Status 
 

 
 Community 
 

 
 Docs 
 

 
 Contact 
 

 
 
 
 Manage cookies
 
 
 

 
 
 
 Do not share my personal information
 
 
 

 
 
 
 



 




 
 
 
 
 
 
 
 
 
 You can’t perform that action at this time.