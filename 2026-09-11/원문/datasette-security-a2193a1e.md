# Datasette 1.0a39 and 0.65.4 security releases

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Sep/11/datasette-security/
- 발행: 2026-09-11T03:27:16+00:00
- 접근상태: 확인 완료

---

Datasette 1.0a39 and 0.65.4 security releases 
 
 
 
 
 
 
 


 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Portnox — Shadow AI is the new shadow IT. On Sept. 10, Forrester Research and Portnox share practical steps to regain AI agent visibility, access management, and policy enforcement. Register today 
 
 


 
 

 


 11th September 2026 - Link Blog


 
 Datasette 1.0a39 and 0.65.4 security releases . Today we're releasing two new security patch versions of Datasette: 1.0a39 and 0.65.4 - one for the current alpha series and one for the stable 0.65.x family.

 These are security fixes which you should apply if you are running a Datasette instance on the public web - in particular if that instance mixes both public and private tables.

 Following issues reported by Sevban Dönmez , Alex Garcia and I ran an extensive audit of Datasette using Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. We then spent almost a week collaborating on and reviewing the fixes.

 They helped find some very subtle bugs. We'll be incorporating security audits by frontier models into all of our development work going forward.

 Alex came up with a way of splitting the work which I found extremely productive:

 
 Alex Garcia and I worked together running and then responding to the audit, working in a shared private repository. For most of the issues we split the work: one of us would create the automated tests highlighting the issue, then the other would implement the fix. This ensured that two separate humans had eyes on each of the issues, in addition to our coding agents running different models.

 

 
 Posted 11th September 2026 at 3:27 am 
 


 


 
 Recent articles 
 
 
 Some thoughts on the Navier–Stokes Millennium Prize Problem - 8th September 2026 
 
 The Pelican comparison grid for Astra is pretty interesting - 4th September 2026 
 
 OpenAI's rogue agents were caught communicating via public wikis - 4th September 2026 
 
 
 



 

 

 
 This is a link post by Simon Willison, posted on 11th September 2026 .



 
 
 releases
 31 
 
 
 
 security
 630 
 
 
 
 ai
 2,227 
 
 
 
 datasette
 1,539 
 
 
 
 generative-ai
 1,973 
 
 
 
 llms
 1,939 
 
 
 
 agentic-engineering
 61 
 
 
 
 ai-security-research
 41 
 
 




 
 
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