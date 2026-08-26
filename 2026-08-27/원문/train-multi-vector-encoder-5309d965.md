# Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers

- 출처: Hugging Face Blog
- 원본 링크: https://huggingface.co/blog/train-multi-vector-encoder
- 발행: 2026-08-26T00:00:00+00:00
- 접근상태: 확인 완료

---

Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers 

 

 

 

 
 
 
 
 Hugging Face Models Datasets Spaces Buckets new Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden"> 
 
 
 
 
 Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers
 
 Published
 August 26, 2026 Update on GitHub Upvote 27 +21 Tom Aarsen tomaarsen Follow :last-child]:mb-0"> 
 Table of Contents What are Multi-Vector models? Why Finetune? Training Components Model Finetuning an existing multi-vector model Building one from a base transformer Which starting point should you pick? Dataset Data on the Hugging Face Hub Local Data Dataset Format Loss Function Training Arguments Evaluator Trainer Callbacks Multi-Dataset Training Evaluation Optimizing the index Acknowledgements Additional Resources Training Examples Documentation Sentence Transformers is a Python library for using and training embedding and reranker models for a wide range of applications, such as retrieval augmented generation, semantic search, semantic textual similarity, and more. Its v6.0 update introduces a fourth model type: MultiVectorEncoder , for ColBERT-style late interaction retrieval, alongside a complete training approach for it. In this blogpost, I'll show you how to use it to finetune a multi-vector model that outperforms general-purpose retrievers on your data. This method can also train strong new multi-vector models from scratch. Everything below runs on pip install -U "sentence-transformers[train]" .

 Finetuning multi-vector models involves several components: the model itself, datasets, loss functions, training arguments, evaluators, and the trainer class. I'll have a look at each of these components, accompanied by practical examples of how they can be used for finetuning strong multi-vector models.

 Lastly, in the Evaluation section, I'll show you that my finetuned multi-vector-encoder/mLateOn-medical model, trained in 14.5 hours on a single RTX 3090 alongside this blogpost, easily outperforms every general-purpose retrieval model I could find on my medical retrieval evaluation: dense, sparse, lexical, and multi-vector alike.

 

 If you're interested in finetuning dense embedding models, sparse embedding models, or rerankers instead, then consider reading through my prior Training and Finetuning Embedding Models , Training and Finetuning Sparse Embedding Models , and Training and Finetuning Reranker Models blogposts.

 
 This blogpost is about training multi-vector models. If you want to learn how to use them, from loading and encoding to indexing in vector databases, see the companion Multi-Vector (Late Interaction) Embedding Models with Sentence Transformers blogpost.

 
 
 
 
 
 
 Table of Contents
 
 
 
 What are Multi-Vector models? 
 Why Finetune? 
 Training Components 
 Model 
 Finetuning an existing multi-vector model 
 Building one from a base transformer 
 Which starting point should you pick? 
 
 
 Dataset 
 Data on the Hugging Face Hub 
 Local Data 
 Dataset Format 
 
 
 Loss Function 
 Training Arguments 
 Evaluator 
 Trainer 
 Callbacks 
 Multi-Dataset Training 
 
 
 Evaluation 
 Optimizing the index 
 
 
 Acknowledgements 
 Additional Resources 
 Training Examples 
 Documentation 
 
 
 
 
 
 
 
 
 What are Multi-Vector models?
 
 
 A dense embedding model compresses a whole text into a single vector, and similarity is one dot product between two such summaries. A multi-vector model (also called a late-interaction or ColBERT-style model) skips that compression. It keeps one small vector per token and scores a query against a document with the MaxSim operator, where every query token finds its best-matching document token and the scores are summed. Token-level matching preserves exactly the fine-grained signals that a single vector has to average away, which usually means stronger retrieval, at the cost of a bigger index.

 The companion Multi-Vector Embedding Models blogpost covers the architecture, encoding, scoring, and indexing in detail, so I'll keep this section short and get to the training.

 

 
 
 
 
 
 Why Finetune?
 
 
 Finetuning multi-vector models significantly improves their retrieval performance on your specific domain: the vocabulary, the query style, and the notion of relevance all differ between web search, legal discovery, code search, and scientific literature review. Because queries and documents are matched token by token, multi-vector models pick up fine-grained domain signals that single-vector models tend to average away, and they respond very well to even modest amounts of in-domain finetuning data.

 Beyond that, most released retrieval models were configured for short passages. The classic ColBERT checkpoints truncate documents at 180 or 300 tokens, and many popular dense models at 256 or 512, because their MS MARCO-style training data rarely goes beyond that. If your documents are long, these models silently discard most of every document before scoring it. On my medical evaluation with passages averaging 941 tokens, I measured that this truncation costs up to 0.24 NDCG@10, considerably more than any difference between model architectures. When you train your own model, you configure the document length that your data needs.

 LightOn ran into this same dynamic with code retrieval, where general LateOn wasn't enough and they trained LateOn-Code . Your domain, whether that's medical, legal, financial, or your company's internal documents, is not getting an official model. This blogpost shows you how to build it yourself, in a matter of hours, on a single consumer GPU.

 
 
 
 
 
 Training Components
 
 
 Training MultiVectorEncoder models involves the following components:

 
 Model : The model to finetune or the architecture to build fresh. 
 Dataset : The data used for training and evaluation. 
 Loss Function : A function that measures the model's performance and guides the optimization process. 
 Training Arguments (optional): Parameters that impact training performance, tracking, and debugging. 
 Evaluator (optional): A class for evaluating the model before, during, or after training. 
 Trainer : Brings together all training components. 
 
 Let's take a closer look at each component.

 
 
 
 
 
 Model
 
 
 Multi-vector training gives you a real choice of starting point, and it matters more than you might expect.

 
 
 
 
 
 Finetuning an existing multi-vector model
 
 
 If you want to further finetune an existing multi-vector model, you don't have to worry about the architecture at all:

 from sentence_transformers import MultiVectorEncoder

 # Loading in fp32 is preferred for training if your memory can handle it 
model = MultiVectorEncoder(
 "lightonai/mLateOn-unsupervised" ,
 model_kwargs={ "torch_dtype" : "float32" },
 processor_kwargs={ "model_max_length" : 8192 }, # the tokenizer-level token limit 
)
 
 The checkpoint brings its own recipe along: its query and document marker tokens, its projection head, its scoring skiplist. For finetuning, you generally want to keep all of that and change only what your data demands. The first thing to check is the length configuration, since many released checkpoints cap documents at 180 to 512 tokens (see Why Finetune? ), and my medical passages run to 1,400 tokens. The mLateOn family already serves the backbone's full 8192 token context, but if your starting checkpoint carries caps, lift them:

 # Let the model read full documents instead of the caps it was trained with, 
 # e.g. GTE-ModernColBERT-v1 ships with query_length=48 and document_length=300 
model[ 0 ].query_length = None 
model[ 0 ].document_length = None 
 
 With the per-task caps unset, truncation falls back to the tokenizer's model_max_length , which is why I configure that limit at load time above.

 I made one more change, adding a punctuation skiplist that excludes punctuation tokens from document-side scoring and storage. In a 4-way ablation (none, punctuation, stopwords, both) it modestly won on quality, and it shrinks the document index by 9.6% on this data for free:

 import string

 # model[2] is the MultiVectorMask module 
model[ 2 ].skiplist_words = list (string.punctuation)
model[ 2 ].resolve_with_tokenizer(model.tokenizer) # token ids are cached, so re-resolve after changing 
 
 
 
 
 
 
 Building one from a base transformer
 
 
 You can also point MultiVectorEncoder at any base transformer, and a fresh, randomly initialized token-level projection is appended for you:

 from sentence_transformers import MultiVectorEncoder

model = MultiVectorEncoder( "answerdotai/ModernBERT-base" , model_kwargs={ "torch_dtype" : "float32" })
 # MultiVectorEncoder( 
 # (0): Transformer({..., 'architecture': 'ModernBertModel'}) 
 # (1): Dense({'in_features': 768, 'out_features': 128, 'bias': False, ...}) 
 # (2): MultiVectorMask({'skiplist_words': [], 'skiplist_tasks': ['document'], ...}) 
 # (3): Normalize({...}) 
 # ) 
 
 That's the classic ColBERT pipeline: a Transformer producing contextualized token embeddings, a token-level Dense projecting each of them down to 128 dimensions, a MultiVectorMask deciding which tokens count during scoring, and a token-level Normalize . The projection starts random, so training is required before this model is useful. Interestingly, this works with strong dense embedding backbones too. A fresh projection on Alibaba-NLP/gte-modernbert-base reached within 0.03 of the existing-checkpoint starting points in my experiments, from nothing but the projection and 25k training pairs.

 The classic ColBERT tokenization tricks ( [MASK] query expansion, [Q] / [D] prefix tokens, a document length cap, a punctuation skiplist) are all off by default and configurable. See Creating Custom Models for the full set. For what it's worth, I tested [MASK] query expansion in four configurations for my domain finetune and none of them made a measurable difference, so don't feel obliged to reach for the classic recipe.

 
 
 
 
 
 Which starting point should you pick?
 
 
 I measured this directly while preparing this blogpost, taking six starting points and training each with the identical recipe on 25k medical question-passage pairs from MIRIAD , then evaluating on 1,000 held-out questions against a 50,000 passage corpus:

 
 
 
 Starting point 
 Zero-shot NDCG@10 
 After 25k pairs 
 Delta 
 

 
 lightonai/mLateOn-unsupervised 
 0.9087 
 0.9398 
 +0.0311 
 
 
 lightonai/mLateOn 
 0.9277 
 0.9319 
 +0.0042 
 
 
 lightonai/LateOn-unsupervised 
 0.9026 
 0.9206 
 +0.0180 
 
 
 lightonai/LateOn 
 0.9185 
 0.9105 
 -0.0080 
 
 
 lightonai/GTE-ModernColBERT-v1 
 0.9198 
 0.9007 
 -0.0191 
 
 
 Fresh head on gte-modernbert-base 
 - 
 0.9177 
 - 
 
 
 
 
 The result surprised me, and it replicated across two model families. *The -unsupervised checkpoints adapt to a new domain far better than their finished siblings, overtaking them despite starting lower. These checkpoints sit after large-scale contrastive pretraining but before supervised finetuning on general retrieval, so they carry all the late-interaction structure with none of the general-purpose tuning that domain training then has to undo. The finished checkpoints, by contrast, barely moved or even regressed, at every learning rate I tried.

 So, if the model family you like publishes a pre-supervised checkpoint, start there. If not, a fresh projection on a strong retrieval-pretrained backbone is a close runner-up. Continuing from a fully finished checkpoint is the weakest option for domain adaptation, despite being the most natural-feeling one.

 
 
 
 
 
 Dataset
 
 
 The MultiVectorEncoderTrainer uses datasets.Dataset or datasets.DatasetDict instances for training and evaluation. You can load data from the Hugging Face Datasets Hub or use local data in whatever format you prefer (e.g. CSV, JSON, Parquet, Arrow, or SQL).

 Note: Lots of public datasets that work out of the box with Sentence Transformers have been tagged with sentence-transformers on the Hugging Face Hub, so you can easily find them on https://huggingface.co/datasets?other=sentence-transformers . Consider browsing through these to find ready-to-go datasets that might be useful for your tasks, domains, or languages.

 
 
 
 
 
 Data on the Hugging Face Hub
 
 
 You can use the load_dataset function to load data from datasets on the Hub:

 from datasets import load_dataset

train_dataset = load_dataset( "tomaarsen/miriad-4.4M-split" , split= "train" )

 print (train_dataset)
 """ 
 Dataset({ 
 features: ['question', 'passage_text'], 
 num_rows: 4467542 
 }) 
 """ 
 
 This is the dataset I'll train on in this blogpost: 4.4 million medical questions from MIRIAD , each paired with the source passage that contains its answer (averaging 941 tokens). Simple (query, relevant passage) pairs like these are the easiest retrieval training data to collect for your own domain, and as you'll see, they're all you need.

 
 
 
 
 
 Local Data
 
 
 You can also use load_dataset for loading local data in common file formats:

 from datasets import load_dataset

dataset = load_dataset( "csv" , data_files= "my_file.csv" )
 # or 
dataset = load_dataset( "json" , data_files= "my_file.json" )
 
 And if your local data requires pre-processing, you can use datasets.Dataset.from_dict to initialize your dataset with a dictionary of lists:

 from datasets import Dataset

queries = []
documents = []
 # Open a file, perform preprocessing, filtering, cleaning, etc. 
 # and append to the lists 

dataset = Dataset.from_dict({
 "query" : queries,
 "document" : documents,
})
 
 
 
 
 
 
 Dataset Format
 
 
 It is important that your dataset format matches your loss function (or that you choose a loss function that matches