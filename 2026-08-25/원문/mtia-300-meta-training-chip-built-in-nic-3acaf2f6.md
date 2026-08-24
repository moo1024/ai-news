# MTIA 300: Meta’s First Training Chip with Built-in NICs and Communication-Offloading Engines

- 출처: Meta Engineering
- 원본 링크: https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
- 발행: 2026-08-24T17:45:52+00:00
- 접근상태: 확인 완료

---

MTIA 300: Meta's First Training Chip with Built-in NICs and Communication-Offloading Engines - Engineering at Meta 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 

 
 

 

 

 
 
 
	Skip to content 

 

 
	

 

 
	
 
 
 
 
 

 
 Search this site 
 

 
 
 

 
 
 

 
 
 
 
 

 

 

 
 Open Source 
 
 
 
 Open Source 
 Meta Open Source 
 
 
 Platforms 
 
 
 
 Android 
 iOS 
 Web 
 
 
 Infrastructure Systems 
 
 
 
 Core Infra 
 Data Infrastructure 
 DevInfra 
 Production Engineering 
 Security & Privacy 
 Research Publications 
 
 
 Physical Infrastructure 
 
 
 
 Connectivity 
 Data Center Engineering 
 Networking & Traffic 
 Research Publications 
 
 
 Video Engineering & AR/VR 
 
 
 
 Video Engineering 
 Virtual Reality 
 Research Publications 
 
 
 Artificial Intelligence 
 
 
 
 ML Applications 
 AI Research 
 Research Publications 
 
 
 Watch Videos 
 
	
 
 
 

 
 
 
 
 
 
 
 
 
 
 

 

 

 

 
 


 
 

 
 
 

 
 
 POSTED ON AUGUST 24, 2026 TO Data Infrastructure , DevInfra , Networking & Traffic , Production Engineering 
 MTIA 300: Meta’s First Training Chip with Built-in NICs and Communication-Offloading Engines 

 

 
 
 
 
 
 By Rajiv Krishnamurthy , Wes Bland 
 

	
 

 
 MTIA 300 is the first of Meta’s family of in-house training and inference accelerators optimized for training ranking and recommendation models. 
 We’re sharing how MTIA 300’s built-in NIC chiplets allow it to meet the communication needs associated with training recommendation models with superior performance over general-purpose GPUs. 
 By co-designing MTIA’s communication library, HCCL, alongside the chip we’ve taken a fundamentally different approach to chip design and made communication a first-class citizen. 
 
 Deep learning models may deliver personalized content—from short videos to friend posts—to people on apps. As these models have grown in complexity, so has the importance of the compute that trains them, and the network that connects those accelerators. 

 Training recommendation models is a unique infrastructure challenge. Unlike large language models, which need enormous floating-point throughput, recommendation models are bottlenecked by a need for fast and efficient communication between the accelerators that train them. Their embedding tables can contain over 99% of the model’s parameters, requiring hybrid parallelism that generates frequent AllReduce, AllToAll, and AllGather collectives across hundreds of accelerators. On chips like GPUs these communication operations compete with training computation for the same resources, often leaving expensive hardware underutilized. 

 We’ve addressed this challenge starting on the Meta Training and Inference Accelerator (MTIA), our family of homegrown AI chips, with MTIA 300 , the first of the MTIA family optimized for training recommendation and ranking models. By co-designing MTIA 300 with HCCL , a communication library co-designed with the hardware from scratch, we’ve made communication a first-class citizen in the chip’s design, not an afterthought handled by general-purpose compute cores. 

 Integrating the Network Directly on the Chip 
 With MTIA 300, the network interface lives inside the chip package itself (see Figure 1). Two network chiplets, each containing six custom 800 Gbps RDMA NICs, provide 1.2 TB/s of total I/O bandwidth without ever crossing a PCIe bus. This eliminates the host-device-NIC bottleneck present in traditional GPU architectures, where the CPU must mediate between the accelerator and the network. (More details about the silicon design are available in our recent paper from the ISCA 26 conference.) 

 Because we use the same 12 Ethernet-based NICs for scale-up communication (within a rack of 16 nodes, at up to 1 TB/s) and scale-out communication (across racks, at 200 GB/s), we can flexibly partition the NICs to adjust to changing needs.  

 Figure 1. The MTIA 300 chip architecture. Diagram of MTIA 300 chip. 
 As model requirements shift, we can reconfigure this split by reconfiguring the network rather than changing the hardware. To minimize per-transaction latency, we introduced express doorbells. The work request write itself serves as the doorbell, eliminating an additional memory read and saving ~800 ns per operation. 

 Offloading Communication From the Compute Grid 
 On GPUs, libraries such as NCCL execute collective communication as GPU kernels that consume streaming multiprocessors—the same hardware needed for training computation. When collectives and training kernels run simultaneously, both slow down. 

 MTIA 300 takes a different approach. Alongside its 12×6 grid of processing elements (PEs) for computation, the chip includes 16 dedicated message engines (MEs) that handle all communication independently. 

 

 Each ME contains:  

 
 an RISC-V core for orchestrating w 
 an NIC interface that routes requests to the correct NIC 
 a near-memory compute (NMC) block that performs reductions at 128 bytes/cycle  
 
 Positioned at the chip edges next to HBM and cache, the NMCs collectively deliver more than 2.8 TBs of reduction throughput—more than double the I/O bandwidth—enabling line-rate execution of AllReduce and ReduceScatter collectives without touching the compute grid. 

 The result is near-perfect isolation. Running large GEMMs concurrently with collective operations introduces less than 0.5% degradation to compute throughput, as opposed to traditional GPUs that can see over 20% degradation because communication is handled by the same GPU resources. 

 A Compiled-Communication Model 
 Our communication library, HCCL, was co-designed with MTIA 300. Rather than driving communication from the host during execution, HCCL compiles each collective into a complete set of subgraphs—arrays of work-queue entries with explicit dependencies—dispatched to the MEs for fully autonomous execution. Once work reaches the device, the host is uninvolved. Figure 2 shows how the CPU is no longer involved after copying the instructions into HBM. 

 Figure 2. A comparison of traditional accelerator design with host-based network instructions with MTIA 300’s offloaded communication model. 
 This compiled model integrates naturally with PyTorch’s c10d and torchcomms interfaces. Collectives traced through torch.compile are compiled into a single graph alongside compute operators. HCCL selects topology-aware algorithms that exploit the asymmetric bandwidth between scale-up and scale-out, minimizing cross-rack traffic where bandwidth is constrained. For inference workloads, we developed additional paths: one-sided communication where PEs submit work directly through express doorbells, and device-triggered collectives where compute kernels signal hardware-offloaded communication on a parallel stream without breaking graph execution. 

 Performance in Production 
 HCCL achieves up to 940 GB/s of communication bandwidth within a single rack. On a 150-billion-parameter production-recommendation model running across 40 accelerators, MTIA 300’s total communication time is 3.9 times faster than the equivalent GPU cluster. 

 MTIA 300’s design enables further co-design strategies: Its 216 GB of HBM3E allows larger local batch sizes (reducing trainer count and communication overhead); its 1:1 CPU-to-accelerator ratio enables CPU offloading of numerically intensive optimizer operations; and its high network bandwidth lets us use higher-precision datatypes to maintain precision.  

 Looking Ahead 
 While MTIA 300 was designed for training recommendation models, the architectural principles—integrated networking, offloaded collective execution, and system-level co-design of compute and communication—position it for a broader set of workloads. As AI inference evolves toward reasoning, agentic, and long-context use cases, the communication demands a shift: Messages become smaller, more frequent, and latency-sensitive, with tighter per-collective budgets.  

 An architecture that treats the network as a first-class system constraint, optimizing not just bandwidth but also latency and message rate, is well suited to meet these emerging demands. The patterns established in MTIA 300 and HCCL are the foundation for Meta’s next-generation AI silicon . 

 Learn More About MTIA 300  
 To learn more about MTIA 300’s silicon design and the work detailed here, read our papers: 

 
 “ MTIA 300: Meta’s First Training Chip Featuring Built-in NICs and Collective Offloading Engines “ (From ISCA ‘26) 
 “ HCCL: Collective Communication for Meta Training and Inference Accelerators ” (to be published at SC26 ). 
 
 Share this: 
 Share on Facebook (Opens in new window) 
 Facebook 
 
 Share on Threads (Opens in new window) 
 Threads 
 
 Share on WhatsApp (Opens in new window) 
 WhatsApp 
 
 Share on LinkedIn (Opens in new window) 
 LinkedIn 
 
 Share on Reddit (Opens in new window) 
 Reddit 
 
 Share on X (Opens in new window) 
 X 
 
 Share on Bluesky (Opens in new window) 
 Bluesky 
 
 Share on Mastodon (Opens in new window) 
 Mastodon 
 
 Share on Hacker News (Opens in new window) 
 Hacker News 
 
 Email a link to a friend (Opens in new window) 
 Email 
 
 
 


 

 

	
 

 
 


 
 
 Read More in Networking & Traffic 
 
 View All 
 

 
 
 
 
 
 
 
 
 
 
 FEB 24, 2026 
 
 

 
 
 
 RCCLX: Innovating GPU Communications on AMD Platforms 
 
 

 

 
 
 
 
 
 
 
 
 
 
 OCT 20, 2025 
 
 

 
 
 
 Disaggregated Scheduled Fabric: Scaling Meta’s AI Journey 
 
 

 

 
 
 
 
 
 
 
 
 
 
 OCT 13, 2025 
 
 

 
 
 
 OCP Summit 2025: The Open Future of Networking Hardware for AI 
 
 

 

 
 
 
 
 
 
 
 
 
 
 SEP 29, 2025 
 
 

 
 
 
 Meta’s Infrastructure Evolution and the Advent of AI 
 
 

 

 
 
 
 
 
 
 
 
 
 
 SEP 26, 2025 
 
 

 
 
 
 Networking at the Heart of AI — @Scale: Networking 2025 Recap 
 
 

 

 
 
 
 
 
 
 
 
 
 
 MAY 1, 2025 
 
 

 
 
 
 Taking the plunge: The engineering journey of building a subsea cable 
 
 

 

 
 
 
 

 

 
 

 
 
 
 

 

 
	


 
 
 Related Posts 
 
 
 
 
 
 Aug 24, 2026 
 MetaRoCE: A New RDMA Transport Built for AI-Scale Ethernet 
 
 
 
 
 
 
 
 
 Sep 29, 2025 
 Meta’s Infrastructure Evolution and the Advent of AI 
 
 
 
 
 
 
 
 
 Aug 22, 2024 
 Inside the hardware and co-design of MTIA 
 
 
 
 Related Positions 
 
 
 Data Engineer, Product Analytics
 
 
 SUNNYVALE, US
 
 
 
 
 
 Data Engineer, Product Analytics
 
 
 REMOTE, US
 
 
 
 
 
 Data Engineer, Product Analytics
 
 
 BELLEVUE, US
 
 
 
 
 
 Data Engineer, Product Analytics
 
 
 REDMOND, US
 
 
 
 
 
 Data Engineer, Product Analytics
 
 
 MENLO PARK, US
 
 
 
 
 
 See All Jobs 
 
 
 



 -->

 
	
 

 

 

 

 
 

 

 
 
 Available Positions 
 
 
 Data Engineer, Product Analytics
 
 
 SUNNYVALE, US
 
 
 
 
 
 Data Engineer, Product Analytics
 
 
 REMOTE, US
 
 
 
 
 
 Data Engineer, Product Analytics
 
 
 BELLEVUE, US
 
 
 
 
 
 Data Engineer, Product Analytics
 
 
 REDMOND, US
 
 
 
 
 
 Data Engineer, Product Analytics
 
 
 MENLO PARK, US
 
 
 
 
 
 See All Jobs 
 
 Technology at Meta 
 
 
 
 
 Engineering at Meta - X
 
 
 
 Follow
 
 
 
 
 
 
 
 
 AI at Meta
 
 
 
 Read
 
 
 
 
 
 
 
 
 Meta Quest Blog
 
 
 
 Read
 
 
 
 

 
 
 
 
 Meta for Developers
 
 
 
 Read
 
 
 
 
 
 
 
 
 Meta Bug Bounty
 
 
 
 Learn more
 
 
 
 

 
 
 
 
 RSS
 
 
 
 Subscribe
 
 
 
 
 
 Open Source 
	Meta believes in building community through open source technology. Explore our latest projects in Artificial Intelligence, Data Infrastructure, Development Tools, Front End, Languages, Platforms, Security, Virtual Reality, and more.


 
 
 
 
 ANDROID
 
 
 
 
 
 iOS
 
 
 
 
 
 WEB
 
 
 
 
 
 BACKEND
 
 
 
 
 
 HARDWARE
 
 
 

 
	Learn More
 

 
 

 
 

 


 
 
 
 
 
 
 
 
 
 
 
 Engineering at Meta is a technical news resource for engineers interested in how we solve large-scale technical challenges at Meta.

 
 
 
 
 Home Company Info Careers 
 
 
 
 
 
 
 

 
 

 

 
 
 

 
 © 2026 Meta 
 

 
 
 
 Terms Privacy Cookies Help 
 
 
 

 

 

 

 
 

 

 
 
 
 
 To help personalize content, tailor and measure ads and provide a safer experience, we use cookies. By clicking or navigating the site, you agree to allow our collection of information on and off Facebook through cookies. Learn more, including about available controls: Cookie Policy 

 
 Accept