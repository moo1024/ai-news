# Maiao: Gerrit-style code review workflow for GitHub, GitLab, Gitea, others

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://github.com/runetes/maiao
- 발행: 2026-08-25T22:40:07+00:00
- 접근상태: 확인 완료

---

GitHub - runetes/maiao: Seamless GitHub PR management from the command-line · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 
 

 
 
 
 
 
 
 

 Uh oh!
 
 There was an error while loading. Please reload this page .




 
 
 

 








 

 

 

 
 
 
 
 
 
 
 
 
 runetes
 
 / 
 
 maiao 
 

 Public 
 
 
 forked from adevinta/maiao 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 0 
 
 

 
 
 
 
 
 Star
 57 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Pull requests 
 0 


 
 
 
 
 
 
 
 
 Actions 
 


 
 
 
 
 
 
 
 
 Projects 
 


 
 
 
 
 
 
 
 
 Security and quality 
 0 


 
 
 
 
 
 
 
 
 Insights 
 


 
 
 
 
 
 
 
 
 Additional navigation options 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Code
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pull requests
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Actions
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Projects
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Security and quality
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Insights
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu     Latest commit   History 107 Commits 107 Commits Folders and files Name Name Last commit message Last commit date .github .github     HomebrewFormula HomebrewFormula     cmd/ maiao cmd/ maiao     docs docs     pkg pkg     scripts scripts     .dockerignore .dockerignore     .gitignore .gitignore     .release-please-manifest.json .release-please-manifest.json     CHANGELOG.md CHANGELOG.md     CONTRIBUTING.md CONTRIBUTING.md     DISCLAIMER.md DISCLAIMER.md     LICENSE LICENSE     go.mod go.mod     go.sum go.sum     license_test.go license_test.go     mise.toml mise.toml     release-please-config.json release-please-config.json     View all files Repository files navigation README Contributing License More items Maiao 
 
 
 

 
 Note: This is a community fork of adevinta/maiao . The original maintainers are no longer at Adevinta and the upstream repository is no longer actively maintained. This fork continues development under runetes/maiao .

 
 Gerrit-style code review workflow for GitHub, GitLab, Gitea, Forgejo, Bitbucket Cloud, and Cursor Origin 

 Maiao brings the power of stacked pull requests (or merge requests) to your git hosting provider, enabling you to break large features into small, reviewable commits where each commit becomes its own PR/MR.

 What is Maiao? 
 Maiao provides the git review command that:

 
 Creates one PR/MR per commit in your branch 
 Stacks PRs/MRs automatically with proper parent-child dependencies 
 Registers native stacks when available (GitHub Stacks, GitLab auto-detected stacks) 
 Manages fixups elegantly using git commit --fixup 
 Tracks commits via Change-IDs (using the Gerrit commit-msg hook) 
 Auto-rebases your stack when PRs/MRs get merged 
 Auto-detects your provider from the remote URL 
 
 Supported Providers 
 
 
 
 Provider 
 PR/MR type 
 WIP/Draft 
 Native stacks 
 
 
 
 
 GitHub 
 Pull Request 
 API field 
 Yes (explicit registration) 
 
 
 GitLab 
 Merge Request 
 Draft: title prefix 
 Yes (auto-detected from target branch, up to 20 MRs) 
 
 
 Gitea 
 Pull Request 
 WIP: title prefix 
 No 
 
 
 Forgejo/Codeberg 
 Pull Request 
 WIP: title prefix 
 No 
 
 
 Bitbucket Cloud 
 Pull Request 
 Not supported 
 No 
 
 
 Cursor Origin (beta) 
 Pull Request 
 API field 
 Yes ( parentPullNumber ) 
 
 
 
 Maiao auto-detects the provider from your remote URL for known hosts ( github.com , gitlab.com , codeberg.org , bitbucket.org , origin.cursor.com ). For self-hosted instances, it prompts on first use and saves the choice to git config maiao.provider .

 Quick Example 
 # Make multiple commits 
git commit -m " Add user authentication " 
git commit -m " Add authorization middleware " 
git commit -m " Add admin endpoints " 

 # Create stacked PRs/MRs for all commits 
git review 
 Result : Three PRs/MRs created and stacked:

 
 PR #1: Add user authentication → main 
 PR #2: Add authorization middleware → PR #1 
 PR #3: Add admin endpoints → PR #2 
 
 Key Benefits 
 
 Granular Reviews : Each commit reviewed independently for faster, focused feedback 
 Clear History : One logical change per PR/MR maintains clean git history 
 Easy Fixups : Address review feedback with git commit --fixup <sha> 
 Automatic Stacking : Tool manages PR/MR dependencies automatically 
 Native Stacks : Integrates with GitHub Stacks and GitLab's auto-detected stacks 
 Merge Detection : Stack updates automatically when PRs/MRs merge 
 Rebase Integration : Handles upstream changes gracefully 
 Multi-Provider : Works across GitHub, GitLab, Gitea, Forgejo, Bitbucket Cloud, and Cursor Origin 
 
 Native GitHub Stacks 
 Maiao treats GitHub native stacks as a progressive enhancement. When two or more PRs are pushed, Maiao probes the Stacks API (cached for 24 hours) and registers the PRs as a stack if supported. On older GitHub Enterprise instances the feature is silently skipped — branch-based stacking still works as before.

 # Control via git config (default: auto) 
git config maiao.useNativeStack auto # use when available, skip otherwise 
git config maiao.useNativeStack true # always register; warn if unavailable 
git config maiao.useNativeStack false # disable entirely 
 Documentation 
 
 Getting Started - Installation and workflow guide 
 How Does It Work - Technical details and architecture 
 Pricing - Free and open source 
 
 Learn About Stacked Diffs 
 Maiao implements the stacked diffs methodology. Learn more:

 
 Stacked Diffs Versus Pull Requests - Jackson Gabbard's foundational article on the philosophy 
 Graphite's Guide to Stacked Diffs - Comprehensive guide to the workflow and best practices 
 The Pragmatic Engineer: Stacked Diffs - Industry analysis and adoption patterns (paywalled) 
 
 Why "Maiao"? 
 As Maiao encourages users to create smaller and nicer commits in their pull requests, it has been given the name of a tiny island:

 

 Contributing 
 Contributions are welcome! See CONTRIBUTING.md for details.

 License 
 MIT License - see DISCLAIMER.md for details.

 About Seamless GitHub PR management from the command-line
 Resources Readme License Contributing Contributing Activity Custom properties Stars 57 stars Watchers 0 watching Forks 0 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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