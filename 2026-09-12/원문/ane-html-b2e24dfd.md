# Retrospectively Reverse-Engineering Apple's Neural Engine

- 출처: Hacker News
- 원본 링크: https://eiln.github.io/posts/ane.html
- 발행: 2026-09-12T07:54:03+00:00
- 접근상태: 확인 완료

---

Retrospectively Reverse-Engineering Apple's Neural Engine | Eileen Yoon Eileen Yoon Home   |   About    Retrospectively Reverse-Engineering Apple's Neural Engine Aug 10, 2026 (5089 words) I stopped working on the reverse-engineered Apple Neural Engine (ANE) driver three years ago, upon a sad mini realization that the ANE block is just not that useful, and I could be doing more useful things, and moved onto upstreaming other, more useful, blocks. The ANE's architecture was too opinionated to build a general-purpose accelerator platform around it, and a linux driver effectively opening ANE hardware API access could not broaden the class of workloads it could do. Even macOS only regularly uses their own ANE to generate upsampled preview images in Finder.
 https://github.com/eiln/ane/tree/main 
 
M1 die shot: https://mastodon.social/@dougall/115149886886125067 The M5 (2025)'s headline feature was "LLM performance", and they also conveniently folded the ANE cores inside the GPU cores — I knew it was coming, but it officially feels like the beginning of the end for the standalone NPU. So, in honor of the ANE’s apparent demise, we will do something even more useless: go back and reverse-engineer the ANE on the M1, finish what we started. It's been three years (fuck), and I should know more than I did when I first worked on this.
 If the goal three years ago was to make the ANE useful by running ops on it; this time, it's more about mapping the full internal architecture — compute, datapath, scheduler, memory, and execution model — because those internal design decisions reveal the assumptions about ML workloads that Apple was willing to commit to silicon first in the A11 Bionic (2017), and what that says about the shift from CNN-era NPUs to today's GPUs running transformer workloads.
 1. Compute
 The 16 compute cores are probably the least interesting part of the ANE. Apple originally targeted dense image-processing CNN workloads, which consists of dense tensor reductions with predictable reuse. The M1 ANE compute core is a large parallel array of multiply-accumulate (MAC) units, but that alone says almost nothing about what workloads it was designed for and accels at.
 A convolutional layer does a dot product between an activation window and learned kernel weights, and attention does a dot product between a query and key vector. A dot product is a dot product, and a MAC does just that. What specialized ANE to the 2017 CNN models is not the MAC, but dataflow surrounding the MACs: when and where MAC inputs and outputs enter, stay, move. The assumption that transformers broke, especially with autoregressive decode, was predictable reuse patterns, which the ANE exploited to architect a dataflow efficient enough to run on phones. The M5 decision confirms that ANE's compute core remained still useful for transformers, but inside a different dataflow.
 Still, here's the datapath inside each of the 16 compute cores:
 ┌────────────────────── core ─────────────────────┐
 │ ┌───────── 256× MACs ─────────┐ ┌────────────┐ │
 │ │ MAD ─► add ─► accumulator │─►│ activation │ │
 │ │ ▲ │ │ └────────────┘ │
 │ │ └──────────┘ │ │
 │ └─────────────────────────────┘ │
 └─────────────────────────────────────────────────┘
 Multiply-Accumulate
 ANE has 16 parallel compute cores. Each compute core has 128 FP16 (or 256 INT8) parallel multiply-accumulate (MAC) lanes. Each MAC lane performs the recurrence:
\[
s\leftarrow s+a\times b
\] Multiply two operands \(a\) and \(b\), and then add the product to the running sum (accumulator).
 Repeating the MAC operation over T cycles computes a T-term dot product:
\[
s_T=s_0 + \sum_{t=0}^{T-1} a_t \, b_t.
\] A MAC lane thus performs a scalar reduction over time . A 16-core ANE has 2048 parallel MAC lanes,
\[
128\ \text{lanes/core}\times16\ \text{cores} =
2048\ \text{parallel MAC lanes}
\] So each cycle performs 2048 parallel reductions spatially , with time being the only reduction axis:
\[
S_T[q,p] = S_0[q,p] +
\sum_{t=0}^{T-1} a_t[q,p]\,b_t[q].
\] An individual MAC lane does not know what dimension of the matrix or tensor it is reducing over. It's important to note that a dot product vs matrix multiplication vs convolution arises from how the operands are mapped and scheduled onto the core. The ANE core (with the exception of kernel memory, discussed later) does not encode a 4-channel CNN layer into the hardware.
 Internally, the MAC datapath consists of a multiplier, adder, and a 32-bit accumulator register. Each cycle, the adder adds the fresh multiplier output with the previous sum, which then becomes the new running sum.
 operand a ──┐ ┌────────────┐ p[31:0] ┌──────────────┐ s_next[31:0] ┌─────────────┐
 ├──►│ MULTIPLIER │────────────►│ 32-BIT ADDER │────────────────►│ ACCUMULATOR │
 operand b ──┘ └────────────┘ └──────▲───────┘ └──────┬──────┘
 │ │ s[31:0]
 └────────────────────────────────┘
 This feedback path keeps the partial sum in memory local to the MAC lane, so it does not need fetched from an external memory far away, between MAC cycles.
 Regarding resolution, it does fixed-point reduction with FP16 at readout. The multiplier is 16-bit, accumulated in a 32-bit register as Q16.16, then read out as FP16 via sign-extend and etc. Working in integer (hex) FP16 representation, to probe the accumulator range, build a CoreML ANE program that computes a dot product with a vector of all (1)s, so each multiplier results in a bounded v, but the running sum in the accumulator keeps growing:
\[
s=\sum_{i=0}^{255}v=256v.
\] (v) CPU hex CPU value ANE hex CoreML value 127.9375 0x77ff 32752 0x77ff 32752 128 0x7800 32768 0x7c00 +∞ −128 0xf800 −32768 0xf800 −32768 −128.125 0xf801 −32800 0xfc00 −∞ Since 32768 is itself a valid FP16 word (0x7800), the ANE's 0x7c00 can't be FP16 output overflow, the clamp happens inside the accumulator, at \(2^{15}\). Thus the accumulator saturates at \(2^{15}\), exactly the range of a signed 32-bit fixed-point value with 16 fractional bits.
 Nonlinear Activation
 For a fused layer, the ANE computes:
\[
y = f(\sum_k x_k w_k + b)
\] Importantly, completed MAC sums feed directly into the post-MAC activation block, avoiding an intermediate memory round-trip. This is possible because the activation is pointwise: once a scalar reduction is complete, its activation depends only on that scalar and can be applied immediately.
 To determine how the ANE implements tanh() , compile a CoreML model containing a single TANH activation layer and inspect the resulting compiled hardware register file (hwx). The coefficient region contains 33 consecutive FP16 words beginning at 0x4288 :
 00004270: 3120 3001 0000 0000 0000 0000 0000 0000
00004280: 0000 0044 0000 003c 0000 f52f d633 bc35 # 0.000000 0.124329 0.244873 0.358398 
00004290: 6537 7038 1539 a239 183a 793a c93a 0a3b # 0.462158 0.554688 0.635254 0.704102 0.761719 0.809082 0.848145 0.879883 
000042a0: 3e3b 673b 883b a23b b63b c63b d33b dd3b # 0.905273 0.925293 0.941406 0.954102 0.963867 0.971680 0.978027 0.982910 
000042b0: e53b eb3b ef3b f33b f63b f83b fa3b fb3b # 0.986816 0.989746 0.991699 0.993652 0.995117 0.996094 0.997070 0.997559 
000042c0: fc3b fd3b fe3b fe3b ff3b 0000 0000 0000 # 0.998047 0.998535 0.999023 0.999023 0.999512 
000042d0: 003c 0300 6000 0000 0000 0000 0000 0000 Those 33 FP16 words match 33 IEEE LE FP16 quantized samples of \(\tanh(x)\):
\[
T_i=\operatorname{round}_{16}\!\left(\tanh(i/8)\right),
\qquad i=0,1,\ldots,32.
\] Now switch to RELU activation layer:
 activation program NonlinearMode lookup coefficients identity 0 none ReLU 1 none tanh 2 33 FP16 words Thus, mode 2 selects a custom 33-entry lookup table. 33 points defines 32 intervals. With \(R=3\), the knots are
\[
x_i=\frac{i}{8},\qquad i=0,\ldots,32,
\] covering \([0,4]\) with spacing \(1/8\). The input maps into the table as \(u=2^R|x|\),
so \(R\) sets the knot spacing. The resolution is smoother than its 33 bin; I suspect that adjacent entries are linearly interpolated. To test, build an impulse LUT with a single spike:
\[
T_8=1,\qquad T_k=0\ \text{for }k\ne8,\qquad R=3.
\] Then sweep the input across the two cells around \(T_8\). The measured output forms a triangle: magnitude rises linearly from \(0\) at \(|x|=7/8\) to \(1\) at \(|x|=1\), then falls linearly to \(0\) at \(|x|=9/8\).
 Thus, we know that mode 2 implements a 33-entry piecewise-linear LUT. \(R\) scales the input into LUT coordinates,
\[
u=2^R|x|,
\] so the knot spacing is \(\Delta x=2^{-R}\). \(\lfloor u\rfloor\) and \(\lceil u\rceil\) select the adjacent entries, and \(\alpha=u-\lfloor u\rfloor\) gives the interpolation weight between them.
 Scaling and Bias
 CoreML also supports a linear scaling and bias \(ax + b\) transform. I then suspected \(ax + b\) could share the linear interpolation hardware of mode 2. To confirm, construct a CoreML model with a ReLU with a constant scale and offset:
\[
z=4x-2,\qquad
y=\operatorname{ReLU}\left(\frac{z}{2}+1\right),
\] If the compiler folds the constant scale and offset into the convolution:
\[
W'=\frac12W=2,\qquad
b'=\frac12b+1=0,
\] 
\[
y=\operatorname{ReLU}(2x).
\] Decoding model.espresso.weights confirms exactly this folded transformation on ReLU:
 authored convolution: W = 4, b = -2
 activation affine: s = 0.5, c = 1
 compiled convolution: W' = 2, b' = 0
 And the register file hexdiff shows how bias and activation are fused into the same post-MAC path at compile time:
 Probe Tasks BiasMode PostScaleMode NonlinearMode Plain convolution 1 0 0 0 Explicit Core ML Bias 1 1 0 0 Bias + ReLU 1 1 0 1 Bias + tanh 1 1 0 2 Extremely cursed idea: use nonlinear interpolation to compute an additional kernel pass, or quantize int8 into int4 weights.
 2. Scheduler
 The ane driver source code is disappointingly boring. The driver never gives the ANE a CONV , MATMUL , or RELU opcode to run. All the neural operations have all already been compiled into a command stream of task descriptors (TDs), and the driver software simply loads the task to memory, sets the pointer to the opaque task blob via (TM_ADDR, TM_SIZE), and submits the staged task by ringing the doorbell (TM_PUSH).
 static void ane_tm_push_tq ( struct ane_device * ane, struct ane_request * req)
 {
 int qid = req -> qid;
 tm_write32 (ane, TM_ADDR, tq_read32 (ane, TQ_ADDR1 (qid)));
 tm_write32 (ane, TM_INFO, tq_read32 (ane, TQ_SIZE1 (qid)) | req -> td_count);
 tm_write32 (ane, TM_PUSH, TQ_PRTY_TABLE[qid] | (qid & 7 ) << 8 ); // magic
 }
 https://github.com/eiln/ane/blob/main/ane/src/ane_tm.c#L87 
 The hardware then owns the submission until completion, and raises an interrupt to the ARM64 core when it's done.
 static void ane_tm_handle_irq ( struct ane_device * ane)
 {
 int line;
 
 line = 0 ;
 for (u32 n = 0 ; n < tm_read32 (ane, TM_IRQ_EVTC (line)); n ++ ) {
 This (boring) command submission frontend resembles that of a GPU's, think NVIDIA's pushbuffer/PBDMA. The software submits a command stream resident in memory, and the GPU's command processor walks over command stream and dispatches the commands, without knowing what that command executes.
 TM_ADDR and TM_INFO are global staging registers, and TM_PUSH atomically commits that staged launch state, given that nothing happens until TM_PUSH is written ("magic"). TM_INFO in particular stores the total number of descriptors in the supplied stream:
 TM_INFO[31:16] = descriptor_dwords - 1
TM_INFO[15:0] = descriptor_count
 TM_INFO register naturally maps onto a hardware counter:
 if (fetch) begin 
 if (word_ctr == descriptor_dwords_minus_1) begin 
 word_ctr <= 0 ;
 desc_ctr <= desc_ctr + 1 ;
 end else begin 
 word_ctr <= word_ctr + 1 ;
 end 
 end 
 Why the "minus 1"? Encoding length - 1 is an RTL-friendly way to terminate a zero-based counter out of the critical path. But note how, compared to GPU commands which parse a variable-length stream of descriptors in a ringbuffer, ANE only receives the total count, indicating that descriptors are fixed-size.
 Task Queue
 Going one layer deeper, what's in a task queue (TQ) that the task manager selects from?
 +------------------+
CPU / driver ------>| Task Manager |
 | |
 | schedule / fetch |
 | / dispatch |
 +--------+---------+
 |
 +------------------+------------------+
 | | |
 v v v
 +---------+ +---------+ +---------+
 | TQ 0 | ... | TQ 3 | ... | TQ 7 |
 | BAR[32] | | BAR[32] | | BAR[32] |
 | NID | | NID | | NID |
 | state | | state | | state |
 +---------+ +---------+ +---------+
 There's 8 copies of the same register block (indexed by qid (0…7)), structured as:
 TQ[qid] + 0x000 STATUS
 0x010 PRIORITY
 0x014 VACANT
 0x01c INFO
 
 0x020 BAR1[0..31] // task1
 0x0a0 NID1
 0x0a4 SIZE2
 0x0a8 ADDR2
 
 0x0ac BAR2[0..31] // task2
 0x12c NID2
 0x130 SIZE1
 0x134 ADDR1
 
 next qid: +0x148
 Each TQ holds:
 (1) Per-TQ scheduling state (status, priority, and vacancy) (2) Two sets of command stream descriptors, per-TQ (ADDR1/ADDR2, SIZE1/SIZE2, NID1/NID2, and 32 BARs). The two slots are certainly a ping-pong staging scheme to let one slot execute, while software modifies the other slot. Notice how TM_PUSH executes a task referenced in TM_ADDR/TM_SIZE by attaching a qid:
 tm_write32 (ane, TM_PUSH, TQ_PRTY_TABLE[qid] | (qid & 7 ) << 8 ); // magic
 The natural interpretation is that the descriptor stream specifies what task to run, while the qid selects the launch context the descriptor runs under. The resident TQ context (BAR, NID) is much like a GPU hardware channel.
Here's my driver populating a single TQ to launch it:
 int ane_tm_enqueue ( struct ane_device * ane, struct ane_request * req)
 {
 int qid = req -> qid;
 
 tq_write32 (ane, TQ_STATUS (qid), 0x1 );
 
 for ( int bdx = 0 ; bdx < ANE_TILE_COUNT; bdx ++ ) {
 tq_write32 (ane, TQ_BAR1 (qid, bdx), req -> bar[bdx]);
 }
 
 tq_write32 (ane, TQ_SIZE1 (qid), ((req -> td_size >> 2 ) - 1 ) << 0x10 );
 tq_write32 (ane, TQ_ADDR1 (qid), req -> btsp_iova);
 tq_write32 (ane, TQ_NID1 (qid), (req -> nid & 0xff ) << 8 | 1 );
 
 return 0 ;
 }
 https://github.com/eiln/ane/blob/main/ane/src/ane_tm.c#L70 
 The o