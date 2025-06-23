import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

def get_response(llm_id, query, allow_search, system_prompt, provider):
    try:
        
        if provider.lower() == "groq":
            llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)
        elif provider.lower() == "openai":
            llm = ChatOpenAI(model=llm_id, api_key=OPENAI_API_KEY)
        else:
            return "Unsupported provider. Must be 'groq' or 'openai'."

        tools = []
        if allow_search:
            if not TAVILY_API_KEY:
                return "Tavily API key missing but search was requested."
            tools = [TavilySearch(max_results=2, api_key=TAVILY_API_KEY)]

        if isinstance(query, list):
            query = "\n".join(query)

        agent = create_react_agent(
            model=llm,
            tools=tools,
            prompt=system_prompt
        )

        state = {"messages": query}
        response = agent.invoke(state)

        messages = response.get("messages", [])
        ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

        return ai_messages[-1] if ai_messages else "No AI response found."

    except Exception as e:
        print("get_response() Exception:", e)
        import traceback
        traceback.print_exc()
        return f"Internal Error in get_response: {str(e)}"
