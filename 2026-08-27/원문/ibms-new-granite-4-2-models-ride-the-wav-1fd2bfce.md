# IBM's new Granite 4.2 models ride the wave of interest in local LLMs

- 출처: Ars Technica AI
- 원본 링크: https://arstechnica.com/ai/2026/08/ibms-new-granite-4-2-models-ride-the-wave-of-interest-in-local-llms/
- 발행: 2026-08-26T11:10:49+00:00
- 접근상태: 확인 완료

---

IBM's new Granite 4.2 models ride the wave of interest in local LLMs - Ars Technica 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 

 
 

 
 
 
 
 
 
 
 Skip to content
 

 
 
 
 
 
 
 
 
 Ars Technica home 
 
 

 
 
 
 

 
 
 
 
 Sections
 
 
 

 
 
 
 
 
 
 Forum
 

 
 

 
 Subscribe
 
 
 
 

 
 
 Search
 
 

 
 
 
 
 AI
 
 
 
 
 
 Biz & IT
 
 
 
 
 
 Cars
 
 
 
 
 
 Culture
 
 
 
 
 
 Gaming
 
 
 
 
 
 Health
 
 
 
 
 
 Policy
 
 
 
 
 
 Science
 
 
 
 
 
 Security
 
 
 
 
 
 Space
 
 
 
 
 
 Tech
 
 
 

 
 

 
 
 
 
 
 Feature
 
 
 
 
 
 Reviews
 
 
 
 
 
 
 
 

 
 
 
 
 AI
 
 
 
 
 Biz & IT
 
 
 
 
 Cars
 
 
 
 
 Culture
 
 
 
 
 Gaming
 
 
 
 
 Health
 
 
 
 
 Policy
 
 
 
 
 Science
 
 
 
 
 Security
 
 
 
 
 Space
 
 
 
 
 Tech
 
 
 
 

 
 Forum
 

 
 

 
 Subscribe
 
 
 
 

 
 
 

 
 
 
 

 
 
 
 
 
 Story text 
 

 
 Size 
 
 Small 
 Standard 
 Large 
 


 Width
 * 
 
 
 Standard 
 Wide 
 


 Links 
 
 Standard 
 Orange 
 


 
 * Subscribers only 

    Learn more 
 

 
 
 Pin to story
 
 
 
 
 
 
 
 
 
 
 

 
 
 Theme 
 
 
 
 
 

 
 
 
 
 
 
 HyperLight
 
 
 
 Day & Night
 
 
 
 Dark
 
 
 
 System
 
 
 
 
 
 
 

 
 
 
 Search 
 
 

 
 

 
 

 
 
 
 
 
 Sign In
 

 
 
 

 
 
 

 
 
 
 
 
 Sign in dialog...
 

 
 
 
 
 
 
 Sign in
 
 
 
 
 

 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 Enterprise AI
 
 
 

 
 IBM’s new Granite 4.2 models ride the wave of interest in local LLMs
 

 
 The focus is on agentic capability and predictable enterprise deployment.
 


 
 
 Samuel Axon
 
 –
 
 
 Aug 26, 2026 7:10 am
 
 | 
 
 103
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 Pulling Granite 4.2 8B via Ollama in macOS.

 
 Credit:

 
 Samuel Axon

 
 
 
 
 
 
 
 
 
 
 
 Pulling Granite 4.2 8B via Ollama in macOS.

 
 Credit:

 
 Samuel Axon

 
 
 
 
 
 
 
 
 

 
 
 
 
 Text
 settings 
 
 
 
 
 
 

 
 
 
 
 
 
 
 Story text 
 
 
 
 
 

 
 Size 
 
 Small 
 Standard 
 Large 
 


 Width
 * 
 
 
 Standard 
 Wide 
 


 Links 
 
 Standard 
 Orange 
 


 
 * Subscribers only 

    Learn more 
 

 
 
 Minimize to nav
 
 
 
 
 
 
 

 

 
 
 
 
 

 
 
 
 
 

 IBM has rolled out the newest models in its family of open-weight large language models designed to be downloaded and self-hosted. The newly launched Granite 4.2 comes in 3B, 8B, and 30B parameter variants.

 Like previous versions, IBM is taking a decoder-only approach here. These new releases offer a 128,000-token context window natively. The 8B and 30B variants (not the 3B one) also go through an agentic reinforcement-learning block; they were trained for expanded capabilities like using the terminal, searching the web, or using external tools. The 3B model supports tools too, but without the same level of specialized training.

 Beyond those tweaks, this release is particularly notable because, as IBM itself writes, “Granite 4.2 is the reasoning-focused release of the Granite language-model family.”

 When researchers or developers in the field say a model is capable of reasoning, they do not mean it in the same sense as we often assume when talking about human reasoning; the models are not consciously understanding the problem. Instead, they’re talking about functional reasoning, in particular via “chain-of-thought” and carrying intermediate results forward through multiple steps.


 
 
 
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 For the user, this means more rigorous and accurate responses in some cases, but often slower response times and higher compute demands.

 IBM’s Granite family of models rarely grabs headlines for being the fastest or most aggressively innovative. Relative to even other competitors in the local enterprise space, like Nvidia’s Nemotron, the pitch seems to be predictable deployments—which is the priority you might expect from IBM these days.

 There has been an enormous amount of discourse about the cost and compute crunch around frontier cloud models from companies like Anthropic or OpenAI lately. Across many domains, both individual developers and enterprise organizations have been exploring local models as cheaper alternatives.

 That has also led to increased interest in model routers—AI tools whose main job is to interpret user prompts, tasks, or projects and route them to appropriately scoped models to balance performance, speed, and cost.

 Models like this are also popular with hobbyists, AI researchers, and individual developers because they can be tinkered with on local hardware without per-token API fees.



 
 

 
 
 






 
 
 
 
 
 
 Samuel Axon
 

 Senior Editor 
 
 

 
 
 
 Samuel Axon
 
 Senior Editor 
 

 
 Samuel Axon is the editorial lead for tech and gaming coverage at Ars Technica. He covers physical and generative AI, large language models, software development, gaming, entertainment, and mixed reality. He has been writing about gaming and technology for nearly two decades at Engadget, PC World, Mashable, Vice, Polygon, Wired, and others. He previously ran a marketing and PR agency in the gaming industry, led editorial for the TV network CBS, and worked on social media marketing strategy for Samsung Mobile at the creative agency SPCSHP. He also is an independent software and game developer for iOS, Windows, and other platforms, and he is a graduate of DePaul University, where he studied interactive media and software development.
 
 
 
 


 
 
 
 103 Comments
 
 
 

 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 Comments
 

 
 
 Forum view 
 
 

 
 
 
 
 Loading comments...
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 Prev story 
 

 
 
 Next story 
 
 
 
 
 


 
 
 
 
 
 
 
 Most Read 
 
 
 
 
 
 
 
 
 
 
 1. 
 World humanoid robot games show runners breaking records, bursting into flames 
 
 
 
 
 
 
 
 
 2. 
 Apple's new desktop computers are designed specifically for local AI development 
 
 
 
 
 
 
 
 
 3. 
 The world's busiest spaceport is about to get a lot quieter, at least for now 
 
 
 
 
 
 
 
 
 4. 
 Google's anti-nausea Motion Assist dots finally rolling out on Android 
 
 
 
 
 
 
 
 
 5. 
 SpaceX intends to invest up to $100 billion in massive Louisiana spaceport 
 
 
 
 
 
 
 
 
 Customize 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
 Ars Technica has been separating the signal from
 the noise for over 25 years. With our unique combination of
 technical savvy and wide-ranging interest in the technological arts
 and sciences, Ars is the trusted source in a sea of information. After
 all, you don’t need to know everything, only what’s important.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 More
 from Ars
 
 About Us 
 Staff Directory 
 Ars Newsletters 
 General FAQ 
 Posting Guidelines 
 AI Policy 
 RSS Feeds 
 
 
 
 Contact 
 Contact us 
 Advertise with us 
 Reprints 
 
 
 

 
 
 
 
 Manage Preferences
 
 
 
 © 2026 Condé Nast. All rights reserved. Use of and/or
 registration on any portion of this site constitutes acceptance of our User Agreement and
 Privacy Policy and
 Cookie Statement and Ars
 Technica Addendum and Your
 California Privacy Rights . Ars Technica may earn compensation on
 sales from links on this site. Read our
 affiliate link policy . The material on this site may not be
 reproduced, distributed, transmitted, cached or otherwise used, except
 with the prior written permission of Condé Nast. Ad
 Choices