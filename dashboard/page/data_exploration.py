import streamlit as st
import pandas as pd
import numpy as np
import base64
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def upload_df():
    df = pd.read_csv('dataset2.csv', sep=',', encoding='windows-1252')
    df = df.sort_values('date', ascending=False)
    return df

@st.cache
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv</a>'
    return href

def plot_pie(df_occ,n_ent,att):
    labels = df_occ.iloc[0:n_ent].index
    values = df_occ.iloc[0:n_ent][att]

    fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
    fig_pie.update_layout(
                        autosize=False,
                        width=350,
                        height=350,
                        margin=dict(
                                l=50,
                                r=50,
                                b=50,
                                t=50,
                                pad=4
                            ),
    paper_bgcolor="#e5ecf6",) 
    return fig_pie


def plot_satisfaction(x,y):
    fig1, ax = plt.subplots(figsize=(10,6))
    ax = plt.scatter(x=x, y=y)
    m, b = np.polyfit(x, y, 1)
    ax = plt.plot(x, m*x + b)
    plt.ylabel('Score')
    plt.xlabel('Time')
    plt.yticks(np.arange(6), labels=['0','1', '2', '3', '4', '5'])
    return fig1

def entità_specifica(df, att, textIn):
    df_ut = df[df[att]==textIn]
    st.dataframe(df_ut)
    
    user_col1, user_col2, user_col3 = st.beta_columns([7, 1, 7])
    #with user_col1:
    #st.write('Distribuzioni delle recensioni di '+userid+' nel tempo')
    fig = px.box(df_ut, x="score", y="Time", points="all", hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
    #fig = px.scatter(df_ut, x = 'score', y='Time', hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
    #st.write('Distribuzioni delle recensioni di '+textIn+' nel tempo')
    #st.plotly_chart(fig)
    #with user_col3:
    #st.write("Indice di soddisfazione dell'utente in base ai prodotti comprati")
    x = df_ut.Time
    y = df_ut.score
    #fig1 = plot_satisfaction(x,y)
    fig1 = px.scatter(df_ut, x='Time', y='score', trendline="ols", trendline_color_override='red',  hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
    #st.plotly_chart(fig1)
    return fig, fig1

def aspect_plot(textIn, att, df):
    fig, fig1 = entità_specifica(df, att, textIn)
    st.write('Distribuzioni delle recensioni di '+textIn+' nel tempo')
    st.plotly_chart(fig)
    st.write("Indice di soddisfazione dell'utente in base ai prodotti comprati")
    st.plotly_chart(fig1)

def custom_plot(df):
    st.markdown("""<hr style="height:2px;border-width:0;color:#e5ecf6;background-color:gray">""", unsafe_allow_html = True)  
    st.write('Custom plot')
    plot_aspect = st.selectbox("Scegli il plot che vuoi Visualizzare", (' ','Box plot','Pie plot','Scatter plot','Bar plot'))

    if plot_aspect == 'Scatter plot':
        x = st.selectbox("Scegli attributo sull'asse delle x", list(df.columns))
        y = st.selectbox("Scegli attributo sull'asse delle y", list(df.columns))
        color = st.selectbox("Scegli attributo su cui raggruppare i risultati",  list(" ")+list(df.columns))
        trendline = st.radio("Trendline", ('Si', 'No'))

        if st.checkbox('Plot'):
            if color and trendline == 'Si':
                fig = px.scatter(df, x=x, y=y, color=color, trendline="ols", trendline_color_override='red', hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
                st.plotly_chart(fig)
            elif trendline and color == " ":
                fig = px.scatter(df, x=x, y=y, trendline="ols", trendline_color_override='red', hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
                st.plotly_chart(fig)            
            elif color and trendline == 'No':
                fig = px.scatter(df, x=x, y=y, color=color, hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
                st.plotly_chart(fig)
            else:
                fig = px.scatter(df, x=x, y=y, hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
                st.plotly_chart(fig)
    
    if plot_aspect == 'Box plot':
        x = st.selectbox("Scegli attributo sull'asse delle x", list(df.columns))
        y = st.selectbox("Scegli attributo sull'asse delle y", list(df.columns))
        color = st.selectbox("Scegli attributo su cui raggruppare i risultati",  list(" ")+list(df.columns))
        if st.checkbox('Plot'):
            if color != " ":
                fig = px.box(df, x=x, y=y, notched=True, points="all", color=color, hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
                st.plotly_chart(fig)
            else:
                fig = px.box(df, x=x, y=y, notched=True, points="all", hover_name='Summary', hover_data=['ProfileName', 'score', 'date'])
                st.plotly_chart(fig)

def app():
    
    html_temp = """ 
    <br>
    <div>
        <h2 style ="color:black;text-align:center;"> Data exploration </h2> 
        In questa sezione potrai esplorare i dati del dataset.
        Sfrutta il menù a tendina per selezionare i parametri desiderati.
    </div>
    <hr style="height:2px;border-width:0;color:gray;background-color:gray">
    <br>
    """
    
    st.markdown(html_temp, unsafe_allow_html = True) 

    df = upload_df()
    n = st.slider('Quante istanze desideri vedere?', 0, df.shape[0], 25)
    st.dataframe(df.head(n))
    #st.markdown(get_table_download_link(df), unsafe_allow_html=True)
    
    st.markdown("""<hr style="height:2px;border-width:0;color:#e5ecf6;background-color:gray">""", unsafe_allow_html = True) 
    ##################################### SECOND ##########################################################################
    st.write("## Quale aspetto vuoi analizzare?", unsafe_allow_html = True)
    att = st.selectbox("Scegli l'attributo che vuoi controllare", (' ','productid','userid','score','categoria_prodotto'))
    if att != " ":
        col1, col2, col3 = st.beta_columns([5.35, 1, 7])
        df_occ = pd.DataFrame(df[att].value_counts())
        with col1:
            st.write("Occorrenze",df_occ)
        with col3:
            n_ent = st.slider('Numero di entità nel grafico a torta', 0, len(df_occ), 5)
            fig_pie = plot_pie(df_occ,n_ent,att)          
            st.plotly_chart(fig_pie)

        if att == "userid" :
            textIn = st.text_input("inserisci "+ att +" che vuoi analizzare")
            if textIn:
                aspect_plot(textIn, att, df)

        elif att == "productid":
            textIn = st.text_input("inserisci "+ att +" che vuoi analizzare")
            if textIn:
                aspect_plot(textIn, att, df)

        elif att == "categoria_prodotto":
            textIn = st.text_input("inserisci "+ att +" che vuoi analizzare")
            if textIn:
                aspect_plot(textIn, att, df)
    ##################################### THIRD ##########################################################################
    
    st.markdown("""<hr style="height:2px;border-width:0;color:#e5ecf6;background-color:gray">""", unsafe_allow_html = True) 
    expander_query = st.beta_expander('Custom Dataset & Plot')
    with expander_query:
        exp = st.text_input("Inserisci la query (e.g. score < 3 and/or userid == 'userid')")
        if exp:
            if exp == " ":
                n_ent_1 = st.slider('Quante istanze desideri vedere del dataset originale?', 0, df.shape[0], 25)
                st.write(df.head(n_ent_1))
                custom_plot(df)
            else:
                n_ent_2 = st.slider('Quante istanze desideri vedere del dataset query?', 0, df.query(exp).shape[0], 25)
                st.write(df.query(exp).head(n_ent_2))

                if st.checkbox('Vuoi lavorare su questo dataset?'):
                    new_df = df.query(exp)
                    st.warning('Dataset aggiornato')
                    custom_plot(new_df)

  #          if ok == True:
  #              st.markdown("""<hr style="height:2px;border-width:0;color:#e5ecf6;background-color:gray">""", unsafe_allow_html = True)  
  #              st.write('custom plot')
  #              att = st.selectbox("Scegli il plot che vuoi Visualizzare", (' ','Box plot','Pie plot','Sccater plot','Bar plot'))
