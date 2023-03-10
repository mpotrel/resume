import streamlit as st
from resume.tabs.resume.education_tab import display_education
from resume.tabs.resume.experience_tab import display_experience
from resume.tabs.resume.skills_tab import display_skills


def display_main_page():
    st.header("Resume")
    st.subheader("Introduction")
    st.markdown(
        """
        Hi! My name is Manu and I'm a machine learning engineer, though my background is that of a math guy.\\
        I was attending both math and computer science classes during my first two years at the [CYU](https://www.cyu.fr) but I had to make a choice before my third year, so I went for math.\\
        I decided to pass the _Agrégation de mathématiques_ and taught high school and uni students for a few years before deciding to learn machine learning.\\
        A few certifications later, I landed an internship and then a job doing NLP for a health company.\\
        I should mention that, although I am still learning, I am very serious about clean code.
    """
    )

    education_tab, experience_tab, skills_tab = st.tabs(
        ["Education", "Work experience", "Skills"]
    )

    with education_tab:
        display_education()

    with experience_tab:
        display_experience()

    with skills_tab:
        display_skills()
