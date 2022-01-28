import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv



def app():
    st.title('NBA Team Stats Explorer')
    st.sidebar.markdown('Search')
    
    st.sidebar.header('Search')
    selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

    # Web scraping of NBA player stats
    @st.cache
    def load_data(year):
        url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
        html = pd.read_html(url, header = 0)
        df = html[0]
        raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
        raw = raw.fillna(0)
        playerstats = raw.drop(['Rk'], axis=1)
        return playerstats
    playerstats = load_data(selected_year)

# Sidebar - Team selection
    sorted_unique_team = sorted(playerstats.Tm.unique())
    selected_team = st.sidebar.multiselect('Team',sorted_unique_team)



# Filtering data
    df_selected_team = playerstats[(playerstats.Tm.isin(selected_team))]

    st.header('Team Stats')
    test = df_selected_team.astype(str)
    st.dataframe(test)



