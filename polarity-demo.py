"""
Come farlo funzionare
Una volta compilato vai sul cmd nella cartella dove è presente il file
comando: streamlit run nomefile.py
"""

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import joblib

st.title('Polarity review')
html_temp = """ 
    <div style ="background-color:#92a8d1;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit polarity review Classifier ML App </h1> 
    </div> 
    """
      
# this line allows us to display the front end aspects we have  
# defined in the above code 
st.markdown(html_temp, unsafe_allow_html = True) 

link = ""
#st.image(link)
st.write("Write your review example:")
review = st.text_input("Type here", 'I love pizza but this was terrible!!')



filename = "C:/Users/matte/Desktop/università/magistrale/Data Analytics/progetto/rf_classifier.pkl"
#loaded_model = pickle.load(open(filename, 'rb'))
#loaded_model = joblib.load(filename)
"""
pickle_in = open('C:/Users/matte/Desktop/università/magistrale/Data Analytics/progetto/rf_classifier.pkl', 'rb') 
print(pickle_in)

classifier = pickle.load(pickle_in) """

"""
if st.button("Predict"): 
    polarity = classifier.predict(review)
st.success('The output is {}'.format(polarity)) 
"""