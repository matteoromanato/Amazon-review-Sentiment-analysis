import streamlit as st

def app():
    
    html_temp = """ 
    <br>
    <div>
        <h2 style ="color:black;text-align:center;"> Home </h2> 
        Questa dashboard permette di effettuare
        una analisi esporativa di alcune recensioni in Amazon.com
        e testare la polarità di una recensione. 
    </div>
    <br>
    <div>
       La sezione di interesse è selezionabile nel menù a sinistra. 
    </div>
    <hr style="height:2px;border-width:0;color:gray;background-color:gray">
    <br>

    """
    
    st.markdown(html_temp, unsafe_allow_html = True) 

    readme = """

    L'obiettivo del progetto era quello di analizzare alcune recensioni in Amazon per evidenziare informazioni utili ai produttori e ai consumatori.
    Successivamente addestrare un modello basato sul machine learning per predire la polarità delle recensioni.
    Ho confrontato diversi approcci:
    - Lexicon based
    - Supervised Machine Learning (Random forest, Logistic regression)
    - Unsupervised (K-means, ASUM)
    - AI approach using Google-news-embedded-300

    ### Codice
    Il codice è disponibile [[qui]](https://colab.research.google.com/drive/1bjU-lboFpcfqoZxYxUy5l1CsEtZdDZ_E#scrollTo=p0ADvJCuPJ1B).
    
    ### Pre-requisiti
    Il metodo ideale è utilizzare Google Colab o un Jupyter Notebook

    ### Usage
    Il codice è eseguibile ma presta attenzione al percorso del dataset quando effettui l'import.
    Il percorso su Colab inizia con: 
    ```python
    '/content/...'
    ```

    ### Dataset
    Il dataset usati era **amazon-fine-food-reviews** [[link]](https://www.kaggle.com/snap/amazon-fine-food-reviews).
    Il mio progetto aveva due dataset che ho unito in modo da tenere solo le istanze del dataset con meno istanze (erano comunuque tante).
    

    ## Authors
    Matteo Romanato - matteoromanato14@gmail.com 
    <p>
    <a href="https://www.linkedin.com/in/matteo-romanato-b44414124/" rel="nofollow noreferrer">
        <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
    </a> &nbsp; 
    <a href="https://github.com/matteoromanato" rel="nofollow noreferrer">
        <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
    </a>
    </p>
    """

    st.markdown(readme, unsafe_allow_html = True) 