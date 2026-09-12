# [AINews] DeepSeek v4.1-Flash: 763B-P8B-D16B novel causal Encoder–Decoder architecture with vision marks the Return of the Whale

- 출처: Latent Space
- 원본 링크: https://www.latent.space/p/ainews-deepseek-v41-flash-763b-p8b
- 발행: 2026-09-12T05:56:05+00:00
- 접근상태: 확인 완료

---

[AINews] DeepSeek v4.1-Flash: 763B-P8B-D16B novel causal Encoder–Decoder architecture with vision marks the Return of the Whale 
 
 
 
 
 

 

 

 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 

 

 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 

 
 
 

 
 
 
 
 
 
 

 

 
 
 
 
 

 

 

 

 

 
 

 
 

 

 

 
 Subscribe Sign in AINews: Weekday Roundups [AINews] DeepSeek v4.1-Flash: 763B-P8B-D16B novel causal Encoder–Decoder architecture with vision marks the Return of the Whale We agree with Sebastian: this should have been DeepSeek v5 Sep 12, 2026 ∙ Paid 45 Share We are late to this but better than never. Have been busy finalizing the second AIE NYC , which is happening in one month. Get your tix before prices go up - we will announce speakers from Bridgewater, Ramp, Coatue, Mastercard, Vanguard, Coinbase, Blackrock, Fidelity, Point72, Capital One, JPMC, Wells Fargo, Bloomberg, A24 (yes the movie studio) Labs, Two Sigma, Apollo Global, and more next week! 
 The way DeepSeek pursues their research agenda is nothing short of fascinating. In between major DeepSeek versions, from v2 to v3 to v4, they have released intermediate papers with a hyperfocused architectural improvement and basically a 100% hit rate, from Math (esp GRPO ) , Coder , and R1 , not to mention more recent work on Manifold Constrained Hyperconnections and Compressed Sparse Attention . After the enormous attention in 1H2025 from the R1 paper, DeepSeek started laying low, and for about the past year, was happy to let peers like GLM and Kimi take the lead on Open Models. 
 It looked dicey for a little bit, but true whalebros never wavered, and now DeepSeek are sending a weirdly mixed message by doing a completely new architecture, retiring V4 Pro and going all in on this new model, and yet only titling it v4.1 Flash, it seems to be a test of whether or not you know how to read through the basic headlines to understand true advances. 
 Yes, v4.1 Flash is technically behind other open models in some benchmarks. But that’s because we don’t yet have benchmarks that concisely capture what v4.1, and the broader research agenda of DeepSeek, is aiming for - the most creative and efficient use of context we have ever seen openly explained. 
 DeepSeek @deepseek_ai 🚀 Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.

🔹 Introducing the smallest model in our new architecture family, with native visual understanding.
🔹 Designed for greater capability, faster inference, higher throughput, and scaling to larger models.

1/6 6:10 AM · Sep 10, 2026 · 6.04M Views 933 Replies · 3.02K Reposts · 27.7K Likes If you are the sort to only read model versions and benchmark headlines, you are exactly the type of superficial person that DeepSeek is looking to fool. The best way to understand DeepSeek’s enormous advance here is to look at Sebastian’s meme:
 Sebastian Raschka @rasbt I know, sorry, but it's hard to resist 3:21 AM · Sep 11, 2026 · 6.72K Views 8 Replies · 3 Reposts · 120 Likes Same model name, but hardly a 0.1 bump by anyone’s standards, and they even threw in vision without making you wait for a separate model . For a better visualization you can look at all the model innovations stacked up over time from the OG encoder-decoder architecture from Attention is All You Need: 
 …architecture.petergostev.chatgpt.site</a> ","username":"petergostev","name":"Peter Gostev","profile_image_url":"https://pbs.substack.com/profile_images/1934694573797670912/1gnGJwlr_normal.jpg","date":"2026-09-10T20:43:13.000Z","photos":[{"img_url":"https://substackcdn.com/image/fetch/$s_!-BQ4!,w_1028,c_limit,f_auto,q_auto:best,fl_progressive:steep/l_play_button_usfui2,w_88,e_colorize:0/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F__ss-rehost__tw-video-preview-13_2098148819175104520.jpg","link_url":"https://t.co/wJzLLmRJms"}],"quoted_tweet":{},"reply_count":54,"retweet_count":334,"like_count":2762,"impression_count":218344,"expanded_url":null,"video_url":"https://video.twimg.com/amplify_video/2098148819175104520/vid/avc1/1316x720/36dLkQiID-HcJSjm.mp4","video_preview_media_key":"13_2098148819175104520","belowTheFold":true}" class="pencraft pc-display-flex pc-flexDirection-column pc-gap-12 pc-padding-16 pc-reset bg-primary-zk6FDl outline-detail-vcQLyr pc-borderRadius-md sizing-border-box-DggLA4 pressable-lg-kV7yq8 font-text-qe4AeH tweet-fWkQfo twitter-embed"> Peter Gostev @petergostev I've asked Astra to read the DeepSeek v4.1 Flash paper and compare it to the original Transformer architecture in 3D - you can zoom in an inspect each element side by side. Things have changed quite a bit.

Try yourself: …architecture.petergostev.chatgpt.site 8:43 PM · Sep 10, 2026 · 218K Views 54 Replies · 334 Reposts · 2.76K Likes If you read our V4 Pro writeup and Engram you should be up to date on the basic architectural reading for DeepSeek as of April 2026, but what we are HUGE fans of is the prefill/decode separation introduced here, 8B in prefill (input tokens), 16B in decode (output tokens), causing our alphabet soup of “DeepSeek v4.1-Flash: 763B-P8B-D16B” if you extend the established notation for MoEs. That’s a sparsity of 1-2%, and if you read the DeepSeek v4.1 Flash tech report , combined with new tweaks like Sliding-Window Attention Bounded Replay, makes for a KV cache footprint up to 1/8 that of V4 Flash… which make it much better/faster/cheaper for long running agents: 
 We are so glad that DeepSeek is back publishing SOTA research. Our last highlight is their comments on post-training, where they largely seem to agree with Prof Jie Tang : 
 Jasper Lu @lu__jasper This is notable. DeepSeek, a lab usually first to pioneer novel algorithms and architectures, is saying that at this point, the ROI of improving data quality far exceeds that of working on novel post-training algorithms.

I think this has already been true for some time for… DeepSeek @deepseek_ai 🚀 Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.

🔹 Introducing the smallest model in our new architecture family, with native visual understanding.
🔹 Designed for greater capability, faster inference, higher throughput, and scaling to larger models.

1/6 4:08 PM · Sep 10, 2026 · 176K Views 56 Replies · 143 Reposts · 1.67K Likes 
 
 AI News for 9/9/2026-9/10/2026. We checked 12 subreddits, 544 Twitters and no further Discords. AINews’ website lets you search all past issues. As a reminder, AINews is now a section of Latent Space . You can opt in/out of email frequencies! 
 AI Twitter Recap DeepSeek launched V4.1-Flash as a new open-weight flagship focused on extreme inference efficiency and low cost. 
 Independent benchmark account Artificial Analysis reported that DeepSeek V4.1 Flash surpasses DeepSeek V4 Pro 0813 despite being much cheaper, scoring 40 on the Artificial Analysis Intelligence Index , just below GLM-5.3-Flash and above the latest V4 Pro, while being priced at $0.30 / 1M input tokens and $1.20 / 1M output tokens with cached input at $0.006 / 1M and an additional 50% off-peak discount ; they also describe it as a 763B total-parameter model with 8B active input and 16B active output parameters, 1M-token context , text+image input, MIT license , and US/API availability via DeepSeek first party @ArtificialAnlys , @ArtificialAnlys , @ArtificialAnlys 
 Vals called it the new #1 open-weight model on the Vals Index , ahead of Kimi K3, at just $0.30 per test , the cheapest model in the open-weight top 10; they also note the eval ran with 1M context , 384 max output tokens , temperature 1 , default top-p/top-k, and high reasoning effort @ValsAI , @ValsAI , @ValsAI 
 Baseten shipped day-0 support and summarized the product positioning as smarter, faster, and more efficient than DeepSeek v4 Pro 0813 , with text and vision , US-only , ZDR , and 1M context @baseten 
 Ollama began rolling it out to Max and Team accounts, later expanding to Pro plan subscribers @ollama , @ollama , @ollama 
 Architecture and paper-level technical details The most discussed technical novelty is a causal encoder-decoder design aimed at lowering active compute and KV/cache costs. 
 Artificial Analysis says the model uses a new causal Encoder–Decoder architecture , with 8B active parameters for input/prefill and 16B active parameters for output/decode @ArtificialAnlys 
 Sebastian Raschka characterized V4.1 as a “big overhaul” and said they “should have called it DeepSeek V5,” explicitly highlighting the encoder-decoder setup as the key break from prior DeepSeek generations @rasbt 
 Multiple technical readers reacted to the design as unusually hybrid: one called it “a very interesting mix of very conservative and sometimes old ideas in research and potentially cutting edge efficiency and hardware design in engineering” @_xjdr 
 A concise architecture read from Stochastic Chasm compared the design philosophy to HySparse, NSA, and DeepSeek’s own CSA/HCA from V4 , summarizing it as a local sliding-window branch plus sparse retrieval branch , suggesting this sparse/local hybrid is becoming a broader pattern @stochasticchasm 
 The same account noted multimodal changes were not radical , saying DeepSeek mostly “lets the backbone handle most of it and give it visual tokens,” with 3x3 pixel unshuffle instead of the more common 2x2 @stochasticchasm 
 They later flagged a “big difference from K3 on vision encoders,” implying the vision front-end diverges materially from recent Chinese peers @stochasticchasm 
 TeortaxesTex observed a recurring DeepSeek pattern of doing something unusual in the first N layers —previously dense or hash-routed, now SWA-only —speculating this may reflect repeated training difficulties in early layers @teortaxesTex 
 Later, the same account argued the stack is “down to 40 layers , arguably only 20 legit decoder layers ,” underscoring just how aggressively DeepSeek may be compressing effective depth in decode-critical paths @teortaxesTex 
 Another thread fragment from TeortaxesTex suggested DeepSeek is doing multiple compression frequencies , “it’s just all CSA2,” in response to architectural discussion around memory compression @teortaxesTex 
 Nrehiew’s technical notes emphasize KV cache compression as central to the design, calling it a case study in “how obsessing over KV Cache compression gets you a hyper-efficient frontier model” @nrehiew_ 
 In a follow-up, nrehiew highlighted infrastructure specifics from the report: dispatch strategy to reduce long-tail stalls , router replay from previous checkpoints , management of shorter-completion off-policy effects via dataset-level capping , discard schemes , bounded off-policy ratio and loss masking , and persistent KVs and routers when a new checkpoint is updated; they also mention a final stage with full-vocab OPD on 40+ teacher models @nrehiew_ 
 Nrehiew concluded that the design looks cleaner than the older HSA + CSA combination in V4, saying it was “very clearly designed for inference,” and cited a striking ~890 bytes/token KV size for the benchmarked score regime @nrehiew_ 
 Stochastic Chasm inferred QAT for the KV cache , saying this would explain why the model performs better than peers under FP4 KV cache @stochasticchasm 
 Benchmark results and numbers Independent evals consistently paint V4.1-Flash as unusually strong on cost-adjusted intelligence, long context, and automation, with a major caveat around verbosity. 
 Artificial Analysis’ headline: 40 AA Index , above V4 Pro and below GLM-5.3-Flash @ArtificialAnlys , corroborated separately by Scaling01 @scaling01 
 Artificial Analysis reported AutomationBench-AA: 69% , tying GPT-6 Astra (69%) and above Grok 4.6 (67%) , while improving 15 points over V4 Flash 0731 and sitting 12 points above V4 Pro 0813 (57%) and 7 points above GLM-5.3 (62%) @ArtificialAnlys 
 On GDPval-AA v2 it reportedly gains 164 Elo , from 1468 to 1632 , overtaking Kimi K3 at 1584 @ArtificialAnlys 
 On AA-LCR v1.1 it scores 84% , on par with GPT-5.6 Sol and Gemini 3.8 Flash at 84% @ArtificialAnlys 
 Artificial Analysis also says V4.1 Flash is among the most verbose models measured , averaging 89k tokens per Intelligence Index task — 25% more than GLM-5.3 (71k), 29% more than GLM-5.3-Flash (69k), 62% more than V4 Pro 0813 (55k), and even above Fable 5.1 (78k) and Claude Opus 5 (73k) @ArtificialAnlys 
 Even with that verbosity, AA estimates just $0.27 per Intelligence Index task , roughly 7x below GLM-5.3 ($2.01) and Kimi K3 ($2.00) , and ~2.5x below V4 Pro 0813 ($0.67) @ArtificialAnlys 
 Vals’ result reinforces cost leadership: $0.30/test , #1 open-weight on their board @ValsAI 
 A separate reaction thread summarized DeepSWE-style claims more aggressively, saying V4.1 Flash offered better performance than GPT-5.6 Sol and Opus 5 in DeepSWE at 94% lower API costs , but that statement is secondhand summary rather than a primary benchmark post in this dataset @kimmonismus 
 Running it locally and inference engineering reactions A large fraction of discussion centered on the surprising ease of running V4.1-Flash on commodity-ish local hardware through offload and SSD streaming. 
 Fraser Price reported full-precision DeepSeek 4.1 Flash + DSpark at 200 TPS on 4 Max-Qs with just 64GB system RAM , offloading a 200GB Engram/hash table to NVMe ; he says this made keeping the full structure in RAM unnecessary and promised a vLLM recipe @fraserpricee 
 He later improved that to 300+ TPS on 4 RTX Pros , still at full precision , with <32GB peak system RAM , using a custom vLLM fork and SSD support @fraserpricee 
 Antirez showed DwarfStar running V4.1 Flash on a 128GB M5 Max , saying SSD streaming made it unexpectedly fast; he speculated both recent SSD-streaming changes and the possibility that DS4.1 “uses the same experts more” contributed @antirez 
 TeortaxesTex reacted that it is “incredible you can run fro