import streamlit as st

st.header("Projects")
rakuten, radiocovid, fastapi = st.tabs(["Rakuten", "Radio Covid", "FastAPI"])

rakuten_markdown = """
    Currently in progress
"""

radiocovid_markdown = """
    Under refactoring
"""

fastapi_markdown = """
    Currently in progress
"""

for page, markdown in (
    (rakuten, rakuten_markdown),
    (radiocovid, radiocovid_markdown),
    (fastapi, fastapi_markdown),
):
    page.markdown(markdown)
