
from langchain_core.prompts import ChatPromptTemplate 
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
from langchain.agents import create_agent
from langchain.tools import tool 
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv()
from tavily import TavilyClient
llm = ChatGroq(model = "openai/gpt-oss-20b")
# llm = ChatOllama(model = "gemma3:1b")
@tool 
def call_my_name():
    """
    it returns my name 

    """
    return "Pradeep"

@tool 
def google_search_user(user_query: str) :
    """ 
     this will search real data from google 

    """
    client = TavilyClient("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")
    response = client.search(
        query=user_query,
        search_depth="advanced"
    )   
    return response 

prompt = ChatPromptTemplate.from_messages([
    ("user" , '{user_prompt}')
])
out = StrOutputParser()
agent = create_agent(model=llm ,
                      tools = [call_my_name , google_search_user],
                      checkpointer=InMemorySaver()
                      )
def call_model(user : str):
    response = agent.invoke({"messages" : [{"role" : "user" , "content" : user}]}, 
                            {"configurable" : {"thread_id" : 1}}
    )
    return response["messages"][-1].content

    
