# I used AWS cognito for a startup. I wouldn't do it again

- 출처: Hacker News
- 원본 링크: https://joshkaramuth.com/blog/aws-cognito-authentication-startup-nightmare/
- 발행: 2026-08-28T13:21:03+00:00
- 접근상태: 확인 완료

---

I Used AWS Cognito for a Startup. I Wouldn't Do It Again. | Josh Karamuth
 Home Blog Essays Tags Work with me Deployment Setup I Used AWS Cognito for a Startup. I Wouldn't Do It Again. I let AWS Cognito gaslight me for three weeks so you don't have to. Here's the unfiltered autopsy.
 
Published: July 10, 2026 
#cognito 
#aws 
#engineering 
#cloud I was three days into setting up authentication for our startup when I realized something was wrong. Not “I missed a semicolon” wrong. More like “I followed every step in the documentation and the password reset flow still redirects to the wrong place” wrong.

 I had the docs open in twelve tabs. I had copy-pasted the code samples. I had even watched a tutorial from someone who sounded like they’d been through this exact nightmare before.

 Here’s the thing. I’ve implemented authentication before. I’ve wrestled with Auth0, tamed Firebase Auth, and even rawdogged a custom JWT system that I’m not proud of but it worked. So when our startup needed auth and the team leaned toward Cognito because “it’s already in the AWS ecosystem and the first 50,000 monthly active users are free,” I thought, how bad could it be?

 I regret everything.

 The Documentation Was Written for Five Different People at Once 
 Reading Cognito docs feels like someone took three separate manuals, threw them in a blender, and then sprinkled in some outdated Stack Overflow answers for flavor.

 AWS is trying to serve too many audiences simultaneously. You’ve got the enterprise architect who wants to understand the underlying identity protocols. You’ve got the frontend developer who just wants a login form. You’ve got the mobile developer who needs native SDKs. And the docs try to be everything to everyone, which means they end up being useful to exactly nobody.

 I’d search for “Cognito custom attribute validation” and land on a page that starts with a paragraph about directory schemas that assumes I’ve already read four other pages I didn’t know existed. There’s no clear linear path. It’s just a web of hyperlinks and prayers.

 And the code examples. Oh, the code examples. Half of them are for the old JavaScript SDK. Some reference the Amplify v1 API. Others use the raw AWS SDK. The docs don’t always clearly tell you which version they’re talking about, so you’re left playing detective with import statements.

 The Day Amplify v6 Betrayed Me 
 Speaking of versions. Let me tell you about the JavaScript library situation, because this one genuinely caught me off guard.

 When we started building, Amplify was on version 5. I wrote our auth flow, tested it, committed it, moved on to other features. A few weeks later, I came back to fix a bug and noticed some deprecation warnings in the console. No problem, I thought. I’ll just update to the latest version.

 Friends. Amplify v6 didn’t just change a few method signatures. It fundamentally rearchitected how you interact with Cognito. Functions I had built entire UI flows around were gone. Replaced. Vanished. The migration guide existed, technically, but it felt more like a treasure map with half the landmarks missing.

 I rewrote the code. Not refactored. Rewrote. Authentication logic that was working perfectly fine in production had to be rebuilt because the library maintainers decided the old API was no longer the blessed path. That’s not an upgrade. That’s a hostage situation.

 Local Development is a Special Kind of Pain 
 Here’s a fun fact about Cognito: it’s cloud-based. I know, shocking. But what that means practically is that you can’t just spin up a local instance and test your auth flows offline. You’re always hitting actual AWS endpoints.

 Now, there are tools like the serverless-offline plugin and local Cognito emulators that try to bridge this gap. But they’re community projects with varying levels of maintenance and fidelity. The official story from AWS is basically “test against the cloud,” which is great advice unless you’re on a plane, or your internet is spotty, or you just want fast iteration cycles without waiting for network round trips.

 I spent an embarrassing amount of time setting up a local mock that didn’t quite match the real thing, which meant bugs would slip through locally and show up in staging. The whole point of local development is catching issues early, and Cognito actively works against that.

 You Want Customization? Best I Can Do is a Logo 
 This one stung.

 The hosted UI that Cognito provides is functional. It’s there. It works, mostly. But if you want it to look like your brand and not like an AWS service wearing a costume, you’re going to have a bad time.

 You can change the logo. You can tweak some CSS via the console. But the layout, the structure, the overall feel? That’s AWS’s house, and you’re just renting a room. If you need anything beyond basic customization, the advice from the community is usually “build your own UI using the SDK.” Which, fine, I get it. But at that point, what exactly is the hosted UI saving me?

 The Email-Only Configuration That Broke My Spirit 
 Let me tell you about the moment I almost threw my laptop out a window.

 Our app only needed email authentication. No usernames. Users sign up with an email, verify it, set a password, done. Simple concept, right?

 So I went into the Cognito user pool settings and configured it to use email addresses as the sign-in identifier. I set up the attribute mappings. I created the sign-up flow. Everything seemed fine until I realized that Cognito treats “email” differently depending on whether it’s a core attribute, an alias, or a custom attribute, and the configuration options are spread across multiple screens in the console with interdependencies that are never fully explained.

 I made a mistake in the initial setup. A small one. I had configured something as a custom attribute that should have been a standard one. No problem, I thought. I’ll just change it.

 You cannot change it.

 Once a user pool attribute is created as custom, it’s custom forever. And if your authentication scheme depends on the relationship between certain attributes, and you get that relationship wrong, your options are roughly: delete the entire user pool and start over, or build an elaborate migration process that moves users to a new pool with the correct configuration.

 For a production app with active users, “just delete it” is not really an option. So now you’re scripting user migrations, handling password resets in the new pool, and apologizing to your users for the inconvenience. All because a dropdown in a console was a little too ambiguous.

 What I Actually Learned 
 I don’t want to just complain. That’s easy. But I do want to be honest about what this experience taught me, because I think there’s something useful here beyond “Cognito bad.”

 Authentication is not the place to cut corners. The “it’s already in the ecosystem” argument is seductive, but ecosystem proximity doesn’t matter if the tool makes you miserable every time you touch it. The free tier pricing is attractive until you calculate the engineering hours spent fighting the documentation and rewriting code for breaking API changes.

 Next time, I’m picking a tool based on developer experience first, not AWS service integration convenience. The time we lost debugging Cognito issues could have paid for several years of a paid auth provider. And we would have shipped faster, with less cold pizza consumed at midnight.

 If you’re reading this because you’re currently evaluating Cognito for your project, I’m not going to tell you what to do. But I will say this: build a small proof of concept first. Something nontrivial. Something with custom attributes and email verification and a password reset flow. See how it feels. Time yourself. Count the documentation tabs you have open by the end of it.

 If that number is over twenty, maybe reconsider.

 I’m still using Cognito on this project, by the way. We’re too far in to rip it out now. But every time I open the AWS console and see that user pool sitting there, I feel a small, quiet resentment. Like an old roommate who never does the dishes and keeps “borrowing” your stuff.

 You know the feeling.
 
Need a Developer Who Gets It Done?
 
If this post helped solve your problem, imagine what we could build
 together! I'm a full-stack developer with expertise in Python, Django,
 Typescript, and modern web technologies. I specialize in turning complex
 ideas into clean, efficient solutions.

 
Let's Work Together
 
Connect on LinkedIn
 
Comments
 0"> 
Leave a Comment
 Comment submitted!
 
Your comment is pending moderation and will appear here once
 approved.

 
 
Name
 
 
Comment
 
 Submit Comment 
Submitting...
 
 
Try again
 No comments yet. Be the first to share your thoughts!
 
 Load More Comments 
Loading...
 Home Blog Essays Tags Work with me © 2026 Josh Karamuth RSS Feed