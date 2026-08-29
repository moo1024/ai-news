# I accidentally turned LLM memory into program analysis

- 출처: Hacker News
- 원본 링크: https://pwning.systems/posts/llm-memory-program-analysis/
- 발행: 2026-08-28T23:27:45+00:00
- 접근상태: 확인 완료

---

I accidentally turned LLM memory into program analysis :: pwning.systems 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 


 

 

 
 
 
 
 pwning.systems 
 MENU 
 
 
 
 ABOUT 
 
 BUGS 
 
 LINKS 
 
 POSTS 
 
 RSS 
 
 
 
 
 

 
 
 
 I accidentally turned LLM memory into program analysis 
 
 [ 28 Aug 2026 ] // JORDY ZOMER // 19 MIN READ
 
 
 Over the past few months I have been playing around quite a bit with LLM agents, particularly for vulnerability research.

 They are becoming surprisingly good at navigating large codebases, explaining unfamiliar subsystems and helping explore potential attack surfaces. However, once an investigation starts taking a few hours, I kept running into the same problem: the model would slowly lose track of what we had actually established.

 It might suggest an approach that we had already ruled out, forget that an assumption turned out to be false, or confidently continue reasoning from an observation that was no longer valid. Obviously, telling an LLM that something is wrong does not necessarily mean that it will stop believing all of the things that depended on it :)

 I initially started looking into memory systems because I wanted to make LLMs more useful for complex vulnerability research and reduce this type of hallucination.

 There are of course already plenty of solutions for giving LLMs memory. Usually this involves storing old conversations or observations somewhere, embedding them, and then retrieving the most relevant pieces whenever the model needs them again.

 This works reasonably well, but there was something about it that bothered me.

 During a vulnerability research sesh, I don’t just want the model to remember what we said.

 I want it to maintain what we currently know .

 Imagine that during an investigation we establish the following:

 
 attacker controls object_a
 object_a points to object_b
 object_b is a kernel object
 From this, we may conclude that the attacker can control a kernel object.

 A normal memory system could store all of these observations and retrieve them again whenever we ask about the exploitability of the bug. The LLM then figures out the same conclusion.

 Great! 

 However, suppose that two hours later we discover in LLDB that object_a does not actually point to object_b , and that our previous observation was based on a wrong assumption.

 At that point our memory may contain something like:

 object_a points to object_b
 attacker can control object_b
 object_a does not actually point to object_b
 Now we retrieve some subset of these memories and hope that the LLM correctly figures out which conclusions are still valid.

 This started to feel a little familiar to me.

 This looks like program analysis 
 A lot of the work I normally do involves program analysis.

 When analysing a program, we usually have a bunch of facts about the program and some rules that derive additional facts from them.

 For example, imagine we know:

 calls(foo, bar)
 calls(bar, baz)
 We could define a rule stating that if one function calls another function, which itself can reach a third function, then the first function can reach the third function as well.

 Eventually we calculate a fixed point containing everything we can derive from the program. More importantly, if one of our input facts changes, there are plenty of techniques for updating only the affected results instead of rerunning everything from scratch.

 This is also exactly what I wanted from an LLM during vulnerability research.

 If an observation changes, I don’t want the model to reconstruct the entire investigation from a transcript and hopefully notice all of the consequences. I want the affected conclusions to become invalid automatically.

 When looking at the problem from this perspective, I started wondering why we were making the LLM reconstruct its entire state over and over again.

 What if we just maintained it? 

 And this is how I somehow ended up writing a Datalog engine for LLMs :)

 Datalog 
 Before we continue, it is probably useful to briefly explain what Datalog actually is.

 
 Datalog is a declarative logic programming language. Instead of writing instructions describing how something should be calculated, we describe facts and rules from which new facts can be derived.

 
 For example, we could store the following facts:

 controls ( attacker , object_a ). 
 points_to ( object_a , object_b ). 
 kernel_object ( object_b ). 
 And then define the following rule:

 controls_kernel_object ( Attacker ) :- 
 controls ( Attacker , ObjectA ), 
 points_to ( ObjectA , ObjectB ), 
 kernel_object ( ObjectB ). 
 From our existing facts, the engine can therefore derive:

 controls_kernel_object ( attacker ). 
 Nothing particularly exciting yet.

 However, suppose we later discover that:

 points_to ( object_a , object_b ). 
 was incorrect.

 If controls_kernel_object(attacker) was derived from that fact, we know exactly which conclusion depends on the observation that just changed, and we can automatically invalidate it.

 This is considerably nicer than putting all of the old information into a prompt and asking an LLM to hopefully notice the same thing.

 Lemmalog 
 This eventually turned into Lemmalog .

 The basic idea is that an LLM should not necessarily be responsible for maintaining its own knowledge. Instead, I split the problem into two parts.

 The LLM handles the fuzzy part:

 "LLDB shows that the freed object is later reused
 as the destination of the write."
 |
 v
 freed(object_a)
 reused_as(object_a, write_target)
 And Lemmalog handles the deterministic part:

 facts
 |
 v
 rules
 |
 v
 derived facts
 This means that the LLM is still responsible for understanding natural language, source code, debugger output and all the other messy information that appears during an investigation.

 LLMs happen to be quite good at this.

 But once that information has been converted into structured facts, we no longer need the model to repeatedly determine all of its consequences. The database can do that instead.

 Retractions 
 One of the first interesting problems I ran into was removing facts.

 Adding facts to a Datalog database is relatively straightforward: add the new fact and evaluate any rules which may now produce additional results.

 Removing something is a little more annoying.

 Take the following example:

 a . 
 b . 
 c :- a . 
 c :- b . 
 Here c has two separate reasons for being true.

 If we remove a , we cannot simply remove c , because b still provides another derivation for it. However, if we remove both a and b , c should disappear as well.

 This turns out to be quite important during vulnerability research, because a conclusion may be supported by multiple observations.

 For example:

 candidate_3_is_exploitable
 may remain true even if one particular exploit primitive turns out not to work, because there is another independent path to the same result.

 So Lemmalog has to keep track of how facts were derived and update their support when something changes.

 Conveniently, this also gives us another useful property:

 we can ask why something is true. 

 Why? 
 Imagine we have been running an agent for a few hours while investigating something and it eventually concludes:

 candidate_3_is_exploitable
 That is nice, but I would also quite like to know why.

 Because Lemmalog already tracks the dependencies of derived facts, we can ask it for the provenance of a conclusion. For example, we may get something that conceptually looks like this:

 candidate_3_is_exploitable
 |
 +-- attacker_controls_pointer
 | |
 | +-- observation_41
 |
 +-- pointer_reaches_target
 |
 +-- observation_57
 +-- rule_12
 If observation_41 later turns out to be incorrect, we know that this conclusion may no longer be valid, and because the database knows this as well, it can remove the affected conclusions automatically.

 This was originally mostly necessary to make incremental evaluation work correctly, but it turns out that being able to ask an AI agent why it believes something is quite useful as well :)

 It also addresses one of the more annoying failure modes I encountered with LLM-assisted research. Sometimes a model will confidently say something like:

 we already established that this pointer is attacker-controlled
 when that is not actually true.

 If a conclusion exists in Lemmalog, I can ask where it came from. If there is no provenance supporting it, then it is not part of the maintained state.

 This obviously does not prevent an LLM from hallucinating during extraction, but it does make it much harder for unsupported conclusions to silently become part of the investigation.

 Facts also change over time 
 Another issue is that replacing old facts is not always the same as deleting them.

 Suppose we originally believe:

 primitive_a is viable
 and later discover:

 primitive_a is not viable
 For most current queries, we probably only care about the second statement. However, if we want to understand why we previously explored a particular exploit strategy, the old state is still useful.

 For this reason Lemmalog can associate facts with validity intervals.

 Conceptually, we can represent the state as something like:

 viable(primitive_a) [10:14, 12:37)
 not_viable(primitive_a) [12:37, ...)
 This allows us to answer both:

 Is primitive_a viable now?
 and:

 Why did we think primitive_a was viable earlier?
 without keeping two apparently contradictory facts around and asking the LLM to decide which one we meant.

 Again, this is not really a language model problem.

 It is mostly a database problem.

 Why not just use a vector database? 
 Vector databases are very useful.

 If I ask:

 What did we find earlier about this allocation path?
 semantic search is probably exactly what I want.

 But cosine vibe similarity and truth are not quite the same thing.

 A vector database can retrieve:

 object_a points to object_b
 because it is relevant to my question. It does not inherently know that the statement was disproven two hours later, or that five other conclusions depended on it and should therefore no longer be considered valid.

 This made me realise that there are really two different problems hiding under the term “memory”.

 The first is:

 What information from the past is relevant to this question?
 The second is:

 Given everything we have learned so far, what is currently true?
 Retrieval is very good at the first problem.

 Lemmalog is mostly an experiment in solving the second one.

 The two can also be combined, which is what I currently do.

 A vulnerability investigation is basically an analysis state 
 The more I worked on this, the more similarities with program analysis started appearing.

 During a vulnerability investigation we have observations:

 this field is attacker-controlled
 assumptions:

 this object survives until the second callback
 relationships:

 primitive_b depends on primitive_a
 hypotheses:

 this could become an arbitrary write
 and conclusions:

 candidate_3 is exploitable
 This maps surprisingly well to the things we already do in program analysis.

 We have input facts:

 observations
 rules:

 relationships between observations
 derived facts:

 conclusions
 a fixed point:

 everything currently known
 and when an input changes, we perform incremental evaluation:

 update affected conclusions
 Because we track dependencies, we can also explain where results came from:

 provenance
 At some point it became fairly obvious that I had approached the problem like a static analysis engine without intentionally meaning to.

 This also changed how I thought about the role of the LLM itself.

 You can almost think of the whole system as a slightly strange compiler.

 The LLM acts as the front-end:

 source code,
 debugger output,
 natural language notes
 |
 v
 structured facts
 Lemmalog is the intermediate representation and analysis engine:

 structured facts
 |
 v
 deductive rules
 |
 v
 maintained state
 Another LLM invocation can eventually turn that state back into natural language, suggest the next experiment, or use it to perform some action.

 The amusing part is that our parser is probabilistic, while everything after it does not necessarily have to be.

 Does it actually make LLMs better? 
 This is of course the important question.

 The engine itself now supports incremental evaluation, retractions, provenance, temporal facts, aggregations, entity reconciliation, hybrid retrieval, demand-driven queries and a bunch of other things that I probably added because implementing Datalog features is more fun than I expected.

 There is also an MCP server which allows agents to use Lemmalog directly.

 But none of that matters very much if giving an LLM this memory does not actually improve anything.

 So I plugged it into MemEval and tested it on both LongMemEval and LoCoMo using their standardized reader models and evaluation setup. Extraction during ingestion is Claude Sonnet 4.6 (chunked and file-cached, so it is paid once per conversation); everything after extraction uses the benchmark’s own standardized readers and judges.

 The results were a little better than I expected.

 LongMemEval 
 LongMemEval tests whether an LLM can answer questions about information spread across long conversation histories. The split I used contains 102 questions, divided equally between user facts, assistant facts, preferences, multi-session questions, temporal reasoning and knowledge updates.

 Because 17 questions per category is not exactly a massive sample size, I ran Lemmalog three times rather than getting excited about whichever run happened to score highest.

 The result was:

 Lemmalog
 F1: 0.463 +/- 0.010
 Accuracy: 0.575 +/- 0.004
 For comparison, the published memory-system results are:

 PropMem 0.550
 SimpleMem 0.480
 Lemmalog 0.463 +/- 0.010
 OpenClaw 0.244
 Full Context 0.222
 My own full-context GPT-4.1 run scored 0.197 F1.

 So Lemmalog is not beating PropMem yet