import streamlit as st
from streamlit_lottie import st_lottie
import json, requests
from datetime import datetime
import datetime


st.set_page_config(page_title="About Me", layout='wide')
st.write('<style>div.block-container{padding-top:3rem};</style>', unsafe_allow_html=True)

st.markdown("""
<style>
	[data-testid="stHeader"] {
		background-color: #b6ccfe;
	}
</style>""",
unsafe_allow_html=True)


st.markdown(
        f"""
    <style>
    .stApp {{
        background: linear-gradient(to bottom , #ffcfd2, #98f5e1); 
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

custom_css = """
    <style>
        .img{
        border-radius:50%;
        border: 20 solid white;
        }
    </style>
"""
img_path = r'C:\Users\suman\Documents\suman.jpg'
st.markdown(f"<img classsrc={img_path}>")


# custom_css = """
# <style>
#     * {
#         margin: 0;
#         padding: 0;
#         box-sizing: border-box;
#         font-family: arial;
#         }
#         body {
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         min-height: 100vh;
#         background: salmon;
#         }
#         .wrapper {
#         display: inline-flex;
#         }
#         .wrapper .static-txt {
#         color: #fff;
#         font-size: 60px;
#         }
#         .wrapper .dynamic-txts {
#         margin-left: 15px;
#         height: 70px;
#         line-height: 70px;
#         overflow: hidden;
#         }
#         .dynamic-txts li {
#         color: pink;
#         list-style: none;
#         font-size: 60px;
#         position: relative;
#         top: 0;
#         animation: slide 6s steps(4) infinite;
#         }
#         @keyframes slide {
#         100% {
#             top: -280px;
#         }
#         }
#         .dynamic-txts li span {
#         position: relative;
#         }
#         .dynamic-txts li span::after {
#         content: "";
#         position: absolute;
#         left: 0;
#         height: 100%;
#         width: 100%;
#         background: salmon;
#         border-left: 2px solid pink;
#         animation: typing 1.5s steps(10) infinite;
#         }
#         @keyframes typing {
#         100% {
#             left: 100%;
#             margin: 0 -35px 0 35px;
#         }
#     }
# </style>    
# """

# Header = """
# <div class="wrapper">
#   <div class="static-txt">I'm</div>
#   <ul class="dynamic-txts">
#     <li><span>Suman</span></li>
#     <li><span>Focused</span></li>
#     <li><span>Passionate</span></li>
#     <li><span>Hardworking</span></li>
#   </ul>
# </div>
# """
# st.markdown(custom_css, unsafe_allow_html=True)
# st.markdown(Header, unsafe_allow_html=True)

# st.markdown(HEAD, unsafe_allow_html=True)

# def gif_profile():
#     col1, col2 = st.columns(2)
#     with col1:
#         @st.cache_data()
#         def load_lottieurl(url: str):
#             r = requests.get(url)
#             if r.status_code != 200:
#                 return None
#             return r.json()

#         lottie_book = load_lottieurl('https://lottie.host/f3520c07-690a-4719-8da6-cad4ef256cc0/LVuL9qCPRE.json')
#         st_lottie(lottie_book, speed=1, height=400, key="initial")   
    

# gif_profile()       

# def End():
#     col1, col2 = st.columns(2)
#     with col1:
#         custom_css = """
#             <style>
#                 .header{
#                     color: blue;
#                     padding-top: 40px;
#                     padding-left: 100px;
#                     font-size: 70px;
#         }
#             </style>
#         """
#         Now = datetime.datetime.now()
#         Now_string = Now.strftime("%H:%M:%S")
#         Now_time = (datetime.datetime.strptime(Now_string, '%H:%M:%S')).time()

#         def Str_to_time(Time):
#             TIME = (datetime.datetime.strptime(Time, '%H:%M:%S')).time()
#             return TIME
        
#         if Str_to_time('05:00:00') <= Now_time <= Str_to_time('11:59:59'):
#             with col1:
#                 head = """
#                     <h2 class='header'>
#                     Hello, Good Morning
#                     </h2>
#             """
#             st.markdown(custom_css, unsafe_allow_html=True)
#             st.markdown(head, unsafe_allow_html=True) 

#         elif Str_to_time('12:00:00') <= Now_time <= Str_to_time('16:59:59'):
#             with col1:
#                 head = """
#                     <h2 class='header'>
#                     Hello, Good Afternoon
#                     </h2>
#                 """
#                 st.markdown(custom_css, unsafe_allow_html=True)
#                 st.markdown(head, unsafe_allow_html=True)

#         elif Str_to_time('17:00:00') <= Now_time <= Str_to_time('16:59:59'):
#             with col1:
#                 head = """
#                     <h2 class='header'>
#                     Hello, Good Evening
#                     </h2>
#                 """
#                 st.markdown(custom_css, unsafe_allow_html=True)
#                 st.markdown(head, unsafe_allow_html=True) 
#         else:
#             with col1:
#                 head = """
#                     <h2 class='header'>
#                     Hello, Good Night
#                     </h2>
#                 """
#                 st.markdown(custom_css, unsafe_allow_html=True)
#                 st.markdown(head, unsafe_allow_html=True)     