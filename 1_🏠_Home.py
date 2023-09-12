########################################### Import Libraries ############################################################
import pandas as pd
import streamlit as st
from pickle import load
import base64, os
import sys, path
from catboost import CatBoostClassifier


########################################## Setup File Directory #########################################################
dir = path.Path(__file__)
sys.path.append(dir.parent.parent)


########################################### Setup Page Config ###########################################################
st.set_page_config(layout="wide", page_title="Diabetes Check")


######################################### Setup Page BackGround #########################################################
@st.cache_data()
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

add_bg_from_local('./Images/Main.jpg')


############################################ Setup Page Header ###########################################################
@st.cache_data()
def header():
    custom_css = """
        <style>
             .header{
                color: #fff;
                text-align: left;
                font-size: 66px;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
        </style>
    """

    head = """
        <h1 class="header">
            Diabetes
        </h1>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(head, unsafe_allow_html=True)
if __name__ == '__main__':
    header()   


####################################### Setup Page Column and User input ##################################################
#Set columns.
col1, col2, col3 = st.columns(3)

@st.cache_data()
def process_input(input_value):
    result = input_value
    return result

# Age Column.
with col1:
    AGE = st.number_input("Age", value=0)
AGE = process_input(AGE)

# Bmi Column.
with col1:
    BMI = st.number_input('Body Mass Index', value=0)
BMI = process_input(BMI)

# HbA1c Column.
with col1:
    HB = st.number_input('HbA1c Level', value=0)
HB = process_input(BMI)

# Blood Glucose Level Column.
with col1:
    BGL = st.number_input('Blood Glucose Level', value=0)
BGL = process_input(BMI)

# Gender column.
with col1:
    GENDER = st.selectbox('Gender', ('Male', 'Female'))
GENDER = process_input(GENDER)

# Hypertension Column.
with col1:
    HT = st.selectbox('Hypertension', ('Yes', 'No'))
HT = process_input(HT)  

# Smoking History column.
with col1:
    SH = st.selectbox('Smoking History', ('current', 'non_smoker', 'past_smoker'))
SH = process_input(SH)

# Heart Disease column.
with col1:
    HD = st.selectbox('Heart Disease', ('Yes', 'No'))
HD = process_input(HD)   
      

################################################# Conditional User Input #####################################################
@st.cache_data
def user_input():
    if HT == 'Yes':
        HT = 1
    else: 
        HT = 0
    if HD == 'Yes':
        HD = 1
    elif HD == 'No':
        HD = 0            
    new_data = pd.DataFrame({'age' : AGE, 'bmi' : BMI, 'HbA1c_level' : HB, 'blood_glucose_level' : BGL, 'hypertension' : 1, 'heart_disease' : HT, 'gender' : GENDER, 'smoking_history' : SH}, index = [0])
    return new_data


######################################################## Predict New Data ##########################################################
@st.cache_data
def Prediction():
    model = load(open('./Model And Scaling/CAT_BOOST.pkl', 'rb'))
    pred = model.predict(user_input())
    return pred


####################################################### Button For Prediction #######################################################
with col1:
    if st.button('Check'):
        if Prediction()[0] == 1:
            st.write('Yes')
        else:
            st.write('No')    