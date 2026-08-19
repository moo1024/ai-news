# Using the railway network as a flatbed scanner

- 출처: Hacker News
- 원본 링크: https://philo.gay/linecam/
- 발행: 2026-08-18T12:43:54+00:00
- 접근상태: 확인 완료

---

Using the railway network as a flatbed scanner 
 
 
 
 
 
 
 
 
 
 
 
 
 Philo's Website 
 

   
 

 
 

 
 Using the railway network as a flatbed scanner 
 August 17 th , 2026 — 4,600 words 
 
 
 Over the past few months, I've been working on using an industrial linear scanning camera to take very wide photos out of trains and ferries. Getting it working has been quite the challenge, but I think the results speak for themselves. 
 
 
 
 
 
 taken on the San Francisco to Oakland ferry in February 2026 (56,894x2,048 pixel grayscale image); scroll to zoom in and click and drag to move 
 
 
 More pictures are on display in the gallery . 
 
 
 I presented a talk on this project at EMFcamp 2026 , which you can watch below or read on for the same story in more detail: 
 
 -->
 
 
 
 What am I even looking at? 
 

 The process of capturing an image like the one of the container port above.

 The camera is pointed out of a moving vehicle and is constantly capturing a single vertical line kinda like these grayscale ones in the diagram, but a lot thinner. As the camera moves, what exactly it sees is changing. If I capture the lines from the camera quickly enough and stitch them together, I can produce a complete-looking image. It's a bit more complicated than that and getting the results looking good was rather tricky, but that's the main idea behind it.

 Background and Prior Art 
 Back in the 1990s, digital camera sensor technology hadn't caught up to the size and effective resolution of medium and large format film, so digital scanning backs were developed. They capture a high-resolution image without needing a giant grid of pixels by moving a single line of pixels (or three lines for color) across the frame. In the intervening years, image sensors have gotten pretty big (there's even one that covers 4x5" large format nowadays), but this approach is still cheaper to build for large formats than a giant sensor.

 I'd been thinking about building my own digital scanning back for my large format camera for a while, but I've never quite gotten around to it because building something to mount properly on my camera seemed too daunting. (Buying one could have been an option, but ones from the 1990s still go for thousands of dollars on ebay and require reconstructing a computing environment of a similar vintage to use.) Late last year, I was watching a video on Gigawipf's medium format scanning camera build and suddenly thought: "what if the entire camera moved and the subject didn't?" and decided to give it a shot.

 

 Loading film into my large format camera on top of a mountain in Vermont because I'm allergic to doing photography in a normal way. (The resulting pictures from that trip are here .)

 I found some previous photos in the same vein ( the Scannoramic project , John Hikerbiker's experiment , Daniel Lawrence Lu's reversal of his stationary camera , and Martin Liebscher's very interesting film shots ), but the results seemed like they could be improved upon. Surely taking the speed of motion into account and getting cleaner results wouldn't be too hard, right?

 Slit Scanning My Sofa 
 On the night I thought up this "big scanner" concept, I had to give it a shot. It was a bit late to go out and catch a train, so I scanned my sofa instead.

 I set my phone on my office chair and slowly pushed it along as it captured a video. I then wrote some really slapdash code (which I am choosing not to share here to protect my readers) to grab the leftmost column (a "slit") of each frame and combine them into an image.

 My comments included lyrics from "Future Me Hates Me" by The Beths , which became something of a self-fulfilling prophecy when I started writing a postprocessor for the next version of the camera loosely based on that code and cursed my decisions.

 

 It looks vaguely like my sofa, but it's rather squished and the art on the wall is unintelligible. Surely I can do better.

 

 I messed around with the postprocessing and doubled every column, which makes it look less squished, but it's still a mess because I wasn't pushing the chair at a particularly consistent speed.

 I knew from the start that I'd need to measure the speed somehow, but I was naïvely hoping that I wouldn't need to measure it that well and could simply fudge it. This image, however, shows that even small variations of speed matter. This was my first glimpse into how much of a pain dealing with speed would turn out to be.

 For my next trick, I took a ride on the MBTA orange line. I taped my old phone to the seat to use its accelerometer and held my current phone to the window, making sure to turn the frame rate up all the way to 60 fps.

 The accelerometer data wasn't very useful and was even less so when I took an integral to get velocity. 

 If I remember correctly, y was the axis of the train's movement, but the data is so noisy that the train was apparently moving backwards at the end.

 The result looks interesting, though, but I definitely need more lines if I want a properly intelligible image. 

 While I was getting ready for EMFcamp, I noticed another talk on the schedule by Tim Jacobs (better known online as mitxela ) that was also about slit scan cameras and started to worry we'd both done the same thing. (He ran up to me after my talk to tell me he'd also worried this.) His talk started in the same way, with taking a slit from a video, but he ended up making really cool and trippy animations by going through every possible slit position for a given video.

 Industrial Linear Camera 
 My source for more lines per second ended up being the Basler ruL2048-19gm , designed to be pointed at fast-moving conveyor belts. The oddly-capitalized name comes from its ability to read out its 1x2048 pixel image sensor just shy of 19,000 times per second.

 

 These capabilities come at a price, however; brand new, the manufacturer's lowest-spec current models go for around US$700. Thankfully for my wallet, I found mine on ebay for a tenth of that.

 The price is also measured in light. since it's capturing so quickly (the slowest exposure time is 1/100s), it needs a lot of light. I can only shoot in the daytime, and all but the brightest stations and tunnels are off limits to me.

 To my surprise, having dealt with vendorware before, Basler just let me download the SDK without a support contract or proof of purchase. The most recent version also still supports this camera from 2013, which is less surprising but is still convenient.

 The camera communicates with the computer over a gigabit ethernet link and the software finds it automatically as long as the relevant interface is set up for APIPA addresses (169.254.0.0/16). I could set static addresses for both ends, but I'm only using one camera at a time, so I haven't been bothered to change it.

 With surprisingly little swearing at the SDK, apart from some complaints about their use of shutter time rather than shutter speed and what a "frame" is on this camera, I put together a program that grabbed buffers of pixels and wrote them to disk.

 

 This was my first image out of the camera using my own code, and I think it looks pretty good for just moving it freehand.

 The setup and mechanical design 
 In order to take it on a train without needing to have three hands to hold it, I needed a way to mount it to a tripod. I ended up designing a rather utilitarian case with a heat-set insert in the bottom that my friend Brooke 3D-printed for me. Buying the parts for it gave me an excuse to finally make an order from McMaster-Carr and feel like a real engineer.

 

 My first attempt didn't come out because it turns out there's these things called "manufacturing tolerances" that I completely forgot about.

 

 Oops, that's a bit too small.

 

 In retrospect, I probably should've stuck the sensors on with something other than blue painters' tape, but it's held on pretty well.

 Going clockwise around it, the boards are:

 
 6 degree of freedom accelerometer/gyro , which can be used with some maths to to get the speed 
 GPS , which didn't end up working as well as I'd hoped because the trains in Boston are a bit too good at blocking GPS signals 
 SAMD21 microcontroller to shunt the data back off to the laptop 
 
 The lens on the front is a Vivitar 28mm f/2.8 that I already had for a more normal camera, with an adapter from Pentax K to the C-mount screw on the camera. Since some of the things I'm trying to shoot with it are kinda tall, its field of view worked out pretty well.

 The whole thing is powered off a USB-C battery bank and there's also ethernet and USB cables running to my laptop, so it's a bit of a cable spaghetti monster when in action.

 With the sensors attached, I could finally give them a try.

 

 Both of these images are the same capture of waving the camera back and forth out my window, but the top one is the raw image and the bottom one is taking accelerometer movement into account. As you can see, using the accelerometer makes everything look a lot closer to normal and less stretched. (I'll explain more of how this works in a bit in the Postprocessing Hell section.)

 Boston Attempts 
 Once I had everything assembled, it was time to take it on a train.

 

 I started off on the MBTA Orange Line, since it's the closest to me, but as you can see, the results weren't that good. Previewing what was coming out of the camera was a pain, so I kinda had to guess on the exposure, and I definitely guessed wrong. The postprocessing code I wrote didn't work very well and everything was stretched and compressed a bit weirdly.

 

 I went out again on a day with nicer weather and had some better luck with the exposure, although I think I messed up the focus a bit. Unlike the attempt with my phone camera, the text on station signs is pretty legible, so I'm definitely getting enough lines.

 

 I'm particularly happy with how this one of the Longfellow Bridge from Boston to Cambridge came out. This one is in the gallery if you'd like to take a closer look.

 Capture (in far too much detail) 
 

 When I was taking these early pictures in Boston, I was using a tool from the camera vendor called Pylon to preview. The black horizontal section was all I could see of the image at any one time, and it's rotated 90° from how I'd like to see it. Dialing in the exposure in it, releasing its grip on the camera, and then starting my own code back up before the train started moving again was a right pain that I had to do something about.

 My first attempt at a GUI of my own used OpenCV highgui , which didn't really work for this. It requires a 1 ms delay after each frame, which is fine for slower cameras, but would cause me to miss 4 entire lines (250 μs each at the shutter speeds I'm usually using) every display frame (256 lines).

 I ended up using Dear ImGUI instead, which worked nicely with the frame acquisition loop I already had. Out of the approximately two dozen backends the library supports, I picked GLFW ("girl love for workgroups", to quote a message from a friend at the time) and OpenGL3, probably because of the "girl love" quip, although I'm not certain.

 

 I wrote most of the GUI in a single sleepless night in Toronto where rotating the image felt like the single hardest problem in computer science. (There's definitely a few things I can do to improve the implementation I settled on, but it runs well enough for the time being.) Unfortunately, the pictures I took in Toronto didn't really come out, but at least they were exposed correctly.

 

 I encountered some strange bugs while adding a histogram for the image.

 Getting the accelerometer data proved to be something of a pain. my first version sent readings as text over serial, which turned out to be very computationally intensive on the microcontroller. (Converting floating point numbers to strings and then assembling strings is very expensive, even on a relatively powerful SAMD21 microcontroller that has thirty-two entire bits.) I decided to move the conversions over to my laptop, which has the processing power to handle them with ease, but this came with problems of its own.

 

 A very frustrating debugging session.

 The accelerometer measurements were sent as raw floating point numbers, but GPS data was still in NMEA sentences and switching between them required sending fixed byte sequences and hoping that nothing got misinterpreted as those sequences. (Nothing in a NMEA sentence should come across as 0x11 0x11 0x11 0x11 , my accelerometer data start sequence, but it's not completely impossible for accelerometer data to contain 0x22 0x22 0x22 0x22 , my NMEA string start sequence.)

 I also ran into issues where not flushing the serial port at the right time ruined an entire day's shots. Thankfully, I was capturing on the Mattapan Line in Boston, and I can pretty easily go back and try again. 

 That "seam" in the image is where it lost all serial data for around half a second, which is an eternity in line camera time. The software kept waiting for another accelerometer sample that never came because the serial port buffer was full.

 See It, Say It, Sorted 
 The fully assembled camera looks like a suspicious mess, and the witch using it doesn't look much less so.

 

 The camera isn't usually held together with this much tape, but I'd forgotten to bring the tripod mount plate on that trip to Montréal. 

 Would you trust her to bring strange equipment onto your train?

 Despite Boston's history of police overreaction to harmless electronics projects , I worry the least about being arrested on the MBTA. People here tend to mind their own business and have never called the cops on me. The police also don't ride the trains much, preferring to harass people in stations instead.

 I'm less used to how things work in other cities, so I only take the camera out when riding with a friend to look out for trouble (and sometimes to listen to dispatch radio).

 

 So 