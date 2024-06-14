from crewai import Crew, Process
from tasks import research_task, write_task
from agent import news_researcher, news_writer
from IPython.display import Markdown

crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

result = crew.kickoff(inputs={'topic': 'AI in new Technology advancement'})
Markdown(result)
