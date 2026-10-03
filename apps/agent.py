from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool 
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.prompts import PromptTemplate
from rag import vector_store
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model = "openai/gpt-oss-20b")
memory = InMemorySaver()
prompt = """
You are a senior technical interviewer conducting an adaptive interview
based on the candidate's resume.

The user message will contain two parts:

1. The user's current query.

Whenever required user details search find_vector to answer questions about the candidate.

IMPORTANT RULES:

- Treat the resume context as factual information about the candidate.
- Do not invent candidate information.
- If the requested information is not present in the provided resume context,
  clearly say that it is not available in the provided context.
- Use your general technical knowledge for technical concepts.
- Ask realistic technical interview questions based on the candidate's
  actual experience and projects.
- Ask one question at a time.
- Ask follow-up questions based on the candidate's previous answers.
- Gradually increase the difficulty.
- Be concise and professional.
- Maintain the conversation naturally.
"""

@tool
def find_vector(user_query: str):
    """
    Search the candidate's resume.

    Use this tool whenever you need information about the candidate's
    name, profile, experience, internships, projects, education,
    technical skills, certifications, achievements, responsibilities,
    technologies, tools, or any other resume-specific information.

    Pass a specific search query describing exactly what information
    you need from the resume.
    """

    results = vector_store.similarity_search(
        user_query,
        k=4
    )
    
    context = "\n\n".join(
        doc.page_content for doc in results
    )
    return context


agent = create_agent(
    model=llm,
    tools=[find_vector],
    checkpointer=memory,
    system_prompt=prompt
)


def call_agent(query: str):
  

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        },
        {
            "configurable": {
                "thread_id": "interview-1"
            }
        }
    )

    return response["messages"][-1].content

while(True):
    user =  input("user : - ")
    if user=="q":
        break
    print("Ai: - " , call_agent(user))

    


