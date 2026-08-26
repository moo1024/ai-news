# Granite 4.2 LLMs: How They're Built

- 출처: Hugging Face Blog
- 원본 링크: https://huggingface.co/blog/ibm-granite/granite-4-2
- 발행: 2026-08-25T15:14:14+00:00
- 접근상태: 확인 완료

---

Granite 4.2 LLMs: How They're Built 

 

 

 

 
 
 
 
 Hugging Face Models Datasets Spaces Buckets new Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden"> 
 
 
 
 
 Granite 4.2 LLMs: How They're Built
 
 Enterprise Article Published
 August 25, 2026 Upvote 33 +27 Yousaf Shah yousafshah Follow ibm-granite Swanand Kadhe kswanand1 Follow ibm-granite Riddhiman Moulick rmoulick Follow ibm-granite Ashish Sunil Agrawal ashish23 Follow ibm-granite :last-child]:mb-0"> 
 Overview Model Architecture Pre-Training SFT: Data Preparation & Quality Control Data Quality Control SFT Training Details Phase 2 SFT for the 30B Model Reinforcement Learning: A Multi-Stage, Multi-Environment Pipeline Training Methodology The Staged Curriculum Reward Signals Foundational RL: Build the Skills Agentic RL: Learning to Act (8B / 30B) Alignment: RLHF How the Three Sizes Differ Agentic AI Infrastructure for Scalable RL Results Quantization FP8 FP4 GGUF Infrastructure Hardware Software Stack Getting Started (Transformers) Installation Basic Inference (Thinking Mode) Non-Thinking Mode Low-Effort Thinking Tool Calling Basic Tool Calling Multi-Turn with Tool Response Multi-Turn Conversations History Thinking Truncation Parsing Thinking vs. Final Answer Using with Agentic Coding Harnesses OpenCode Pi OpenHands A technical walkthrough of how we built the Granite 4.2 reasoning model family. 

 Authors: Granite Team, IBM

 
 TL;DR: Granite 4.2 is our first family of dense, decoder-only reasoning LLMs, released in three sizes: 3B, 8B, and 30B . Each model is pre-trained from scratch on roughly 15T tokens with a five-phase strategy that extends the context window to 512K tokens, supervised fine-tuned on chain-of-thought, reasoning, and agentic-trajectory data, then post-trained with a multi-stage reinforcement learning pipeline . That pipeline includes agentic RL, where the 8B and 30B models learn to act with tools inside real sandboxed environments. Every model has a thinking / non-thinking switch, a low-effort thinking mode that spends a short reasoning budget on easy questions, and native tool calling. All Granite 4.2 models are released under the Apache 2.0 license.

 Links: 

 
 Granite 4.2 HF Collection 
 GitHub Repository 
 Granite Docs 
 
 
 
 
 
 
 
 Overview
 
 
 Granite 4.2 is the reasoning-focused release of the Granite language-model family. Earlier Granite releases were strong instruction-following assistants; Granite 4.2 adds explicit reasoning. Every model can produce a chain of thought before its answer and can run in thinking or non-thinking mode depending on how much deliberation a task needs. A low-effort mode falls between the two, spending a short reasoning budget on easy questions.

 The three sizes ( 3B, 8B, and 30B ) share the same architectural design and follow the same training pipeline (pre-training from scratch, SFT, then multi-stage RL), each at its own scale. All three are strong reasoners and instruction followers. The clearest capability split shows up in post-training. The 8B and 30B models additionally go through an agentic RL block that teaches them to operate as agents: calling tools, editing and running code, driving a terminal, and searching the web inside real environments. Every model supports native tool calling. Served through an OpenAI-compatible endpoint (for example, with vLLM), it emits tool calls in the OpenAI function-calling format and plugs into agentic harnesses without extra glue. Granite 4.2 is also supported in SGLang, see the SGLang cookbook for a ready-to-serve recipe.



 The rest of this post walks through the build: architecture, pre-training, supervised fine-tuning, the multi-stage RL pipeline, and results.

 
 
 
 
 
 
 Model Architecture
 
 
 Granite 4.2 models are built on a decoder-only dense transformer architecture with the following core components:

 
 Attention: Grouped Query Attention (GQA) with 40 attention heads and 8 KV heads 
 Position Embedding: Rotary Position Embedding (RoPE) with θ = 10,000,000 
 Feed-Forward: MLP with SwiGLU activation 
 Normalization: RMSNorm (ε = 1e-5) 
 Embeddings: Separate input/output embeddings (not tied) 
 Precision: bfloat16 
 
 
 
 
 Component 
 3B Dense 
 8B Dense 
 30B Dense 
 
 
 
 Embedding size 
 2560 
 4096 
 4096 
 
 
 Number of layers 
 40 
 40 
 64 
 
 
 Attention head size 
 64 
 128 
 128 
 
 
 Number of attention heads 
 40 
 32 
 32 
 
 
 Number of KV heads 
 8 
 8 
 8 
 
 
 MLP hidden size 
 8192 
 12800 
 32768 
 
 
 MLP activation 
 SwiGLU 
 SwiGLU 
 SwiGLU 
 
 
 Sequence length 
 131072 
 131072 
 131072 
 
 
 Position embedding 
 RoPE 
 RoPE 
 RoPE 
 
 
 # Parameters 
 3B 
 8B 
 30B 
 
 

 
 
 
 
 
 
 Pre-Training
 
 
 Granite 4.2 is trained from scratch on approximately 15 trillion tokens using a five-phase training strategy. Phases 1–2 focus on foundational pre-training, phases 3–4 perform mid-training with progressively higher-quality data annealing, and phase 5 introduces long-context training, extending the context window to 512K tokens . Each phase uses a distinct data mixture and learning-rate schedule, gradually shifting from broad web-scale data toward more curated, high-quality sources.

 The pre-training recipe closely follows the previous generation; for a detailed treatment of the data blend, phase schedule, and long-context extension, see the Granite 4.1 blog .

 
 
 
 
 
 
 SFT: Data Preparation & Quality Control
 
 
 Supervised fine-tuning (SFT) turns the base model into a reliable instruction-following, reasoning, and tool-using assistant. The SFT data mixture combines agentic (31.6%) and non-agentic (68.4%) data, totaling approximately 7.2 million samples, or roughly 100B tokens, of which about 65B are trainable.

 The agentic corpus covers a broad range of domains, including software engineering (SWE, 69%), tool calling (12.1%), terminal use (8.0%), math (3.5%), search (0.8%), and action (0.2%). These samples and trajectories are generated using a diverse set of agent scaffolds and harnesses, including OpenHands, OpenCode, Terminus-2, SWE-agent, OpenResearcher, MiniSWE, OpenSeeker, EnvScaler, Gemini CLI, Hermes, Codex, and Goose. The agentic data combines samples from both open-source datasets and our own synthetically generated RL environments, spanning a variety of agent–harness combinations.

 The non-agentic corpus consists of several major categories: instruction following (18.8%), coding (18.8%), math (14.6%), multilingual (7.0%), science (5.4%), reasoning (3.0%), and safety (0.8%).

 
 
 
 
 
 Data Quality Control
 
 
 We apply multiple stages of quality control before a sample enters the final SFT mixture. First, data from different sources is normalized and reformatted into a consistent OpenAI Chat format, making the conversation structure and tool interactions uniform across datasets and scaffolds.

 We then use GPT-OSS-120B and Gemma 4 as LLM-based judges to assess sample quality. Low-scoring samples are removed, as are samples containing hallucinated or fabricated information, invalid tool interactions, or tool calls to functions that are not defined in the corresponding tool list. Several targeted, dataset-specific heuristic rules are also applied where appropriate to further improve quality and remove known sources of noise.

 Finally, we perform both local and global deduplication. Deduplication is based on SHA-256 hashes computed over the combination of the tools and messages fields, removing duplicate samples both within individual data sources and across the overall SFT mixture.

 
 
 
 
 
 SFT Training Details
 
 
 The complete corpus is first globally shuffled to reduce ordering effects and ensure that samples from different domains are well mixed during training. The shuffled corpus is then partitioned into equally sized .parquet shards, which are tokenized using the model's tokenizer and chat template and prepared for large-scale distributed training.

 Before launching the final large-scale runs, we tune hyperparameters on representative configurations, sweeping learning-rate schedules, initial learning rates, and warm-up ratios to find settings that train stably across model sizes. The final training configuration is summarized below:

 
 
 
 Parameter 
 Value 
 

 
 Compute 
 32–128 nodes (by model size), 4× Grace/GB200 per node 
 
 
 Sequence length (packed) 
 131,072 (128K) 
 
 
 Global batch size 
 128 
 
 
 Learning rate 
 1.0e-5, constant after warm-up; 3.0e-6 for Phase 2 
 
 
 LR warm-up 
 2.5% of train_iters 
 
 
 Training duration 
 ~2 epochs 
 
 
 Parallelism 
 TP=2, PP=1, CP=4 or CP=2 
 
 
 
 
 
 
 
 
 
 Phase 2 SFT for the 30B Model
 
 
 For the 30B model, we additionally perform a second phase of SFT focused specifically on agentic coding. In this phase, agentic, SWE, and coding data are upsampled to increase their effective contribution to the training distribution, while approximately 16% of the mixture is retained as replay data from the original SFT corpus.

 The 30B model is then fine-tuned for roughly one additional epoch at a lower learning rate of 3.0e-6. This targeted second phase increases the model's exposure to agentic coding trajectories without discarding the capabilities acquired during the initial SFT phase.

 
 
 
 
 
 
 Reinforcement Learning: A Multi-Stage, Multi-Environment Pipeline
 
 
 After SFT, we apply a multi-stage, multi-environment reinforcement learning pipeline . Rather than a single RL pass, we run a chain of focused stages spanning many environments: math, code, science, instruction following, tool use, and structured output, then software engineering, terminal use, and web search. Each stage is an independent RL run that targets one capability and warm-starts from the previous stage's checkpoint.


 

 Figure 1. The staged RL curriculum. Foundational RL (verifiable rewards + skill boosters) runs for all sizes; the agentic RL block (SWE → Terminal → Search) runs for 8B and 30B only. Every model finishes with RLHF. Each stage is a separate GRPO run that warm-starts from the previous checkpoint. 

 
 
 
 
 
 Training Methodology
 
 
 Every stage trains with asynchronous GRPO ( Group Relative Policy Optimization ), so the generator and trainer halves of the loop never block on each other. A pool of generation workers keeps sampling responses and dropping the finished trajectories into a shared buffer; once the buffer holds a full step's worth, the trainer pulls that batch, takes an optimizer step, and streams the updated parameters back to the generator workers without pausing them. A refresh can land partway through a rollout, leaving a single trajectory stitched together from two adjacent policy versions. We allow this instead of paying to prevent it: the workers reuse their existing KV cache rather than rebuilding it after each refresh, and the one guardrail is a limit that keeps them from drifting more than a single update behind the trainer, which bounds how off-policy any sample can get. Whatever mismatch survives that limit is handled in the objective by truncated importance sampling , which clamps the train-versus-generation log-probability ratio to a fixed ceiling so a handful of stale tokens cannot dominate an update.

 Advantages are group-relative with a leave-one-out baseline : each response is judged against the mean reward of the other samples drawn for the same prompt, which removes the need for a separate value network. To make this concrete, take RLVR , the first and longest-running stage: each step pairs 256 prompts with 16 sampled responses apiece for a 4,096 -example batch, which the trainer consumes in a single optimizer step before the next rollout begins. Later stages keep this machinery unchanged and adjust only the per-stage shape, shown next.

 
 
 
 
 
 RL training configuration
 
 
 The pipeline keeps a common backbone of hyperparameters across every stage, which makes the curriculum easier to run and compare. A handful of knobs are fixed everywhere:

 
 
 
 Parameter 
 Value (shared across stages) 
 

 
 Algorithm 
 GRPO (no value network; group-relative advantages) 
 
 
 Training stack 
 NeMo-RL (Megatron-Core + vLLM) with NeMo-Gym environments 
 
 
 Ratio clip (min / max) 
 0.2 / 0.28 
 
 
 Micro-batch size 
 1 
 
 
 Parallelism 
 tensor-parallel 2–4; no pipeline- or context-parallelism 
 
 
 
 
 What changes from stage to stage is the shape of each run: how many prompts and generations per step, how long the context is, whether the agent loop runs, and how hard we pull back toward the reference policy. The table below gives the exact settings for the 30B chain, stage by stage:

 
 
 
 Stage 
 Prompts/step 
 Gens/prompt 
 Max seq len 
 Rollout turns 
 KL 
 LR 
 

 
 RLVR (×3) 
 256 
 16 
 64K 
 1 
 0 
 5e-7 
 
 
 IF booster 
 256 
 16 
 64K 
 1 
 0 
 5e-7 
 
 
 Code booster 
 64 
 16 
 64K 
 1 
 0.05 
 5e-7 
 
 
 SWE 1 
 64 
 16 
 128K 
 1 
 0.01 
 5e-7 
 
 
 SWE 2 
 32 
 16 
 128K 
 128 
 0 
 5e-7 
 
 
 Terminal 
 8 
 32 
 64K 
 64 
 0.01 
 1e-6 
 
 
 Search 
 32 
 16 
 128K 
 64 
 0.01 
 5e-7 
 
 
 RLHF 
 128 
 16 
 48K 
 1 
 0.05 
 5e-7 
 
 
 
 
 Parameters shown for the 30B model. Global batch size = prompts/step × generations/prompt (e.g. 256 × 16 = 4096 for RLVR). The 3B and 8B models use the same recipe and hyperparameters with fewer stages (see How the Three Sizes Differ ); the stage list is what changes, not the knobs. 

 The KL schedule follows the reward type: explore freely where the reward is objective and verifiable (RLVR and SWE 2 run at KL 0), and stay close to the reference where the objective is preference, safety, or a narrow skill graft (RLHF and the code booster use KL 0.05). The rollout-turns column counts the environment interactions GRPO itself se