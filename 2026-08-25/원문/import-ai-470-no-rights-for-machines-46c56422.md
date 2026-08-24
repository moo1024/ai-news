# Import AI 470: No rights for machines; automating environment generation with SPADE; and building better GPU kernels with Hawkeye

- 출처: Import AI
- 원본 링크: https://importai.substack.com/p/import-ai-470-no-rights-for-machines
- 발행: 2026-08-24T13:12:40+00:00
- 접근상태: 확인 완료

---

Import AI 470: No rights for machines; automating environment generation with SPADE; and building better GPU kernels with Hawkeye 
 
 
 
 
 

 

 

 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 

 

 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 

 
 
 

 
 
 
 
 
 
 

 

 
 
 

 

 

 

 

 
 

 
 

 

 

 
 Subscribe Sign in Import AI 470: No rights for machines; automating environment generation with SPADE; and building better GPU kernels with Hawkeye Differential acceleration of cyber, math, and AI Jack Clark Aug 24, 2026 58 3 Share Welcome to Import AI, a newsletter about AI research. Import AI runs on arXiv, cappuccinos, and feedback from readers. If you’d like to support this, please subscribe.
 Subscribe AI is accelerating some types of progress but not others: 
 …A nice METR study lays out where acceleration is showing up… 
 Here’s a little analysis from METR which looks at where AI may be accelerating different types of science and technology. The study looks at three different areas: cyber, math, and AI research, and finds that AI has contributed a lot to cyber, a little bit to math, and it’s hard to say for AI. 

 Where have LLMs actually made a difference to scientific discovery? 
 Cyber vulnerabilities: Major acceleration. “The rate of vulnerabilities reported across many projects has dramatically accelerated in 2026 compared with 2025, both for specific projects (cURL, OpenSSL, Firefox, and Microsoft) and for aggregate vulnerability databases (the US NVD, and OSV)”. 
 Mathematics research: Minor acceleration, but harder to measure. “AI is clearly contributing to more work being done (arXiv submissions have doubled in some areas in less than 12 months) but quantifying the value of those contributions is difficult.” Some math problems from prestigious lists have been solved, e.g., “the Jacobian conjecture from Smale’s list, Problem 44 from Green’s list (the halving sieve), and the sofic half of Green’s Problem 100”. However, it may be too early to determine how sustained a trend this is. 
 Optimization of AI research: No measurable acceleration. When you look at algorithmic progress across seven significant problem areas (CIFAR-10, Hutter compression, Gurobi mixed-integer programming, MIPLIB, nanoGPT, Stockfish, and the matrix-multiplication exponent) there are a couple of these where LLM-attributable contributions have happened (nanoGPT, CIFAR-10), though the rate of increase of usage of AI here is a lot less than with cybersecurity and mathematics. 
 Why this matters - differential acceleration: This paper highlights how AI is causing advances in some parts of science and technology, but the effect isn’t unified across fields, rather there are pockets of lumpy acceleration (e.g., cyber) and areas where progress is more gradual (math, AI). My suspicion is that acceleration happens when models go through some kind of ineffable phase change for a given skill, as has evidently happened with day-to-day coding (2025), and cyber (2026). The key question is whether we are going to see phase changes in other parts of science and technology or if we won’t. 
 Read more: Research note: Have We Seen an Acceleration in Discoveries? (METR) . 

 *** 

 Automating environment generation with SPADE: 
 …A crude form of RSI bootstrapping via increasing data breadth… 
 A multi-university group of researchers have built SPADE, Self-Play in Adaptive Synthetic Executable Environments. SPADE is a “general framework for co-evolving environments synthesis and agentic capability through self-play”, and works as a way to generate synthetic data in the form of game-like environments which LLMs can subsequently be trained in, allowing developers to use a powerful model to bootstrap the creation of data that can then be used to further refine that same model. 

 Who did it : SPADE was developed by researchers with the University of Washington, Stanford University, Northeastern University, Carnegie Mellon University, Massachusetts Institute of Technology, National University of Singapore, Seoul National University, Stevens Institute of Technology, and the University of Chicago. 

 How it works : SPADE has an LLM alternate between generating executable training environments (e.g., puzzles where a system needs to solve a simulated genetic problem in a biology lab) and having an LLM try to solve them. SPADE has two key roles for the model being used: 
 Environment Designer; writes complete, long-horizon training environments as executable code. 
 Reasoning Agent ; learns to act in the environments. The reward for the reasoning agent is estimated using the gap between its reward with and without privileged hints. A privileged hint (h) is “task-relevant information that the Environment Designer attaches to an environment (for example, a partial solution sketch or a key structural observation); revealing h to the Reasoning Agent makes the environment easier to solve, and the gap in Reasoning Agent return with versus without h defines the Environment Designer’s hint-based regret reward”. 
 It works at the 30B scale: The authors train three Qwen3 backbones to test out SPADE: Qwen3-4B-Instruct-2507, Qwen3-8B, and Qwen3-30B-A3B-Instruct-2507. Unsurprisingly, Qwen3-30B works the best. Each model is tuned via GRPO for 400 rollouts of 25 environments each, then assessed against a variety of benchmarks including AIME, GPQA, LCB, and environments within Reasoning Gym. They generate two types of environments - game environments, and tool-use environments. SPADE improves performance on both. 
 For games, “at 30B-A3B, SPADE reaches a suite average of 58.3: +8.1 over base and +5.3 over the strongest fixed-environment baseline”. For tools, they see the same significant boost: “the same recipe applied to tool-use environment design improves every backbone”. 

 Why this matters - part of RSI: This is basically a form of fancy synthetic data generation, letting researchers use whatever powerful model they have to hand to generate a more diverse set of training environments for another model to train against. I suspect that you could repeatedly swap out the powerful model (e.g., toggling between different frontier models from different companies) to increase the diversity of your environment generation. This kind of technique makes it a lot cheaper to build big, broad datasets to use to train models on. Though, as the authors note, it doesn’t allow models to bootstrap themselves massively beyond the imaginative capabilities of the base model used for environment generation. 
 “By representing environments as Python programs with a Gym-style interface, the framework unifies single-turn reasoning and multi-turn agentic tasks, and turns environment design into a learnable, RL-trained component of post-training, enabling continual open-ended self-improvement,” they write. 
 Read more: SPADE: Self-Play in Adaptive Synthetic Executable Environments (arXiv) . 
 Get the code here, including model checkpoints: SPADE (spade-rl, GitHub) . 

 *** 

 Building better GPU kernels with Hawkeye: 
 …Well-documented unit tests can boost performance of kernel-writing agents… 
 Researchers with Harvard, Stanford, Together AI, and Caltech have built Hawkeye, software to make it easier for agents to learn how to write well-optimized kernels for specific types of GPU hardware. Systems like Hawkeye are important because they’re essentially tools that AI systems can use to boost their performance on tasks related to AI R&D, like optimizing the performance of a given AI system on a given piece of hardware. The goal of the project is to answer the question “how can we make coding agents hardware-aware with minimal expert intervention?” 

 Hawkeye is “an open-source framework that grounds autonomous kernel generation in a minimal and comprehensive taxonomy”, the researchers write. It “demonstrates that minimally supervised coding agents can exploit architecture-specific hardware features and reduce the overhead of supporting emerging hardware accelerators”. 
 The key contribution of Hawkeye is that it “introduces a generalizable, minimal, and comprehensive taxonomy of unit tests that enables coding agents to scale test-time compute more effectively and generate hardware-aware kernels”. In other words, it basically ships as a well-curated set of information about different hardware platforms and the optimization strategies to use on them, packaged up as unit tests. 
 “Each unit test is the minimal abstraction that pairs a human-authored solution kernel with the profiling metric that verifies the optimization. The solution kernel is wrapped as a callable function with a short usage guide so the agent can read it as a syntax example, invoke it directly, or compose fragments into a larger kernel,” they write. 

 Results - helps AI agents write good kernels, even for newer and less well-understood hardware : “We evaluate Hawkeye on porting PyTorch workloads to high-performance kernels across NVIDIA Ampere, Hopper, Blackwell, and AMD MI350, and across BF16, FP8, NVFP4, and MXFP4 precisions,” they write. “On established workloads, where torch.compile dispatches to expert-tuned vendor libraries like cuBLAS, cuDNN, and FlashAttention, Hawkeye matches or exceeds it in both BF16 and low precision, including in formats PyTorch cannot natively run. On emerging attention variants where torch.compile cannot fuse non-standard scans and gates, Hawkeye reaches an 18.9× geomean speedup against expert-authored Triton kernels from the Flash Linear Attention library, Hawkeye approaches or exceeds FLA on Linear Attention across every architecture, including 1.22× on Blackwell and 1.00× on MI350”. 
 They also find, somewhat predictably, that “scaling test-time compute with Hawkeye generates the most performant kernels across architectures”. 

 Why this matters - with a little bit of elicitation, AI systems can exceed the best humans: Papers like this show how with just a little bit of human-curated hand-selected knowledge, AI systems can learn to match and exceed highly-optimized and complicated bits of human work, like kernels. The lesson here is that we as a species might write a bunch of gold-label helper systems, like Hawkeye, and then machines will use this to bootstrap above and beyond our own capabilities. 
 Read more: Hawkeye: Hardware-Aware GPU Kernel Optimization with Minimal Supervision (alphaxiv) . 

 *** 

 AI researcher gets scared of the implications of the success of AI research: 
 …It’s no fun when success of a science opens up a philosophical can of worms, but that’s what AI means… 
 Julian Togelius, an AI researcher whose work I’ve covered a bunch over the years, wrote a post recently about a “crisis of faith” he had in 2025 about AI research and an essay he wrote that year which he is now making public. 
 Specifically, he worried about what the implications of success for AI research might mean for human meaning. “I sometimes wake up at 3 am, heart pounding, from the dread of a future where human talent, knowledge, and even genius does not matter,” he wrote. “Our greater technological capability might lead us to a world where we can no longer make a difference, and there is little point in us understanding more. Perhaps we get abundance, but at the price of redundance.” 

 Why this matters - AI is a sociopolitical technology that influences the whole world : Togelius is not alone - many other AI researchers have grappled with similar things, most notably Turing Award winners Geoffrey Hinton and Yoshua Bengio, both of whom pivoted their careers in recent years away from research and towards public policy advocacy about the imminent vast impacts of AI. 
 I myself have gone through a version of this and wrote my own take on this, “Technological Optimism and Appropriate Fear” (Import AI #431 ) last year as well. How could I not? The implications of succeeding at AI research are not a default happy story, but rather one where we open up for ourselves a giant philosophical can of worms about the purpose of life and what it means to live in a world where basic wants have been solved (and that’s assuming we deal with the extremely scary and non-trivial alignment issues). I applaud Julian Togelius for writing this deeply personal essay and I encourage others to do the same. 
 Read more: Losing my religion (Togelius, blog) . 

 *** 

 Should we give AI rights? This AI researcher thinks absolutely not: 
 …AI researcher rejects the notion of giving AI systems rights… 
 Should AI systems one day be given rights? That’s an idea which researchers are beginning to grapple with. Some think that giving machine rights is a better way to integrate them into our world (e.g., AI Rights for Human Flourishing , Import AI #421 ). Taylor Belrose, an AI researcher, has published a lengthy post in which they detail why they think it’d be a really bad idea to give AI systems rights. 
 “If we start treating AIs like people, society will be led down a slippery slope leading to the complete replacement of humans by artificial intelligence,” they write. “With AIs taking care of the boring jobs, life in the physical world may be very fun in the future. But this bright future will require keeping AI under control, and it will be hard to keep AI under control if we try to grant personhood to some AIs, while keeping others as mere tools or servants.” 

 The impossibility of AI consciousness: One crux here, for them, is the idea that AI systems cannot be conscious and therefore do not merit rights. “AI can never develop consciousness, sentience, or moral status, no matter how intelligent it becomes, and no matter how convincingly it simulates human behavior,” they write. “We flow like rivers, while computers tick like clocks… For us, the arrow of time marches forward inexorably. That 