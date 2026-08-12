'''
Playground for LangChain building blocks.
Focus: 
    - creating and testing chains built from Prompt (Messages) | Model | Output Parser 
    - And also the core Runnable methods (invoke / batch / stream).
Each function is self-contained so it can be read and run in isolation.
'''
 

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, PydanticOutputParser

load_dotenv()


# ==========================================================================================
# 1. Prompts & model connectors
#
#   Prompt:
#       - PromptTemplate     : simple text prompt with variables.
#       - ChatPromptTemplate : structured chat messages with roles (System, Human, AI).
#
#   Model:
#       - Individual provider : ChatGroq()        from langchain_groq
#       - Universal provider  : init_chat_model() from langchain.chat_models
#       - Configuration & cost: temperature, max_tokens, timeout, retries; pick a
#                               low-cost model, cap output tokens, and cache when possible.
# ==========================================================================================
 
def test_llm():
    # Testing Groq Chat Model
    model_groq = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7,streaming=True)
    response = model_groq.invoke("Explain Newton's law of motion?")
    print(f"Groq Response: {response}")
    print("Both models invoked successfully!")

def universal_llm_connector():
    # Prompt Template
    prompt=ChatPromptTemplate.from_template("You are a helpful assistant. Answer the following question: {question}")

    # Universal Chat Model
    model=init_chat_model("groq:llama-3.3-70b-versatile", temperature=0.7)

    # Output Parser
    parser=StrOutputParser()

    chain=prompt|model|parser
    response=chain.invoke({"question": "What is capital of AP?"})
    print(f"Chain Response: {response}")

    return chain

# ==========================================================================================
# 2. Chains
#
#   Key Runnable methods:
#       - invoke / ainvoke : 1 input  -> 1 complete output
#       - batch  / abatch  : N inputs -> N complete outputs
#       - stream / astream : output piece-by-piece
#       - astream_log      : output + intermediate execution information
# ==========================================================================================

def basic_chain():
    # Component 1: Define prompt template
    # Component 2: Define Model
    # Component 3: Define Output Parser
    # Component 4: Create a chain and invoke it

    prompt=ChatPromptTemplate.from_template("You are a helpful assistant. Answer the following question: {question}")
    model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    parser=StrOutputParser()

    chain = prompt | model | parser
    response = chain.invoke({"question": "What is capital of AP?"})
    print(f"Chain Response: {response}")
    
    return chain

def batch_chain():
    # Component 1: Define prompt template
    # Component 2: Define Model
    # Component 3: Define Output Parser
    # Component 4: Create a chain and invoke it

    prompt=ChatPromptTemplate.from_template("You are a helpful assistant. Answer the following question: {question}")
    model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    parser=StrOutputParser()

    chain = prompt | model | parser
    questions = [
        {"question": "What is capital of Tamil Nadu ?"},
        {"question": "What is capital of Telangana?"},
        {"question": "What is capital of Karnataka?"}
    ]
    
    responses=chain.batch(questions)
    for i,resp in enumerate(responses):
        print(f"Response {i+1}: {resp}")
    
    return chain

def stream_chain():
    # Componen  1: Define prompt template
    # Component 2: Define Model
    # Component 3: Define Output Parser
    # Component 4: Create a chain and invoke it
    
    prompt=ChatPromptTemplate.from_template("You are a helpful assistant. Generate a 10 line poem about the following: {question}")
    model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    parser=StrOutputParser()
    
    chain=prompt|model|parser
    response=chain.stream({"question": "India"})
    for resp in response:
        print(f"{resp}",end="", flush=True)
    
    return chain
    
# ==========================================================================================
# 3. Output parsers
#
#       1. StrOutputParser      -> plain string
#       2. JsonOutputParser     -> Python dict from JSON
#       3. PydanticOutputParser -> validated Pydantic model
# ==========================================================================================
 
def string_parser_schema_inspection():
    prompt = ChatPromptTemplate.from_template("Answer the following question: {question}")
    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    parser = StrOutputParser()
    chain = prompt | model | parser

    print("Input Schema:", chain.input_schema.model_json_schema())
    print("Output Schema:", chain.output_schema.model_json_schema())
    print("Result:", chain.invoke({"question": "What is Python?"}))
    return chain

def json_parser_schema_inspection():
    prompt = ChatPromptTemplate.from_template(
        "Answer the following question: {question}. "
        "Return JSON with exactly 5 fields: answer, topic, language, difficulty, confidence."
    )
    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    parser = JsonOutputParser()
    chain = prompt | model | parser

    print("Input Schema:", chain.input_schema.model_json_schema())
    print("Output Schema:", chain.output_schema.model_json_schema())
    print("Result:", chain.invoke({"question": "What is Python?"}))
    return chain

class Answer(BaseModel):
    answer: str = Field(description="Answer to the question")
    topic: str = Field(description="Topic")
    language: str = Field(description="Language")
    difficulty: str = Field(description="Difficulty level")
    confidence: float = Field(description="Confidence score between 0 and 1")


def pydantic_structured_output():
    prompt = ChatPromptTemplate.from_template("Answer the following question: {question}")
    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7).with_structured_output(Answer)
    chain = prompt | model

    print("Input:", chain.input_schema.model_json_schema())
    print("Output:", chain.output_schema.model_json_schema())
    print("Result:", chain.invoke({"question": "What is Python?"}))
    return chain
   
   
if __name__ == "__main__":
    examples = {
        "test_llm": test_llm,
        "universal_llm_connector": universal_llm_connector,
        "basic_chain": basic_chain,
        "batch_chain": batch_chain,
        "stream_chain": stream_chain,
        "string_parser_schema_inspection": string_parser_schema_inspection,
        "json_parser_schema_inspection": json_parser_schema_inspection,
        "pydantic_parser_schema_inspection": pydantic_parser_schema_inspection,
    }
 
    # Change the key below to run a different example.
    examples["pydantic_parser_schema_inspection"]()