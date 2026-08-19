# Anthropic's ‘watermark’ text adulteration in Claude is a perversion of writing

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing
- 발행: 2026-08-16T21:53:43+00:00
- 접근상태: 확인 완료

---

Daring Fireball: Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 

 
 
 
 
 
 
 By John Gruber 


 
 Archive 
 The Talk Show 
 Dithering 
 Projects 
 Contact 
 Colophon 
 Feeds / Social 
 Twitter 
 -->
 Sponsorship 
 

 
 
 
 
 WorkOS : Make your app agent-ready.

 

 

 

 
 Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing 
 Sunday, 16 August 2026 

 When I wrote this week about Anthropic’s announcement that all Claude models, worldwide, would soon begin “watermarking” everything they generate, including text, to comply with this EU regulation , we were left to speculate how this was going to work, because Anthropic offered not even a vague description of how it would work — despite the fact that the title of the announcement was, absurdly and insultingly, “ How Claude Marks AI-Generated Content ”.


 My initial speculation was that maybe they’d hide invisible non-printing Unicode characters in the text. Just spitballing. Turns out that’s not what they’re going to do. What they’re going to do is apply a form of steganography, where the choice of words (or other token output) at inference time will leave fingerprints that can later, maybe, be detected probabilistically.


 I initially guessed “invisible characters” not because I didn’t think of the semantic word-choice technique, but because I was a fool who took Anthropic at its word in their description of what they would do. Their original support document claims:


 
 When a supported Claude model generates text, it weaves an
imperceptible watermark directly into the text itself. You won’t
see it, and it doesn’t change the meaning, quality, or readability
of Claude’s response.

 

 They say “imperceptible” and “doesn’t change the meaning, quality, or readability”. Their words. Not almost imperceptible. Not slightly changes the meaning, quality, or readability. That made sense to me, because that’s absolutely what I want — nay, demand — from any tools I use personally. It’s unacceptable for a tool to sacrifice an iota of clarity, coherence, meaning, quality, etc. for the purpose of embedding hidden clues within the text to suggest its provenance. That’s what I would and will demand. And Anthropic’s (original) support document unambiguously claims that’s what their system will enable. So if that were true, I couldn’t see what was left other than hiding invisible characters within the text.


 My error was believing Anthropic that their system wouldn’t adulterate and corrupt the semantics of the text their models generate. That is in fact exactly what they plan to do. I should have my head examined for believing a single word of a document titled “How Claude Marks AI-Generated Content” that doesn’t explain, at all, how Claude marks (or will mark) AI-generated content.


 How It’s Actually Going to Work 

 Yesterday, on an entirely different website than the original “How Claude marks AI-generated content” article (the one that didn’t explain anything at all about how it works), Anthropic published “ How Claude’s Text Watermark Works ”, which does actually explain in layman-accessible terms how it’s going to work. I will return to Anthropic’s new highly euphemistic and slightly misleading description below.


 There’s a bunch of research on this topic, some of which I have also linked to below. But the very best description of the general idea behind the technique is an interactive essay by James Padolsey, “ How AI Text Watermarking Works” . It’s a wonderfully cogent read, and the interactive elements splendidly illustrate the main concepts. A+ work. If you have any interest in this at all, I dare say you must read — and play with — Padolsey’s piece.


 But here’s my stab at a layman’s high-level summary. If you toss a coin N times and note the results, you can determine with a degree of certainty whether the coin is fair or biased. LLMs are, in their popular incarnations, non-deterministic. Ask the same question of the same model and you often get at least slightly different answers. Maybe the same meaning, but different phrasing. At each decision point for generating the next token, the model makes a choice. With these semantic watermarking techniques, they make different choices for some tokens based on word lists that could be called “green” and “red”. At each decision point, they’re a little more likely to pick a word from the green list than the red list. That doesn’t mean they never choose words from the red list. Just that they’re less likely to than they would if the adulterated marking technique weren’t in place. (Same way that a crooked 51-49 coin will still land “wrong” side up 49 times out of 100 on average.)


 Words or word phrases are sorted into the green and red lists deterministically on the fly, at each “next token” generation point. So sometimes a specific word will be on the green list, and other times it will be on the red list. Someone with the secret key can determine which list a word will be on at each token generation point (which is how the watermarking is detected); those without the secret key cannot. This means there will never be a list of words that Claude prefers or eschews.


 With coin flipping, the higher N is — the more times you flip — the more confident you can be that the coin is fair or biased. So too with this semantic watermarking. The more words in the text, the more accurate the analysis will be that the text was generated by a specific AI model or not. With too few coin flips, you can’t achieve any confidence at all regarding a coin’s fairness. With too few words (or tokens), there’s no way to achieve any confidence whether a string of text was AI-generated or not.


 Given a string of text to examine for signs of a specific watermarking system, if there are more words tagged as green and fewer tagged as red than would otherwise be expected, the text can be flagged — with some degree of confidence — as having been generated, or merely modified, by the AI system that applies the specific secret-key watermarking system. The amount of confidence in the determination will obviously vary, significantly, based on the size of the text string and randomized weights given to words on the green and red lists. But only Anthropic will be able to determine if text was seemingly generated by Claude, and Anthropic will only be able to detect the watermarks that are applied by Claude. Claude can’t detect the hidden watermark signals generated by, say, Gemini, and Gemini can’t detect the hidden watermark signals created by Claude, because each implementation is predicated on secret keys held only by the LLM provider.


 Objections to the Technical Premise 

 One of my fundamental problems with this is that no two synonyms carry the exact same meaning. “ He leaped at the chance ” and “ He jumped at the opportunity ” are very similar sentences expressing the same general sentiment, but they are not the same. The exact words we choose when writing matter. I want any LLM I use to choose the very best, most precise words at every single decision point. An obvious constraint that I accept is time and computation. Within the constraint of executing inference quickly, and at a certain cost per token, I want the best words. This constraint matches human writing. I could surely write a better column by taking longer to write it. I write with a sense of how much care I should put into every word and punctuation choice I make. I take more time with certain paragraphs, sentences, or even individual word choices when my gut feeling says I should.


 In other words, these are necessary trade-offs. These factors are all in my interest: speed, cost, quality. Ideally I would like perfect writing, at instantaneous generation speed, at zero cost. None of those things are possible. Computation is not free of charge (and cloud-based LLM inference with leading models is actually expensive). Inference is not instantaneous. And great writing, whether natural or artificial, can only approach perfection.


 The idea that anything other than my needs should factor into the generation of text for me is patently offensive.


 This isn’t just about text one might generate with the intention of passing it off as their own natural work. This isn’t even about LLM proofreading of work written by hand. Anthropic is saying that all new Claude models are going to adulterate every single bit of text longer than 200 tokens (~150 words) they generate, including everything it presents to its users to read. So even in a private conversation between a user and Claude, which will never be read by anyone other than the user, Claude will begin making word choices in the name of marking its output in statistically predictable ways rather than maximizing clarity and precision.


 Even today’s so-called frontier models are already decidedly lacking in lucidity . Claude, ChatGPT, Grok, et al. are “better writers” than most humans and produce better prose than the median human. But: no shit. Most people are terrible writers. The “average person” is pretty stupid and half of all people are stupider than that . And there are many smart, interesting people who are miserable writers. So as impressive as LLMs are, the bar is low. The best writing I see come out of these models is worse than anything I would choose to read for pleasure. And now Anthropic is saying they’re going to make it worse, on purpose, for purposes that do not benefit me in any way? Even if only slightly worse?


 Get fucked.


 Objections to the EU Regulation 

 Speaking of objections, the relevant EU regulation motivating all of this, “ Code of Practice on Transparency of AI-Generated Content ”, is red-tape nanny-state pipe-dream nonsense. Here’s Ben Thompson’s summary from a paywalled Stratechery update this week :


 
 
 The regulation applies to text longer than 200 tokens. 
 The provider must mandate in their terms-of-service that users
not remove the watermarking. 
 The solution should be robust in terms of evading “typical
processing solutions” like screen shots, scanning and OCR,
copy-and-pasting, translations, etc. 
 
 

 Taken literally, compliant LLM terms of service must forbid users from rephrasing the output from models that comply with this regulation, because the word choices are the marks. But it’s not the European Union that is trying to impose their absurd, impractical, witch-hunt-fueling regulation on the entire world. That falls on Anthropic.


 Complying with this, particularly with regard to text , is only going to create problems for honest users. Dishonest users attempting to pass off AI-generated text as their own writing (students, employees, whoever) will simply circumvent detection through non-compliant AI paraphrasing tools.


 James Padolsey — whose interactive visual explanation of how these schemes work I linked to above — explains this in a post titled “ Anthropic’s Weak Watermarks Appease a Weak Law ” (which, if it rings a bell, I linked to in a standalone post earlier today):


 
 The same thought that led to this law could have applied to
calculators at the time of their inception, had their outputs
revealed themselves through artefacts. Thankfully, a sum borne of
the brain is treated no differently from one produced by a
calculator. Likewise with spellcheckers. To make assistance
suspect only once the tool becomes capable enough to compose a
whole sentence is not a principled boundary. It is a moral premium
placed on difficulty itself.


 Anthropic has nevertheless chosen a blanket, model-level
implementation that appears broader than the law’s minimum
requirement. That may be convenient compliance engineering, but it
discards distinctions the law expressly attempted to preserve. The
result is a signal broad enough to implicate harmless and
assistive use, yet fragile enough to be removed by a motivated
person through substantial recomposition. It risks concentrating
suspicion on ordinary and assistive users while remaining weakest
against deliberate deception.

 

 Padolsey is the creator of Declaude , a delightfully simple web app that allows you to “Paste in AI-flavored text and get the same content back as plain prose”. Declaude’s original purpose is cleaning the saccharine Claude personality stink from text (whether it was created by Claude or any other LLM), but, if Anthropic persists in its stated plan to begin adulterating all text Claude generates, Declaude will also serve as a copy-paste single-extra-step way to eliminates those marks. Declaude is interesting and useful already, but it exemplifies how ill-considered and futile this EU regulation is when it comes to prose.


 Google SynthID 

 Google has a watermarking system in place that they call SynthID, which they apply to AI-generated images, video, audio, and text. I’m concerned in this article only with text. With multimedia, embedded watermarks can be metadata within files , and truly not affect the experiential quality of the work when viewed or listened to. With text, we are talking about the actual words that are chosen. From the “AI-generated text” section of Google DeepMind’s own description of SynthID :


 
 We’ve expanded SynthID to watermarking and identifying text
generated by the Gemini app and web experience. Large language
models generate text one word (token) at a time. Each word is
assigned a probability score, based on how likely it is to be
generated next. So for a sentence like “My favorite tropical
fruits are mango and…”, the word “bananas” would have a higher
probability score than the word “airplanes”. SynthID adjusts these
probability scores to generate a watermark. It’s not noticeable to
the human eye, and doesn’t affect the quality of the output.

 

 In a group chat, a friend of mine quoted the above, and I responded that if a chatbot wrote “My favorite tropical fruits are mango and a