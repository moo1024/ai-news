# I miss the old Claude Code

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://alexkras.com/focus-is-the-main-feature-why-i-miss-the-old-claude-code/
- 발행: 2026-08-26T06:34:35+00:00
- 접근상태: 확인 완료

---

I Miss the Old Claude Code 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 

 

 

 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 Skip to content 
 
 
 
 
 
 
 Menu 
 Archive 
 Top Posts 
 GitHub 
 LinkedIn 
 Contact 
 
 
 
 
 
 
 
 
 
 
 
 
 I Miss the Old Claude Code 
 August 26, 2026 August 23, 2026 by Alex 
 
 
 
 Table of Contents 
 
 How Anthropic won me over 
 
 Then something changed 
 
 The Bloat 

 
 The Model 
 
 The Tooling 
 
 The Marketing 
 
 
 
 Now what? 
 
 Combating AI Bloat 

 
 5 Questions 
 
 
 
 Conclusion 
 


 Like many others, Anthropic won me slowly, over time.




 How Anthropic won me over 



 I started with generative AI through a web interface I hosted myself, using my own API keys through Open Router and my own local models. Because Open Router makes it easy to switch models, I noticed Anthropic’s models consistently gave more concise responses – they just got to the point quicker. That focus was worth a lot to me, so I drifted toward Sonnet over comparable OpenAI models.




 Then I had a task to summarize a book. I wasn’t using Opus often because I had to pay out of pocket for it, so I tried Gemini Pro first. Gemini spun for a few minutes and produced something short. Then I tried the same task in Opus. It spun its wheels for three to four minutes, and the result was exactly what I’d hoped for. I sat back, amazed at how well it worked.




 In parallel, Anthropic released Claude Code. I’d been trying other tools – Aider, Cursor, Copilot – but nothing worked as well. Claude Code felt like an extension of my brain. It wasn’t trying to come up with complicated engineering solutions. It would just grep the repo for relevant files, read them, and grep for more as it went on. Exploring the codebase exactly as I would.




 Then something changed 



 Somewhere along the way, things changed. Just as Anthropic slowly won me over, it has begun to slowly rub me the wrong way. I still love Claude Code. It’s highly customized to what I do and easy to extend. My current employer provides Claude Code enterprise subscription, which has proven itself to be a great productivity boost.




 But it increasingly feels like I have to fight the tool to get my work done, and it seems far less focused than it used to be. I’m not the only one, especially when it comes to Claude Opus 5. Here are some examples of people describing the same problem in their own words.




 
 Rough tier list of where I'd put every major model right now pic.twitter.com/gFDFZfECaR 
— Theo – t3.gg (@theo) August 22, 2026 
 



 (@theo rank Opus ranks below gpt-5.6-sol and luna, kimi k3, and deepseek v4 flash)




 
 You are not going crazy, Opus 5 does write really differently to other Opuses – much longer answers, more stock phrases like (load bearing), more em dashes, more clauses (if, while), but it doesn't use longer words. 

We mined 10s of thousands of Claude real world outputs from… https://t.co/Izo8Vr9yxe 
— Peter Gostev (SF 24-28 August) (@petergostev) August 12, 2026 
 



 
 You are not going crazy, Opus 5 does write really differently to other Opuses

 



 
 With all due respect to Boris Cherny, this response is part of the problem.

The complaints about Opus 5 have become pretty consistent: it’s lazy, sloppy, and verbose. That matches my own experience. Responding that people simply haven’t understood the right use case misses the… https://t.co/5uI9Ax9Noq 
— Chubby♨️ (@kimmonismus) August 23, 2026 
 



 
 The complaints about Opus 5 have become pretty consistent: it’s lazy, sloppy, and verbose.

 



 
 Anthropic once used to lead the AI race now it's nowhere to be seen.

Everything was great till Opus 4.7

After that they tried to play a strong game around Mythos and launched Fable. Didn't work out.

Opus 5 is simply verbose and prone to unrequested over-engineering.

Anthropic…
— Pratham (@Prathkum) August 22, 2026 
 



 
 Everything was great till Opus 4.7 … Opus 5 is simply verbose and prone to unrequested over-engineering.

 



 The Bloat 



 I believe the bloat I’m experiencing with Claude comes down to three areas.




 The Model 



 First, and biggest, is the model itself. Opus 5 is extremely chatty – big words, a lot of them, and it’s hard to keep it focused on the objective. It got to the point where Anthropic itself released the Concise Output Style, which was likely added just to get Opus 5 under control (lack of focus IMO predates Opus 5).




 
 Working on a longer term fix, this is a quick band aid that we found works pretty well in the meantime. More to come.
— Boris Cherny (@bcherny) August 20, 2026 
 



 The Tooling 



 Second is the tooling. The Anthropic team seems to ship fast and ship a lot. Generating code IS cheap now, but that doesn’t mean an unstoppable flow of new features is the right thing for users. 




 One example is how Claude Code refactored the /doctor command: it used to run through setup and confirm everything worked. Now they’ve turned it into an audit of all the prompts and systems – perhaps a problem outside Anthropic they’re trying to get ahead of – an ever growing bloat of skills, MCPs and Claude.md files. 




 The /doctor skill is a surface-level fix for a System problem. 




 This is where generative AI comes up short. Some of these systemic problems need systemic solutions – careful thinking and smart engineering; not just slapping something onto an existing tool.




 The Marketing 



 Anthropic has always been a little interesting (dare I say alarmist) when it came to marketing, but it never bothered at all, because the tools were so good. Their new marketing seems to lead people away from focus.




 One example is the recently released AI-native SDLC Playbook . Like Opus 5 output, I had to run it through an AI model just to make sense of it all. Assuming I understood it correctly, it advocates for a world where the /doctor situation happens daily and to the entire codebase. 




 The proposal makes it easier to turn ideas into features and code, removing friction, which is another way of saying making it easier to introduce bloat. Maybe this is Anthropic’s internal process now? This would explain the issue at hand… 




 Now what? 



 I hold the opposite view: in a world where code generation is cheap, each feature needs more attention, not less, before it hits production. Controlling the bloat may become the biggest challenge for every company in the age of generative AI. 




 As a user, fan, and early advocate of Claude Code, this is painful and sad to watch. This post is my attempt to verbalize what some of us have been feeling, and I hope Anthropic sees it and takes it into account. I encourage them to get back to the basics and stay focused.




 Claude’s advantage is not permanent and competitors are taking notice.




 Combating AI Bloat 



 Here is a framework I use daily to combat bloat.




 5 Questions 



 
 To do or not to do? 
 
 Should this exist at all? 
 
 



 Now or later? 
 
 Does it matter right now or can this wait? 
 
 



 This much or less? 
 
 What is the absolute minimum scope to get this done? 
 
 



 This way or easier? 
 
 Is there a simpler way to build this? 
 
 



 Ourselves or someone else? 
 
 Is this our core competency or should another group of people or a tool handle this? 
 
 
 



 Conclusion 



 I encourage Anthropic to address this runaway train while they still can. I appreciate the tools they’ve built, and look forward to using this technology for many years to come.

 

 
 Categories AI , Software Engineering 
 Top 28 Programming Books Recommended by Hacker News Users (Analyzed with ChatGPT) 
 
 
 

 
 

 
 Leave a Comment Cancel reply You must be logged in to post a comment.
 
	
 
 

 
 

	
 
 


 
 
 
 
 © 2026 alexkras.com • Built with GeneratePress