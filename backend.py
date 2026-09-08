from langgraph.graph import StateGraph , START, END
from langchain_core.messages import BaseMessage , HumanMessage
from langchain_groq import ChatGroq
from typing import TypedDict , Annotated
from dotenv import load_dotenv
import time
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

llm = ChatGroq(
    model = "groq/compound-mini"
)

# reducer
from langgraph.graph.message import add_messages

class ChatState(TypedDict):

    # all type of messages inherit from BaseMessage like Human msg,Ai msg,tool msg,system msg
    messages : Annotated[list[BaseMessage] , add_messages] 

def chat_node(state: ChatState):
    # take user query from state
    messages = state["messages"]

    # send to llm
    response = llm.invoke(messages)

    # response -> store in state

    return {'messages' : [response]}

checkpointer = MemorySaver()

graph = StateGraph(ChatState)

graph.add_node('chat node',chat_node)

graph.add_edge(START,"chat node")
graph.add_edge("chat node",END)

chatbot = graph.compile(checkpointer=checkpointer)

#generator to stream
stream = chatbot.stream(
    {'messages':[HumanMessage(content = 'whats the recipe to make maggie')]},
    CONFIG = {'configurable': {'thread_id':'thread-1'}},
    stream_mode="messages"

)


