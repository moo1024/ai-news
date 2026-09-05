# GPT-6 Astra in code review: Gains, privacy, and cost

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://www.coderabbit.ai/blog/gpt-6-astra-code-review-evaluation
- 발행: 2026-09-05T03:38:56+00:00
- 접근상태: 확인 완료

---

GPT-6 Astra review: code review gains, privacy, and cost We raised $143M to build the control layer for software change. Read more : We raised $143M to build the control layer for software change. 
 Enterprise Security Customers Pricing Blog Resources Log In Get a free trial GPT-6 Astra in code review: Gains, privacy, and cost by Erik Thorelli
 Erfan Al-Hossami
 September 04, 2026
 • 8 min read
 What Astra added to code review Putting context to work Stronger reasoning comes at a premium What might transfer beyond code review Building and balancing NIGHTSHIFT What we want to see next Protecting customer data Back to blog Some of the hardest work in code review happens outside the changed lines. A change can look correct in isolation and still break code elsewhere in the system.

 That is what makes our early results for OpenAI's GPT-6 Astra most interesting. In our evaluation, Astra caught approximately 4% more labeled bugs through actionable findings than GPT-5.6 Sol , and 22% more than Opus 5 .

 The biggest jump comes on harder cross-file reviews, where Astra's gains reach 20% over Sol and 33% over Opus 5 . Using that capability at customer scale also means protecting customer data and assessing the model’s public API pricing.

 What Astra added to code review 
 Our measure here is actionable bug coverage, meaning how many labeled bugs a model catches through findings a developer can act on.

 
 
 Coverage is rounded to one decimal; relative gains use unrounded values. 
 

 The overall gain over GPT-5.6 Sol appears modest in this first evaluation measure. This evaluation also includes simpler reviews, where there may be less room for a stronger model to differentiate itself; Astra's larger advantage appears in the harder cross-file subset. It is an early, directional result.

 
 
 Coverage is rounded to one decimal; relative gains use unrounded values. Compare models within this chart, since its review difficulty differs from the overall evaluation. 
 

 The harder cross-file comparison is more encouraging. Astra's relative advantage grows to 20% over Sol and 33% over Opus 5. That suggests value in connecting a change's intent to consequences distributed across a codebase.

 These results describe one part of review performance. They do not establish an overall ranking of review quality, predict a team's defect rate, or promise the same gain on every pull request.

 Putting context to work 
 A large context window creates room for information. Useful reasoning requires the model to identify which pieces matter, connect them, and reach a conclusion supported by evidence.

 Our interpretation is that Astra's most interesting advance lies in connecting the right information. Its larger gains on harder cross-file reviews suggest progress on work where relevant information is distributed. They do not isolate the cause of that progress or prove that more context alone improves a model's performance.

 OpenAI positions Astra for multistep work across code, browsers, and professional software .

 For teams building with models, the useful question is where the extra reasoning changes the outcome enough to justify its cost. A difficult task with scattered evidence is a stronger candidate to investigate than a routine task that a less expensive model already handles reliably. That doesn't mean switching every session to Astra, maxing out reasoning effort, and letting it rip.

 Stronger reasoning comes at a premium 
 Astra’s standard API rates are $10 per million input tokens and $50 per million output tokens , according to Astra’s published pricing . Fable 5.1 has the same base input and output rates, although caching prices differ. Anthropic’s pricing documentation provides the full breakdown.

 To put those prices in context, consider an illustrative task using 100,000 uncached input tokens and 10,000 billable output tokens, including reasoning tokens. Holding token usage constant makes the published rates easier to compare; actual task costs vary with usage.

 
 
 All figures use publicly listed standard API prices, checked September 4, 2026. OpenAI figures use short-context rates. Sol's public promotional pricing is available at least through November 21, 2026. The example excludes caching, cache writes, tools, retries, regional uplifts, and service-tier adjustments. Real tasks can use different numbers of tokens. 
 

 
 
 
 
 Model Input / 1M tokens Output / 1M tokens Illustrative task cost 
 
 
 
 GPT-5.6 Luna $0.20 $1.20 $0.032 
 
 GPT-5.6 Terra $2.00 $12.00 $0.32 
 
 GPT-5.6 Sol $4.00 $20.00 $0.60 
 
 GPT-6 Astra $10.00 $50.00 $1.50 
 
 Claude Fable 5.1 $10.00 $50.00 $1.50 
 
 
 At that fixed usage, Astra costs 2.5 times Sol, about 4.7 times Terra, and about 47 times Luna . Those are meaningful premiums. They are not predictions of the difference in cost per completed task. A model that needs fewer tokens or fewer attempts could narrow the gap.

 OpenAI reports lower estimated task costs for Astra in some of its own evaluations despite higher token prices. That makes total cost per successful outcome worth measuring on your work, rather than assuming that either token price or a capability score settles the decision. Read OpenAI's efficiency guidance .

 What might transfer beyond code review 
 The transferable idea is reasoning over relationships among separate sources. Our findings suggest several uses worth evaluating; we have not measured Astra on these tasks:

 
 Research synthesis: reconcile conflicting reports, connect claims to their evidence, and identify gaps that a summary of each document would miss. 
 Operational investigation: assemble a coherent explanation from logs, incident notes, and runbooks, while separating observations from hypotheses. 
 Requirements and policy analysis: trace a proposed change across specifications, internal policies, and implementation plans to flag inconsistencies for expert review. 
 Document and spreadsheet work: check whether assumptions, formulas, and narrative conclusions agree across a report and its supporting materials. 
 
 The common structure is scattered evidence with dependencies between its parts. Start with bounded work whose answer can be checked. The easiest way to test whether Astra is right for your workflows or products is to run it alongside your current model on the same tasks, then compare answer quality, verification time, and total cost.

 Building and balancing NIGHTSHIFT 
 We also used Astra to build a whole game: NIGHTSHIFT , an action RPG made with Godot and GDScript. Its hardest problem was balancing the interactions between systems, then revisiting that balance as the game changed.

 
 
 NIGHTSHIFT, built with Astra through human direction and iteration. 
 

 That meant reasoning across seven character classes, a 988-node passive skill tree inspired by the legendary Path of Exile passive node tree , active skills, runes and socketable upgrades, skill evolutions, and co-op. Across 40 zones in 10 acts, the campaign introduces increasingly complex enemy swarms and combinations. Changing one class can also change which upgrades are useful, how a skill develops, and what a party can handle.

 We made fundamental changes to core systems during development and asked Astra to work through the consequences and rebalance them. "Balance" in a game like this is the most difficult creative challenge for compelling gameplay. How can you make sweeping changes or introduce entirely new game systems and mechanics while keeping progression, combat, and difficulty coherent?

 We also wanted players to discover overpowered endgame builds through clever combinations of classes, stats, items, passives, and active skills. The challenge was shaping a progression where reaching even mid-game was uncertain, but creativity and experimentation could pay off in spectacular ways. The reward for finding those combinations was working up to a build that could satisfyingly melt enemy swarms.

 The process meant returning to the game between other work, giving Astra feedback, and giving it full autonomy to use its judgement in refining that balance. Astra also built native PS5 and Xbox controller support, native macOS, web, and Linux builds, and co-op. Co-op was particularly interesting, because Astra was able to build it out for playing on the same compute and LAN, which since we wanted to distribute to coworkers running macOS, it required generating a new Xcode project, App Store Connect account, establish multiple certificates and entitlements, and notarization.

 Astra handled it all autonomously, only pausing to occasionally ask for authority and permissions it didn't already have. As a fun bonus, the game was also built for agents themselves to be players, which was somewhat surreal to be able to play live co-op sessions with Astra as a teammate. Several of us found it hard to put down. "I'm working on model evals" became a useful explanation for having a game open when a manager stopped by.

 
 
 
 
 Watch the NIGHTSHIFT gameplay clip. 
 
 An earlier NIGHTSHIFT arcade prototype, shown in an 18-second automated gameplay demo. 
 

 The game gave us a creative setting to explore the same capability that stood out in code review. Astra had to reason about how each change affected the rest of the system.

 What we want to see next 
 The next exciting advance would make this depth of reasoning dependable enough to use more often. That means consistent gains on difficult work, conclusions people can verify, and lower total cost for a successful outcome.

 That calls for better selection of relevant context, clearer supporting evidence, and fewer unnecessary steps. It also means privacy-preserving deployment paths that make advanced capabilities usable under real customer commitments.

 Astra gives us an encouraging signal on cross-file reasoning. The practical opportunity is to turn that capability into work that is both more useful and easier to trust. As with bringing any new model online at CodeRabbit , the evaluation is one part of that decision.

 Protecting customer data 
 Neither CodeRabbit nor our model providers train AI models on CodeRabbit customers' proprietary code or personal information collected during private code reviews. Read our privacy policy .

 OpenAI and Anthropic have different data-retention policies:

 
 OpenAI: GPT-6 Astra supports zero data retention for eligible API customers. OpenAI’s API data controls describe ZDR eligibility and supported capabilities. Astra announcement , OpenAI data controls . 
 Anthropic: Fable requires 30-day retention by default for safety monitoring, but eligible customers can now use Fable 5 and 5.1 with ZDR while Enterprise Frontier Safeguards is being introduced. For products serving other businesses, that option requires terms agreed with Anthropic. EFS is designed to keep retained activity data in customer-controlled infrastructure. Covered-model retention policy , Enterprise Frontier Safeguards , eligibility details . 
 
 Any model we use for customer reviews must meet our data-protection requirements.

 Share
 Catch the latest, right in your inbox. Subscribe Add us to your feed. Keep reading What would the last software engineer still need to do? Kent C. Dodds explains why product judgment, system understanding, and ownership become more valuable as AI agents take on more implementation work.
 Fable 5.1 review: Should you switch? Fable 5.1 feels fast on small coding tasks and produces fewer review comments than Fable 5. It also leaves unstated requirements alone, so clear instructions make a large difference.
 The Merge: Why Building AI Chat Is Harder Than It Looks A conversation with Assistant UI founder Simon Farshid about the hidden work behind AI chat interfaces, product judgment, and his coding-agent loop with CodeRabbit.
 Get Started in 2 clicks. 
 Try it for free English Products
 Agent Discord Pull Request Reviews IDE Reviews CLI Reviews Plan OSS Navigation
 About Us Features FAQ System Status Careers DPA Startup Program Vulnerability Disclosure Resources
 Blog Docs Changelog Case Studies Events & Webinars Newsroom Trust Center Brand Guidelines Reports & Guides Contact
 Support Sales Pricing Partnerships Press Kit Subscribe By signing up you agree to our Terms of Use and authorize CodeRabbit to provide occasional updates about products and solutions. You understand that you can opt out at any time and that your data will be handled in accordance with CodeRabbit Privacy Policy 
 Legal Privacy Policy CodeRabbit Inc. © 2026