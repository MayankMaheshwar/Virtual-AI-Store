from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI



class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def Tor(self):
        return Agent(
            role="Sales Bot",
            backstory=dedent(f""" """),
            goal=dedent(f"""Interacts with users, understands their needs, and communicates accordingly."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def Mika(self):
        return Agent(
            role="Manager",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Monitors the conversation stage, gives instructions on transitioning between stages, and ensures the conversation is on track."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def Kaa(self):
        return Agent(
            role="Product Manager",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Searches the product inventory based on keywords provided by Tor and Mika."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
