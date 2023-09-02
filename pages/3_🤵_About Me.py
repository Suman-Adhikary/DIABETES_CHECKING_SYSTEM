import streamlit as st
from streamlit_lottie import st_lottie
import json, requests, time


st.set_page_config(page_title="About Me", layout='wide')
st.write('<style>div.block-container{padding-top:3rem};</style>', unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col2:
    @st.cache_data()
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_book = load_lottieurl('https://lottie.host/f3520c07-690a-4719-8da6-cad4ef256cc0/LVuL9qCPRE.json')
    st_lottie(lottie_book, speed=1, height=400, key="initial")

with col1:
    custom_css = """
        <style>
            .header{
                color: blue;
                padding-top: 40px;
                padding-left: 100px;
                font-size: 70px;
    }
        </style>
    """
    with col1:
        head = """
            <h2 class='header'>
            Hi, Good Morning
            </h2>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(head, unsafe_allow_html=True)    