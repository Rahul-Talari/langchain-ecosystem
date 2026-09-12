
## LangChain ecosystem overview

**LangChain Ecosystem:**

### Core packages
- **langchain:** high-level framework for building LLM apps such as RAG pipelines, agents, tools, and memory
- **langgraph:** stateful agent orchestration and graph-based collaboration with retries
- **langchain-core:** core abstractions including prompts, Runnable / LCEL, and output parsers
- **langsmith:**
  - Tracing: step-by-step execution debugging
  - Evaluation: quality measurement for LLM outputs and RAG accuracy
  - Monitoring: production metrics such as latency, failures, usage, and cost
  - Compliance: auditing, reproducibility, governance, and regulated environments
- **langserve:** deploy as REST APIs

### Integration packages
- **langchain-openai**: OpenAI integrations
- **langchain-anthropic**: Anthropic integrations
- **langchain-community**: community and third-party integrations

### Runnables
- **invoke / ainvoke:** one input to one output
- **batch / abatch:** multiple inputs to multiple outputs
- **stream / astream:** streaming output piece by piece
- **astream_log:** output plus intermediate execution information

### Chain composition
- **Sequential:** A → B → C
- **Parallel:** A → (B, C) → results together via RunnableParallel
- **Passthrough:** pass input unchanged to the next step

### Prompt and model abstractions
- **PromptTemplate:** text prompt with variables
- **ChatPromptTemplate:** chat messages with roles
- **Model providers:**
  - individual providers like `ChatGroq()`
  - universal provider like `init_chat_model()`
- **Model configuration:** temperature, max_tokens, timeout, retries
- **Cost optimization:** choose cheaper models, limit output tokens, use caching

### Output parsers
- **String:** `StrOutputParser`
- **JSON:** `JsonOutputParser`
- **Pydantic:** `PydanticOutputParser`

### Document loaders
- **PDF files:** PyPDFLoader, PyMuPDFLoader, UnstructuredPDFLoader
- **Text files:** TextLoader
- **Multiple files:** DirectoryLoader
- **Complex docs:** UnstructuredLoader
- **Web pages:** WebBaseLoader

### Loader comparison
| Loader | Speed | Metadata | Use case |
| --- | --- | --- | --- |
| pypdfloader | good | basic | simple PDFs |
| pymupdfloader | best | rich | high-volume docs |
| unstructuredpdfloader | slower | detailed | tables and layouts |
