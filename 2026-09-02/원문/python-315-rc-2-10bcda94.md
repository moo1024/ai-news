# Python 3.15.0 candidate 2 is here!

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Sep/1/python-315-rc-2/
- 발행: 2026-09-01T14:59:18+00:00
- 접근상태: 확인 완료

---

Python 3.15.0 candidate 2 is here! 
 
 
 
 
 
 
 


 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Greptile — The Al code reviewer that runs your code. Catch bugs that only show up at runtime. Try it for free 
 
 


 
 

 


 1st September 2026 - Link Blog


 
 Python 3.15.0 candidate 2 is here! ( via ) Hugo van Kemenade (release manager for Python 3.14 and 3.15) announces the final release candidate for Python 3.15, scheduled for release in October:

 
 Entering the release candidate phase, only reviewed code changes which are clear bug fixes are allowed between this release candidate and the final release. [...]

 We strongly encourage maintainers of third-party Python projects to prepare their projects for 3.15 during this phase, and publish Python 3.15 wheels on PyPI to be ready for the final release of 3.15.0, and to help other projects do their own testing. Any binary wheels built against Python 3.15.0 release candidates will work with future versions of Python 3.15.

 
 Back in 2021 I found a bug in Python 3.10 by running my test suites against it... but I hadn't done this during the RC period, so that bug had already shipped! Since then I've always paid much closer attention to these RCs.

 The new RC isn't available for GitHub Actions just yet - keep an eye on actions/python-versions for that. For the moment though you can add this to a testing matrix:

 strategy :
 matrix :
 python-version : ["3.14", "3.15"] 

 steps :
 - uses : actions/setup-python@v7 
 with :
 python-version : ${{ matrix.python-version }} 
 allow-prereleases : true 
 check-latest : true 

 The allow-prereleases and check-latest flags mean that today this will test against RC1, and when RC2 lands it will automatically switch to that version (and then the stable version once that comes out.)

 
 Posted 1st September 2026 at 2:59 pm 
 


 


 
 Recent articles 
 
 
 Understanding ChatGPT Work - 30th August 2026 
 
 Conceptual integrity and counting lines of code - 19th August 2026 
 
 Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things - 16th August 2026 
 
 
 



 

 

 
 This is a link post by Simon Willison, posted on 1st September 2026 .



 
 
 open-source
 318 
 
 
 
 python
 1,280 
 
 
 
 github-actions
 71 
 
 




 
 
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