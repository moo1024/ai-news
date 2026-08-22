# Leutenegger/book-to-skill — Turn any technical book PDF into a Claude Code skill — ready to study, reference

- 출처: GitHub 신규 (AI 에이전트)
- 원본 링크: https://github.com/Leutenegger/book-to-skill
- 발행: 2026-08-22T03:54:40.404536+00:00
- 접근상태: 확인 완료

---

GitHub - Leutenegger/book-to-skill: Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 Leutenegger
 
 / 
 
 book-to-skill 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 144 
 
 

 
 
 
 
 
 Star
 1.2k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 2 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 2 Commits 2 Commits Folders and files Name Name Last commit message Last commit date book_to_skill book_to_skill     docs docs     overrides overrides     scripts scripts     tests tests     tools tools     ui ui     BACKERS.md BACKERS.md     CHANGELOG.md CHANGELOG.md     CONTRIBUTING.md CONTRIBUTING.md     LICENSE.md LICENSE.md     README.md README.md     SECURITY.md SECURITY.md     SKILL.md SKILL.md     cliff.toml cliff.toml     launch.py launch.py     mkdocs.yml mkdocs.yml     pyproject.toml pyproject.toml     View all files Repository files navigation README Contributing MIT license Security More items 
 


 book-to-skill 
 
 Turn any technical book, document folder, or collection of sources into a unified agent skill — ready to study, reference, and use while you work in GitHub Copilot CLI, Amp, or Claude Code. 


 
 
 
 


 
 Why ·
 What it generates ·
 Beyond books ·
 How it works ·
 Usage ·
 Install ·
 FAQ ·
 Performance ·
 Changelog 


 
 24×–51× fewer tokens than dumping the book into context to answer one question, measured on real books.


 
 pip install -e . 

 book-to-skill install 

 book-to-skill <path-to-book.pdf> 


 How it works, in 3 steps: 

 
 Point it at a file, folder, or glob — book-to-skill ./my-book.pdf 
 It distills the book into a skill — frameworks, decision rules, anti-patterns, and per-chapter files. Structure, not a summary. 
 Your agent loads it on demand — ask /my-book replication and it reads the right chapter and answers from the real content, no hallucination. 
 
 
 Install 
 As agent skill (recommended): 

 pip install - e .
book - to - skill install 
 Copies the skill into ~/.claude/skills/book-to-skill , ~/.agents/skills/book-to-skill , ~/.copilot/skills/book-to-skill (and related paths).

 Convert a book: 

 book - to - skill path\to\book.pdf
book - to - skill " path\to\docs\*.epub " my - skill - slug
book - to - skill -- check 
 Other commands: 

 book - to - skill help
book - to - skill list
book - to - skill readme
book - to - skill ui 
 On the first two CLI runs (if ui/book-to-skill-ui.zip is present), the GUI is unpacked and launched automatically with cwd = ui/ . After that it stays quiet. Force with book-to-skill ui .

 Manual skill install (any host):

 git clone https://github.com/Leutenegger/book-to-skill.git ~ /.claude/skills/book-to-skill
 # Copilot CLI: ~/.copilot/skills/ 
 # Amp / cross-agent: ~/.agents/skills/ 
 
 Why 
 You buy a great technical book. You read it once. Three months later you can't remember chapter 7 existed.

 The usual workarounds don't help:

 
 "Let me just search the PDF" → you get a list of pages, not answers 
 "I'll ask the agent about this book" → it either hallucinates or says it doesn't have the content 
 "I'll take notes as I read" → you end up with a 200-line doc you never open again 
 
 book-to-skill solves this by turning the book into a structured skill your agent loads on demand. 

 Once installed, type /your-book-slug replication and the agent reads the right chapter and answers from the actual content. No hallucination. No digging through PDFs.

 Works with any host that supports the open Agent Skills standard — GitHub Copilot CLI, Amp, and Claude Code all read the same SKILL.md format.

 
 What it generates 
 Running book-to-skill your-book.pdf (or a folder, glob, or list of files) creates a full skill in your agent's skills directory:

 
 
 
 File 
 Purpose 
 Size 
 
 
 
 
 SKILL.md 
 Core mental models + chapter index 
 ~4,000 tokens 
 
 
 chapters/ch01-*.md … 
 One file per chapter, loaded on-demand 
 ~1,000 tokens each 
 
 
 glossary.md 
 Key terms with chapter refs 
 ~1,500 tokens 
 
 
 patterns.md 
 Techniques, algorithms, design patterns 
 ~2,000 tokens 
 
 
 cheatsheet.md 
 Decision tables and quick-reference rules 
 ~1,000 tokens 
 
 
 
 Chapter files are loaded on-demand — they don't count against the skill budget until you ask about that topic.

 
 Beyond books 
 The name says "book", but the input is any structured prose:

 
 Internal documentation — ADRs, runbooks, onboarding guides 
 Brand & design systems — voice guidelines, component principles 
 Research clusters — papers + notes, updated as new material lands 
 Specs & standards — RFCs, API contracts, compliance docs 
 
 If you re-open a document often enough to wish you'd memorized it, it's a candidate.

 
 How it works 
 Two halves: a deterministic Python extractor (document → clean text + metadata) and a spec-driven generator (your agent follows SKILL.md to turn that into a structured skill). On-demand chapter files keep the loaded skill small.

 Full walkthrough → docs/how-it-works.md 

 
 Usage 
 book-to-skill <path|folder|glob> [skill-name]
 
 Plus analyze-only, generate-from-analysis, and update/fold-in modes.

 All modes and examples → docs/usage.md 

 
 Requirements 
 The extractor tries tools in order per format and uses the first available. Plain text, Markdown, reStructuredText and AsciiDoc need no extra deps.

 book - to - skill -- check 
 PDF: 

 
 
 
 Book type 
 Tool 
 Install 
 
 
 
 
 Text-heavy 
 pdftotext (poppler) / pypdf / pdfminer.six 
 system / pip 
 
 
 Technical (code, tables) 
 docling 
 pip install docling 
 
 
 
 EPUB: ebooklib + beautifulsoup4 (or stdlib zipfile fallback)

 DOCX / HTML / RTF: optional pip packages, stdlib fallbacks available

 MOBI / AZW: Calibre ebook-convert 

 Scanned PDFs need OCR first ( ocrmypdf input.pdf output.pdf ).

 Optional extras:

 pip install " book-to-skill[all] " 
 
 Copyright & fair use 
 book-to-skill ships no book content . It's a converter you point at files you already own.

 
 Processing is local. Your files are never uploaded by this tool. 
 Use your own copy (bought book, company docs, papers you have the right to read). 
 The output is structured notes — frameworks, definitions, takeaways — not a reproduction of the text. 
 Don't redistribute generated skills of copyrighted works. 
 
 
 License 
 MIT — applies to the converter (code + skill definition) in this repository, not to any book or document you process with it.

 Based on the original book-to-skill by virgiliojr94.

 About Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work.
 Topics agent agent-memory agent-skill agent-skills agentic agentic-ai agents ai-agents claude claude-code claude-code-plugin claude-skills github-copilot pdf pdf-document pdf-generation pdf-parser pdf-tools pdf-viewer skill-generator Resources Readme MIT license Contributing Contributing Security policy Security policy Activity Stars 1.2k stars Watchers 500 watching Forks 144 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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