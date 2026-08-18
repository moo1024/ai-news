# Markdown SVG upgrades

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/
- 발행: 2026-08-16T23:59:37+00:00
- 접근상태: 확인 완료

---

Markdown SVG upgrades 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: WorkOS — auth.md by WorkOS: agents register users, no sign-up form. Try it! 
 
 


 
 

 


 16th August 2026

 

 I started building my markdown-svg-renderer tool in May , but I've since added enough features to it that it's worth talking about here again.

 It's evolved into my ideal tool for sharing Markdown transcripts that include SVG documents. Given my proclivity for drawing pelicans riding bicycles this is a problem that I needed to solve!

 The tool is very simple. Navigate to markdown-svg-renderer in your browser and paste in some Markdown to see it rendered... or save that Markdown to a CORS-friendly URL or a GitHub Gist and paste in a URL to that document.

 The URL option will give you a bookmarkable page, for example https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6f9e48293be5c916652d29f0dc0b0657 - which bakes in the URL to this Gist .

 If you visit the Gist you'll see raw SVG:

 

 In the rendered tool that looks like this instead:

 

 As you can see, that SVG block in the Markdown has been transformed into a rendered SVG (in this case animated) plus several tabs.

 The tabs are the really fun bit. The PNG and JPEG tabs render that SVG to those image formats in the browser and lets you copy or download them - useful for sharing on platforms that don't support SVG directly.

 The MP4 tab is new today - it examines the SVG to see if it contains any animations, attempts to guess how long the looped video should be, then renders a whole bunch of frames of the animation and loads 30+MB of ffmpeg.wasm so it can compile those frames into an MP4 video using the full power of FFMPEG compiled to WebAssembly and running in the browser.

 Being able to turn an animated SVG into a MP4 again makes it easy to share on platforms that can't support SVG animation natively. It's a neat trick!

 

 Posted 16th August 2026 at 11:59 pm 
 


 


 
 Recent articles 
 
 
 Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things - 16th August 2026 
 
 Now we have a timeline of the OpenAI accidental attack against Hugging Face - 7th August 2026 
 
 One-shotting a Raccoon Heist game using Claude Fable 5 - 5th August 2026 
 
 
 



 

 

 
 This is a note by Simon Willison, posted on 16th August 2026 .



 
 
 svg
 56 
 
 
 
 tools
 74 
 
 
 
 markdown
 35 
 
 




 
 
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