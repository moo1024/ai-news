# AI-written code is still your code

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://martiansoftware.com/articles/ai-written-code-is-still-yours
- 발행: 2026-08-31T12:08:25+00:00
- 접근상태: 확인 완료

---

AI-Written Code Is Still Your Code. Are You OK With That? 
 Martian
Software, Inc. Home Open Source atomicfileoutputstream blobstore hope and doubt macnificent martian-hex martian-log tictac twothousandfortyeight Archived Projects... jar2sh JSAP nailgun nearshare.net rundoc snip tarproxy tivonage trivial persist ChatKeeper ChatKeeper Home Download Purchase All Releases Roadmap CLI Quick Start Guide Command Line Helper Windows Command Line
Help Terms of Service /
EULA Privacy Policy Blog Newsletter AI-Written Code Is Still Your Code. Are You OK With That? Marty Lamb |
August 25, 2026
 Back to Index 
 Coding agents keep pushing the cost of writing software close to zero. This is valuable because writing software has historically been a big part of the work needed to ship software. For a lot of projects, testing, documenting, packaging, and other code-adjacent work have consumed much less effort, when they’re done at all.
 But the writing part has always bundled with it another important part that we’ve been taking for granted: understanding software. Aside from the most basic comp sci homework problems, it’s pretty hard to write something you don’t understand and still get a passing grade from your professor, your boss, or your customers. We’ve taken this understanding part so much for granted because we’ve rarely needed to think of it as separate from writing the code. Sure, there’s a lot out there on designing systems so that others can understand them, but I’m talking about understanding our own code. That we wrote. Ourselves. Because of course you understand that! Right?
 Anyone who has written code for any amount of time has had the humbling experience of finding something they wrote a long time ago and wondering what the hell they were thinking. But at the time, it made sense to them, and they were able to reason about it.
 Now that agents do the writing for us, the whole understanding bit is becoming optional. Heck, just have agents review and test the code too, and we can avoid those pesky mental models altogether!
 We’ve never needed to treat understanding our own code as a separate cost from writing it, because writing it largely forced us to understand it. 
 If your application is sufficiently low-stakes, cool. Go nuts. I’ve done this myself for one-off personal tooling and a couple of fun little projects that would otherwise forever inhabit my “someday” pile.
 But when you build software, you own it, and I don’t only mean in the intellectual property sense. You also take on the responsibility for its quality and its security, and for debugging, operating, maintaining, and evolving it over time. Are you prepared for that when building software with AI? That’s the new question: not “Can we build this?” but rather “Do we want to own this?” It should at least be a conscious decision rather than a responsibility you discover after the code is already yours.
 Human understanding of generated code is increasingly looking like the new bottleneck. I’m not alone in that conclusion. It’s crystal clear that AI can be a complexity factory. 
 I’ve been thinking a lot lately about what software would look like if we made keeping software understandable to humans a first-class design goal in the age of AI. Not necessarily understanding every line of an application at all times, but designing systems whose individual pieces are understandable and whose boundaries let humans zoom in and out and safely reason about them at multiple levels. It’s led to some interesting ideas that I’m continuing to develop.
 Discuss this post on Hacker News 
 Building software that developers can actually understand, own, and reason about? Thinking about complexity, developer experience, or how AI changes the way we build?  
 Let's compare notes! 
 Back to Index 
 Get updates in
your inbox.
Unsubscribe at any time. 
 About 
  ⋅  
 Contact 
  ⋅  
Martian mascot and logo design by Betsy Lamb