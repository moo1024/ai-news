# s1dashu/ip-as-logo-skill — A compact Agent Skill for highly simplified, rounded, subtly neo-skeuomorphic IP

- 출처: GitHub 신규 (에이전트 스킬)
- 원본 링크: https://github.com/s1dashu/ip-as-logo-skill
- 발행: 2026-08-19T22:24:39.770046+00:00
- 접근상태: 확인 완료

---

GitHub - s1dashu/ip-as-logo-skill: A compact Agent Skill for highly simplified, rounded, subtly neo-skeuomorphic IP mascot logos. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 s1dashu
 
 / 
 
 ip-as-logo-skill 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 90 
 
 

 
 
 
 
 
 Star
 2k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 3 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 23 Commits 23 Commits Folders and files Name Name Last commit message Last commit date assets assets     .gitignore .gitignore     LICENSE LICENSE     README.md README.md     SKILL.md SKILL.md     View all files Repository files navigation README MIT license More items IP as Logo 
 ip-as-logo is a compact Agent Skill for generating highly simplified company-ready mascot logos. It treats the result as a logo first and a character second: familiar cute animals by default, bold rounded silhouettes, strict complexity limits, oversized corner composition, and extremely subtle neo-skeuomorphic shading.

 It follows the open Agent Skills format and is designed to work with any compatible AI agent, rather than being tied to a specific agent product.

 You can also browse the free IP as Logo Skill website , a searchable library backed by Cloudflare R2 and Supabase.

 

 Don't have Codex, Doubao, Coze, or Workbuddy? Visit our website to download ready-made logos for free. Every logo is free for commercial use.

 What it enforces 
 
 One dominant silhouette built from roughly 6–10 basic shapes 
 Three semantic colors by default: two IP base colors plus one background color 
 Three proposed directions followed by six independently generated candidates after user approval 
 Familiar, broadly appealing animals as the default open-ended subject; objects, machines, fantasy artifacts, and obscure creatures require a clear product reason 
 A quantified restrained-color default: softened chromatic backgrounds, warm neutrals, and explicit silhouette/detail contrast targets 
 Thick, rounded forms without sharp or fragile details 
 An 82–90% close crop that visibly peeks or rises from the lower-left or lower-right, with paired identifying features preserved 
 Flat-first artwork with continuous low-frequency gradients capped at 0.08 OKLCH lightness span 
 Opaque square output without an App-icon mask, border, or transparent margin 
 Explicit rejection rules for illustration-level complexity, pure flatness, and excessive 3D volume 
 
 Install 
 Install the complete skill with the Agent Skills CLI:

 npx skills@latest add s1dashu/ip-as-logo-skill 
 The installer detects the repository's root SKILL.md , lets you choose a supported coding agent, and installs the complete ip-as-logo directory, including its supporting assets. Use --global for a personal installation available across projects:

 npx skills@latest add s1dashu/ip-as-logo-skill --global 
 Agent compatibility 
 Supported agents include Codex, Coze, Doubao, YouMind, Manus, Gemini Apps, and Replit Agent . This skill only supports agents with built-in image-generation capabilities that can return generated images as assets.

 Use 
 Ask your AI agent for an IP mascot logo, for example:

 Create a rounded ghost IP logo on a deep navy background.
 
 The skill does not ask for a color-mode choice by default. Every default candidate uses three semantic colors: two IP base colors plus one background color. It no longer reserves any fraction of the candidate set for two-color logos. Closely related highlight and shade variants may be introduced around either IP base color for the ultra-light neo-skeuomorphic effect without counting as additional semantic colors. A two-color logo is generated only when the user explicitly requests it, and then uses background-colored negative space for facial marks rather than introducing a third color.

 When the user already names an IP subject, the skill proposes three controlled design treatments of that subject. When the subject is open, it proposes familiar animal mascots first and ties each to a product attribute or brand promise. In open-ended batches, 95–100% of candidates should be familiar animals; non-animal subjects are limited to a small minority with a direct product connection, never used merely to manufacture novelty.

 Large batches create variety within commercially plausible animal mascots through species or breed, ear and muzzle proportions, expression, lower-left versus lower-right emergence, crop, silhouette, and secondary color organization. Clocks, locks, industrial tools, measuring instruments, vehicles, abstract machines, fantasy artifacts, and obscure creatures are not default company mascots.

 If the skill runs inside a product repository, it inspects relevant read-only context before asking questions. If product context is insufficient, it asks one consolidated round of background questions. Once context is sufficient, it always presents three concise directions and proposes generating six independent images. It proceeds after the user agrees, or immediately when the user has already explicitly authorized six outputs.

 When the user accepts all three directions, the default batch contains two variants per direction: A1 , A2 , B1 , B2 , C1 , and C2 . When the user selects one direction, the skill generates six controlled variants of that direction. If the user rejects the proposed quantity or distribution, their replacement instructions take precedence.

 Compatible agents may generate the six candidates in parallel with subagents up to the runtime's available concurrency, using additional waves when needed. Codex can use ImageGen when available; other agent environments may use any configured image generator. If no generator is available, the skill asks the user to provide or enable one instead of pretending that an image was generated. Every result is a separate full-resolution square asset, never a six-logo contact sheet.

 When the user does not supply a palette, the skill favors clearly chromatic but restrained backgrounds rather than neon color or muddy gray. It uses OKLCH target bands when numeric control is available, prefers warm off-white with charcoal or deep navy, and keeps the normal design to exactly three semantic colors: two IP base colors plus the background. Ultra-light highlight and shade variants must remain close to their corresponding IP base color.

 Repository structure 
 SKILL.md
assets/ip-as-logo-wall.webp
README.md
LICENSE
 
 The skill itself intentionally consists of a single instruction document. The repository also includes the showcase image above, but no scripts, style references, or generation dependencies.

 Model behavior 
 Image-generation models may still introduce background gradients, crop paired features, replace continuous micro-gradients with layered color patches, or add too much volume. The skill treats those as failures to report or retry, rather than silently claiming compliance or repairing the image after generation.

 License 
 MIT

 About A compact Agent Skill for highly simplified, rounded, subtly neo-skeuomorphic IP mascot logos.
 ip-as-logo-skill.vercel.app Topics codex codex-skill image-generation logo-design mascot-design Resources Readme MIT license Activity Stars 2.0k stars Watchers 1 watching Forks 90 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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