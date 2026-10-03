from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
load_dotenv()

llm = ChatGroq(model = "openai/gpt-oss-20b")
prompt = ChatPromptTemplate.from_messages([
    ("user" , '{user_prompt}')
])
out = StrOutputParser()
def call_model(user):
    chain = prompt | llm |out
    response = chain.invoke({"user_prompt" : user})
    return response

    
