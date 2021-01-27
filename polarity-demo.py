
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import pickle
from afinn import Afinn

st.title('Polarity review')
html_temp = """ 
    <div style ="background-color:#92a8d1;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit polarity review Classifier ML App </h1> 
    </div> 
    """
      
# this line allows us to display the front end aspects we have  
# defined in the above code 
st.markdown(html_temp, unsafe_allow_html = True) 

html_temp_pic = """ 
    <div style ="padding:13px; text-align: center"> 
        <img src="data:image/jpeg;base64,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">
    </div> 
    """
st.markdown(html_temp_pic, unsafe_allow_html = True) 
st.write("Write your review example:")
review = st.text_input("Type here", 'I love pizza but this was terrible!!')
review = np.array(review)
review.reshape(1, -1) 

#load_model = pickle.load(open('log_classifier.h5', 'rb')) 
afinn = Afinn()

# Apply model to make predictions
if st.button("Predict"): 
    #polarity = load_model.predict(review)
    polarity = afinn.score(review)
    print("polarity value: ",polarity)
    if polarity < 3 and polarity > -3:
        st.success('Polarity neutral') 
    elif polarity < -3:
        st.success("Polarity: negative")
    else:
        st.success("Polarity: positive")
