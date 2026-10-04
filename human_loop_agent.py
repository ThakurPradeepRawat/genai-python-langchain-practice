from pydantic import BaseModel
from typing import Literal 
from langchain_groq import ChatGroq 
from langgraph.graph import StateGraph , START , END 
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables.config import RunnableConfig
from dotenv import load_dotenv
load_dotenv()

class ChatResponse(BaseModel):
    query : str 
    email_draft :str  = ""
    feedback : str = ""  

llm = ChatGroq(model = "openai/gpt-oss-20b")

def genrate_Email(state : ChatResponse):
    res = llm.invoke(f'You are an email expert genrate user required email , user_query: {state.query}')
    state.email_draft = str(res.content)
    return state 

def human_approval(state : ChatResponse):
    feedback = interrupt({
        "draft_email" : state.email_draft , 
        "query" : "Do you want to send this email ?"
    })

    fb =  str(feedback ).strip().lower()
    if fb in ("yes" , "approve" , "ok"):
        state.feedback = ""
        return state 
    else:
        state.feedback = fb 
        return state


def controller(state: ChatResponse):
    if state.feedback : 
        return 'send_email'
    else:
        return 'genrate_Email'
def send_email(state : ChatResponse):
    print("Mailed")
    return state

graph = StateGraph(ChatResponse)
graph.add_node("genrate_Email" , genrate_Email)
graph.add_node("human_approval" , human_approval)
graph.add_node("send_email" , send_email)

graph.add_edge(START , "genrate_Email")
graph.add_edge("genrate_Email" , "human_approval")
graph.add_conditional_edges("human_approval", controller, {'send_email' :'send_email', 
                                                           'genrate_Email' :'genrate_Email'
                                                           })
graph.add_edge('genrate_Email' , END)

memory = InMemorySaver()
graph = graph.compile(checkpointer=memory)


while True:

    query = input("User: ")

    if query.lower() == "bye":
        break

    config: RunnableConfig = {
            "configurable": {
                "thread_id": "my_bot_1"
            }
        }

    result = graph.invoke(
        ChatResponse(query=query),
        config=config
    )

    while "__interrupt__" in result:

        interrupt_data = result["__interrupt__"][0]

        print("\nDraft Email:")
        print(interrupt_data.value["draft_email"])

        print("\nDo you want to send this email?")
        print("Type 'yes' to send")
        print("Or provide feedback to regenerate")

        user_input = input("You: ")

        result = graph.invoke(
            Command(resume=user_input),
            config=config
        )

    print("\nAI:", result)
    
    
    




    

