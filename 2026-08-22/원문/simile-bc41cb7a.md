# Simulation: the new Scaling Law — Joon Sung Park, Simile AI

- 출처: Latent Space
- 원본 링크: https://www.latent.space/p/simile
- 발행: 2026-08-21T23:37:38+00:00
- 접근상태: 확인 완료

---

Simulation: the new Scaling Law — Joon Sung Park, Simile AI 
 
 
 
 
 

 

 

 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 

 

 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 

 
 
 

 
 
 
 
 
 
 

 

 
 
 
 
 

 

 

 

 

 
 

 
 

 

 

 
 Subscribe Sign in Latent Space: The AI Engineer Podcast Simulation: the new Scaling Law — Joon Sung Park, Simile AI 25 3 1× 0:00 Current time: 0:00 / Total time: -1:09:37 -1:09:37 Audio playback is not supported on your browser. Please upgrade. Simulation: the new Scaling Law — Joon Sung Park, Simile AI Simile’s CEO about his journey from the viral Generative Agents to creating 8 Billion Digital Twins of every living human... and why it’s gone from fun exploration to very serious business. Aug 21, 2026 25 3 Share Transcript When we first dicsussed the Summer of Simulative AI in 2024 we knew it would be a brief summer, but it has recently come back with a vengeance with SimGym in April and now Simile AI’s $2B Series B , backed by GreenOaks and Index Ventures with prominent backers like Fei-Fei Li and Andrej Karpathy, running tens of millions of simulations for Fortune 100 clients like CVS and 85–99% accuracy vs human focus groups. 
 Time to catch up on why this Second Summer of simulation is working! 
 From creating Smallville , the landmark 2023 paper on Generative Agents that showed AI characters could remember, plan, socialize, and develop emergent behaviors , to now building foundation models of human behavior, Joon Sung Park is trying to answer a much bigger question: what if we could simulate the world before making decisions in it? In this episode, the Simile co-founder and CEO joins us to unpack the path from generative agents to digital twins, why today’s frontier models still fail to capture how humans actually behave, and what it would take to eventually simulate all 8 billion people on Earth. 
 We go deep on Simile’s approach to modeling human behavior : long-form interviews, observational and transaction data, randomized controlled trials, population-level and individual-level models, and post-training on the causal mechanisms behind why people make decisions. Joon explains how his research created digital twins that reproduced human behavior and attitudes 85% as accurately as people reproduced their own responses , why models optimized to be rational can be bad simulations of irrational humans, and why understanding “social physics” may require changing model weights rather than simply prompting frontier LLMs. 
 We also explore the much larger ambition behind simulation : testing products and policies before deploying them, finding counterintuitive paths toward desired outcomes, modeling emergent behavior across entire societies, and potentially tackling problems like climate change , democratic instability, and UBI . Joon reflects on scaling laws for simulation , the economics of data-center-scale simulated worlds , the connection to Thomas Schelling and psychohistory, why simulation is surprisingly similar to painting, and whether we might already be living in one. 
 We discuss: How Smallville and Generative Agents led to Simile 
 Why Joon’s team asked: “What if we can just recreate the world that we live in?” 
 Why useful personal agents require deep models of their users 
 Memory architectures, Markdown files, and the limits of prompting 
 “Social physics” and behavioral foundation models 
 Why web data captures what people say more than what they actually do 
 Interviews, transactions, observational data, and randomized controlled trials 
 Why predicting the future matters less than understanding how to shape it 
 How Simile creates representative simulated populations 
 Simulation versus prediction and the connection to Foundation’s psychohistory 
 How to evaluate simulations instead of simply stacking LLM hallucinations 
 Creating digital twins of 1,000 real people and reaching 85% behavioral accuracy 
 Why frontier models can struggle to reproduce real human behavior 
 Why good simulations need to reproduce human biases and mistakes 
 Post-training models on randomized controlled trials 
 Population-level versus individual-level simulation 
 Scaling laws for human simulation 
 The long-term ambition to simulate all 8 billion people on Earth 
 Whether simulations could help solve climate change or detect collapsing democracy 
 Thomas Schelling and the history of agent-based modeling 
 Why future simulations could require an entire data center 
 Multi-agent simulations and what happens when simulated people interact 
 Replacing expensive human panels with synthetic populations 
 Why market research is only the starting point for simulation 
 Why Joon sees simulation as surprisingly similar to painting 
 Using simulation to study questions like UBI 
 Whether we are already living in a simulation 
 Why AGI and simulation may be the twin technologies of advanced civilizations 
 Joon Sung Park LinkedIn: https://www.linkedin.com/in/joonspark 
 X: https://x.com/joon_s_pk 
 Website: https://www.joonsungpark.com 
 Simile: https://www.simile.com 
 Timestamps 00:00:00 Introduction and Joon’s Path from Art to AI 
 00:01:46 Smallville, Generative Agents, and the Origins of Simulation 
 00:05:03 “Let’s Just Create a World” and the Future of Personal Agents 
 00:09:53 Social Physics and Behavioral Foundation Models 
 00:14:08 Prediction vs. Simulation: How Do You Shape the Future? 
 00:16:59 How Simile Models Real People and Populations 
 00:25:35 Evaluating Simulations, Digital Twins, and 85% Accuracy 
 00:30:23 Post-Training Models to Reproduce Human Behavior 
 00:40:04 Scaling Laws and Simulating 8 Billion People 
 00:43:10 From Schelling to Society-Scale Agent Simulations 
 00:46:13 The Cost and Economics of Simulating the World 
 00:52:05 Real-World Use Cases, Synthetic Populations, and the Market 
 00:57:27 The Future of Simulation, Painting, and UBI 
 01:04:23 Are We Already Living in a Simulation? 
 01:06:08 Building Simile and Hiring 
 Transcript Introduction: Joon Sung Park, Simile, and the Story So Far Vibhu [00:00:00]: Today, we have Joon in the podcast. Excited to kick this one off. Very exciting company. I wanna kick off and ask you the question, talk us through the story of your life. How have you gotten here? 
 Joon [00:00:13]: Yeah, for sure. I’m really excited to be here. A story of my life. So I was born in Korea, and I lived there for a good 11 years or so of my life, and then my family moved to Boston. So we moved when I was 11, and my parents were doctors, so they were going through their postdoctoral studies. My dad was a surgeon, so he was doing his sabbatical years at the Boston Children’s Hospital. So I grew up there, not too close to tech. I was very much a music and artsy, painting kind of guy. 
 Vibhu [00:00:49]: Painting. 
 Joon [00:00:49]: Exactly. I got into painting a little bit later, in high school, but that’s what I used to do. And then I grew up mostly in the East Coast after Korea. So I lived a good number of years in New Hampshire, and then I went to college in Pennsylvania. And I got into more of this tech scene, in college. So I was originally trained to be an artist. I thought that would be my professional career. So it wasn’t a hobby. It was like, “Hey, let’s make a living out of this.” And then gradually, I got really interested in this idea of, hey, the greatest artist often creates their own medium, and the best medium that we had available today was in computation. So I decided to go deeper into that, and one thing led to another, and we can go deeper into this, but I decided that research was something that I gradually got interested in, and here I am. 
 Smallville, Generative Agents, and the 2023 Breakout Paper Swyx [00:01:46]: So there’s a lot that you packed into the research components. You had one of the best papers of 2023, which was the generative agents paper, commonly known as the Smallville paper. 
 Swyx [00:01:58]: Feel free to call back to anything else that you mentioned, but most people would have heard of you from this. Do you have any statistics on how many people have, like, read it? arXiv gives you something, right? Some stats. 
 Joon [00:02:10]: Yeah, it’s a good question. How many people have read it, I’m not sure. 
 Joon [00:02:14]: I know we do keep track of citations, and they are going up quite fast. 
 Swyx [00:02:23]: Yeah, Google Scholar has 7,200 citations. 
 Vibhu [00:02:25]: I feel like it made a bigger hit than that, and it was a pretty instrumental paper. It got cited so many times. 
 Swyx [00:02:34]: It is frequently the answer when people ask, “What is the best paper you’ve read recently?” It’s this one. 
 Vibhu [00:02:39]: I thought the memory component was pretty underrated. It was a very good early memory system, and one of the biggest papers. 
 Foundation Models and the Search for Killer Applications Joon [00:02:47]: Yeah, so maybe I can talk a little bit about how this particular paper came together. So when I got into research, it was back in 2020 when I started my PhD program at Stanford, and that was the year, when we were about to get GPT-3 to be available. So we already had GPT-2, and you could sense that there was this new class of models that was just becoming available in the market, and the team got very intrigued. And the general consensus was, “Well, is this model going to be useful for anything?” “It’s really strange that these models are not trained to do any particular task.” But we decided to take a bet. So a large group of scholars at Stanford, and it was led by one of my co-founders, Percy Liang, and we came together 
 Swyx [00:03:35]: Who coined foundation models. 
 Joon [00:03:36]: Who coined the term foundation models. We wrote this paper, where that term came from called Opportunities and Risks of Foundation Models. And during that process, really the thing that I started to think deeply about was, here is a model that is fundamentally new in our ecosystem. The reason why this was new was it wasn’t, again, trained to do anything in particular, but its premise was it could do anything and everything. It was like a stem cell, if you were to take a biology analogy. And I got really interested in this idea that, well, if we were to really think about what are the killer applications that this particular technology would enable, what would that be? Many of my colleagues were using this for simple classification, simple generations. Interesting that these models can do that, but from an interaction perspective, not that interesting. We’ve known how to do that for many decades. And what we came down to was these models are trained on this very broad data from the web, right? So these are human behavioral data. It’s social media, Wikipedia, all these data. So if you poke at the right angle, then you could see human behavior that would just pop out that’s quite realistic, and we’ve never seen that before. 
 The Time Machine Game and Recreating the World Joon [00:04:45]: So that got us really interested. The exercise that we decided to do, with this particular group of colleagues, Michael Bernstein, Percy Liang, and myself, who ended up becoming my co-founder at Simile, we sat down and we played this game that we call the time machine game. 
 Joon [00:05:03]: Imagine we were to get on a time machine and fast-forward 10 years and look back. What would have been the single application that will have mattered that would be the most interesting and inspiring? And when we thought, “Well, what if we can just recreate the world that we live in?” it’s really hard to get more ambitious than that. Like, let’s just create a world. 
 Joon [00:05:24]: And that’s where we started. And initially, we had this paper that was a precursor to the generative agents paper called Social Simulacra. 
 Swyx [00:05:32]: Before you go further, were there other candidates for the most ambitious thing in the time machine exercise? What was number two or number three? 
 Personal Agents, User Models, and Why Simulation Came First Joon [00:05:44]: There is a close second that we were considering, which ended up becoming more of these automation tools, especially the vision around really personalized agents that would do things for you. 
 Swyx [00:05:59]: That’s also happening. 
 Joon [00:06:00]: It’s also happening. But it was interesting for us, right, in that the reason why, we decided to go with the idea of simulation, one, I was a huge science fiction nerd, and this idea of creating simulation, I was personally really just fascinated. I loved the idea. It’s really cool to see, like, a game town like this and just see these agents live in it. But at the same time, my bet was if you were to create a really amazing personal assistant out of this technology, what you need first is an amazing model of your users. So I told a model, “Hey, can you go buy late dinner for me?” And it orders Hawaiian pizza, and I do not like pineapples on my pizza. Then it totally failed. The way for it to not make that mistake is only by having a deep understanding of who I am. And I gave a very simple and dumb example here, but you can imagine how this core understanding of people is instrumental. This is how, if we have our family and closest friends, they have a good mental model of who we are. That’s the basis of our social connection. So our bet also was this technology around simulation, creating accurate representation of people ought to precede the more complex agents that would automate the world that we live in. So that was the bet. But that was a very close second, and I’m still very much fascinated by it. I think there’s a lot of interesting work that’s going around. My hot take here, though, is I don’t think we’ve seen a true personal assistant that’s useful, in ways that me