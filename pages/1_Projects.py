import streamlit as st
from resume.tabs.projects.resume import display_resume
from resume.tabs.projects.fastapi import display_fastapi
from resume.tabs.projects.rakuten import display_rakuten
from resume.tabs.projects.radiocovid import display_radiocovid


st.header("Projects")
resume, rakuten, radiocovid, fastapi = st.tabs(
    ["Resume", "Rakuten", "Radio Covid", "FastAPI"]
)

for tab, display in (
    (resume, display_resume),
    (rakuten, display_rakuten),
    (radiocovid, display_radiocovid),
    (fastapi, display_fastapi),
):
    with tab:
        display()
