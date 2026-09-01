# Introducing wrapture

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Aug/31/introducing-wrapture/
- 발행: 2026-08-31T23:59:36+00:00
- 접근상태: 확인 완료

---

Introducing wrapture 
 
 
 
 
 
 
 


 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Greptile — The Al code reviewer that runs your code. Catch bugs that only show up at runtime. Try it for free 
 
 


 
 

 


 31st August 2026 - Link Blog


 
 Introducing wrapture . New from Graham Dumpleton (of wrapt , mod_wsgi, and New Relic's Python agent fame), who describes Wrapture as taking the monkeypatching ideas from wrapt and extending them to apply to testing and tracing at the same time.

 Wrapture ( full documentation here ) makes it easy to wrap any function or method such that all access can be traced, or can be overridden to return a different value.

 It acts as both an alternative to unittest.mock and a way to implement tracing against an existing project:

 
 Attaching observation to code you do not control, recording what flows through it, and doing so without disturbing the program being watched, is a problem I have never really stopped thinking about.

 
 Wrapture includes OpenTelemetry support and even has an entirely configuration-based mechanism for adding tracing to an existing Python project, which looks like this:

 capture = " summary " 

[[ observe ]]
 target = " domain:Calculator " 
 name = [ " outer " , " inner " ]

[[ sink ]]
 type = " jsonlines " 
 path = " trace.jsonl " 
 This is still a very young project - just a few weeks old - but it's off to a very promising start.

 Interestingly, this is also Graham's first attempt at large entirely agent-driven project:

 
 Every line of code and documentation in wrapture was written by an AI assistant working under my direction. I want to be upfront about that, and equally upfront about what it was not. This was not vibe coding, where a one-shot prompt produces a pile of generated code and the person driving hopes for the best because they lack the knowledge to judge what came back. Vibe coding has earned its bad reputation. I engineered wrapture carefully from the start. I have spent a long time in this particular corner of Python and knew exactly what the result needed to be, and the AI was the means of producing it rather than the source of the design.

 
 In a follow-up post, Unit testing with wrapture , Graham shows the testing patterns supported by the new library:

 def test_stub_with_wrapture ():
 with wrapture . binding (
 Gateway , "charge" 
 ). on_call . returns ({
 "id" : "stub" , "amount" : 0 }
 ):
 assert OrderService (). place (
 500 
 )[ "id" ] == "stub" 
 And this neat example of a test that calls and then modifies the return value from the original method:

 def test_pinned_result_with_wrapture ():
 charge = wrapture . binding (
 Gateway , "charge" 
 )
 charge . on_call . transforms_result (
 lambda r : { ** r , "id" : "ch_TEST" }
 )
 with charge :
 assert OrderService (). place (
 500 
 ) == {
 "id" : "ch_TEST" , "amount" : 500 
 } 

 (In both of these examples the OrderService().place(...) method calls Gateway().charge(...) .)

 
 Posted 31st August 2026 at 11:59 pm 
 


 


 
 Recent articles 
 
 
 Understanding ChatGPT Work - 30th August 2026 
 
 Conceptual integrity and counting lines of code - 19th August 2026 
 
 Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things - 16th August 2026 
 
 
 



 

 

 
 This is a link post by Simon Willison, posted on 31st August 2026 .



 
 
 graham-dumpleton
 5 
 
 
 
 monkey-patching
 9 
 
 
 
 python
 1,279 
 
 
 
 testing
 94 
 
 
 
 pytest
 25 
 
 
 
 observability
 9 
 
 
 
 ai-assisted-programming
 405 
 
 
 
 agentic-engineering
 60 
 
 
 
 opentelemetry
 3 
 
 




 
 
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