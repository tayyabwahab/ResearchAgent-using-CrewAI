import os 
from crewai import Agent, Crew, Task, Process, LLM
from langchain_ollama import OllamaLLM


llm = OllamaLLM(
    model="ollama/mistral:latest",
    # base_url="http://localhost:11434"                # Uncomment it if you find issue running ollama locally 
    # base_url="http://host.docker.internal:11434"    # To run it inside the docker, uncomment this line
)

agent_research = Agent(
    role="Research Analyst",
    goal="Find out the latest and trending articles in the field of AI and data science",
    backstory="""You are an expert researcher with expertise in AI and data science. 
    You keep yourself updated with the latest and trending articles in the field of AI and data science.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

agent_writer = Agent(
    role="Technical Writing Expert",
    goal="Write a blog post about the latest and trending articles in the field of AI and data science",
    backstory="""You are an expert technical writer with expertise in writing technical articles about the latest and trending articles in the field of AI and data science.""",
    verbose=True,
    llm=llm
)

task1 = Task(
    description="""Analyze the latest and trending articles in the field of AI and data science.
    Filter out top major trends, technologies and their applications. Create a detailed report""",
    agent=agent_research,
    expected_output="A detailed report analyzing the latest trends in AI and data science",
)

task2 = Task(
    description="""Write a detailed article about the latest and trending articles in AI and data science.
    The article should be very intereting and engaging.""",
    agent=agent_writer,
    expected_output="An engaging and detailed article about the latest trends in AI and data science",
)

crew = Crew(
    agents=[agent_research, agent_writer],
    tasks=[task1, task2],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff()

print(result)

