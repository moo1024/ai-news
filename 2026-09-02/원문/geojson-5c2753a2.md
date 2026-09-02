# GeoJSON Map Viewer

- 출처: Simon Willison
- 원본 링크: https://simonwillison.net/2026/Sep/1/geojson/
- 발행: 2026-09-01T18:05:45+00:00
- 접근상태: 확인 완료

---

Tool: GeoJSON Map Viewer 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 




 
 
 

 
 
 Simon Willison’s Weblog 
 Subscribe 
 
 


 
 
 Sponsored by: Greptile — The Al code reviewer that runs your code. Catch bugs that only show up at runtime. Try it for free 
 
 


 
 

 


 1st September 2026

 



 
 
 
 Tool 
 
 GeoJSON Map Viewer 
 — View and visualize GeoJSON data on an interactive OpenStreetMap with customizable styling options. Paste GeoJSON objects (Feature, FeatureCollection, or Geometry) into the editor, adjust fill color and opacity, and render the features directly on the map. 
 
 I was helping Natalie gather some maps of local political boundaries (for the Granada Community Services District and the Midcoast Community Council and found a need to display some GeoJSON files on a map and export that as a PNG. I asked GPT-5.6-Sol for suggestions of tools and it proactively built one. After some iterations using Claude Code for web and Fable 5.1 we got to this finished tool.

 As for the GeoJSON.. it turns out if you ask ChatGPT Work to provide boundaries for almost anything it will churn away extracting and combining files from different Government data sources and build exactly what you need.

 I got this polygon from:

 
 I want a polygon that represents the exact boundary of the El Granada GCSD 

 
 And this one from:

 
 Get me a GeoJSON file for the boundary (or boundaries if that makes sense) for the MCC - Midcoast Community Council - that operates near Half Moon Bay CA 

 
 Here's a link that displays both of them at the same time on the new GeoJSON map viewing tool.

 
 
 

 

 Posted 1st September 2026 at 6:05 pm 
 


 




 
 Recent articles 
 
 
 Claude Fable 5.1 made me a really nice animated pelican - 1st September 2026 
 
 Understanding ChatGPT Work - 30th August 2026 
 
 Conceptual integrity and counting lines of code - 19th August 2026 
 
 
 





 

 


 
 This is a beat by Simon Willison, posted on 1st September 2026 .



 
 
 geospatial
 83 
 
 
 
 tools
 75 
 
 
 
 geojson
 16 
 
 
 
 chatgpt
 202 
 
 





 
 
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