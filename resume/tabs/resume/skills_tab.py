import streamlit as st


def display_skills():
    st.subheader("Skills")

    python_col, others_col = st.columns(2)
    python_markdown = """
        #### Python
        - Python libraries for ML
            - Scikit-Learn
            - TensorFlow
            - PyTorch
            - Skorch
            - Sacred
        - Python libraries for data handling
            - SQLAlchemy/Psycopg (with Alembic)
            - Matplotlib
            - Seaborn
            - Pandas
            - Numpy
        - Other python libraries
            - Streamlit
            - FastAPI
            - Joblib
            - SciPy
    """
    others_markdown = """
        #### General
        - Mathematics
            - Linear algebra
            - Statistics
            - Calculus
        - Programming
            - Python: Probably the language I am most familiar with.
            - SQL, Bash: I have been working with PostgreSQL databases and bash scripts for a while now.
            - C/C++, Java, Javascript: I can only say that I'm familiar with those languages but nothing more than a few low scale projects.
        - Workflow
            - Agile: Mainly Scrum
            - GitLab CI/CD
            - Docker
            - TDD
    """

    with others_col:
        st.markdown(others_markdown)
    with python_col:
        st.markdown(python_markdown)
