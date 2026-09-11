# Any Nix package, live in your browser

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Sep/10/trynix/
- 발행: 2026-09-10T23:44:15+00:00
- 접근상태: 확인 완료

---

Any Nix package, live in your browser 
 
 
 
 
 
 
 


 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Portnox — Shadow AI is the new shadow IT. On Sept. 10, Forrester Research and Portnox share practical steps to regain AI agent visibility, access management, and policy enforcement. Register today 
 
 


 
 

 


 10th September 2026 - Link Blog


 
 Any Nix package, live in your browser ( via ) Farid Zakaria calls this his " magnum opus of Nix work", and I can see why.

 trynix.dev provides a qemu-wasm powered x86_64 Linux virtual machine running entirely in your browser through WebAssembly. That VM can then be booted with any Nix package from the past 13 years. They are URL addressable, so you can navigate to this page:

 https://trynix.dev/?pkg=python3%403.6.2 

 Then click "Load" and get an interactive shell against a virtual machine running Python 3.6.2 from 2017.

 Farid is building all sorts of neat things on top of this. One recent example: Review a pull request by booting it introduces trynix-preview , described like this:

 
 GitHub action that comments a link on a pull request which lets you boot the PR’s build in the browser using https://trynix.dev . No servers, just browsers.

 

 
 Posted 10th September 2026 at 11:44 pm 
 


 


 
 Recent articles 
 
 
 Some thoughts on the Navier–Stokes Millennium Prize Problem - 8th September 2026 
 
 The Pelican comparison grid for Astra is pretty interesting - 4th September 2026 
 
 OpenAI's rogue agents were caught communicating via public wikis - 4th September 2026 
 
 
 



 

 

 
 This is a link post by Simon Willison, posted on 10th September 2026 .



 
 
 code-review
 16 
 
 
 
 linux
 54 
 
 
 
 webassembly
 131 
 
 
 
 github-actions
 72 
 
 




 
 
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