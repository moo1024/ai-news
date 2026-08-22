# llm 0.33

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Aug/22/llm/
- 발행: 2026-08-22T17:01:16+00:00
- 접근상태: 확인 완료

---

Release: llm 0.33 
 
 
 
 
 
 
 


 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Teleport — AI agents don’t sleep and will try anything to achieve their goal. Teleport explains how to deploy AI safely, starting with an isolated ephemeral trusted runtime.
 
 


 
 

 


 22nd August 2026

 



 
 
 
 Release 
 
 llm 0.33 
 — Access large language models from the command-line 
 
 My highlights from this release:

 
 
 Upgraded to the OpenAI Python library 3.x and switched the HTTP client dependency from httpx to httpx2 . #1608 , #1631 
 
 
 I shipped a quick 0.32.1 fix for this yesterday, but this is the more comprehensive fix.

 
 
 llm embed and llm embed-multi now accept --key . The Python EmbeddingModel.embed() , EmbeddingModel.embed_multi() , Collection.embed() and Collection.embed_multi() methods accept key= too, passing the resolved per-call key to embedding plugins without changing shared model state. Existing plugins that read self.key continue to work through a compatibility fallback. Thanks, ChrisJr404 . #757 , #1620 
 
 
 The embedding models now use the same pattern for keys that regular LLM models do.

 
 
 llm prompt -t/--template can now be repeated to combine templates in order. This allows model configuration and options from one template to be used with a prompt from another. 
 
 
 This unlocks a neat pattern where you can create templates that package a model with a set of default options:

 llm -m gpt-5.6-luna -o reasoning_effort high --save lhigh
llm "Generate an SVG of a pelican riding a bicycle" --save pelican
# Combine and run the templates
llm -t lhigh -t pelican
 
 
 
 Reasoning-capable Responses API models now support a reasoning_summary option with auto , concise , and detailed values. This can be used with llm openai endpoint --responses . #1600 
 
 
 This is particularly useful for exercising different models that provide their own imitation of the OpenAI Responses API.
 
 

 

 Posted 22nd August 2026 at 5:01 pm 
 


 




 
 Recent articles 
 
 
 Conceptual integrity and counting lines of code - 19th August 2026 
 
 Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things - 16th August 2026 
 
 Now we have a timeline of the OpenAI accidental attack against Hugging Face - 7th August 2026 
 
 
 





 

 


 
 This is a beat by Simon Willison, posted on 22nd August 2026 .



 
 
 annotated-release-notes
 61 
 
 
 
 llm
 625 
 
 





 
 
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