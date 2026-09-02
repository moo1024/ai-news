# llm-gemini 0.34

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Sep/2/llm-gemini/
- 발행: 2026-09-02T16:39:38+00:00
- 접근상태: 확인 완료

---

Release: llm-gemini 0.34 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Greptile — The Al code reviewer that runs your code. Catch bugs that only show up at runtime. Try it for free 
 
 


 
 

 


 2nd September 2026

 



 
 
 
 Release 
 
 llm-gemini 0.34 
 — LLM plugin to access Google's Gemini family of models 
 
 
 
 New model gemini-3.8-flash for Gemini 3.8 Flash , with low, medium and high thinking levels. #146 
 Fixed async responses failing to record the resolved model version. Thanks, Charlie Tonneslan . #137 
 
 
 Google released Gemini 3.8 Flash (and 3.8 Flash Cyber, but that's available to "trusted defenders" only) today.

 Here are the pelicans for high, medium, and low. This is high:

 

 For comparison, here are the same pelicans generated using Gemini 3.7 Flash .

 Something I appreciate about Gemini Flash is that it's fast, cheap, and competent at things like HTML and JavaScript. I was messing around with it and prompted "make me a cool thing in html" and it built this , which is certainly a cool thing in HTML! Took 13 seconds, cost 1.8 cents.

 
 
 Your browser does not support HTML5 video.
 



 If you click through to the demo you'll see one more thing I built with Gemini 3.8 Flash.

 My markdown-svg-renderer tool lets me feed in the URL to a Gist with Markdown in and renders that markdown with fenced code blocks for SVG correctly rendered.

 I used Gemini 3.8 Flash (with my very basic llm-coding-agent coding agent plugin) to add support for HTML as well, so now any HTML blocks in the Markdown are rendered using a sandboxed iframe. Here's the transcript .
 
 

 

 Posted 2nd September 2026 at 4:39 pm 
 


 




 
 Recent articles 
 
 
 Claude's new system prompt really doesn't want to reproduce song lyrics - 2nd September 2026 
 
 Claude Fable 5.1 made me a really nice animated pelican - 1st September 2026 
 
 Understanding ChatGPT Work - 30th August 2026 
 
 
 





 

 


 
 This is a beat by Simon Willison, posted on 2nd September 2026 .



 
 
 ai
 2,213 
 
 
 
 generative-ai
 1,961 
 
 
 
 llms
 1,928 
 
 
 
 llm
 627 
 
 
 
 gemini
 195 
 
 
 
 pelican-riding-a-bicycle
 139 
 
 
 
 llm-release
 228 
 
 





 
 
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