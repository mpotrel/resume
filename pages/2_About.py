import streamlit as st

st.header("About")

intro_markdown = """
    I decided making a website would be the best way not only to advertise my skills but also to actually learn by forcing myself to use frameworks and technologies I'm not too familiar with, but should be.
"""
st.markdown(intro_markdown)

st.subheader("Streamlit")
streamlit_markdown = """
    The framework used for these pages is [Streamlit](https://streamlit.io). This allows for a fast and easy to maintain simple pages.\\
    The reason I chose Streamlit is because I've already had some (very superficial) experience with it, so I decided to try and understand it a bit more.\\
    This is mainly an app to show demos of interesting things (and I hope this applies here), but is probably not quite suited to most production environments. The reason for this is that, as of March 2023, Streamlit does not work asynchronously.\\
    In the meantime, I'm also working a little bit on some JS frameworks in case I find something I like better than Streamlit but I most likely won't find something as easy to maintain, so whatever I find interesting will be added in the project section.
"""
st.markdown(streamlit_markdown)

st.subheader("DigitalOcean")
digital_ocean_markdown = """
    The app itself is hosted on a [Digital Ocean](https://www.digitalocean.com) Ubuntu droplet.\\
    It might seem overkill, but this website is only a front, hiding my true purpose!\\
    As I said earlier, my aim is to improve, so I actually wanted to have some sort of sandbox server that will remain online to simulate production environments.
"""
st.markdown(digital_ocean_markdown)
