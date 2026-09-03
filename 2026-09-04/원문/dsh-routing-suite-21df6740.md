# yjh051108/dsh-routing-suite — dsh-routing-suite — injector + router-standard kit: install the runtime injector

- 출처: GitHub 신규 (AI 에이전트)
- 원본 링크: https://github.com/yjh051108/dsh-routing-suite
- 발행: 2026-09-03T22:24:35.374001+00:00
- 접근상태: 확인 완료

---

GitHub - yjh051108/dsh-routing-suite: dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23). · GitHub 



 
 
 
 

 
 


 


 


 
 

 
 

 

 





 

 




 

 

 

 

 

 

 
 
 

 
 
 




 



 


 
 
 
 

 

 

 

 

 
 



 

 
 


 


 

 
 

 
 
 

 
 


 

 

 
 
 
 

 
 Skip to content 

 
 
 
 
 
 
 

 
 
 
 
 





 

 

 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Copilot app Direct agents from issue to merge MCP Registry Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Code Quality Enforce quality at merge APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events & webinars Ebooks & reports Business insights GitHub Skills SUPPORT & SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features Copilot for Business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search / Sign in Sign up Appearance settings 
 



 
 
 
 
 
 You signed in with another tab or window. Reload to refresh your session. 
 You signed out in another tab or window. Reload to refresh your session. 
 You switched accounts on another tab or window. Reload to refresh your session. 

 
 
 
 Dismiss alert 


 
 
 

 








 





 
 
 
 
 
 
 
 
 
 
 
 {{ message }} 

 
 
 
 
 


 






 
 
 
 
 








 

 

 

 
 
 
 
 
 
 
 
 
 yjh051108
 
 / 
 
 dsh-routing-suite 
 

 Public 
 


 

 
 
 
 

 
 
 
 Notifications
 You must be signed in to change notification settings 

 

 
 
 
 Fork
 148 
 
 

 
 
 
 
 
 Star
 7.1k 
 
 

 

 
 

 
 


 

 
 
 
 
 
 
 
 Code 
 


 
 
 
 
 
 
 
 
 Issues 
 31 


 
 
 
 
 
 
 
 
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
 
 
 
 
 
 


 
 
 
 
 

 
 



 
 
 



 
 
 








 
 
 
 main Branches Tags Go to file Code Open more actions menu Latest commit   History 72 Commits 72 Commits Folders and files Name Name Last commit message Last commit date docs docs     graded graded     injector injector     preset preset     scripts scripts     test test     .gitattributes .gitattributes     .gitignore .gitignore     LICENSE LICENSE     README.en.md README.en.md     README.md README.md     cordis.patch.yml cordis.patch.yml     install.ps1 install.ps1     install.sh install.sh     package.json package.json     View all files Repository files navigation README MIT license More items dsh-routing-suite — 注入器 × 思维模式路由 × 分级模式 套装 
 一个仓库装齐三件套： 运行时注入器 （免重启运行时管理层）+
 思维模式路由预设 （任务感知推理模式，P1-P23 实测）+
 分级任务协议 （脑暴出题 → 规格化计划 → 打卡制 → 组收官 → 终验，含红队门与审计端点）。

 中文 | English 

 组件入口（快速跳转） 
 
 
 
 组件 
 说明 
 入口 
 
 
 
 
 injector 
 运行时注入器： dev_* 工具全家桶（注入/热重载/卸载/侧挂转正/路由自愈） 
 injector/README.md · 文档 
 
 
 preset 
 思维模式路由预设（router-standard / router-spec，按模型 persona 路由） 
 preset/README.md · 实验报告 
 
 
 graded 
 分级模式：会话级两级任务协议（6 工具+三模式+小类模式粒度+红队门+审计端点+超级面板） 
 graded/README.md · 架构 · 理论 · 实测数据 
 
 
 
 研究与数据（graded） 
 "模型也会偷懒——我们测到了，还做了对抗" —— 分级模式插件的公开研究位：

 
 🔬 模型注意力懈怠：观测笔记 ——长程任务里验证勤勉度衰减的真实分段数据（无协议链晚段"1 工具/0 读图" vs 协议链全程在线）+对抗机制对照 
 📊 协议 vs 无协议：实测对比 ——同型 3D 任务三会话对比表+ASCI I 图 
 🧪 测量工具 —— node scripts/measure.mjs 你的会话.jsonl ：任何人可对自己会话复算上述指标（脱敏：只输出数字） 
 📁 实测数据 ——三会话脱敏指标表+懈怠强度表+审计口径 
 
 一键安装 
 dsh plugin -- profile web add github:yjh051108 / dsh - routing - suite 
 
 本套装已含上述三组件（injector/preset/graded 均为仓库内普通目录，内容直接入库）；
graded 发布物： graded/dsh-external-dsh-graded-mode-0.0.1-rc1.tgz （或 Release 附件）。

 
 DSH Target ： >=0.1.0-rc.6 <0.2.0 （已跟进 rc.8 / 0.1.1-rc.2 / 0.1.2-alpha.1）

 
 DSH 目前处于 developer preview，官方明示会有破坏性变更（breaking changes）。
本仓库的版本跟进记录见 preset/CHANGELOG.md 。

 
 安装链（三步） 
 # 1. 拉套装（单仓库：injector/preset 内容已直接入库，无需 submodule） 
git clone https: // github.com / yjh051108 / dsh - routing - suite.git
cd dsh - routing - suite

 # 2. 一键安装（注入器装配 + 预设复制 + 布局自检 + 提示重启） 
.\install.ps1 
 或手动：

 # 步骤 1：装配注入器（官方装配，重启后由 bundles 接管） 
dsh plugin -- profile web add .\injector
 # dsh 不在 PATH 时：npx '@deepseek-ai/dsh' plugin --profile web add .\injector 

 # 步骤 2：安装 router 预设（每个预设目录平铺复制到 .agent-presets 下，DSH 只扫一级子目录） 
 $target = Join-Path $ env: USERPROFILE ' .dsh\.agent-presets\router-standard ' 
 Copy-Item - Recurse .\preset\router - standard $target 

 $target = Join-Path $ env: USERPROFILE ' .dsh\.agent-presets\router-spec ' 
 Copy-Item - Recurse .\preset\router - spec $target 

 # 步骤 3：重启 DSH → 新会话选择 Router Standard / Router Spec (experimental) 
 
 注意：不要复制 preset 整目录（会多套一层，DSH 发现不了预设）。

 
 组件 
 
 
 
 路径 
 仓库 
 版本 
 作用 
 
 
 
 
 injector/ 
 dsh-super-injector 
 v0.3.3 
 运行时注入器：dev_* 工具全家桶（注入/热重载/侧挂转正/卸载/路由自愈）； github: 装配由 prepare 钩子自动构建 
 
 
 preset/ 
 dsh-router-standard 
 v0.3.0 … 主线 v1.19.1/v34 
 思维模式路由预设：router-standard（分类 persona + 完整 sections）/ router-spec（深度思考优先）。router-pro 为规划中（planned），未随 v0.3.0 发布 
 
 
 graded/ 
 dsh-graded-mode 
 v0.0.1-rc1 
 graded 模式：会话级两级任务协议（脑暴选择题对齐 → 北极星定稿 → 规格化计划 → 按规格注入 → 打卡制 → 组收官 → 终验）；6 工具 + 三模式 + 小类模式粒度 + 红队门 + 审计端点； graded/dsh-graded-mode-3.2.0.tgz 可直接 dsh plugin --profile web add 
 
 
 
 
 版本号以各组件仓库的 git tag 为准（列内链接直达对应 Release）。

 
 三个组件随本仓库统一演进（ injector/ 、 preset/ 与 graded/ 已是仓库内普通目录，内容直接入库）；上游独立仓库保留用于独立发布，后续可转镜像/归档。预设安装目录为 preset/router-standard （已平铺，无额外嵌套）。

 router-standard 预设能力（P1-P23 实测摘要） 
 
 三行为带 + weak 内路由 ：spec（计划-集体）/ react（执行者）/ mixed（陷阱，回避）/ weak（模型自分类） 
 按模型选 persona ：Pro=spec 句+few-shot（区分度 +5.0）；Flash=neutral+classify（+5.7） 
 近距离引导 ：每轮用户消息后注入固定引导（缓存 92-94% 命中），路由 96% + 收敛 100% + 反稀释 
 单任务三锚 （persona 静态）：回顾 + 收敛 + 反跑题 —— 开放任务完成率 0% → 100% 
 plan-mode 保留 ：只替换 persona section，plan 边界不失忆 
 AI 自优化工具 ： dev_router_status / dev_router_mode / dev_mode_subagent 
 
 v0.3.0 变更（真实装配链路修复） 
 
 首轮路由真实生效 （ #13 ）：经 agent/inbox/claimed 在装配前捕获首条真实用户消息，首个请求即按任务分类（此前所有会话首轮无条件 weak） 
 近距离引导改走 agent/pre-step （ #34 / #36 / #55 ）：引导与用户消息同请求注入，真实链路上可达，且不再产生额外的第二次 API 调用（此前每轮多 1 次调用 = 费用 2×） 
 缺导入修复 （ #11 ）、preset.yml YAML 引号（ #53 ）、promoted 后完整回归（ #44 ）、安装脚本与文档修正（ #35 / #42 / #41 ）、injector git 装配自动构建（ #40 ） 
 
 文档 
 
 注入器引导（规范铁律 10 条）： injector/README.md 
 路由预设论文与实验： preset/docs/paper.md + preset/docs/experiments.md （P1-P23） 
 仓库结构迁移（submodule → 直接文件）： docs/FLATTEN-MIGRATION.md 
 
 许可证 
 MIT。致谢：xiaobright/modeltest（V4.1b 评测）、xiaobright/dsh-anchored-standard（锚定机制）。

 About dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23).
 Topics ai-agents cordis deepseek-harness dsh dsh-plugin Resources Readme MIT license Activity Stars 7.1k stars Watchers 17 watching Forks 148 forks Report repository Releases Packages Contributors Languages 
 




 

 

 
 

 

 
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