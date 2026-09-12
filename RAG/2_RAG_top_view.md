# RAG Top View

## 1) Core engineering layers

**Prompt Engineering:** Designing instructions and prompts for the LLM. Prompt = how to ask.

**Context Engineering:** Designing the information and context provided to the LLM. Context = what to provide. Includes RAG, agents, and memory.

**Harness Engineering:** Loop engineering + graph engineering.

**LLM Foundations:** Large language models are trained on massive text corpora and generate text by predicting the next token. Core capabilities include understanding, reasoning, summarization, translation, and code generation.

**Data sources:** Web crawler, web scraping, PDF parsers.

### LLM basics
- **Transformer architecture:** tokenization, attention, context windows, positional encoding
- **Model behavior:** temperature, top-p, max tokens, sampling settings
- **Model types:** base models, instruction-tuned models, chat models, multimodal models
- **Training goals:** next-token prediction, alignment, safety tuning, preference optimization
- **Inference concerns:** latency, cost, context length, hallucination risk

---

## 2) RAG overview

**RAG (Retrieval-Augmented Generation):** An AI architecture that retrieves relevant information from external knowledge sources, augments the prompt with it, and passes it to the LLM to generate accurate, context-aware, up-to-date responses.

### RAG pipeline

1. **Knowledge Base Construction**
   - Ingestion
   - Preprocessing
   - Chunking
   - Embedding generation
   - Vector DB indexing / KG construction

2. **Query Processing**
   - User query
   - Query embedding
   - Retrieval from vector DB / graph DB / relational DB
   - Context augmentation in the prompt

3. **LLM Generation**
   - Prompt + retrieved context + memory
   - LLM generates the final response

4. **Post-Processing & Evaluation**
   - Response formatting
   - Citation and source attribution
   - Guardrails / safety checks
   - Hallucination and quality evaluation

---

## 3) Security and guardrails

**Security:** Guardrails protect against harmful, malicious, or untrusted inputs.

### Why guardrails?
- Protect against harmful content
- Prevent sensitive data leakage
- Ensure safe, relevant, and compliant outputs
- Prevent abuse and excessive usage

### Guardrail types
1. **Content Filters**
   - Hate, toxicity, sexual content, violence, self-harm, misconduct
   - Prompt injection protection against jailbreaks and instruction overrides

2. **Sensitive Information / PII Filters**
   - Detect, mask, or redact confidential or personal data

3. **Denied Topics**
   - Restrict malware, fraud, weapon-related, and other prohibited domains

4. **Word / Phrase Filters**
   - Block predefined keywords, phrases, or regex patterns

5. **Grounding / Relevance Checks**
   - Validate contextual relevance and reduce hallucinations

6. **Output Validation**
   - Ensure policy compliance, safe output, and schema correctness

7. **Rate Limiting / Abuse Protection**
   - Prevent spam, abuse, and adversarial attacks

### Query-time safety flow
- **User Query**
  - Input validation
  - Content filters
  - PII detection
  - Injection checks
  - Denied topic check
  - Rate limit enforcement
- **Retrieval**
  - Relevance scoring
  - Grounding prep
- **Generation**
  - Model inference with guardrails in system prompt
- **Output Validation**
  - Safety re-check
  - Schema validation
  - Faithfulness checks
- **Logging & Monitoring**
  - Audit trail
  - Abuse detection

---

## 4) Evaluation

**Evaluation:** Answer relevance, groundedness, LLM-as-Judge, direct assessment, pairwise assessment.

Retrieval: Recall@K, Precision@K, MRR, NDCG
Generation: Relevance, Groundedness, Faithfulness, Correctness

### Evaluation methods

1. **Human-in-the-loop**
   - Pros: High accuracy, better trust and safety.
   - Cons: Expensive, slower, less scalable, subjective bias.

2. **LLM-as-Judge**
   - Pros: Detailed feedback, scalable, low cost.
   - Cons: Model bias, no human intuition, version drift.

3. **Benchmark Evaluation**
   - Tests on standard datasets such as MMLU, GSM8K, HumanEval, HELM.
   - Pros: Fair, fast, comparable, easy to track improvements.
   - Cons: Data leakage, prompt sensitivity, may not reflect real-world use.

### LLM response evaluation
- **Answer Relevance:** Does the answer address the user query?
- **Groundedness:** Is the answer supported by the retrieved or provided context?
- **Faithfulness:** Does the model avoid inventing facts?
- **LLM-as-Judge:** Uses another model to score or compare responses.

---

## 5) Knowledge Base Construction: Loaders, Chunking, embedding, vector DB/KG construction 

**Parsing**
- Document parser
- Web crawler
- Web parser

**Chunking**
- See chunking strategies: https://www.pinecone.io/learn/chunking-strategies/

**Embedding**: predefined - frequency-based, neural network based, MTEB; customized: fine-tuned
- Frequency-based: BOW, TF-IDF, N-grams
- Neural network-based: word2vec, fastText, BERT, LLM-based
- Token-level and sentence-level embeddings
- Fine Tune Embeddings, MTEB

**Vector indexing**: Algorithm and DB selection
- Vector DB algorithms
- Many vector DB options

- **Build Vector DB from Scratch:** https://www.linkedin.com/posts/deshwalmahesh_vectordb-learrning-opensource-activity-7331540641677557761-5OjE
- **Different types of search:** https://www.linkedin.com/posts/bhavishya-pandit_llm-opensource-llama-activity-7332269883692322817-aUF2


**Knowledge base**
- Vector DB
- Graph DB
- Relational DB

---

## 6) Advanced retrieval techniques

### Query Enhancement
- Query Expansion: generate alternative queries
- Multi-Query Retrieval: search with multiple query variations
- Self-Query Retrieval: convert query into search + filters

### Filter, Retrieve, Rank
- Metadata Filtering: filter by metadata
- Vector Search: semantic similarity search
- Reranker: reorder retrieved results by relevance
- Hybrid Search: combine keyword + vector search
- KG Retrieval: retrieve related entities and relationships

### Advanced retrieval patterns
- Sentence Window → add surrounding context
- Auto Merge → combine related chunks
- Reranker → reorder by relevance

---

## General practical AI task areas

- **Tabular: ML**
- **Text Corpus: NLP**
- **Audio**
- **Images/videos: Computer Vision**
- **text+Image+Video+Audio = Multimodal**
