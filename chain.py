from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

def test_llm():
    # Testing Groq Chat Model
    model_groq = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    response = model_groq.invoke("Explain Newton's 2nd law of motion?")
    print(f"Groq Response: {response}")
    print("Both models invoked successfully!")

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
    

def schema_inspection():
    # Component 1: Define prompt template
    # Component 2: Define Model
    # Component 3: Define Output Parser
    # Component 4: Create a chain and invoke it
    # Component 5: Inspect the input and output schema of the chain

    prompt=ChatPromptTemplate.from_template("You are a helpful assistant. Answer the following question: {question}")
    model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    parser=StrOutputParser()

    chain = prompt | model | parser
    
    # Inspecting the input and output schema of the chain
    input_schema=chain.input_schema.schema()
    output_schema=chain.output_schema.schema()
    
    print(f"Chain Input Schema: {input_schema}")
    print(f"Chain Output Schema: {output_schema}")
    
    return chain

if __name__ == "__main__":
    schema_inspection()