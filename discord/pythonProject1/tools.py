from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

tool = SerperDevTool()
docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)