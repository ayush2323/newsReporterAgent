from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()


def get_tool():
    os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
    return SerperDevTool()


def get_docs_scrape_tool():
    return ScrapeWebsiteTool(
        website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
    )


tool = get_tool()
docs_scrape_tool = get_docs_scrape_tool()
