# How well do agents use test/verification techniques?

- 출처: Hacker News
- 원본 링크: https://danluu.com/agentic-testing/
- 발행: 2026-09-08T02:58:16+00:00
- 접근상태: 확인 완료

---

How well do agents use test/verification techniques? 



 How well do agents use test/verification techniques? 
| Patreon 


 We previously noted that, while it's easier than ever to hit a particular quality bar by having coding agents use effective test techniques, software quality seems to be getting worse , indicating that whatever defaults developers are using may not work very well. Here, we test if simple instructions to agents to use particular techniques or libraries improve implementation correctness, as a kind of test to see how effective agents are when guided by someone with no expertise in testing who's maybe heard that you should apply certain techniques or use certain libraries.


 We'll re-use the Zstd implementation eval discussed in this comparison of agentic programming language effectiveness and, instead, compare different testing techniques and testing libraries when agents are given a prompt to implement Zstd with different addendums, such as "Use test-driven development", "Use Lean 4", "Use QuickCheck", "Use property-based testing", etc. I also ran some other evals, such as on the IMAP RFC, which are briefly discussed.


 All implementations were in Rust. The 26 prompt conditions tested were ACL2, Alloy, "Audit and fuzz risky areas", "Audit first", Creusot, Default (no additional instructions), Differential testing, Fuzzing, Hegel, Insta, Judgement (agents asked to use the best technique), Kani, Lean 4, "Make no mistakes", Metamorphic testing, Mutation testing, Property-based testing, Proptest, QuickCheck, rstest, Rust built-in test framework, SMT solvers (with Z3, cvc5, and Yices, all available), Spin, TDD, TLA+, and Verus. Additional, 4 skills were tested: Hegel with the official Hegel skill , the ECC Rust test skill (ECC is a collection of skills with 250k GitHub stars and 38k forks), the Trail of Bits property test skill , and a test skill I wrote (I'm a luddite who uses prompts instead of skills and have no feel for how to write a good skill). Other than my skill, the skills were chosen because those were the top skills codex turned up when asked to find relevant skills.


 Predictions 

 I pre-registered some guesses on how conditions will do:


 
 TDD will underperform (55% confidence)

 
 I actually added TDD specifically because I thought it would underperform 
 My confidence is low here because I don't know what agents will do when instructed to do TDD; perhaps agents won't do TDD and will do something that doesn't underperform (or perhaps I'm wrong about TDD underperformance) 
 
 Formal methods will not overperform (52% confidence)

 
 My thought here is that formal methods are effective and useful (more so now than ever), good test methods are also effective and useful and, on simple problems, formal methods shouldn't outperform if used at a similar level of competence 
 As with the above, but even more so, my confidence is low here because I don't know what agents will do when instructed to do anything, and formal methods have been more hyped than effective test techniques for agentic coding, so it's entirely plausible that labs have trained agents with RL environments with synthetic data which trains them to be very effective with formal methods without having trained agents to be effective with good test techniques (which I would expect to be easier to do, but not done because of how relatively untrendy effective test techniques are) 
 
 Make no mistakes will not outperform no instructions (95% confidence)

 
 It's a joke, and one that a lot of people have tried. If it worked, surely people would've noticed? 
 
 The ECC test skill (with 250k stars and 38k forks) will not outperform (65% confidence)

 
 It's somewhat big and doesn't have any information I'd expect to be useful. It instructs agents to use TDD; to the extent that it gets agents to use TDD, I'd expect this to make things worse (and it's more directive than the TDD condition and perhaps more likely to succeed, although for all I know that makes it less likely to succeed); the rest of the information doesn't seem useful and has some cost 
 All of my skill predictions are low confidence because I don't tend to use skills and don't know how to really evaluate them. I'm thinking of this like, "how effective would it be if I passed the text in as a prompt and had this thing floating around in the LLM's context window?" 
 
 Hegel's skill will not outperform (65% confidence)

 
 It's very big (the SKILL.md plus the linked Rust reference are over 20k tokens) and reads more like a tutorial than agent instructions 
 
 The Trail of Bits test skill will not outperform (55% confidence)

 
 It has what looks like it might be useful information, but it's also fairly big 
 
 

 Overall results 

 Below, we have a very messy graph which shows the results for the conditions tested (codex with GPT-5.6 Sol, with medium and xhigh efforts). When looking at data, I tend to prefer much denser and messier graphs than most people, such as the first graph here . Because most people find these kinds of graphs unreadably messy, I tend to split information out into a series of graphs, each of which shows less information, when presenting information to others. For reasons discussed elow, I'm not going to do this here and am just going to present this extremely messy graph where we have cost on the x axis and the fraction of runs that passed 100% of the (hidden) tests on the y axis, average of 80 runs from each condition and effort (mousing over items shows bootstrap covariance, 50% uncertainty , and there's some attempt at making like things similar colors, e.g., blue-ish for formal methods, green-ish for property-based testing, etc.):



 
 
 
 


 One thing we can see is that nothing really wildly outperforms. However, Default (no additional instructions) does well above average. Looking at xhigh, on average, the fuzzing and PBT-related conditions did a little better than formal methods on average, with the situation being a lot more mixed at medium. The testing-related skills codex recommended we try underperformed, although our quick custom skill did ok (a major difference is that our skill is designed to nudge away from their default behavior towards more productive behaviors whereas the other skills seem more like tutorials). TDD didn't do well, as predicted (one skill also suggested that agents used TDD, and that skill also fared poorly in the cases where agents attempted to follow the instruction).


 If we actually look at what agents did, it quickly becomes apparent that, in general, agents don't know how to use these tools or techniques very well. As we noted here , and as everybody I've talked to has also noted, agents are really bad at testing and don't seem to understand how to test reasonably "by default". For example, here's a comment by Gary Bernhardt :


 
 AI agents' approach to testing, more or less:


 
 Take the pathological cases dreamed up by someone objecting to mocks 15 years ago, without ever having actually used mocks. Naive dreams of excessive mocking.
 

 Make those pathologies the backbone of your testing strategy.
 
 
 

 It turns out, if you ask agents to use a particular test technique or test library, this approach doesn't change as much as you'd hope. We'll look at what happened in cases in more detail, but at a high level, with test techniques, agents tend to either just write the tests they would normally write, but inside a framework for a different type of test technique, or they'll use a technique superficially but not really do the things that get the value out of the technique. For the most part, when a technique was named, they did what Gary described, but with respect to that technique (for example, for formal methods, they mostly proved irrelevant properties and with property-based testing, agents would lean heavily on totally random inputs and heavily hit invalid/rejection cases or find a trivial property to check and run low-value random cases against the trivial property). Results weren't materially different on the IMAP RFC (where I tried 40 runs of each condition) or other random RFCs (where I tried a few individual runs). In general, regardless of the type of problem, whether it's some kind of bit manipulation problem like Zstd, a protocol like IMAP 1 , or anything else, agents did not use formal methods or test libraries or techniques in an effective way.


 On xhigh, agents were generally able to get the tests they wrote to pass, but they wrote poor tests (e.g., they'd submit four identical bitstreams into a test of a feature that uses four bitstreams and miss any bug that would occur because they transposed bitstreams). And as we noted previously on the Zstd eval with respect to languages , running at a lower effort level in a naive loop gets worse results (agents do even more of this and stall out with lower correctness).


 I'm curious why AI labs haven't created RL envs to get agents to learn how to test well since software not working reasonably seems important for coding agent adoption and it also seems like the kind of thing that's amenable to RL. As we previously saw, agents have gotten quite good at bounded runtime optimization problems , which makes sense because that's exactly the kind of thing you cheaply create a ton of RL envs to train on. Maybe this is one of those things that's harder than it seems when you try it, but creating RL envs for effective testing and test techniques seems like it's in the same class of problem. Perhaps the limiting factor is just that knowledge of effective test techniques isn't very widespread, so no one's thought to try it and people are getting agents to test inefficiently (for example, by doing standard unit testing) 2 , or maybe this problem is much harder to package up than runtime optimization for some reason? It's possible this will be a moot point soon if agents get so good that they can generally write correct code without testing or verification, but at least for the state of publicly available agents from inception until now (September 2026), it seems like agents having some idea how to test without being guided by a testing expert would've substantially increased agentic coding effectiveness.


 Below we'll look at how agents did things for each condition, ordered from worst correctness to best, but I would caution anyone against drawing any kind of strong conclusions from the ordering.


 A lot of the failures here seem analogous to the failures we saw when we looked at the impact of programming language on token usage and correctness , in that the failures are often idiosyncratic. For example, with programming languages, we saw that agents had a fairly high rate of getting the semantics of byte conversion incorrect in Clojure but not Java, even though agents "should" (and probably sort of do) know that they can get Java byte conversion semantics by converting with unchecked-byte instead of byte .


 Although people have all sorts of hand wave-y high-level explanations for why some languages are better for agents than others, when we look at what agents actually do and what the failure modes are, none of the explanations I've heard for why someone's pet language is suited for agentic coding, whether it's Elixir or Ocaml or J, are actually true (with the exception of comments about Rust's memory safety, which were validated in the multi-language pandoc eval we tried by comparison memory safety issues between agent-written C, C++, and Rust ). Instead, we see a bunch of idiosyncratic failures that happen for unclear reasons 3 . With languages, because we can observe a moderate correlation between language popularity and performance (both lower cost and higher correctness), it seems reasonable to guess that the reason is because there was more training data (possibly synthetic data and not just human-written code) for more popular languages. Here, there isn't a clear pattern, other than that agents are mostly not very effective at applying test or verification techniques when all they have is the name of a library or technique (we'll discuss what works better afterwards). If you don't want to read about what happened in each condition, click here to skip to the last item .


 Verus 

 Verus uses an SMT solver and various types of reasoning to prove that the code matches specifications.


 Although Verus can prove that code matches specifications, agents didn't do that. Instead, they made proofs about various abstract properties relating to Zstd. I've not used a tool like Verus myself, so I can't speak to what an expert or even a beginner user would normally do, but from reading the tutorial, I find it a bit odd that agents didn't attempt to use Verus to verify any of the actual code and only used it to do abstract reasoning, as it seems designed to make it easy to prove properties about the actual code.


 Additionally, if we look at the properties proved, there were generally few properties proved and the properties that were proved were uninteresting. For example, agents would prove things like "given a valid cursor/index/distance, the resulting operation remains in bounds", which isn't bad to prove, but wasn't really a source of bugs. Also, agents would frequently write vacuous proofs that were effectively A => A . An actual Verus proof of this form was:


 requires 
 0 < a <= window, 
 0 < b <= window,
 0 < c <= window,
 ensures
 0 < c <= window,
 0 < a <= window,
 0 < b <= window,
 

 In cases where agents actually proved something, they generally proved something relatively simple and avoided proving properties about the parts that were likely to have a bug (for example, agents often failed to reverse the bitstream order for encode and decode and would write tests that failed to detect this because the tests were palindromic; perhaps some kind of proof of reversal here might get agents to "think" about this in a different way).


 It doesn't seem th