# llm 0.32.1

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Aug/21/llm/
- 발행: 2026-08-21T17:16:13+00:00
- 접근상태: 확인 완료

---

Release: llm 0.32.1 
 
 
 
 
 
 
 


 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Teleport — AI agents don’t sleep and will try anything to achieve their goal. Teleport explains how to deploy AI safely, starting with an isolated ephemeral trusted runtime.
 
 


 
 

 


 21st August 2026

 



 
 
 
 Release 
 
 llm 0.32.1 
 — Access large language models from the command-line 
 
 Fresh installs of LLM stopped working the other day because the OpenAI Python library dropped its usage of httpx , and it turned out LLM depended on that library but only installed it via a transitive openai dependency.

 This dot-release fixes that for the moment by pinning to openai<3 , and a soon-to-drop 0.33 release will switch from httpx to httpx2 .
 
 

 

 Posted 21st August 2026 at 5:16 pm 
 


 




 
 Recent articles 
 
 
 Conceptual integrity and counting lines of code - 19th August 2026 
 
 Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things - 16th August 2026 
 
 Now we have a timeline of the OpenAI accidental attack against Hugging Face - 7th August 2026 
 
 
 





 

 


 
 This is a beat by Simon Willison, posted on 21st August 2026 .



 
 
 httpx
 6 
 
 
 
 openai
 449 
 
 
 
 llm
 624 
 
 





 
 
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