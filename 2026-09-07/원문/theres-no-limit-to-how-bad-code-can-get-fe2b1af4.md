# There's No Limit to How Bad Code Can Get

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/
- 발행: 2026-09-06T09:08:06+00:00
- 접근상태: 확인 완료

---

Comment: There's No Limit to How Bad Code Can Get 
 
 
 
 
 
 
 


 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Portnox — Shadow AI is the new shadow IT. On Sept. 10, Forrester Research and Portnox share practical steps to regain AI agent visibility, access management, and policy enforcement. Register today 
 
 


 
 

 


 6th September 2026

 


 
 Comment My comment on There's No Limit to How Bad Code Can Get — Lobste.rs


 
 [In reply to a comment about burning it down to start from scratch when technical debt becomes overwhelming] 

 In my experience it's  so rare  for that to work.

 You announce the old thing is irrecoverably drowning in tech debt. You spin up a team to rewrite it from scratch. Work begins.

 Meanwhile the old thing remains a moving target: it's running the core business, so changes are still necessary. The developers working on it know that it's going to be made obsolete by the new thing soon, so they don't have any incentive to go beyond the smallest effort possible to add the new features. Technical debt continues to mount.

 Meanwhile, the team working on the new thing are ambitious and probably a little naive. They start out at a great pace - it's greenfield after all - but as time progresses it becomes apparent that nobody fully understands the behavior and scope of the thing they are replacing. If it was well documented and tested it wouldn't  need  to be replaced, after all...

 After months (or even years) without delivering value, the pressure is on to "ship it", so the new system is launched to handle a subset of what the old system handled - or often for some new feature that was too hard to build with the now mostly unmaintained old system.

 ... so now you have TWO systems in production - the janky old system that nobody wants to touch, and a new system which handles just a few production features and is 80% inactive code that is meant to replace the old system, eventually.

 If you're  really lucky  the company won't have lost patience with the new system and will allow that work to continue. The longer this all takes, and the longer the old system stays in production and stubbornly continues to work, the higher the risk that "priorities have changed" and the new system total replacement work is abandoned, leaving you with two systems where you used to have one.

 The best article I've read about completing this process responsibly is  Migrations: the sole scalable fix to tech debt  by Will Larson.

 If I run into a situation like this in the future, my strong recommendation will be to shore up the old system with as much automated testing as possible and then seeing if targeted refactors can get it to the desired shape. My hunch is that in many cases that will have a much higher chance of success than the siren call of a greenfield replacement.

 

 

 Posted 6th September 2026 at 9:08 am 
 


 




 
 Recent articles 
 
 
 The Pelican comparison grid for Astra is pretty interesting - 4th September 2026 
 
 OpenAI's rogue agents were caught communicating via public wikis - 4th September 2026 
 
 Claude's new system prompt really doesn't want to reproduce song lyrics - 2nd September 2026 
 
 
 





 

 


 
 This is a beat by Simon Willison, posted on 6th September 2026 .



 
 
 migrations
 14 
 
 
 
 technical-debt
 11 
 
 





 
 
 Monthly briefing
 
 
 Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments.
 

 
 Pay me to send you less!
 

 
 Sponsor & subscribe
 
 


 


 
 









 
 
 Disclosures 
 Colophon 
 © 
 2002 
 2003 
 2004 
 2005 
 2006 
 2007 
 2008 
 2009 
 2010 
 2011 
 2012 
 2013 
 2014 
 2015 
 2016 
 2017 
 2018 
 2019 
 2020 
 2021 
 2022 
 2023 
 2024 
 2025 
 2026