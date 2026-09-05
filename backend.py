from langgraph.graph import StateGraph , START, END
from langchain_core.messages import BaseMessage , HumanMessage
from langchain_groq import ChatGroq
from typing import TypedDict , Annotated
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "openai/gpt-oss-120b"
)

# reducer
from langgraph.graph.message import add_messages

class ChatState(TypedDict):

    # all type of messages inherit from BaseMessage like Human msg,Ai msg,tool msg,system msg
    messages : Annotated[list[BaseMessage] , add_messages] 

def chat_node(state: ChatState):
    # take user query from state
    

    # send to llm

    # response -> store in state


graph = StateGraph(ChatState)

graph.add_node('chat node',chat_node)