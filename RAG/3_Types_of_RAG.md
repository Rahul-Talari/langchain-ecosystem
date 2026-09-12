# Evolution of RAG Architectures

1. Naive RAG - Retrieve → Generate
2. Advanced RAG
   - Retrieval quality: better chunking, embedding model, vector DB, hybrid search, metadata filtering, reranking
   - Query optimization: query rewriting, query transformation, HyDE, RAG-Fusion, Step-Back Prompting
   - Retrieval control: Self-RAG, FLARE, RAPTOR, CRAG, Adaptive RAG
   - Multi-step reasoning: multi-hop, IRCoT, GraphRAG, LightRAG, HippoRAG, KAG
   - Alternative retrieval: BM25, Text-to-SQL, graph traversal
   - Agentic RAG: ReAct, Multi-agent RAG

| #   | Category                          | Simple Explanation                                                       | Representative Systems                    |
| --- | --------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------- |
| 1   | Naive RAG                         | Reduces hallucinations with external knowledge.                          | RAG                                       |
| 2   | Advanced RAG                      | Improves retrieval quality and reasoning.                                | Better chunking, embeddings, vector DBs  |
| 3   | Query Transformation              | Rewrites the user query before retrieval to improve downstream search.   | HyDE, RAG-Fusion, Step-Back Prompting     |
| 4   | Retrieval-Aware / Self-Reflective | Retrieves only when needed and validates results.                       | Self-RAG, FLARE, RAPTOR                   |
| 5   | Corrective & Adaptive RAG         | Checks retrieval quality and chooses the best path.                     | CRAG, Adaptive RAG                        |
| 6   | Multi-Hop Reasoning               | Retrieves information in multiple steps for complex questions.           | IRCoT                                     |
| 7   | Graph-Based RAG                   | Uses knowledge graphs to capture missing relationships.                 | GraphRAG, LightRAG, HippoRAG, KAG        |
| 8   | Vectorless RAG                    | Uses keywords, SQL, or graphs instead of embeddings.                   | BM25, Text-to-SQL, Graph Traversal        |
| 9   | Agentic RAG                       | Solves dynamic multi-step tasks using tools and planning.               | ReAct, Multi-agent RAG                    |
| 10  | Training-Integrated RAG           | Retriever and LLM are trained together instead of separately.            | REALM, RETRO, Atlas, RA-DIT               |
| 11  | Efficiency-Focused RAG            | Reduces latency and cost while handling many retrieved documents.      | FiD, Speculative RAG                      |
