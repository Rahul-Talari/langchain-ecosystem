1. what is chunking?
   - Chunking is the process of breaking large documents into smaller, manageable pieces for AI indexing, search, and generation

2. Why we need chunking?

   - Context limits              : Fits text into LLM and embedding model windows.
   - Retrieval Quality & Latency : Pinpoints exact passages instead of searching whole books.
   - Cost control                : Lowers token consumption during search and generation

3. How can we do chunking?
   - GENERAL STRATEGIES
      → Fixed-Size Chunking        : Split text into fixed-size chunks                                    -> character text splitter
      → Recursive Chunking         : Split hierarchically using paragraph → sentence → word boundaries    -> Recursive Text Splitter
      → Document-Specific Chunking : Chunk according to document structure: Java, Python, HTML, Markdown
      → Semantic Chunking          : Split based on topic boundaries; Uses embeddings to identify semantic similarity
      → Agentic/LLM-Based Chunking : Use LLMs to identify meaningful chunk boundaries

   - CONTEXT / BEST PRACTICES
      → Overlap          : Repeat content between adjacent chunks → Preserves boundary context                         1,2   techniques
      → Context-Enriched : Add relevant document/section context → Helps LLM understand the chunk                      2,3,4 techniques
      → Metadata         : Document + Section + Page + Source + Access Info → Helps filter/manage chunks
      → Chunk Expansion  : Retrieve relevant chunk + neighboring chunks → Restores surrounding context after retrieval
      
   - TUNING
       → Chunk Size      : 250–500 tokens → General RAG; 500–1,000 tokens → Complex docs
       → Chunk Overlap   : 10–20% of chunk size

   - CONSIDERATIONS
      1. CONTENT Type     : Text + Tables + Images + Charts + Code
      2. QUERY & RETRIEVAL: Query Type: Simple + Analytical + Multi-hop  &   Retrieval: Precision vs Recall
      3. MODEL Limits     : Embedding + LLM Context Window
      4. SYSTEM           : Cost + Latency + Storage

4. How to decide this is the best one? Evaluation & Selection Tuning

   A. RETRIEVAL
       → Context Precision       : Retrieved context is relevant
       → Context Recall          : Required context is retrieved
       → Recall@K / Precision@K  : Retrieval effectiveness
       → MRR / NDCG              : Ranking quality

   B. GENERATION   Answer Quality: Relevance + Correctness + Groundedness
   C. SYSTEM       Latency + Cost: Speed + Token/Compute usage
