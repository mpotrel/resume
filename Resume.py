import streamlit as st
from resume.landing_page import display_main_page

st.set_page_config(page_title="Resume", layout="wide")
st.title("Manuel Potrel")
display_main_page()
