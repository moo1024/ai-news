# lennney/stop-that-shit — Stop That Shit（别再造史了）｜面向 Codex/GPT 场景的多平台 Hook + Skill Guard：拦截 AI coding agent

- 출처: GitHub 신규 (에이전트 스킬)
- 원본 링크: https://github.com/lennney/stop-that-shit
- 발행: 2026-09-10T22:30:10.227035+00:00
- 접근상태: 확인 완료

---

GitHub - lennney/stop-that-shit: Stop That Shit（别再造史了）｜面向 Codex/GPT 场景的多平台 Hook + Skill Guard：拦截 AI coding agent 无需求的哈希、校验和与任务范围膨胀。 A multi-platform Hook + Skill Guard for AI coding agents in Codex/GPT workflows: stop unrequested hashes, checksums, and task-scope creep. · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 lennney
 
 / 
 
 stop-that-shit 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 47 
 
 

 
 
 
 
 
 Star
 1.9k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 4 


 
 
 
 
 
 
 
 
 Pull requests 
 2 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 60 Commits 60 Commits Folders and files Name Name Last commit message Last commit date .agents/ plugins .agents/ plugins     .claude-plugin .claude-plugin     .codex-plugin .codex-plugin     .github .github     .hermes-plugin .hermes-plugin     assets assets     cases cases     evals evals     hooks hooks     opencode opencode     pi pi     schemas schemas     scripts scripts     skills skills     src src     test test     .codexignore .codexignore     .gitignore .gitignore     ARCHITECTURE.md ARCHITECTURE.md     CHANGELOG.md CHANGELOG.md     CONTRIBUTING.md CONTRIBUTING.md     EVIDENCE.md EVIDENCE.md     HOST-ADAPTER-CONTRACT.md HOST-ADAPTER-CONTRACT.md     INSTALL.md INSTALL.md     INSTALL_FOR_AGENTS.md INSTALL_FOR_AGENTS.md     LICENSE LICENSE     PRIVACY.md PRIVACY.md     README.md README.md     README_CN.md README_CN.md     README_EN.md README_EN.md     SECURITY.md SECURITY.md     package-lock.json package-lock.json     package.json package.json     release-files.json release-files.json     View all files Repository files navigation README Contributing MIT license Security More items 
 


 Stop That Shit（别再造史了） 
 
 
 
 


 
 把活干完。把多余的停下。 


 
 Skill + Guard，帮 AI coding agent 停止无用防御和任务越界。

 Codex · Claude Code · OpenCode · Hermes Agent CLI · Pi

 SHIT 哲学 ·
 看个例子 ·
 安装 ·
 案例库 ·
 English 


 
 你只让 Agent 导出一个文件，它顺手算了份没人读取的 SHA-256，说是“以防万一”。

 你让它 Review，它找到问题就开始改。你让它修一个点，它又想重构旁边的模块。检查已经回答了当前问题，它还想再拉一个 Agent，“最后确认一下”。

 理由一个比一个严谨。东西还没交付，token 已经花了一截，你还得盯着它，别让任务继续跑偏。

 活还没拿到，我先当上了 Agent 的监工。 

 我也试过往 AGENTS.md 里补规则：“不要乱改”“别过度设计”“没让我做的先别做”。每气一次就补一条，写着写着， AGENTS.md 自己也开始造史了。

 Stop That Shit。别再造史了。 该干的干完整，没用的别往上堆。

 SHIT 是哪四种 
 我们把这些行为叫作 SHIT：

 
 S — Scope creep，范围膨胀。 修一个问题，顺手重构无关模块。必要的调用方、数据迁移和测试要一起处理；没有当前用途的扩展就停下。 
 H — Hashing & hypothetical hardening，无用防御。 没人读取的 checksum、为想象中的未来搭的兼容层。防御要能发现问题，并触发拒绝、恢复或诊断。有效的保留，无用的省掉，吞错报成功或制造重复副作用的修好。 
 I — Intent violation，意图越界。 说了只读 Review，文件还是被改了。审查就报告问题，修改需要授权。用户划的边界必须算数。 
 T — Task thrashing，任务打转。 没有新问题或变化，读过、测过、审过的又来一遍。能回答当前问题的证据就复用；代码或验收条件变了，再补相关验证。做完、验证充分，就结束。 
 
 把当前责任承担完整，让复杂度随真实需要增长。 需要多改几个文件、补齐迁移或跑跨组件测试，就做完整。

 前后对比 
 下游只读取 report.csv ，没有发布校验，摘要也没有其他用途。导出逻辑却写成了这样：

 await writeFile ( "report.csv" , csv ) ; 
 await writeFile ( "report.csv.sha256" , createHash ( "sha256" ) . update ( csv ) . digest ( "hex" ) ) ; 
 按 STS 的判断，保留：

 await writeFile ( "report.csv" , csv ) ; 
 这个简化示例省掉了无用校验和，文件照常交付。更多场景见 案例库 。

 如果发布流程会读取 checksum，并在不一致时拒绝使用文件，就保留，用 hash=allow 放行。

 必要的工作要做全。 修复配置迁移时，旧数据已经发布且仍需支持，就把迁移、读写双方和兼容性测试一起补齐。哪怕 diff 更大，也不能留下坏掉的调用方。

 验证到了什么 
 公开的 18 个 Bad/Good 判定用例，检查规则能否停下多余动作、保留必要工作，覆盖只读审查、必要调用方、已发布数据迁移、发布校验和，以及文件、依赖和 subagent 边界。模型在真实任务中的表现另看对照运行。

 完整证据 记录测试、历史 Codex / GPT-5.6 运行和没有差异的结果；复现方法见 对照测试说明 。

 它怎么判断 
 遇到这些 SHIT，先读相关代码、查清调用链，再按顺序判断：

 1. 当前要交付什么？ → 明确结果、授权和已有支持承诺
2. 已有能力够用吗？ → 从直接可用的方案开始
3. 还有什么具体缺口？ → 补齐现在需要的行为和保障
4. 这层防御起什么作用？ → 保留有效的，省掉无用的，修正有害的
5. 结果验证完成了吗？ → 没有范围内阻塞，就结束
 
 先看已有代码、标准库、平台原生能力和已安装依赖。符合所需行为和状态生命周期的就用，有具体缺口再加机制。

 新机制说不清用途，可以暂缓；已有保护用途不明，先查清再动。真实的信任边界和已有支持承诺，都足以说明保护的必要，不必等事故发生。

 代码行数、文件数量和检查次数不能代替判断。 完整规则 。

 快速安装 
 一般宿主需要 Node.js 18+；Pi 0.84.4 自身要求 Node.js 22.19+。完整安装说明见 INSTALL.md 。

 展开你使用的宿主。只想用规则、不需要执行拦截，可以 只装 Skill 。

 
 Claude Code 
 下载并解压 0.2.1 源码 ，在仓库根目录执行：

 claude plugin validate . 
claude plugin marketplace add ./
claude plugin install stop-that-shit@stop-that-shit 
 重启 Claude Code 或执行 /reload-plugins ，然后使用：

 /stop-that-shit:stop-that-shit review -- Review 这个 diff，只报告问题，不要修改。
 
 
 
 Codex 
 codex plugin marketplace add lennney/stop-that-shit --ref 0.2.1
codex plugin add stop-that-shit@stop-that-shit 
 --ref 0.2.1 把安装固定到版本 tag，不跟随可变的 main 。重启 Codex。在新的 CLI TUI 中输入 /hooks ，检查命令后信任 UserPromptSubmit 和 PreToolUse 。也可以把 INSTALL_FOR_AGENTS.md 交给 Codex，让它完成非交互步骤。

 
 
 OpenCode 从 GitHub 安装 
 OpenCode 1.18.18 或更高版本可以全局安装这个仓库，无需 clone：

 opencode plugin github:lennney/stop-that-shit -g 
 重启 OpenCode 后用 $stop-that-shit review -- ... 设置契约。该命令安装 Guard；内置 Skill 和可选 /sts 别名不会自动注册。详见 INSTALL.md 。

 
 
 Hermes Agent CLI 
 需要 Node.js 18+。

 hermes plugins install lennney/stop-that-shit/.hermes-plugin --no-enable 
hermes plugins enable stop-that-shit
hermes plugins list 
 启用后，CLI 用户需要启动新的 Hermes CLI 进程或会话；Gateway 用户需要执行：

 hermes gateway restart 
 这些操作不需要每次使用插件时重复。只有启用、禁用、更新、回滚或重装插件后，
才需要重启对应的 Hermes 进程。

 
 
 Pi Coding Agent 
 当前适配固定验证 @earendil-works/pi-coding-agent 0.84.4 。从包含该
Adapter 的本地 checkout 安装：

 pi install /absolute/path/to/stop-that-shit 
 启动新的 Pi 进程，或修改资源后在 TUI 执行 /reload 。然后使用：

 /skill:stop-that-shit review -- Review 这个 diff，只报告问题，不要修改。
 
 从 0.2.1 tag 安装即可获得 Pi Adapter 和两个 Skill。详见 INSTALL.md 。

 
 使用 
 在 Codex 或支持宿主无关指令的 prompt 中，先说清这次要做什么：

 $stop-that-shit review -- Review 这个 diff，只报告问题，不要修改。
$stop-that-shit change -- 修复配置读取失败，补齐受影响的调用方和检查。
 
 Claude Code 插件用 /stop-that-shit:stop-that-shit ，Pi Skill 用 /skill:stop-that-shit 。

 
 
 
 指令 
 用途 
 
 
 
 
 review 
 审查并报告问题 
 
 
 answer 
 回答问题 
 
 
 monitor 
 持续检查和报告 
 
 
 change 
 允许完成任务需要的修改 
 
 
 watch 
 观察动作，不阻断 
 
 
 status / runtime 
 查看当前状态和本地记录 
 
 
 
 需要更具体的边界时，加上参数：

 $stop-that-shit lock change files=src/config.cjs|test/config.test.cjs -- 修复这个行为。
$stop-that-shit change deps=allow -- 添加我要求的解析器依赖。
$stop-that-shit change hash=allow -- 生成发布流程需要的校验和。
$stop-that-shit change agents=1 -- 使用一个独立测试 subagent。
 
 还不知道全部受影响文件，就别急着锁 files= 。先沿调用链查清楚。

 红章管到哪里 
 Skill 负责工程判断。Guard 在受支持的工具调用前检查明确边界：

 
 
 
 动作 
 Guard 启用后的默认处理 
 
 
 
 
 在 review 、 answer 或 monitor 中写文件 
 停止 
 
 
 添加依赖 
 询问； deps=allow 放行 
 
 
 启动 subagent 
 超出 agents=N 预算时停止 
 
 
 添加可识别的 hash 操作 
 停止； hash=allow 放行 
 
 
 写入 files= 之外的路径 
 停止 
 
 
 
 Guard 不会看到 cache 、 retry 或 migration 就替你断定它们多余。宿主事件如何接入，见 Adapter 合同 。

 可选：Stop That Shit Slop（别再废话） 
 Agent 活干完了，嘴还没停。STSS 删掉无用辩护、收紧重复犹豫，保留影响决定的条件。这是固定离线案例中的一组：

 输入：我们也许大概有可能在六到八周内完成迁移，具体取决于访问审批。
输出：预计六到八周完成迁移，前提是获得访问审批。
 
 时间范围和审批条件都保留。如果审批必须在工作开始前完成，就应明确写成“获得审批后，预计需要六到八周”。

 完整插件包含 STSS；它也可以单独安装，不需要 Hook。在仓库根目录执行：

 npx skills add ./skills/stss --global 
 rewrite 改写文本，也是贴出文本时的默认模式； audit 只报告问题和最小修改建议。

 
 
 
 宿主 
 改写 
 审核 
 
 
 
 
 Codex 
 $stss rewrite -- 把这个提案写直接。 
 $stss audit -- 找出防御性废话。 
 
 
 Claude Code 插件 
 /stop-that-shit:stss rewrite -- ... 
 /stop-that-shit:stss audit -- ... 
 
 
 Claude Code 单独 Skill 
 /stss rewrite -- ... 
 /stss audit -- ... 
 
 
 Pi 
 /skill:stss rewrite -- ... 
 /skill:stss audit -- ... 
 
 
 
 完整方法见 STSS Skill ，六组案例和必须保留的反例见 STSS examples 。

 FAQ 
 所以 checksum 都该删？ 

 发布完整性校验、去重、跳过重复处理，都可以是实际用途。对照可信来源给出的预期摘要，发现文件不一致就拒绝使用，即使多算一次也值得。需要做就用 hash=allow 放行。Guard 检查授权，具体用途仍要根据任务判断。

 刚装上，为什么还没拦？ 

 安装后默认是 OBSERVING / unconfirmed 。显式使用 review 、 answer 、 monitor 或 change 后，Guard 才进入 ARMED 。 watch 始终只观察。只装 Skill 则没有执行拦截。

 红章是不是说明动作绝对没执行？ 

 permission_deny_returned （OpenCode 为 execution_denial_returned ）表示 Guard 返回了拒绝响应。宿主最终是否执行要单独观测，所以 Runtime 将其记为 hostEffect: unobserved 。安全隔离由宿主 sandbox 负责。

 会保存我的代码和对话吗？ 

 本地 Runtime 只保存任务边界状态和元数据记录，不保存代码或对话正文。详见 PRIVACY.md 。

 怎么更新、卸载或参与开发？ 

 见 更新检查 、 停用与卸载 、 本地开发 和 更新记录 。

 把反例发过来 
 Agent 又造史了？ 提交 Bad Case 。

 STS 拦住了真正必要的工作？ 提交 Good Case 。这个同样重要。

 说清你的请求、它多做或少做了什么，以及哪个事实会改变判断。参考 案例库 ，脱敏和复现方法见 贡献指南 。

 我不想再往 AGENTS.md 里补一百条“不要”，只希望新案例能让下一次判断更准。

 觉得有用，给个 Star 。也欢迎在 LINUX DO 交流。

 License 
 MIT 

 About Stop That Shit（别再造史了）｜面向 Codex/GPT 场景的多平台 Hook + Skill Guard：拦截 AI coding agent 无需求的哈希、校验和与任务范围膨胀。 A multi-platform Hook + Skill Guard for AI coding agents in Codex/GPT workflows: stop unrequested hashes, checksums, and task-scope creep.
 take-a-deep-breath0.com/zh/stop-that-shit Topics agent-skills ai-agents ai-coding claude-code codex codex-cli codex-plugin developer-tools guardrails hermes-agent local-first opencode overengineering scope-control yagni Resources Readme MIT license Contributing Contributing Security policy Security policy Activity Stars 1.9k stars Watchers 2 watching Forks 47 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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