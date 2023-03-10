import streamlit as st


def display_education():
    st.subheader("Education")
    main_col, various_col = st.columns(2)
    main_md = """
        - Data Scientist
            - __2021__: _DataScientest_, _Sorbonne University_ co-certification
        - Agrégation de mathématiques
            - __2016__: _Lorraine University_
        
        - Math education, Master's degree
            - __2016__: _Lorraine University_
        
        - Fundamental Mathematics
            - __2015__: _Lorraine University_
    """
    various_md = """
        - _Udemy_, _Coursera_, _Udacity_, _FreeCodeCamp_
            - Python
            - Machine Learning and Deep Learning
            - SQL
            - FastAPI
            - Web
            - Big data
            - Docker
            - ...
    """
    main_col.markdown(main_md)
    various_col.markdown(various_md)
