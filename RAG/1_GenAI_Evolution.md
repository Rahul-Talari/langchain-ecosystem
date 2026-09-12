## Quick recap

1. **How NLP Started**  
   Rule-Based → Statistical NLP → Word Embeddings

2. **How Architectures Evolved**  
   RNN → LSTM → GRU → Seq2Seq → Attention → Transformers  
   → Encoder-only / Decoder-only / Encoder-Decoder

3. **How LLMs Are Trained**  
   Pretraining → Instruction Tuning → Alignment → Multimodal Training

4. **What Makes Modern LLMs Powerful**  
   MoE → RAG → RLHF → Multimodal Systems

5. **How We Deploy LLMs**  
   Cloud → Enterprise → High-performance → Open-source APIs  
   → Local / Self-hosted

6. **How We Optimize LLMs**  
   Quantization → LoRA/PEFT → Distillation → Pruning  
   → Caching → Speculative Decoding → KV Cache

---

# GenAI Evolution

## 1) NLP and deep learning evolution

### Traditional NLP
- **Rule-Based Systems:** handcrafted linguistic rules and dictionaries
- **Statistical NLP:** probabilistic methods such as Naive Bayes, HMM, and CRF
- **Word Embeddings:** dense vector representations that capture semantic meaning
  - Examples: Word2Vec, GloVe, FastText

### Recurrent architectures
- **RNN:** processes sequential data step by step using previous hidden states; suffers from vanishing gradients on long sequences
- **LSTM:** RNN variant with memory cells and gates for learning long-term dependencies
- **GRU:** simplified LSTM with fewer gates and faster training

### Seq2Seq architectures
- **Encoder–Decoder:** encoder converts input sequence into a context representation; decoder generates target sequence
- **Attention Mechanism:** allows the model to focus on the most important tokens dynamically and solves the fixed-context bottleneck

### Transformer architectures
- **Transformer:** replaced recurrence with self-attention, enabling parallel processing and long-context understanding

### Transformer variants
- **Encoder-Only Transformer:** learns contextual understanding of input text; best for classification, embeddings, search, and understanding
  - Examples: BERT, RoBERTa, DistilBERT
- **Decoder-Only Transformer:** predicts the next token autoregressively; best for text generation and conversational AI
  - Examples: GPT, LLaMA, Claude, DeepSeek
- **Encoder-Decoder Transformer:** encoder understands input; decoder generates transformed output; best for translation, summarization, and QA
  - Examples: T5, BART, FLAN-T5

---
## 2) How LLMs Evolved and Learned

Models evolved from **representing language → transforming language → generating language**, while training evolved from learning patterns → following instructions → aligned behavior.

### Model evolution

* **Word Embeddings** → represent words as semantic vectors — Word2Vec, GloVe, FastText
* **Seq2Seq** → transform one sequence into another using Encoder–Decoder
* **Transformers** → self-attention replaces recurrence, enabling parallel training and long-range interactions
* **Decoder-only LLMs** → autoregressive next-token generation; dominant for generative AI — GPT, LLaMA, Claude, DeepSeek

### Training evolution

* **Pretraining** → learn language patterns and knowledge from massive datasets using next-token prediction
* **Instruction Tuning** → learn to follow instructions through instruction–response examples
* **Alignment** → improve helpfulness and safety using human preferences and feedback
* **Multimodal Training** → extend learning across text, images, audio, and video

### Why the shift?

1. **Parallelization** → Transformers make large-scale training more efficient.
2. **Scaling** → More data, parameters, and compute improve model capabilities.
3. **Long-range dependencies** → Self-attention captures relationships between distant tokens.
4. **Transfer learning** → One pretrained model can be adapted to many tasks.
5. **Instruction following** → Fine-tuning makes models more useful for real-world applications.

### In one line

**Embeddings → Seq2Seq → Transformers → LLMs**
**Pretraining → Instruction Tuning → Alignment → Multimodal**
---

## 3) What Makes Modern LLMs Powerful

Modern LLMs combine **scale, efficient computation, alignment, external knowledge, and multimodal capabilities**.

### Key enhancements

* **Scaling** → larger models, datasets, and compute improve model capabilities
* **MoE** → activates selected experts per token, enabling large models with lower computation
* **RLHF / Preference Alignment** → aligns model responses with human preferences, helpfulness, and safety
* **RAG** → provides external, up-to-date, and domain-specific knowledge at inference time
* **Multimodal AI** → enables understanding across text, images, audio, and video
* **Tool Use / Agents** → allows models to use search, APIs, code, and external systems to perform tasks

### In one line 

**Scaling → MoE → RLHF → RAG → Multimodal AI → Tool Use / Agents**

---

## 4) Model selection and deployment

### How to select an LLM
- **Quality of data and task complexity**
- **Cost and latency**
- **Privacy and deployment constraints**

### Cloud and enterprise inference
- **RunPod**: GPU cloud platform widely used for AI inference and model hosting
- **Lambda**: GPU cloud and inference infrastructure provider
- **AWS Bedrock**: managed foundation model inference via Amazon AWS
- **Azure AI Foundry**: Microsoft platform for hosting and inferencing foundation models
- **Google Vertex AI**: Google Cloud model training and inference platform

### High-performance inference
- **Fireworks AI**: high-performance inference optimized for fast LLM serving
- **Groq**: ultra-fast inference using custom LPU hardware
- **Cerebras**: AI inference/training on wafer-scale chips
- **SambaNova**: enterprise AI inference and generative AI infrastructure
- **DeepInfra**: cost-efficient inference provider for open-source models
- **OctoAI**: generative AI inference optimization and deployment platform

### Open-source model hosting & APIs
- **Together AI**: training, fine-tuning, and inference for open-source models
- **Hugging Face**: open-source ecosystem offering inference APIs and model hosting
- **Replicate**: API platform to run and deploy open-source AI models
- **Baseten**: AI model deployment and inference platform
- **OpenRouter**: unified API gateway for multiple LLM providers

### Local and self-hosted inference
- **vLLM**: high-throughput inference engine optimized for LLM serving
- **Ollama**: local LLM deployment and inference framework
- **TensorRT-LLM**: NVIDIA-optimized framework for accelerating LLM inference on GPUs
- **llama.cpp**: lightweight C/C++ inference engine for running LLMs on CPUs and edge devices
- **ExLlama**: optimized inference library for quantized LLaMA-style models
- **ONNX Runtime**: cross-platform runtime for optimized AI model inference
- **TGI**: Hugging Face Text Generation Inference server for scalable deployment
- **LM Studio**: desktop application for running local LLMs with a GUI

---

## 5) Model optimization and adaptation

### Optimization / adaptation methods
- **Quantization**: reduces model precision for faster inference and lower memory usage
- **LoRA / PEFT**: parameter-efficient fine-tuning for adapting LLMs cheaply
- **Distillation**: transfers knowledge from a large model to a smaller efficient model
- **Pruning**: removes less important parameters to reduce model size
- **Caching**: reuses previous computations to lower latency
- **Speculative Decoding**: uses smaller draft models to accelerate token generation
- **KV Cache**: stores transformer attention states to speed autoregressive inference

---
