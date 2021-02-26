import streamlit as st
import pandas as pd
from page import data_exploration, prediction, home
from multiapp import MultiApp

app = MultiApp()


html_temp = """ 
    <div style ="background-color:#92a8d1;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Dashboard </h1> 
    </div> 
    <hr style="height:2px;border-width:0;color:gray;background-color:gray">
   
    """
st.markdown(html_temp, unsafe_allow_html = True) 

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data exploration", data_exploration.app)
app.add_app("Prediction", prediction.app)
#app.add_app("wordembed", embed.app)
# The main app
app.run()