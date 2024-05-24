############################################################ Import Packages ###################################################################
import streamlit as st


############################################################ Set Page Config ###################################################################
st.set_page_config(page_title="About Me", layout='wide')
st.write('<style>div.block-container{padding-top:3rem};</style>', unsafe_allow_html=True)


######################################################### Set Page Navbar color #################################################################
st.markdown("""
<style>
	[data-testid="stHeader"] {
		background-color: #b6ccfe;
	}
</style>""",
unsafe_allow_html=True)


########################################################## Set Page Backgruound ##################################################################
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


############################################################ Set Profile Picture ##################################################################
custom_css = """
        <style>
        .centered-image-container {
            padding-top: 80px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .centered-image {
              border-radius: 50%;
              display: block;
              margin-left: auto;
              margin-right: auto;
              width: 200px; 
              height: 200px;
              object-fit: cover;
              border: 4px solid #046dc8;
              padding: 2px;
              border-radius: 50%;
              border-top-color: #b5179e;
              border-left-color: #7209b7;
        }
        </style>
        """
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('<div class="centered-image-container"><img class="centered-image" src="https://avatars.githubusercontent.com/u/92677777?s=400&u=035b385f4fbcc1320f0aafd77bc23579145da0de&v=4" alt="Centered Image"></div>', unsafe_allow_html=True)


################################################################ Set the Header #####################################################################
def header():
    custom_css = """
        <style>
             h1 {
                text-align: center;
                font-size: 70px;
                    }   
             .header{
                color: #fff;
                font-size: 66px;
                font-family: Poppins;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
        </style>
    """

    head = """
        <h1 class="header">
            Hi, I'm SUMAN
        </h1>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(head, unsafe_allow_html=True)
if __name__ == '__main__':
    header() 


######################################################### Set Github and LinkedIn Link #################################################################
st.markdown(
        """
        <div style="text-align:center;">
            <a href="https://github.com/Suman-Adhikary"  style="margin-right: 20px;"><img src="https://img.icons8.com/?size=512&id=3tC9EQumUAuq&format=png" alt="GitHub Logo" width="40" height="40"></a>
            <a href="https://www.linkedin.com/in/sumanhere/"><img src="https://img.icons8.com/?size=512&id=13930&format=png" alt="LinkedIn Logo" width="40" height="40"></a>
        </div>
        """,
        unsafe_allow_html=True
    )


############################################################ Set Resume Download Link ###################################################################
Button_css = """
         <style>
         body {
            text-align: center; 
            }
            .download-button {
            margin-top: 20px;
            background: linear-gradient(to bottom , #ade8f4, #0096c7); 
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 30px;
            font-size: 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            cursor: pointer;
        }

        .download-button:hover {
            background-color: rgba(0, 0, 0, 0.5); 
        }
    </style>
"""

Button = """
   <body>
    <a href="https://drive.google.com/uc?export=download&id=1XOoESqb_L2EdEiR030g0L8Cdx3xVc0ZG" class="download-button">Resume</a>
    </body>
"""
st.markdown(Button_css, unsafe_allow_html=True)
st.markdown(Button, unsafe_allow_html=True)