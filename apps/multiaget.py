from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
from langgraph.graph.state import StateGraph, START, END
from langchain_core.runnables.config import RunnableConfig

load_dotenv()


class FlowModel(BaseModel):
    query: str
    category: Literal["Coding", "Weather", "google_search"] = Field(
        default="google_search"
    )
    ans: str = Field(default="")


class CategoryModel(BaseModel):
    category: Literal["Coding", "Weather", "google_search"] = Field(
        default="google_search"
    )


llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


# ---------------- CATEGORY NODE ----------------

def search_category(state: FlowModel):

    st_llm = llm.with_structured_output(
        CategoryModel,
        method="json_schema"
    )

    result = st_llm.invoke(
        f"""
        Classify the following user question.

        Question:
        {state.query}

        Categories:

        Coding
        - Programming
        - Python
        - Java
        - C++
        - FastAPI
        - APIs
        - DSA
        - debugging
        - software development

        Weather
        - weather
        - temperature
        - rain
        - forecast
        - humidity

        google_search
        - everything else

        If you are unsure, choose google_search.
        """
    )

    state.category = result.category

    print("Category:", state.category)

    return state


# ---------------- ROUTER ----------------

def route(state: FlowModel):
    return state.category


# ---------------- CODING NODE ----------------

def coding(state: FlowModel):

    state.ans = f"Coding question detected: {state.query}"

    return state


# ---------------- WEATHER NODE ----------------

def weather(state: FlowModel):

    state.ans = f"Weather question detected: {state.query}"

    return state


# ---------------- GOOGLE SEARCH NODE ----------------

def google_search(state: FlowModel):

    state.ans = f"Google search required for: {state.query}"

    return state


# ---------------- GRAPH ----------------

graph = StateGraph(FlowModel)


graph.add_node("category", search_category)
graph.add_node("Coding", coding)
graph.add_node("Weather", weather)
graph.add_node("google_search", google_search)


graph.add_edge(START, "category")


graph.add_conditional_edges(
    "category",
    route,
    {
        "Coding": "Coding",
        "Weather": "Weather",
        "google_search": "google_search",
    }
)


graph.add_edge("Coding", END)
graph.add_edge("Weather", END)
graph.add_edge("google_search", END)


# ---------------- MEMORY ----------------

memory = InMemorySaver()

final_graph = graph.compile(
    checkpointer=memory
)


# ---------------- CHAT LOOP ----------------

while True:

    query = input("User: ")

    if query.lower() == "bye":
        break

    state = FlowModel(query=query)

    config: RunnableConfig = {
        "configurable": {
            "thread_id": "my_bot_1"
        }
    }

    res = final_graph.invoke(
        state,
        config=config
    )

    print("AI:", res["ans"])