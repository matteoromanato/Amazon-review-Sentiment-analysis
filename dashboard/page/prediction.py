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
import string
import pickle
from afinn import Afinn
import emoji 
import sklearn
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def target(x):
  if x <= -0.5:
    return -1
  elif x > -0.5 and x < 0.5:
    return 0
  else:
    return 1

def target_a(x):
  if x < -3:
    return -1
  elif x >= -3 and x <= 3:
    return 0
  else:
    return 1

def trasform(pol_aff, pol_vd):
    vd = target(pol_vd)
    af = target_a(pol_aff)
    #print("vd ",vd)
    #print("af ",af)

    if vd == af == -1:
        return -1
    elif vd == af == 1:
        return 1
    elif vd == af == 0:
        return 0
    elif vd == 1 and af == 0:
        return 0
    elif vd == 0 and af == 1:
        return 0
    elif vd == -1 and af == 1:
        return 0
    elif vd == 1 and af == -1:
        return 0
    elif vd == 0 and af == -1:
        return -1
    elif vd == -1 and af == 0:
        return -1
    else:
        print("sono nell' else")

def app():

    html_temp = """ 
        <br>
        <div>
            <h2 style ="color:black;text-align:center;"> Review prediction </h2> 
            In questa sezione potrai provare il sentiment di una recensione custom che potrai digitare per vedere se risulta effettivamente quello che provavi.
        </div>
        <hr style="height:2px;border-width:0;color:gray;background-color:gray">
        <br>
        """
        
    st.markdown(html_temp, unsafe_allow_html = True) 
        
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.write("Write your review example:")
    review = st.text_input("Type here", 'I love pizza but this was terrible!!')

    afinn = Afinn()
    analyzer = SentimentIntensityAnalyzer()
    # Apply model to make predictions
    if st.button("Predict"): 
        polarity_aff = afinn.score(review)
        polarity_vd = res = analyzer.polarity_scores(review)['compound']

        polarity= trasform(polarity_aff,polarity_vd)

        #print("polarity value: ",polarity)
        if polarity == 0 :
            st.warning('Polarity: neutral \N{neutral face}') 
        elif polarity < 0:
            st.error("Polarity: negative \N{nauseated face}")
        else:
            st.success("Polarity: positive \N{grinning face}")
