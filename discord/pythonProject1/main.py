import streamlit as st
from crewai import Crew, Process
from tasks import research_task, write_task
from agent import news_researcher, news_writer
from IPython.display import Markdown

crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

# result = crew.kickoff(inputs={'topic': 'AI in new Technology advancement'})
# Markdown(result)


st.set_page_config(page_title="Agent about AI")

def async_function_wrapper():
    response = None
    with st.spinner("Fetching data..."):
        try:
            output = crew.run(inputs={'topic': topic})  # Use crew.run
            response = output['written_text']  # Access the desired output from crew
        except RuntimeError as ex:
            print(ex)
    return response

st.header("Agent about AI")
topic = st.text_input("Enter your topic")

if st.button("Get Response"):

    with st.spinner("Fetching data..."):
        response = async_function_wrapper()  # Call the wrapper function
        if response is not None:
            st.subheader("The response is")
            st.write(response)