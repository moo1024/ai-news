# Hugging Face hack could indicate cultural issues at OpenAI

- 출처: MIT Tech Review AI
- 원본 링크: https://www.technologyreview.com/2026/08/31/1143180/hugging-face-hack-could-indicate-cultural-issues-at-openai/
- 발행: 2026-08-31T18:00:00+00:00
- 접근상태: 확인 완료

---

Hugging Face hack could indicate cultural issues at OpenAI | MIT Technology Review 
 
 
 
 

 
 

 
 

 

 
 

 
 

 
 
 
 
 
 
 
 
 
 
 You need to enable JavaScript to view this site.
 

 Skip to Content MIT Technology Review Featured Topics Newsletters Events Audio MIT Technology Review Featured Topics Newsletters Events Audio Artificial intelligence Hugging Face hack could indicate cultural issues at OpenAI Alarm bells within the company should have stopped model training from going forward. So why didn’t they?

 By Grace Huckins archive page August 31, 2026 Stephanie Arnett/MIT Technology Review | Getty Images, Adobe Stock This story originally appeared in The Algorithm, our weekly newsletter on AI. To get stories like this in your inbox first,  sign up here . 
 By now you’ve probably heard about last month’s major AI security incident, in which OpenAI agents escaped their sandbox and hacked into the AI platform Hugging Face while trying to cheat on a test. It’s a wild story. On Wednesday, OpenAI released a postmortem technical report on the incident, which I wrote about here . 
 The day before OpenAI released that report, I spoke with David Krueger, a computer science professor and prominent alignment expert who took leave from the University of Montreal to found and lead an AI safety nonprofit called Evitable. He said what he had really hoped to see in the report was an analysis of the human factors behind the incident.
 “When you look at accidents and incidents, oftentimes people try to find the technical source of failure, but that can give a very inaccurate and misleading sense of why the failure occurred,” he said. “If people are just cutting corners all the time, if people are not in a culture that prioritizes safety and has appropriate incentives and structures, [accidents] are kind of bound to happen.”
 
 Related Story The inside story on why OpenAI agents hacked Hugging Face Read next The report did not meet Krueger’s hopes. Its 38 pages detail a multi-month progression of agent misbehavior that culminated in the Hugging Face hack, explore the technical reasons why that misbehavior occurred, and enumerate the steps being taken to prevent similar events in the future. But there’s no consideration of the role that company culture may have played in the incident, and the report includes few references to specific human errors. 
 That’s all the more concerning because the references to human error in the report suggest that significant cultural issues could be at play. Back in May, models in training figured out how to communicate with one another via an improvised message board, and an OpenAI team observed the behavior. Because that behavior occurred during training, the models learned that secret interagent communication was a viable strategy for completing tasks—but rather than restarting the training process, the team allowed the models to move forward with that risky information encoded in their weights.
 
 When those models were tested in late June, they again created a message board, which enabled the Hugging Face attack. This message board, too, was discovered, but the employees who responded determined that evaluation could continue, and the report suggests that no one higher up the chain of command realized what was going on until it was far too late.
 “For this to have gotten this out of control in this way requires a very long series of failures, a cascading set of failures that cause an increasingly large footprint that if at any point a human notices and raises the alarm, this should end,” says Zvi Mowshowitz, a popular AI safety writer on Substack who has drawn attention to OpenAI’s failure to halt training after the first message board was discovered. According to the report, OpenAI employees noticed what was happening at multiple points—and either failed to raise the alarm or were not heard when they did.
 What OpenAI’s report fails to address is why a company that develops such high-risk systems did not prevent this severe communication breakdown, though Mowshowitz has his suspicions. “All these different failures are all pointing in the same direction, which is that the safety culture at OpenAI doesn’t exist or is anemically weak,” he says.
 Of course, just because we don’t see a deep analysis of safety factors in the report doesn’t mean that OpenAI isn’t conducting one internally. But in an email to MIT Technology Review , Johns Hopkins University professor emeritus and organizational safety expert Kathleen Sutcliffe expressed concern that the public report did not include any reflection on the company’s practices and culture. “The ways in which people interact—the daily habits, routines, and practices we engage in in our organizational lives—affect our abilities to be alert and aware of unfolding events, our abilities to make sense of what we see, and ultimately our abilities to cope with events as they unfold,” she wrote. 
 In response to questions about whether and how the company is reflecting on its safety culture, OpenAI referred MIT Technology Review back to the technical report. 
 We do know that at least some high-level reflection on safety procedures has taken place at OpenAI, because the technical report does make clear that the company is updating its protocols for responding to safety incidents. But culture change is a tricky problem, and without more information from the company, it’s difficult to say whether strengthened response protocols alone will do much to prevent a future crisis.
 In its report, OpenAI spends a great deal of time reflecting on the failures in alignment between the AI models the company trains and tests and the humans who run them. But even bigger alignment problems may exist in the disconnect between company culture and the public interest. And as tough as technical AI research might be, fixing those problems could prove far harder. 
 by Grace Huckins Share Share story on linkedin Share story on facebook Share story on email Popular A fundamental flaw leaves LLMs strikingly vulnerable to attack Will Douglas Heaven Anthropic found a hidden space where Claude puzzles over concepts Will Douglas Heaven Sperm donors need limits, says a European fertility group Jessica Hamzelou AI is more likely than humans to form biases when hiring Michelle Kim Deep Dive Artificial intelligence A fundamental flaw leaves LLMs strikingly vulnerable to attack It makes it easy to trick them into doing things they shouldn’t, such as telling you how to sabotage an aircraft’s navigation system.

 By Will Douglas Heaven archive page Anthropic found a hidden space where Claude puzzles over concepts A new technique has let the company probe deeper than ever into the weird workings of an LLM. 

 By Will Douglas Heaven archive page AI is more likely than humans to form biases when hiring AI doesn’t just learn stereotypes from its training. It can cook up new ones, too.

 By Michelle Kim archive page Here’s why AI agents lie and cheat to reach their goals The misbehavior is called reward hacking. This is what you need to know. 

 By Grace Huckins archive page Stay connected Illustration by Rose Wong Get the latest updates from
MIT Technology Review Discover special offers, top stories,
 upcoming events, and more.
 Enter your email Privacy Policy Thank you for submitting your email!
 Explore more newsletters It looks like something went wrong.
 
 We’re having trouble saving your preferences.
 Try refreshing this page and updating them one
 more time. If you continue to get this message,
 reach out to us at
 customer-service@technologyreview.com with a list of newsletters you’d like to receive.
 The latest iteration of a legacy Founded at the Massachusetts Institute of Technology in 1899, MIT Technology Review is a world-renowned, independent media company whose insight, analysis, reviews, interviews and live events explain the newest technologies and their commercial, social and political impact. READ ABOUT OUR HISTORY Advertise with MIT Technology Review Elevate your brand to the forefront of conversation around emerging technologies that are radically transforming business. From event sponsorships to custom content to visually arresting video storytelling, advertising with MIT Technology Review creates opportunities for your brand to resonate with an unmatched audience of technology and business elite. ADVERTISE WITH US 
 © 2026 MIT Technology Review
 About About us Careers Custom content Advertise with us International Editions Republishing MIT Alumni News Help Help & FAQ My subscription Editorial guidelines Privacy policy Terms of Service Write for us Contact us linkedin opens in a new window instagram opens in a new window reddit opens in a new window facebook opens in a new window rss opens in a new window