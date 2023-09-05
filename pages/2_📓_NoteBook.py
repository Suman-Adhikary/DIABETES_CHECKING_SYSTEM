########################################################### Import Libraries #########################################################
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import json, requests
import plotly.express as px
import sys, path

dir = path.Path(__file__)
sys.path.append(dir.parent.parent)


########################################################### Setup Page Configer ######################################################
st.set_page_config(page_title="notebook", layout="wide")
st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


######################################################### Streamlit lottie Animation #################################################
@st.cache_data()
def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

lottie_book = load_lottieurl("https://lottie.host/e5bf3a18-6153-40fe-beeb-86d4a63c1694/FnnSkJAT93.json")
st_lottie(lottie_book, speed=1, height=200, key="initial")         


################################################################## Set Header ########################################################
st.cache_data()
def Main_Header():
    header_css = """
    <style>
        h1 {
            text-align: center;
            font-size: 70px;
        }
        .word1 {
            color: #7b2cbf;
        }

        .word2 {
            color: #c77dff;
        }

        .word3 {
            color: #e0aaff;
        }
        .rainbow-divider {
            height: 2px;
            background: linear-gradient(to right, red, orange, yellow, green, blue, purple);
            margin: -20px 0;
        } 
    </style>
    """

    Main_head = """
        <h1>
            <span class="word1">DIABETES</span>
            <span class="word2">CHECKING</span>
            <span class="word3">SYSTEM</span>
        </h1>
        <div class="rainbow-divider"></div>
    """
    st.markdown(header_css, unsafe_allow_html=True)
    st.markdown(Main_head, unsafe_allow_html=True)
if __name__ == '__main__':
    Main_Header()


########################################################## Datase and Information #######################################################
dataset = pd.read_csv(open('./diabetes.csv', 'rb'))
@st.cache_data(experimental_allow_widgets=True)
def Data():
    Col1, Col2 = st.columns(2)

    custom_css = """
        <style>
            .header{
                color: blue;
                text-align: center;
                font-size: 30px;
    }
        </style>
    """

    # Sample Data.
    with Col1:
        head = """
            <h2 class="header">
                Sample Data
            </h2>
        """
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown(head, unsafe_allow_html=True)
    with Col1:
        st.write(dataset.iloc[0:50, :])

    # Data Download button.
    with Col1:
        st.markdown("<br></br>", unsafe_allow_html=True)
        st.download_button(
            label="Download data as CSV",
            data=dataset.to_csv().encode('utf-8'),
            file_name='large_df.csv',
            mime='text/csv',
            )        

    # Data Info.
    with Col2:
        head = """
            <h2 class="header">
                Data Information
            </h2>
        """
        css_ = """
        <style>
            .p{
            margin: 0;
            }   
            """
        
        a = """
            <p class = p> <strong style="color:blue;"> Age: </strong> Age is an important factor in predicting diabetes risk. As individuals get older, their risk of developing diabetes increases. </p>
            <p class = p> <strong style="color:blue;"> Gender: </strong> Effect of gender may vary. For example, women with a history of gestational diabetes (diabetes during pregnancy) have a higher risk of developing type 2 diabetes later in life. </p>
            <p class = p> <strong style="color:blue;"> Body Mass Index: </strong> BMI is a measure of body fat based on a person's height and weight. It is commonly used as an indicator of overall weight status and can be helpful in predicting diabetes risk. Higher BMI is associated with a greater likelihood of developing type 2 diabetes. </p>
            <p class = p> <strong style="color:blue;"> Hypertension: </strong> Hypertension, or high blood pressure, is a condition that often coexists with diabetes. The two conditions share common risk factors and can contribute to each other's development. </p>
            <p class = p> <strong style="color:blue;"> Heart Disease: </strong> Heart disease, including conditions such as coronary artery disease and heart failure, is associated with an increased risk of diabetes. The relationship between heart disease and diabetes is bidirectional, meaning that having one condition increases the risk of developing the other. </p>
            <p class = p> <strong style="color:blue;"> Smoking History: </strong> Cigarette cause of 2 type diabetes. Smoking can contribute to insulin resistance and impair glucose metabolism. Quitting smoking can significantly reduce the risk of developing diabetes and its complications. </p>
            <p class = p> <strong style="color:blue;"> HbA1c Level: </strong> HbA1c (glycated hemoglobin) is a measure of the average blood glucose level over the past 2-3 months. It provides information about long-term blood sugar control. Higher HbA1c levels indicate poorer glycemic control and are associated with an increased risk of developing diabetes and its complications. </p>
            <p class = p> <strong style="color:blue;"> Blood Glucose Level: </strong> Blood glucose level refers to the amount of glucose (sugar) present in the blood at a given time. Elevated blood glucose levels, particularly in the fasting state or after consuming carbohydrates, can indicate impaired glucose regulation and increase the risk of developing diabetes. Regular monitoring of blood glucose levels is important in the diagnosis and management of diabetes. </p>
            """
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown(head, unsafe_allow_html=True)
        st.markdown(css_, unsafe_allow_html=True)
        st.markdown(a, unsafe_allow_html=True)

if __name__ == '__main__':
    Data()        


############################################################## Data Visualization ############################################################
@st.cache_data()
def Viz_Header():
    css_viz = """
    <style>
        h3{
            text-align: center;
            font-size: 45px;
            color: blue;
        }
        .divider {
            height: 2px;
            background: blue;
            margin: -18px 0;
        }
    </style>
    """

    vi_head = """
        <h3>
           VISUALIZED FEATURE 
        </h3>
        <div class="divider"></div>
    """
    st.markdown(css_viz, unsafe_allow_html=True)
    st.markdown(vi_head, unsafe_allow_html=True)
if __name__ == '__main__':
    Viz_Header()   


############################################################# Each Feature Visualization #######################################################
@st.cache_data()
def Feature_Viz():
    Col1, Col2 = st.columns(2)
    Fea_css = """
        <style>
            .header{
                color: #9381ff;
                text-align: center;
                font-size: 30px;
    }
        </style>
    """   

    # Age Vs Diabetes Column.
    Gender_Diabetes = """
        <h2 class = "header">
            Gender Vs Diabetes
        </h2>
    """     
    with Col1:
        st.markdown(Fea_css, unsafe_allow_html=True)
        st.markdown(Gender_Diabetes, unsafe_allow_html=True)
        dataset["diabetes"] = dataset['diabetes'].map({1 : 'Yes', 0 : 'No'})
        df = dataset.groupby(by=["gender", "diabetes"]).size().reset_index(name="counts")
        fig = px.bar(data_frame=df, x="gender", y="counts", color="diabetes", barmode='stack', labels={"diabetes" : 'Diabetes', 'counts' : 'Count', 'gender' : 'Gender'})
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig)
    
    # Heart Disease Vs Diabetes Column.
    Heart_Diabetes = """
        <h2 class = "header">
            Heart Disease Vs Diabetes
        </h2>
    """
    with Col2:
        st.markdown(Fea_css, unsafe_allow_html=True)
        st.markdown(Heart_Diabetes, unsafe_allow_html=True)
        dataset["heart_disease"] = dataset['heart_disease'].map({1 : 'Yes', 0 : 'No'})
        df = dataset.groupby(by=["heart_disease", "diabetes"]).size().reset_index(name="counts")
        fig = px.bar(data_frame=df, x="heart_disease", y="counts", color="diabetes", barmode='stack', labels={'diabetes' : 'Diabetes', 'heart_disease' : 'Heart Disease', 'counts' : 'Count'})
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig) 

    # Hypertension Vs Heart Disease.
    Hyper_Diabetes = """
        <h2 class = "header">
            Hypertension Vs Diabetes
        </h2>
    """     
    with Col1:
        st.markdown(Fea_css, unsafe_allow_html=True)
        st.markdown(Hyper_Diabetes, unsafe_allow_html=True)
        dataset["hypertension"] = dataset['hypertension'].map({1 : 'Yes', 0 : 'No'})
        df = dataset.groupby(by=["hypertension", "diabetes"]).size().reset_index(name="counts")
        fig = px.bar(data_frame=df, x="hypertension", y="counts", color="diabetes", barmode='stack', labels={"diabetes" : 'Diabetes', 'counts' : 'Count', 'hypertension' : 'Hypertension'})
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig)       

    # Smoking History Vs Diabetes Column.
    Heart_Diabetes = """
        <h2 class = "header">
            Smoking History Vs Diabetes
        </h2>
    """
    with Col2:
        st.markdown(Fea_css, unsafe_allow_html=True)
        st.markdown(Heart_Diabetes, unsafe_allow_html=True)
        df = dataset.groupby(by=["smoking_history", "diabetes"]).size().reset_index(name="counts")
        fig = px.bar(data_frame=df, x="smoking_history", y="counts", color="diabetes", barmode='stack', labels={'diabetes' : 'Diabetes', 'smoking_history' : 'Smoking History', 'counts' : 'Count'})
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig)   

    # Age Vs Diabetes.
    Age_Diabetes = """
        <h2 class = "header">
            Age Vs Diabetes
        </h2>    
    """ 
    with Col1:
        st.markdown(Fea_css, unsafe_allow_html=True)
        st.markdown(Age_Diabetes, unsafe_allow_html=True)
        fig = px.box(data_frame=dataset, x = 'diabetes', y = 'age', color='diabetes', labels={'diabetes' : 'Diabetes', 'age' : 'Age'}).update_traces(quartilemethod="exclusive")
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig)

    # BMI Vs Diabetes.
    BMI_Diabetes = """
    <h2 class = "header">
        Body Mass Index Vs Diabetes
    </h2>    
    """ 
    with Col2:
        st.markdown(Fea_css, unsafe_allow_html=True)
        st.markdown(BMI_Diabetes, unsafe_allow_html=True)
        fig = px.box(data_frame=dataset, x = 'diabetes', y = 'bmi', color='diabetes', labels={'diabetes' : 'Diabetes', 'bmi' : 'Body Mass Index'}).update_traces(quartilemethod="exclusive")
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig)    

    # HbA1c Level Vs Diabetes.
    Hb_Diabetes = """
    <h2 class = "header">
        HbA1c Level Vs Diabetes
    </h2>    
    """ 
    with Col1:
        st.markdown(Fea_css, unsafe_allow_html=True)
        st.markdown(Hb_Diabetes, unsafe_allow_html=True)
        fig = px.box(data_frame=dataset, x = 'diabetes', y = 'HbA1c_level', color='diabetes', labels={'diabetes' : 'Diabetes', 'HbA1c_level' : 'HbA1c Level'}).update_traces(quartilemethod="exclusive")
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig)  

    # Blood Glucose Level Vs Diabetes.
    BGL_Diabetes = """
    <h2 class = "header">
        Blood Glucose Level Vs Diabetes
    </h2>    
    """ 
    with Col2:
        st.markdown(Fea_css, unsafe_allow_html=True)
        st.markdown(BGL_Diabetes, unsafe_allow_html=True)
        fig = px.box(data_frame=dataset, x = 'diabetes', y = 'blood_glucose_level', color='diabetes', labels={'diabetes' : 'Diabetes', 'blood_glucose_level' : 'Blood Glucose Level'}).update_traces(quartilemethod="exclusive")
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig)        

Feature_Viz()        


##################################################################### Important Diabetes ################################################################

@st.cache_data()
def Imp_Header():
    css_viz = """
    <style>
        h4{
            text-align: center;
            font-size: 45px;
            color: blue;
        }
        .divider {
            height: 2px;
            background: blue;
            margin: -20px 0;
        }
    </style>
    """

    vi_head = """
        <h4>
           MAJOR CAUSE OF DIABETES 
        </h4>
        <div class="divider"></div>
    """
    st.markdown(css_viz, unsafe_allow_html=True)
    st.markdown(vi_head, unsafe_allow_html=True)
if __name__ == '__main__':
    Imp_Header()


################################################################# Important Image For Diabetes ##############################################################
@st.cache_data()
def Imp_Img():
    Img_Header_css = """
        <style>
            .header{
                color: #9381ff;
                text-align: center;
                font-size: 30px;
        }
        </style>
    """   

    # Blood Glucose Level.
    st.markdown(Img_Header_css, unsafe_allow_html=True)
    custom_css = """
        <style>
        .centered-image-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .centered-image {
              display: block;
              margin-left: auto;
              margin-right: auto;
              width: 50%;
              border: 5px;
        }
        </style>
        """
    # Blood Glucose Level
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown('<div class="centered-image-container"><img class="centered-image" src="https://assets-global.website-files.com/622154d5a1d5c02e596f4511/62f2bee4de0117f1ec10c745_BloodGlucoseChart.jpeg" alt="Centered Image"></div>', unsafe_allow_html=True)

    # Body Mass Index.
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown('<div class="centered-image-container"><img class="centered-image" src="https://t4.ftcdn.net/jpg/03/26/93/21/360_F_326932160_C2FhYsvUg0vxGJjiMKpTn7JWepR1BpED.jpg" alt="Centered Image"></div>', unsafe_allow_html=True)

    # Hb1Ac Level.
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown('<div class="centered-image-container"><img class="centered-image" src="https://www.breathewellbeing.in/blog/wp-content/uploads/2021/03/shutterstock_1547126156.png" alt="Centered Image"></div>', unsafe_allow_html=True)

if __name__ == '__main__':
    Imp_Img()    