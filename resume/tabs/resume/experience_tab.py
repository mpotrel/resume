import streamlit as st


def display_experience():
    st.subheader("Work experience")

    work_experience_md = """
        - __Mar 2022 - Now__ : Sancare, Data science developer
            - Monitoring and testing tools development
            - NLP models experiments on hospital patient data
            - Model monitoring and deployment on hospital servers
        - __Jan 2023 - Now__: Freelance data science mentor for learning groups
            - One data analyst group
            - Four data scientist groups on various machine learning/deep learning projects
        - __Sep 2021 - Mar 2022__ : Sancare, Data science intern
            - Development of performance monitoring tools
            - Development of NLP model interpretability tools
        - __Sep 2017 - Sep 2021__ : Professeur agrégé de mathématiques
            - Mathematics, statistics and geometry at the CYU
            - Mathematics and numerical sciences in high school
    """
    st.markdown(work_experience_md)
