# danyuchn/asd-ste100-skill — ASD-STE100 Simplified Technical English rules, repurposed as a Claude Code skill

- 출처: GitHub 신규 (에이전트 스킬)
- 원본 링크: https://github.com/danyuchn/asd-ste100-skill
- 발행: 2026-09-02T22:24:33.980040+00:00
- 접근상태: 확인 완료

---

GitHub - danyuchn/asd-ste100-skill: ASD-STE100 Simplified Technical English rules, repurposed as a Claude Code skill for rewriting ambiguous agent-facing English. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 danyuchn
 
 / 
 
 asd-ste100-skill 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 88 
 
 

 
 
 
 
 
 Star
 1.7k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 2 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 master Branches Tags Go to file Code Open more actions menu Latest commit   History 19 Commits 19 Commits Folders and files Name Name Last commit message Last commit date examples examples     references references     LICENSE LICENSE     README.md README.md     SKILL.md SKILL.md     View all files Repository files navigation README MIT license More items ASD-STE100 Skill — Simplified Technical English for Agent Output 
 A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructions cannot be misread.

 This skill repurposes that same discipline for a different reader: an AI agent parsing another agent's output, a tool description, an error message, or an inter-agent instruction, with no human in the loop to resolve ambiguity.

 Why STE, and Why for Agents 
 STE exists because a misread instruction on an aircraft can kill people, and the intended readers were often not native English speakers with no author to call for clarification. The standard's fix: one meaning per word, active voice, simple tenses, one instruction per sentence, short sentences, no dropped words.

 An LLM agent parsing another agent's output is in a strikingly similar position — no back-channel, no way to ask "did you mean X or Y?" The same rules that keep a mechanic from misreading a torque spec keep a downstream agent from misreading a tool description or an inter-agent message.

 Before / After 
 
 
 
 Before 
 After 
 
 
 
 
 "This tool will attempt to synchronize state across the various backends that have been configured, and if a conflict is detected it may resolve it automatically depending on the strategy that has been set, or otherwise it will surface the conflict for manual review." 
 "The tool synchronizes state across the configured backends. If it finds a conflict, it checks the current strategy. If the strategy allows automatic resolution, the tool resolves the conflict. If not, the tool reports the conflict for manual review." 
 
 
 "An error may have occurred while processing your request due to a possible mismatch in the expected data format, which could be caused by an outdated client version." 
 "The request failed. The data format did not match what the server expected. Check your client version — an outdated client is the most common cause." 
 
 
 
 More examples, including illustrations of the official STE rules themselves, in examples/before-after.md .

 What This Skill Does 
 
 Picks a mode. Strict covers procedures, error messages, and tool descriptions. STE-flavored covers READMEs, PR descriptions, and explanatory prose. STE-flavored keeps the sentence discipline but not the fixed-vocabulary lockdown. 
 Reads the input English text for meaning. 
 Flags every rule violation sentence-by-sentence: ambiguous word choice, present-perfect/complex tense, passive voice with an unclear actor, multi-instruction sentences, oversized noun clusters, dropped words, sentences over length, phrasal verbs, nominalized actions, semicolons, hedge stacks, and marketing adjectives. 
 Rewrites each flagged sentence — without dropping any fact, condition, or scope qualifier from the original. If a shorter phrasing would lose required precision, it keeps the longer phrasing and flags the trade-off instead of silently simplifying. 
 Outputs the rewritten text on its own — no preamble, no mode announcement, no change summary — plus a one-line Kept as-is: note when it deliberately left something unsimplified. 
 
 Ask for the reasoning ("show the diff", "which rules did it break") and it outputs a before/after table naming each rule instead.

 The structural rules it checks are mechanical — you can point at the word or punctuation mark that breaks each one. The rules that depend on ASD's dictionary are flagged as advisory rather than enforced, and the rules that need taste are left to you.

 It does not reproduce ASD's official ~900-word approved dictionary. The standard is free to obtain but not free to redistribute: Issue 9 permits reproduction only with ASD's written authority, or by eight listed categories of organisation that this project does not belong to. This skill applies the underlying principle (plainest available word, used the same way every time) rather than checking against a fixed word list. For certified STE-compliant documentation, use the real standard.

 Full rule summary and citations: references/writing-rules.md .

 Installation 
 Quick Install (npx skills) 
 The fastest way to install this skill is the skills CLI — no clone, no path setup. Run it from your project root:

 npx skills add danyuchn/asd-ste100-skill 
 This pulls the skill from the GitHub repo and installs it for the current project. The CLI sends anonymous install telemetry (skill name and timestamp, no personal or device information) to help rank skills on the skills.sh leaderboard. Set DISABLE_TELEMETRY=1 to opt out.

 Update later with npx skills update .

 Clone 
 git clone https://github.com/danyuchn/asd-ste100-skill ~ /.claude/skills/asd-ste100 
 This clones the repo into ~/.claude/skills/ , making the skill available in every Claude Code project. Best for contributors and anyone who wants a live checkout that updates with git pull .

 Usage 
 Trigger with a request to simplify or clarify English text:

 Disambiguate this tool description
Rewrite this error message so an agent can't misparse it
Apply ASD-STE100 to this instruction
 
 Or paste text and ask Claude to "disambiguate this" / "apply STE100 to this" / "reduce ambiguity in this output."

 You get the rewritten text back and nothing else. To see which rules were applied, add "show the diff" or "explain the changes" to the request.

 Scope 
 Built for: agent-to-agent messages, tool/function descriptions, error messages, system prompts, inter-agent instructions — any English text a machine or non-native reader has to parse without a human to ask.

 Not built for: creative writing, marketing copy, or anything where voice and nuance are the point — STE is deliberately flat and literal by design.

 One limit worth stating up front: this fixes the form of a text, not its substance. A paragraph with nothing to say comes out short, clean, and still empty.

 Sources 
 
 ASD-STE100 official site 
 ASD-STE100 — About STE 
 ASD Europe — Simplified Technical English 
 Simplified Technical English — Wikipedia 
 TechScribe — ASD-STE100 Simplified Technical English 
 
 License 
 MIT — see LICENSE .

 About ASD-STE100 Simplified Technical English rules, repurposed as a Claude Code skill for rewriting ambiguous agent-facing English.
 Resources Readme MIT license Activity Stars 1.7k stars Watchers 5 watching Forks 88 forks Report repository Releases Packages Contributors 
 




 

 

 
 

 

 
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