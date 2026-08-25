# [AINews] Andrew Ng gets into AI Engineering

- 출처: Latent Space
- 원본 링크: https://www.latent.space/p/ainews-andrew-ng-gets-into-ai-engineering
- 발행: 2026-08-25T02:50:57+00:00
- 접근상태: 확인 완료

---

[AINews] Andrew Ng gets into AI Engineering - Latent.Space 
 
 
 
 
 

 

 

 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 

 

 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 

 
 
 

 
 
 
 
 
 
 

 

 
 
 
 
 

 

 

 

 

 
 

 
 

 

 

 
 Subscribe Sign in AINews: Weekday Roundups [AINews] Andrew Ng gets into AI Engineering An industry legend starts covering the inevitable! Aug 25, 2026 ∙ Paid 56 1 Share We’ve lost count of how many adoption milestones have been passed since the original Rise of the AI Engineer post, but surely Andrew Ng, cofounder of Google Brain and Coursera among many other things, relaunching DeepLearning.ai with a focus on AI Engineering is a big one : 
 This was done via “ an analysis of over 10,000 job postings; carrying out dozens of structured interviews with AI experts, hiring managers, and recruiters; gathering data through surveys; and synthesizing other online data ” . 
 Here are the four most important AI engineering skills according to Andrew:
 You can read his full post for more from the horses’ mouth, but we agree that “AI Engineering Skills” are broadly applicable to more than just those with the job title of “AI Engineer” and that is an insightful focus. 
 Commentary on the 4 skills:
 Building and deploying AI applications : “ People who are skilled at building and deploying AI applications understand the building blocks of AI (such as LLMs, context engineering, RAG, agentic workflows, machine learning and deep learning) and, importantly, how to use statistical techniques to measure, steer, and govern AI systems so that they behave more predictably. A core skill in doing so is knowing how to drive disciplined evals and error analysis loops . ” 
 yup. this part is closest to the traditional MLE/MLOps workflow , from “zero gradient” aka prompt engineering techniques, to harness engineering, to finetuning and beyond, all the way up to building your own agent lab as folks like Harvey are now doing 
 Software engineering fundamentals. “ Understanding software fundamentals allows you to recognize what tradeoffs even exist. This leads to better decisions in choosing your software stack, designing system architecture, designing your data store, testing, and so on. It also leads to much better outcomes than those for an inexperienced developer who vibe codes a solution without knowing the tradeoffs their coding agent is making — which will often be poor ones, because they don’t know what context to give their coding agent. ” 
 yup. this part is closest to the traditional SWE workflow . LLMs reward expertise — they raise the ceiling (high skill devs) much more than they raise the floor (low skill vibecoders), though both are improved. 
 Using coding agents. “ Using agentic coding effectively is now a key skill for every developer. When you have this skill, you have a good mental model for how agents work. You understand their limitations and how to work around them, and are able to quickly steer them — knowing how much to intervene and how much to leave them alone — to build robust software without wasting excessive time or tokens. You also need to know how to work with a clear spec (and when not to bother doing so), orchestrate multiple agents that work together, and avoid pitfalls like risk an agent messing up your production database. Because agentic coding is evolving quickly, using coding agents skillfully means not only knowing cutting-edge practices, but also having routines to keep trying new tools and evolve your workflows as best practices change . ” 
 When we first spoke about the 1000x AI Engineer in 2023 , when Copilot was the only game in town, this was the part that was the least evident, but clearly on the horizon. Coding exploded in 2024-2026 culminating in the epic 0-$60B run of Cursor and the rise of Claude Code, Codex, Cognition, Cline and other coding powerhouses not starting with C. Being nimble here is a plus, just as much as being wary of tokenmaxxers with LLM psychosis. 
 Shaping the build. “ Effective AI engineering requires having product sense and understanding business context and customer goals , so you can participate in shaping and driving the build… Taking advantage of this opportunity requires knowing how to drive projects forward. For example, knowing when to quickly build an MVP to take to users for testing, and when to slow down and take longer in order to build more carefully.” 
 This is perhaps the only part of AI Engineering that wasn’t foreseen in the original essay; we added the AI PM track in World’s Fair 2024 and soon Design Engineering and other AIE adjacencies because the lines started to blur very quickly in both directions. 
 Overall, a great update to the DeepLearning.AI focus. Welcome Andrew and team!
 
 AI News for 8/22/2026-8/24/2026. We checked 12 subreddits, 544 Twitters and no further Discords. AINews’ website lets you search all past issues. As a reminder, AINews is now a section of Latent Space . You can opt in/out of email frequencies! 
 AI Twitter Recap Agent Harnesses, Persistent Agents, and Enterprise MCP 
 Harness design is becoming a primary optimization surface : Several posts converged on the idea that agent quality is increasingly shaped by the harness rather than just the base model. NVIDIA’s new evaluation work argues that structural checks on agent “skills” barely predict usefulness—scan scores correlate with judged quality at just Spearman ρ = 0.14 —and proposes measuring “Skill Lift” instead: run the same task with and without a skill under identical conditions and score the delta in completed work ( paper summary via @omarsar0 ). In parallel, a position paper on Anthropic-style harnesses argues enterprises should standardize on a single reusable coding-agent harness rather than bespoke orchestration graphs, claiming harness choice can matter more than model choice on enterprise work ( summary via @dair_ai ). 
 Persistent and self-modifying agents are moving from concept to open-source implementations : @andykonwinski introduced Headlong , an open-source “microharness” for persistent agents that think continuously rather than only on request. The system stores trajectories as a DAG of jsonl files, keeps a self-guided inner loop running, and reportedly achieved an unattended self-debugging repair in 48 minutes ; tradeoffs include $1–$2/hr background thinking cost and occasional self-inflicted failures. Complementing that, @omarsar0 described exo , a harness architecture for recursive self-improvement with an append-only event log, swappable executor, and snapshot/rollback-capable sandbox—explicitly designed so agents can rewrite prompts/tools/memory without being able to corrupt durable state. Together, these posts suggest the next wave of agent infra is about durability, forking, rollback, and continuous operation , not just better prompting. 
 MCP is maturing into enterprise infrastructure : Anthropic rolled out enterprise-managed auth for MCP connectors , centralizing authorization through the organization’s identity provider so end users no longer perform per-tool OAuth for connectors like Asana, Atlassian, Canva, Datadog, Figma, Notion, Slack, and Supabase ( announcement from @ClaudeDevs ). Separately, the MCP roadmap highlights upcoming support for long-running workloads with streaming/server push , HTTP for local servers , progressive discovery for large catalogs, and standard identities/delegated permissions ( roadmap summary via @_philschmid ). This closes a notable gap between toy demos and auditable enterprise deployment. 
 Model Releases, Leaks, and Competitive Positioning 
 Qwen3.8-27B continues to punch above its size class : In Code Arena: WebDev, Qwen3.8-27B landed at #9 overall with 1595 points , the only model in its size class in the top 10 and just six ranks behind Qwen3.8-Max ( leaderboard update from @arena ). It also ranked highly in consumer product, brand/marketing, and gaming categories. A related open-source derivative, Carnice-V3-27B , was released by @kaiostephens : a 27B Qwen-based , Hermes-agent SFT intended to fit on consumer GPUs (3090+), with merged BF16 and GGUF variants. 
 Rumor cycle around unreleased frontier models intensified : Multiple tweets referenced apparent early access or traces of unreleased systems: EAP models labeled “claude-melon-eap” and “claude-marshmallow-eap” reportedly emphasized 3D/RL-style tasks and used many thinking tokens ( demo by @Lentils80 ); @kimmonismus collected signs of new Claude models , Ox Alpha , Qwen 4 , and a confirmed GPT Astra ; and @eliebakouch claimed access to a model still in training with a public W&B run. Treat most of this as ecosystem signal rather than verified spec, but it’s notable how much of the discourse is now about pre-release access asymmetry rather than public launches—echoing @michael_nielsen , who warned that controlling access to unreleased models is becoming a source of power concentration. 
 OpenAI and Anthropic positioning remains in flux : OpenAI developers announced GPT-5.6 availability in Kiro and a claimed ~82% cost reduction per successful Terminal-Bench 2.1 task in Kiro’s spec-driven environment for the Terra variant ( announcement ). OpenAI also cut GPT-5.6 Sol API pricing to $4/M input and $20/M output tokens ( pricing note via @kimmonismus ), with Arena updates showing Sol and Luna shifting the cost/performance Pareto frontier ( @arena ). On the Anthropic side, @tenobrus noted there has not been an unambiguous Opus-line upgrade in over six months, even as external testers reported stronger medium-reasoning results from new Claude variants ( @kimmonismus ). 
 Inference, Benchmarking, and Cost-Efficiency 
 Tool latency overlap is emerging as a key harness-level speedup : @a1zhang introduced Speculative Programmatic Tool Calling (sPTC) , which predicts safe tool calls during code generation and launches them early in a copy of the environment so execution overlaps with token generation. The reported improvement is modest so far—about 1.0–1.2× —but the mechanism is important: it shifts optimization from token-level decoding tricks to agent workflow pipelining . @lateinteraction compared it to CPU speculative execution, emphasizing that discarded work is acceptable if most guesses are right. 
 Token accounting and benchmark hygiene remain messy : Several posts called out misleading reporting practices. @bnjmn_marie shared a DeepSWE run with 918.9M input tokens , clarifying many were cache hits, while @cHHillee bluntly argued that counting cached input tokens in “token usage” is “incredibly dumb.” On the eval side, @jmbollenbacher warned that when a quantized model exceeds the reference model on a benchmark, it may indicate overfitting the quant , not genuine improvement; @xeophon summarized the broader lesson: fixing the eval may matter more than hill-climbing it. 
 Cost-normalized agent benchmarks continue to reshape model choices : Together AI reported that under a $100 budget , GLM-5.3 completed 5× more work than Fable 5 on DeepSWE, roughly 17 vs 3 solved tasks , despite similar first-try performance ( tweet ). @reach_vb similarly reported GPT-5.6 Sol Max at 72.7% on DeepSWE v1.1 for $6.47/task versus Fable 5 Max at 69.7% and $21.63/task . Cline also compared Ox Alpha vs Fable on a real bugfix and found both solved it, but Ox used roughly 3× fewer output tokens , suggesting a notably different post-training philosophy around re-verification versus acting on the first conclusion ( comparison from @cline ). 
 On-Device AI and Inference Systems 
 Liquid AI + Artificial Analysis launched a serious on-device benchmark stack : @liquidai released Pipette , an open-source evaluation suite for on-device inference measuring quality, speed, latency, and memory across model + quantization + runtime + device combinations, with 10k+ verified results spanning 35 model classes , 7 quants , llama.cpp runtimes, and four devices. Artificial Analysis paired this with independent phone-scale intelligence evals on iPhone 17 Pro and Galaxy S26 Ultra ( full thread ). 
 Phone-scale results highlight a different Pareto frontier than cloud evals : Under an 8 GB memory / 16K context framing, Nanbeige4.2-3B and LFM2.5-2.6B topped the average score at 63 , with LFM2.5-2.6B much more efficient on iPhone ( 8.0s , 2.3 GB ) than Nanbeige ( 21.4s , 4.0 GB ). MoE designs such as LFM2.5-8B-A1B and Ling 3.0 Tiny are notable because they activate ~ 1B parameters/token , enabling sub-6-second responses on phone hardware. The evaluation also makes explicit that many “smart” reasoning models are poorly matched to mobile memory and latency constraints. 
 Inference vendors are competing on agent-specific throughput, not just raw TPS : NVIDIA’s Groq 3 LPX was described as adding a dedicated token-generation accelerator to Vera Rubin , with a claimed 3,400 output tokens/s on Gemma 4 31B at 100K context in Artificial Analysis benchmarking ( summary via @kimmonismus ); Groq said it will be among the first to deploy it in production ( announcement ). Separately, vLLM published extensive AgentX 1.0 results on real multi-turn coding traces, emphasizing KV offload , prefix reuse , and prefill/decode disaggregation as the keys to high agentic throughput rather than classic single-turn serving metrics ( @vllm_project ). 
 Research, Papers, and Technical Education 
 RL for LLMs and harness-native training remain hot : @cwolferesearch published a comprehensive reinforcement learning guide covering token-level vs completion-level formulations, PPO/GRPO variants, actor-critic methods, rubric-based RL, and agentic RL/world modeling. This coincides with growing attention on “harness-native” RL and agent environments, reflected in paper roundups like @TheTuringPost and discussion of papers such as Agent Lightning , LEGO-RL , EnvH