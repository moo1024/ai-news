# Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows

- 출처: 코딩에이전트 (HN)
- 원본 링크: https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/
- 발행: 2026-09-14T12:01:32+00:00
- 접근상태: 확인 완료

---

Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows - MacRumors 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 

 

 
 
 
 
 
 

 
 
 
 Skip to Content Got a tip for us? Let us know 
 
 a. Send us an email 
 b. Anonymous form 
 close 
 
 
 Open Menu Front Page Roundups Show Roundups Guides How Tos Reviews Buyer's Guide Forums Forums Show Forums menu Login Register New Posts Visit Forums Visit Forums New Posts Login Register Visit Forums Alerts Direct messages Watched New Posts Visit Forums Open Sidebar iPhone Duo iPhone 18 Pro Mac mini Mac Studio iOS 27 iPadOS 27 macOS Golden Gate MacBook Neo iPhone 17e AirTag iPhone 18 iOS 26 iPhone 17 macOS Tahoe iPhone 17 Pro MacBook Pro iPadOS 26 iMac HomePod Apple TV iPad Pro iPhone Air Apple Vision Pro iPhone 16 AirPods 5 Apple Watch Ultra 4 HomePod mini MacBook Air iPad AirPods Max 2 AirPods Pro 3 Apple Deals Apple Watch 12 Apple Watch SE 3 Studio Display iPad Air iPad mini watchOS 27 CarPlay Apple Pay watchOS 26 All > Front Page Roundups Guides How Tos Reviews Buyer's Guide Upcoming Products Forums Archives Tips / Contact Us Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows Monday September 14, 2026 4:37 am PDT by Tim Hardwick Code sleuth "pdfu" has uncovered iOS 27 and macOS Golden Gate private frameworks that show Apple has designed its new Siri architecture to work with third-party AI models at what appears to be a surprisingly deep level.

 
One mechanism called Model Delegation allows Claude to appear as a Siri extension in the same way as the existing built-in ChatGPT extension. In pdfu's video, shared on X , the macOS user brings up the "Search or Ask" bar and chooses Claude as the AI model via an "Ask..." contextual menu. 

 After enabling the Claude extension, the user asks Siri to "Ask Claude" to set a reminder in Apple's Reminders app. Claude then interprets the natural language reminder request and Siri subsequently creates the reminder. The implication is that if the request requires access to an Apple system feature, Claude hands the task back to Siri. 

 In another example, Claude can be seen in a Siri app conversation window receiving a request to create a CSV file – something Siri itself cannot handle – and successfully returning the result. 

 What's more intriguing is the second protocol demonstrated in the video that appears to go considerably further, and could really open up the AI landscape for Apple software requests. 

 An inference provider in "Model Manager Services" apparently allows Apple's own server-side Siri model to be completely replaced by another model, such as GPT-5.6. In this scenario, ChatGPT receives Apple's Siri planner prompt and tool definitions, which enables it to request system actions, receive the resulting personal data, and formulate an answer that Siri presents using its own interface and voice. 

 
 
 And here's an app extension replacing Siri AI's server model with GPT-5.6 Terra. It uses the Inference Providing protocol in Model Manager Services.
GPT-5.6 receives Apple's native Siri planner prompt and tool definitions. It can make tool calls that perform system actions, and... pic.twitter.com/cz88kyq3io 
— pdfu (@itspdfu) September 13, 2026 
 
In the demonstration video, the user asks the ChatGPT model (within the Siri app) to find emails about a specific topic, summarize their contents and action points, then send a message to a person in the user's contacts via the Messages app. The response is then shown as logged in OpenAI's platform web interface.

 The European Union's Digital Markets Act may have helped shape Apple's approach here, as it requires Apple to give third parties effective access to iOS hardware and software features available to Apple's own services, and the European Commission has specifically said this principle extends to Siri. 

 The "Ask..." implementation is currently limited to the ChatGPT extension in the macOS 27 Golden Gate Release Candidate (which is effectively the final version of the software set to be released later today), so Claude is not yet available. Meanwhile, Apple has not yet opened up the model delegation entitlement to third parties and it isn't front-facing to users, but it at least shows how extensively Apple has engineered Siri for future model interoperability.

 Related Roundups: iOS 27 , iPadOS 27 , macOS Golden Gate Tags: ChatGPT , Claude , Siri Guide , Siri AI Related Forums: iOS 27 , macOS Golden Gate [ 80 comments ] Get weekly top MacRumors stories in your inbox. 
 Leave this field empty Popular Stories iOS 27 Introduces New 'iPhone Handoff' Feature Wednesday September 2, 2026 12:35 pm PDT by Joe Rossignol Apple has added a new "iPhone Handoff" feature to iOS 27 that will allow you to switch between two iPhones while using the same phone number on each device.This functionality was briefly mentioned during the WWDC 2026 keynote in June, on a slide that listed hundreds of new features coming in iOS 27 and corresponding software updates, but Apple never shared any further details at the time.... Read Full Article • 168 comments Here's When iOS 27 Rolls Out Today in Every Time Zone [Update: It's Out] Sunday September 13, 2026 3:00 am PDT by Eric Slivka Update 10:04 a.m.: iOS 27 is rolling out now, though it may take a bit for all users to see it, so keep checking!Apple is about to release iOS 27, which will finally deliver more advanced Siri AI capabilities as well as a variety of other refinements, improvements, and new features to iPhones. It's Apple's biggest software update of the year, and Apple announced at Wednesday's iPhone event... Read Full Article • 151 comments Apple Announces iOS 27 Release Date Wednesday September 9, 2026 10:46 am PDT by Joe Rossignol At its event today unveiling the iPhone 18 Pro, AirPods 5, Apple Watch Series 12, and more, Apple announced that iOS 27 will be released later this month.iOS 27 has already been available as a developer beta since June and as a public beta since July, and Apple today said that the update will be released for all users with a compatible iPhone model on Monday, September 14.iOS 27 is... Read Full Article • 40 comments Top Rated Comments U unobtainium 16 hours ago at 04:41 am As it should be. The “walled garden” approach no longer holds when so much of our daily work and lives exists on the device. People should be able to choose which services they trust and find most useful. Thanks EU! Score: 21 Votes ( Like | Disagree ) QuarterSwede 15 hours ago at 05:17 am 
you are being very polite

After 15 years, Siri is still as dumb as day 1
 That’s not remotely true. Siri AI is a big improvement. It’s conversationally and contextually aware which makes it a lot more useful and what people generally want when asking it questions.

While playing Dogs by Pink Floyd, I asked it, “who’s playing the guitar?” It answered correctly in about 3 seconds.

Could old Siri have done that? Absolutely not.

Here’s the actual question in the Siri app where it gave an even more detailed answer. This is from my original question, I didn’t ask it again.


 

 Score: 11 Votes ( Like | Disagree ) klasma 16 hours ago at 04:48 am 
Siri AI

Now that’s an oxymoron if I’ve ever heard one
 Aspirational Intelligence Score: 8 Votes ( Like | Disagree ) A Alloween 16 hours ago at 04:43 am For me this is good news! Because less reasons for EU to complain. Score: 8 Votes ( Like | Disagree ) A aidler 16 hours ago at 05:06 am Pretty much proves that what the EU Commission said was true from the get-go, and that Apple was once again just causing unnecessary drama. Score: 7 Votes ( Like | Disagree ) klasma 16 hours ago at 04:53 am If the on-device models can be replaced by an external service, there is no reason to gatekeep the features to newer iPhone models anymore. But I doubt that Apple would open it up in that way. Score: 6 Votes ( Like | Disagree ) Read All Comments Next Article Gurman: iPhone Duo Likely to Get Face ID, Telephoto Lens by Third Gen Guides iOS 26 Features Our comprehensive guide highlighting every major new addition in iOS 26, plus how-tos that walk you through using the new features.
 iOS 26.6 Features Dozens of security fixes, plus Spotlight optimizations for upcoming iOS 27 release.
 50 macOS Tahoe Features New features and lesser-known changes to check out if you're upgrading.
 iPhone 17 vs iPhone 17 Pro vs iPhone Air Apple's four new iPhones feature more differences between the latest models than ever before, so which one should you buy?
 • Apple Intelligence Guide • iPhone Mirroring Not Working? • 21 Time-Saving iPhone Tips • 14 macOS Tips to Make Your Life Easier • Image Playground Guide • One AirPod Not Working? See more guides Upcoming iPhone 18 Pro Pre-Order Now, Launches Sep 18 iPhone 18 Pro and Pro Max with smaller Dynamic Island, new color options, A20 Pro chip, camera improvements, and more.
 Apple Watch Series 12 Pre-Order Now, Launches Sep 18 Apple's latest Apple Watch with new Health Sensing System, Audio Intelligence features, and more.
 Apple Watch Ultra 4 Pre-Order Now, Launches Sep 18 New Health Sensing System, longer battery life, and more.
 AirPods 5 Pre-Order Now, Launches Sep 18 Two new models with improved sound and comfort, standard active noise cancellation, and more.
 • Mac mini • Mac Studio • iPhone Duo • Smart Home Hub • Apple TV • HomePod mini • iPhone 18 See full product calendar Other Stories iOS 27 is Compatible With These iPhone Models 6 hours ago by Joe Rossignol
 Apple Releases Safari Technology Preview 252 With Bug Fixes and Performance Improvements 6 hours ago by Juli Clover
 iOS 27: Access the New iPhone Recovery Screen 6 hours ago by Tim Hardwick
 iOS 27 Lets You Hide the Messages Button Everyone Hits by Mistake 7 hours ago by Tim Hardwick
 iOS 27: Tone Down Liquid Glass Transparency 7 hours ago by Tim Hardwick
  
 MacRumors attracts a broad audience of both consumers and professionals interested in the latest technologies and products. We also boast an active community focused on purchasing decisions and technical aspects of the iPhone, iPad, Mac, and other Apple platforms.


 About MacRumors.com 

 Advertise on MacRumors 


 Our Staff Arnold Kim Editorial Director Email • X.com Eric Slivka Editor in Chief Email • X.com Juli Clover Managing Editor Email • X.com Joe Rossignol Senior Reporter Email • X.com Mitchel Broussard Deals Editor Email • X.com Tim Hardwick Senior Editor Email • X.com Hartley Charlton Senior Editor Email • X.com Marianne Schultz Project Manager Email • X.com Dan Barbera Video Content Producer Email • X.com Ryan Barrieau Graphic Designer Email • X.com Steve Moser Contributing Writer Email • X.com Aaron Perris Contributor Email • X.com Related Links YouTube iOS 27 is Out Now! These Are the Features You NEED to Try iPhone 18 Pro Hands-On: What Upgrades Actually Matter? iPhone Duo Hands-On: I’m VERY Impressed Apple’s HUGE September Event Recap: Everything Announced (iPhone Duo, 18 Pro, and More) Apple September 9th iPhone Event: EVERYTHING We’re Expecting! The MacRumors Show Apple Surprise and Shine Recap: iPhone Duo, iPhone 18 Pro & More! | Episode 210 iPhone 18 Pro & iPhone Ultra Event Expectations | Episode 209 Apple’s Surprisingly HUGE Week of Announcements | Episode 208 What Apple MUST Get Right With Its Foldable iPhone Ultra ft. @TheMrMobile | Episode 207 Apple Watch’s Biggest Redesign Yet Is Coming | Episode 206 Copyright © 2000-2026 MacRumors.com, LLC. 
 Privacy / DMCA contact / Affiliate and FTC Disclosure 
 Accessibility Statement 
[ Featured On/Off ] [ Full Articles On/Off ] [ Fluid | Fluid HD ] [ Auto | Light | Dark ]