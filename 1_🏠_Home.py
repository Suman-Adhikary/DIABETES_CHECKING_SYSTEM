########################################### Import Libraries ############################################################
import pandas as pd
import streamlit as st
from pickle import load
import base64
import sys, path


########################################## Setup File Directory #########################################################
dir = path.Path(__file__)
sys.path.append(dir.parent.parent)


########################################### Setup Page Config ###########################################################
st.set_page_config(layout="wide", page_title="Diabetes Check")


######################################### Setup Page BackGround #########################################################
@st.cache_data
def add_bg_from_local(image_file):
    st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

add_bg_from_local('./Images/Main_60.jpg')


############################################ Setup Page Header ###########################################################
@st.cache_data
def header():
    custom_css = """
        <style>
             .header{
                color: #fff;
                text-align: left;
                font-size: 66px;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
        </style>
    """

    head = """
        <h1 class="header">
            <font color="#2d00f7">D</font>
            <font color="#6a00f4">I</font>
            <font color="#8900f2">A</font>
            <font color="#a100f2">B</font>
            <font color="#b100e8">E</font>
            <font color="#d100d1">T</font>
            <font color="#e500a4">E</font>
            <font color="#f20089">S</font>
        </h1>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(head, unsafe_allow_html=True)
header()   


####################################### Setup Page Column and User input ##################################################
#Set columns.
col1, col2, col3 = st.columns(3)

USER_INPUT = [0, 0, 0, 0, 0, 0, 0, 0, 0]

@st.cache_data
def process_input(input_value):
    result = input_value
    return result

# Age Column.
with col1:
    AGE = st.number_input("Age", value=0)
    USER_INPUT[0] = process_input(AGE)

# Bmi Column.
with col1:
    BMI = st.number_input('Body Mass Index', step=1.,format="%.f")
    USER_INPUT[1] = process_input(BMI)

# HbA1c Column.
with col1:
    HB = st.number_input('HbA1c Level', step=1.,format="%.f")
    USER_INPUT[2] = process_input(HB)

# Blood Glucose Level Column.
with col1:
    BGL = st.number_input('Blood Glucose Level', value=0)
    USER_INPUT[3] = process_input(BGL)

# Hypertension Column.
with col1:
    HT = st.selectbox('Hypertension', ('Yes', 'No'))
    USER_INPUT[4] = process_input(HT)  

# Heart Disease column.
with col1:
    HD = st.selectbox('Heart Disease', ('Yes', 'No'))
    USER_INPUT[5] = process_input(HD)   

# Gender column.
with col1:
    GENDER = st.selectbox('Gender', ('Male', 'Female'))
    USER_INPUT[6] = process_input(GENDER)

# Smoking History column.
with col1:
    SH = st.selectbox('Smoking History', ('current', 'non_smoker', 'past_smoker'))
    USER_INPUT[7] = process_input(SH)
      

################################################# Conditional User Input ######################################################
@st.cache_data
def user_input():
    if USER_INPUT[4] == 'Yes':
        USER_INPUT[4] = 1
    elif USER_INPUT[4] == 'No':
        USER_INPUT[4] = 0
    if USER_INPUT[5]== 'Yes':
        USER_INPUT[5] = 1
    elif USER_INPUT[5] == 'No':
        USER_INPUT[5] = 0            
    new_data = pd.DataFrame({'age' : USER_INPUT[0], 'bmi' : USER_INPUT[1], 'HbA1c_level' : USER_INPUT[2], 'blood_glucose_level' : USER_INPUT[3], 'hypertension' : USER_INPUT[4], 
                             'heart_disease' : USER_INPUT[5], 'gender' : USER_INPUT[6], 'smoking_history' : USER_INPUT[7]}, index = [0])
    return new_data


######################################################## Predict New Data ########################################################
@st.cache_data
def Prediction():
    model = load(open('./Model And Scaling/CAT_BOOST.pkl', 'rb'))
    pred = model.predict(user_input())
    return pred


####################################################### Button For Prediction #####################################################
CSS = """
    <style>
        .header_pred{
                text-align: left;
                font-size: 30px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }    
    </style>
"""

HEAD_YES = """
        <h6 class="header_pred" style="color:#ff5a5f"> You Have Diabetes. </h6>
"""

HEAD_NO = """
    <h6 class="header_pred" style="color:#affc41"> You Don't Have Diabetes. </h6>
"""

with col1:
    if st.button('Check'):
        st.cache_data.clear()
        if Prediction()[0] == 1:
            st.markdown(CSS, unsafe_allow_html=True)
            st.markdown(HEAD_YES, unsafe_allow_html=True)
            st.cache_data.clear()
        else:
            st.cache_data.clear()
            st.markdown(CSS, unsafe_allow_html=True)
            st.markdown(HEAD_NO, unsafe_allow_html=True)
            st.cache_data.clear()