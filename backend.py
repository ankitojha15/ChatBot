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

