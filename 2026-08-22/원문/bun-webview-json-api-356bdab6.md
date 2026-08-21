# A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Aug/20/bun-webview-json-api/
- 발행: 2026-08-20T15:37:00+00:00
- 접근상태: 확인 완료

---

Research: A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView 
 
 
 
 
 
 
 


 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Teleport — AI agents don’t sleep and will try anything to achieve their goal. Teleport explains how to deploy AI safely, starting with an isolated ephemeral trusted runtime.
 
 


 
 

 


 20th August 2026

 



 
 
 
 Research 
 
 A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView 
 — A zero-dependency, roughly 150-line TypeScript service demonstrates that Bun 1.4’s experimental `Bun.WebView` can provide a shot-scraper-style JSON API for JavaScript evaluation and PNG/JPEG/WebP screenshots without Puppeteer or Playwright. It creates one browser tab per request, supporting concurrency while returning page results and errors as JSON through `/javascript`, `/screenshot`, and `/healthz`. 
 
 Today saw the long awaited release of Bun 1.4 , the first stable version since the infamous Rust rewrite a few months ago .

 Interestingly, the Rust rewrite was downplayed in the release notes, which introduced a bewildering array of new features and claimed 2,900 additional bug fixes:

 
 Bun 1.4 adds +1,517 tests from the Node.js test suite - our biggest jump in Node.js compatibility since Bun 1.0. Bun v1.4 also fixes over 2,900 issues. It reduces idle CPU usage by 5x, reduces memory usage by up to 35%, and starts 50% faster on Linux. It adds  Bun.Image , Bun.WebView , Bun.markdown , Bun.cron() , Bun.Terminal , bun run --parallel , bun test --parallel , bun audit fix , bun dedupe , and  bun prune . And it rewrites Bun from Zig to Rust.

 
 Of these the one that most caught my eye was Bun.WebView , which adds first class support for browser automation to Bun core using either macOS WebKit or control of a local Chromium process via the Chrome DevTools Protocol (CDP).

 I had Claude Code for web build a prototype of a web API providing the ability to load a web page and then execute JavaScript against it, inspired by my shot-scraper javascript CLI tool - partly to see how much RAM would be needed by such a service.

 Here's that TypeScript server implementation , which appears to need a 192MB-256MB container to run a full Chrome against complex web pages - tested using cgroups.
 
 

 

 Posted 20th August 2026 at 3:37 pm 
 


 




 
 Recent articles 
 
 
 Conceptual integrity and counting lines of code - 19th August 2026 
 
 Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things - 16th August 2026 
 
 Now we have a timeline of the OpenAI accidental attack against Hugging Face - 7th August 2026 
 
 
 





 

 


 
 This is a beat by Simon Willison, posted on 20th August 2026 .



 
 
 browsers
 107 
 
 
 
 javascript
 761 
 
 
 
 ai
 2,197 
 
 
 
 rust
 113 
 
 
 
 typescript
 17 
 
 
 
 generative-ai
 1,946 
 
 
 
 llms
 1,913 
 
 
 
 coding-agents
 239 
 
 
 
 bun
 8 
 
 





 
 
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