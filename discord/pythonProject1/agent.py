from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

# call the gemini models
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=False,
                             temperrature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))


def news_researcher(topic):
    return Agent(
        role="Senior Researcher",
        goal="Uncover ground breaking technologies in {topic}",
        verbose=False,
        memory=True,
        backstory=(
            "Driven by curiosity, you're at the forefront of"
            "innovation, eager to explore and share knowledge that could change"
            "the world."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=True
    )


def news_writer(topic):
    return Agent(
        role="Writer",
        goal='Narrate compelling tech stories about {topic}',
        verbose=False,
        memory=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft"
            "engaging narratives that captivate and educate, bringing new"
            "discoveries to light in an accessible manner."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=False
    )
