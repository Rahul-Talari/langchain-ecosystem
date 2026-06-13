# uv add langchain langchain-core langgraph langchain-openai langchain-anthropic python-dotenv langchain_groq

import langchain_core
from dotenv import load_dotenv
from importlib.metadata import version
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

load_dotenv() 
print(f"LangChain version: {version('langchain_core')}")
print(f"LangGraph version: {version('langgraph')}")

def main():
    # Test OpenAI LLM (commented out — API quota exceeded)
    llm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0.2)
    response=llm.invoke("Say 'setup complete!' in one word")
    print(f"Response from openai: {response}")

    # Test Anthropic LLM
    llm=ChatAnthropic(model_name="claude-haiku-4-5-20250929",temperature=0.2)
    response=llm.invoke("Say 'setup complete!' in one word")
    print(f"Response from anthropic: {response}")    

    # Test Groq LLM
    llm=ChatGroq(model_name="llama-3.2-1-70b-instruct",temperature=0.2)
    response=llm.invoke("Say 'setup complete!' in one word")
    print(f"Response from groq: {response}")        
    print("setup complete!")

if __name__ == "__main__":
    main()
