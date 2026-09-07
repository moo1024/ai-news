# Using Blender with coding agents on macOS

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Sep/5/blender-coding-agents-macos/
- 발행: 2026-09-05T15:51:09+00:00
- 접근상태: 확인 완료

---

TIL: Using Blender with coding agents on macOS 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Portnox — Shadow AI is the new shadow IT. On Sept. 10, Forrester Research and Portnox share practical steps to regain AI agent visibility, access management, and policy enforcement. Register today 
 
 


 
 

 


 5th September 2026

 



 

 
 
 
 TIL 
 
 Using Blender with coding agents on macOS 
 — Modern frontier models have got *really good* at using Blender. I've been having a lot of fun trying this out recently - models can produce `.blend` files you can edit in Blender itself, and can also render images and even movies (by rendering a sequence of images and combining them with `ffmpeg`). 
 
 I've been having fun with Blender in ChatGPT Codex on my Mac recently. Getting it to work with coding agents is really easy: install the full Mac application from blender.org and run a prompt like this:

 
 Use the already install /Applications/Blender to render a scene of a pelican riding a bicycle 

 
 In this case I followed that up with these two prompts:

 
 OK add a background and a lot of flair 

 
 Then:

 
 OK make it a whole lot better 

 
 And got this image, generated using Blender's Python API :

 

 This was covered by my existing Codex subscription, but according to AgentsView it would have cost $4.24 at API prices for gpt-6-astra .
 
 

 

 Posted 5th September 2026 at 3:51 pm 
 


 




 
 Recent articles 
 
 
 The Pelican comparison grid for Astra is pretty interesting - 4th September 2026 
 
 OpenAI's rogue agents were caught communicating via public wikis - 4th September 2026 
 
 Claude's new system prompt really doesn't want to reproduce song lyrics - 2nd September 2026 
 
 
 





 

 


 
 This is a beat by Simon Willison, posted on 5th September 2026 .



 
 
 ai
 2,219 
 
 
 
 generative-ai
 1,967 
 
 
 
 llms
 1,934 
 
 
 
 blender
 3 
 
 
 
 pelican-riding-a-bicycle
 142 
 
 
 
 coding-agents
 245 
 
 
 
 gpt-6-astra
 5 
 
 





 
 
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