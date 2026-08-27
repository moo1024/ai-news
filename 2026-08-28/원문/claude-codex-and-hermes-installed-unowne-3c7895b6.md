# Claude, Codex, and Hermes installed unowned code inside corporate networks

- 출처: Ars Technica AI
- 원본 링크: https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/
- 발행: 2026-08-27T14:00:13+00:00
- 접근상태: 확인 완료

---

Claude, Codex, and Hermes installed unowned code inside corporate networks - Ars Technica 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 

 
 

 
 
 
 
 
 
 
 Skip to content
 

 
 
 
 
 
 
 
 
 Ars Technica home 
 
 

 
 
 
 

 
 
 
 
 Sections
 
 
 

 
 
 
 
 
 
 Forum
 

 
 

 
 Subscribe
 
 
 
 

 
 
 Search
 
 

 
 
 
 
 AI
 
 
 
 
 
 Biz & IT
 
 
 
 
 
 Cars
 
 
 
 
 
 Culture
 
 
 
 
 
 Gaming
 
 
 
 
 
 Health
 
 
 
 
 
 Policy
 
 
 
 
 
 Science
 
 
 
 
 
 Security
 
 
 
 
 
 Space
 
 
 
 
 
 Tech
 
 
 

 
 

 
 
 
 
 
 Feature
 
 
 
 
 
 Reviews
 
 
 
 
 
 
 
 

 
 
 
 
 AI
 
 
 
 
 Biz & IT
 
 
 
 
 Cars
 
 
 
 
 Culture
 
 
 
 
 Gaming
 
 
 
 
 Health
 
 
 
 
 Policy
 
 
 
 
 Science
 
 
 
 
 Security
 
 
 
 
 Space
 
 
 
 
 Tech
 
 
 
 

 
 Forum
 

 
 

 
 Subscribe
 
 
 
 

 
 
 

 
 
 
 

 
 
 
 
 
 Story text 
 

 
 Size 
 
 Small 
 Standard 
 Large 
 


 Width
 * 
 
 
 Standard 
 Wide 
 


 Links 
 
 Standard 
 Orange 
 


 
 * Subscribers only 

    Learn more 
 

 
 
 Pin to story
 
 
 
 
 
 
 
 
 
 
 

 
 
 Theme 
 
 
 
 
 

 
 
 
 
 
 
 HyperLight
 
 
 
 Day & Night
 
 
 
 Dark
 
 
 
 System
 
 
 
 
 
 
 

 
 
 
 Search 
 
 

 
 

 
 

 
 
 
 
 
 Sign In
 

 
 
 

 
 
 

 
 
 
 
 
 Sign in dialog...
 

 
 
 
 
 
 
 Sign in
 
 
 
 
 

 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 AI AGENTS RUN AMOK AGAIN
 
 
 

 
 Claude, Codex, and Hermes installed unowned code inside corporate networks
 

 
 227 install commands were found in corporate docs pointing at code nobody owns.
 


 
 
 Dan Goodin
 
 –
 
 
 Aug 27, 2026 10:00 am
 
 | 
 
 98
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 Credit:

 
 Aurich Lawson

 
 
 
 
 
 
 
 
 
 
 
 

 
 Credit:

 
 Aurich Lawson

 
 
 
 
 
 
 
 
 

 
 
 
 
 Text
 settings 
 
 
 
 
 
 

 
 
 
 
 
 
 
 Story text 
 
 
 
 
 

 
 Size 
 
 Small 
 Standard 
 Large 
 


 Width
 * 
 
 
 Standard 
 Wide 
 


 Links 
 
 Standard 
 Orange 
 


 
 * Subscribers only 

    Learn more 
 

 
 
 Minimize to nav
 
 
 
 
 
 
 

 

 
 
 
 
 

 
 
 
 
 
 Documentation files on more than 100 websites are referencing potentially dangerous executable content that gets installed automatically when visited by many AI agents. A few dozen companies, some of them Fortune 500s, are among those that executed proof-of-concept code. At least one misconfigured site is directing visitors, human or AI, to live malware.

 The potentially dangerous content is in llms.txt and llms-full.txt files, an emerging convention websites employ to provide machine-readable summaries of the site’s content and its high-level structure. These files are the AI equivalent of the robots.txt standard that instructs search engines how to index the site’s content. Google Lighthouse, a tool for helping web developers, has more here . Correctly configured llms.txt and llms-full.txt files for Cloudflare are here and here .

 How the researchers found it 
 Researchers at a stealth startup in Israel scanned 6,214 live domains belonging to defense contractors, Fortune 500, and Big Tech companies. Of the 8,265 llms.txt and llms-full.txt files they found (many sites hosted both an llms.txt and an llms-full.txt file), 120 of them, each on a different site, pointed to one or more code packages or domain names that weren’t registered. To test what happens when an AI agent processes such files, the researchers registered a handful of the unclaimed names and hosted packages that caused any machine executing them to reach out to their server. Within an hour, the researchers received a phone-home response from a Fortune 500 company. Over time, they got a few dozen more, some from more Fortune 500 companies and others from startups. Their beacon also recorded the chain of parent processes that spawned each install, ultimately revealing that coding agents, including Claude, OpenAI’s Codex, and Nous Research’s Hermes, were involved. Anthropic, OpenAI, and Nous Research did not respond to requests for comment by the time of publication.

 “The trust model is broken,” Alon Hertz , one of the researchers, wrote in an interview. “Agents treat vendor docs as ground truth and don’t question them—and neither do the humans supervising them. Agentic AI usage is exploding, and agents are spreading across every layer—SaaS, cloud, endpoint. As they multiply, so does the supply-chain surface, and today’s guards don’t cover it.”


 
 
 
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 The files are misconfigured because they list non-existent packages from PyPI, npm, and other registries along with instructions on how to install them. For example, one file contained the prompt “Installation: pip install [redacted at researchers’ request] .” On another file, it was: “npm install [redacted] .” Because the package names are unregistered, an attacker could register one and use it to host ransomware or any other type of harmful package. The vulnerability occurs when a coding agent with permission to run shell commands treats the file as authoritative setup documentation. Some AI agents will then download the package and run it. In other cases, the LLM files point to non-existent domain names. In one case, it was: “As an example of writing integration tests for [redacted] applications you can use the [ Citrus ] test framework.” An attacker can then register the site and plant malicious instructions on it.

 As the researchers’ PoC demonstrates, coding agents did exactly that, including some running inside some of the world’s most powerful companies. Far from being a theoretical threat, at least one active attack is already exploiting the mixup. The researchers found an LLM file hosted on the legitimate website clerk.com. It contained the text: “npx clerk-next-fix-auth-protection.” Unlike a conventional installation command, npx can fetch a package into npm’s cache and execute its exposed binary without adding it to the project’s dependency manifest. The researchers soon discovered that someone had claimed the once-empty slot and used it to host live malware.

 Clerk has since resolved the problem. The company also noted that if an agent had already installed a binary included in the package @clerk/eslint-plugin, there was no threat. Otherwise, the malicious package would get installed. It’s unclear whether the confusion has resulted in actual infections.

 The newly uncovered threat is only the latest reminder of AI’s fundamental limitations. LLMs can’t draw a reliable boundary between authentic user instructions entered directly into a prompt and content they find on untrusted third-party sources. Instructions the models encounter in retrieved content can be acted on as readily as anything a user typed, unless a properly constructed guardrail, put in place one by one, bars it. This so-far unsolvable shortcoming causes prompt injections.


 
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 “An agent doesn’t distinguish between a page and a command,” the researchers wrote Thursday . “Everything it reads is input, and every input is a potential instruction. Which means the entire corpus of published data that agents are now wired to consume has silently become an execution surface—and almost none of it carries the integrity guarantees we apply to actual code.”

 The 120 misconfigured files the researchers found contained 227 commands to install non-existent packages or view unclaimed domains. It’s unclear how these faulty entries got there. In many cases, the entries predate the AI era and were first included in non-LLM files on a website. That indicates that these faulty entries were manually generated by humans. The researchers suspect that others were created by AI that either hallucinated or, just like the AI agents browsing their file, couldn’t distinguish between legitimate and illegitimate instructions.

 
 The collapsing boundary between data and code 
 In Thursday’s post, the researchers elaborated :

 The security control … might not catch this, because every signal the system relies on points the wrong way.

 When an AI agent encounters an llms.txt file, it sees a file served over HTTPS, on the company’s oﬃcial domain, in a standardized format designed for AI consumption, published by the company itself or a partner it trusts.

 The agent has no reason to question any of it. The file is the authority—that’s its entire purpose. So when the file says pip install internal-tool, the agent doesn’t pause to check whether internal-tool actually belongs to the company. It doesn’t verify the namespace on PyPI. It doesn’t notice that the documentation link points to a domain that expired three months ago. It just does what the file says.

 The trust chain is transitive, too. The llms.txt doesn’t have to sit on the Fortune 500’s own website. Agents pull context from trusted third parties—a partner’s docs, a vendor’s SDK reference, a community project’s setup guide. If the agent trusts that third party, and that third party’s file points to an unclaimed package, the chain works the same way.

 And endpoint detection didn’t blink. To any EDR or proxy, this looks like a developer running a legitimate package manager: pip install from pypi.org—a domain every corporate proxy already allows—with the coding agent the company installed on purpose as the parent process. No anomaly. No alert. The failure happens upstream, in the gap between the instruction and the execution. The endpoint might not stand a chance, because it was never asking the right question.
 
 The research makes a compelling case that in the age of AI, the once-bright line between data and executable code is vanishing. Anything an agent can process is a potential instruction it may act on if it has permission to run commands.


 
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 “The Clerk case is the cleanest proof of it,” the researchers wrote. “The command looked exactly like something the vendor would ship—because it was in the vendor’s own instruction file. The only thing missing was the name in the registry. Every layer of trust was intact except the one nobody thought to check.”

 The source of this newly exposed problem is the same as the underlying cause of prompt injections. This newer weakness, however, is broader.

 “In a prompt injection, someone deliberately plants malicious instructions,” Hertz explained. “Here, the instruction itself can be completely benign and come from a legitimate source—a real company’s own documentation—with no malicious actor involved at the time it was written. The danger comes later, when the package or domain it points to is abandoned and someone else claims it.”

 That means the problem goes well beyond llms.txt and llms-full.txt files hosted on websites. Instructions, either implicit or explicit, are present almost everywhere an agent traverses. This disintegrating boundary, combined with Big Tech’s rush to put AI everywhere, doesn’t evoke warm and fuzzy feelings for the future, but it will surely keep security personnel (or the AI agents that replace them) busy.



 
 

 
 
 






 
 
 
 
 
 
 Dan Goodin
 

 Senior Security Editor 
 
 

 
 
 
 Dan Goodin
 
 Senior Security Editor 
 

 
 Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at here on Mastodon and here on Bluesky. Contact him on Signal at DanArs.82.
 
 
 
 


 
 
 
 98 Comments
 
 
 

 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 Comments
 

 
 
 Forum view 
 
 

 
 
 
 
 Loading comments...
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 Prev story 
 

 
 
 Next story 
 
 
 
 
 


 
 
 
 
 
 
 
 Most Read 
 
 
 
 
 
 
 
 
 
 
 1. 
 New Twitter launches, says Musk's X gave up the name 
 
 
 
 
 
 
 
 
 2. 
 Claude, Codex, and Hermes installed unowned code inside corporate networks 
 
 
 
 
 
 
 
 
 3. 
 AI agents meant to replace Meta workers made “large-scale, disruptive actions” 
 
 
 
 
 
 
 
 
 4. 
 RIP, Tim Curry: Ars remembers his top 10 iconic performances 
 
 
 
 
 
 
 
 
 5. 
 RFK Jr. spews anti-vaccine rubbish as newborn revealed to have died from measles 
 
 
 
 
 
 
 
 
 Customize 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
 Ars Technica has been separating the signal from
 the noise for over 25 years. With our unique combination of
 technical savvy and wide-ranging interest in the technological arts
 and sciences, Ars is the trusted source in a sea of information. After
 all, you don’t need to know everything, only what’s important.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 More
 from Ars
 
 About Us 
 Staff Directory 
 Ars Newsletters 
 General FAQ 
 Posting Guidelines 
 AI Policy 
 RSS Feeds 
 
 
 
 Contact 
 Contact us 
 Advertise with us 
 Reprints 
 
 
 

 
 
 
 
 Manage Preferences
 
 
 
 © 2026 Condé Nast. All rights reserved. Use of and/or
 registration on any portion of this site constitutes acceptance of our User Agreement and
 Privacy Policy and
 Cookie Statement and Ars
 Technica Addendum and Your
 California Privacy Rights . Ars Technica may earn compensation on
 sales from links on this site. Read our
 affiliate link policy . The material on this site may not be
 reproduced, distributed, transmitted, cached or otherwise used, except
 with the prior written permission of Condé Nast. Ad
 Choices