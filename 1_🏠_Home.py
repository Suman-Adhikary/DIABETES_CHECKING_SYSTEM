########################################### Import Libraries ############################################################
import streamlit as st
from pickle import load
import base64, os
import sys, path

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
    GENDER = st.selectbox('Gender', ('Male', 'Female', 'Others'))
    GENDER = process_input(GENDER)

# Hypertension Column.
with col1:
    HT = st.selectbox('Hypertension', ('Yes', 'No'))
    HT = process_input(HT)  

# Smoking History column.
with col1:
    SH = st.selectbox('Smoking History', ('Current', 'Non_Smoker', 'Past_Smoker'))
    SH = process_input(SH)

# Heart Disease column.
with col1:
    HD = st.selectbox('Heart Disease', ('Yes', 'No'))
    HD = process_input(HD)     


################################################# Conditional User Input #####################################################
@st.cache_data
def Conditional_Input(Age, Bmi, Hb, Bgl, Gender, Ht, Sh, Hd):
    user_input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    user_input[0] = AGE
    user_input[1] = BMI
    user_input[2] = HB
    user_input[3] = BGL

    if GENDER == 'Male':
        user_input[4] = 1
        user_input[5] = 0
        user_input[6] = 0
    elif GENDER == 'Female':
        user_input[4] = 0    
        user_input[5] = 1    
        user_input[6] = 0    
    elif GENDER == 'Female':
        user_input[4] = 0    
        user_input[5] = 0    
        user_input[6] = 1

    if HT == 'Yes':
        user_input[7] = 1
        user_input[8] = 0
    elif HT == 'No':
        user_input[7] = 0
        user_input[8] = 1        

    if SH == 'Current':        
        user_input[9] = 1
        user_input[10] = 0
        user_input[11] = 0
    elif SH == 'Non_Smoker':        
        user_input[9] = 0
        user_input[10] = 1
        user_input[11] = 0
    elif SH == 'Past_Smoker':        
        user_input[9] = 0
        user_input[10] = 0
        user_input[11] = 1

    if HD == 'Yes':
        user_input[12] = 1
        user_input[13] = 0
    elif HD == 'No':  
        user_input[12] = 0
        user_input[13] = 1  
    return user_input
New_Data = Conditional_Input(AGE, BMI, HB, BGL, GENDER, HT, SH, HD)


######################################################## Scaling New Data #########################################################
@st.cache_data
def Input_Scaling(Input_Data):
    scaler = load(open('./Model And Scaling/Scale.pkl', 'rb'))
    Input_Data = scaler.transform([Input_Data])
    return Input_Data

For_scale = New_Data[0:4]
Apply_scaling = Input_Scaling(For_scale)
New_Data[0:4] = Apply_scaling[0]


######################################################## Predict New Data ##########################################################
@st.cache_data
def Prediction(Data):
    model = load(open('./Model And Scaling/model1.pkl', 'rb'))
    pred = model.predict([New_Data])
    return pred


####################################################### Button For Prediction #######################################################
with col1:
    if st.button('Check'):
        if Prediction == 1:
            st.write('Yes')
        else:
            st.write('No')    