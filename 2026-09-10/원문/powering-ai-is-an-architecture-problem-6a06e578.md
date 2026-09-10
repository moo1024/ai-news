# Powering AI is an architecture problem

- 출처: MIT Tech Review AI
- 원본 링크: https://www.technologyreview.com/2026/09/10/1141649/powering-ai-is-an-architecture-problem/
- 발행: 2026-09-10T11:00:00+00:00
- 접근상태: 확인 완료

---

Powering AI is an architecture problem | MIT Technology Review 
 
 
 
 

 
 
 
 

 
 

 
 

 

 
 

 
 

 
 
 
 
 
 
 
 
 
 
 You need to enable JavaScript to view this site.
 

 Skip to Content Menu MIT Technology Review MIT Technology Review The Big Story Artificial intelligence Biotech & health Climate & energy 10 Breakthrough Technologies EmTech Future live event The Kids issue Menu MIT Technology Review MIT Technology Review The Big Story Artificial intelligence Biotech & health Climate & energy 10 Breakthrough Technologies EmTech Future live event The Kids issue Sponsored
 Artificial intelligence Powering AI is an architecture problem Moving power protection up the voltage stack, outside the building, and into the power path doesn't just solve outages; it changes density, permitting timelines and backup power economics.

 By Ricardo De Azevedo archive page September 10, 2026 Provided by ON.energy 
 On July 22, 2026, a transmission line fault in Ashburn, Virginia—the heart of the world's largest data center cluster—knocked more than 3 gigawatts of load off the grid in seconds. And it wasn't the first time. Two years earlier, a single failed surge arrester dropped roughly 60 Virginia facilities and 1,500 megawatts at once. No one could anticipate so much uniform load responding to grid faults the same way, at the same time.
 The AI power debate is mostly about generation: more turbines, more solar, more transmission. The grid needs more electrons. But the outages in Virginia weren't supply failures; they were architecture failures. And a giant wave of interconnections is arriving on that same architecture, putting grid reliability at risk. It's a problem nobody wants to own.
 Asking more from the grid The grid was built around predictable loads: steel mills, refineries, and houses at dinnertime. Different load sizes, same process—drawing power smoothly, misbehaving occasionally, and recovering gracefully.
 But AI data centers don't behave that way.
 
 An AI campus can swing 70% of its load in milliseconds during a training run, then trip offline just as fast at the first sign of trouble upstream to protect billions in compute. Each is rational alone. Together, at gigawatt scale, they're a problem the grid has never solved—and the next wave of data center campuses is planned at exactly that scale.
 Where the old stack breaks The standard data center power stack hasn't changed in decades. Medium-voltage power arrives, transformers step it down, low-voltage uninterruptible power supply (UPS) units condition it, and it reaches the racks. Push that design to AI scale, and it cracks in three places.
 
 First, the UPS sits deep inside the building, close to the racks. But its batteries are an undersized spare tire, designed to handle an outage for a few minutes, not to absorb load swings this fast and volatile around the clock.
 Second, the UPS spends most of its life in bypass. Legacy converters waste enough power that operators run in eco-mode: A static switch feeds the racks directly from the grid and nothing filters in either direction. The compute's swings go out raw, and grid transients—sub-millisecond events that can damage or take down equipment—come in too fast for any switch to catch.
 Third, the protection logic was written when "large load" meant 50 megawatts. This protection logic can't see the grid it is now a part of, so when trouble hits upstream, it does exactly the wrong thing: it drops out. In the 2024 Virginia event, most of the lost load traced to protection schemes that count voltage dips and disconnect on the third one —as designed, at the worst moment.
 This isn't sloppy engineering. It's careful engineering the load has outgrown.
 Moving into the path The fix is three moves, made together.
 Move it up —from 480 volts to medium voltage (13.8 kilovolts and higher), the voltage large sites draw from the grid.
 Move it out —from the data hall to modular enclosures near the substation so the building holds only compute and the cooling that keeps it alive.
 Move it into the path —instead of a battery that watches and reacts, a system every electron runs through, all the time. There's nothing to detect and nothing to switch because nothing was ever routed around it.
 
 
 On paper, three straightforward upgrades. In practice, they rewrite every line item downstream.
 Making the change When thousands of GPUs spin up together, the system absorbs the swing and hands the grid a flat load profile. When a disturbance hits, the equipment behind it never notices. A difficult neighbor becomes a predictable one. And when the utility needs help, it becomes a useful one.
 Interconnection changes, too. The utility certifies one medium-voltage box instead of untangling every transformer, UPS, chiller, pump, and switchgear lineup behind it. Engineers swap chip generations without a fresh interconnection study. Months come off the permitting timeline.
 Inside the fence, UPS rooms become compute or cooling space. Density per construction dollar climbs.
 And the economics flip. Equipment that runs at medium voltage, sits outside, and stores its own energy can qualify for tax credits, and earn revenue in grid programs like peak shaving and demand response. Backup power stops being insurance and starts paying for itself.
 The architecture test In early 2026, we tested a full-scale system at the National Laboratory of the Rockies, a U.S. Department of Energy facility and the only place in the Western Hemisphere that can replicate real grid faults and AI-scale load swings concurrently in the same loop.
 We hit it from both directions: real AI load profiles hit the compute side at full medium voltage. Grid faults hit the utility side, including a full zero-voltage event. The compute side didn't flinch. Neither did the grid side. It cleared the large-load voltage ride-through requirements from the Electric Reliability Council of Texas (ERCOT), the grid operator, with room to spare.
 Those rules exist because operators no longer take facilities this size on faith, and more are coming. Most of the industry treats them as hurdles. A medium-voltage, inline system clears them out of the box. Compliance isn't an added feature. It's what the architecture does.
 
 The new layer Much of what looks like a grid problem in the AI buildout sits inside the fence, in equipment sized for a load that no longer exists. Move the right pieces up, out, and into the path, and a grid liability becomes a grid asset. Density goes up. Permitting time comes down. Backup power earns its keep.
 The engineering works—and the next wave of AI factories is being built on it. The industry hasn't named this layer yet. We call it the medium-voltage AI UPS. The name matters less than the choice: those factories can arrive as a strain on the grid or as strength for it. We already know how to build the second kind.    
 This content was produced by ON.energy. It was not written by MIT Technology Review’s editorial staff. 
 
 by Ricardo De Azevedo Share Share story on linkedin Share story on facebook Share story on email Popular A fundamental flaw leaves LLMs strikingly vulnerable to attack Will Douglas Heaven AI is more likely than humans to form biases when hiring Michelle Kim Here’s why AI agents lie and cheat to reach their goals Grace Huckins Bill Gates says we’ve passed AI’s danger thresholds. Now what? Mat Honan Deep Dive Artificial intelligence A fundamental flaw leaves LLMs strikingly vulnerable to attack It makes it easy to trick them into doing things they shouldn’t, such as telling you how to sabotage an aircraft’s navigation system.

 By Will Douglas Heaven archive page AI is more likely than humans to form biases when hiring AI doesn’t just learn stereotypes from its training. It can cook up new ones, too.

 By Michelle Kim archive page Here’s why AI agents lie and cheat to reach their goals The misbehavior is called reward hacking. This is what you need to know. 

 By Grace Huckins archive page Bill Gates says we’ve passed AI’s danger thresholds. Now what? In a new interview, the billionaire philanthropist sounds an alarm on the urgency of getting our AI policies in order.

 By Mat Honan archive page Stay connected Illustration by Rose Wong Get the latest updates from
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