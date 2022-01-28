import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



def app():
    st.title('NBA Scores Explorer')

    # Web scraping of NBA player stats
    @st.cache
    def load_data():
        url = "https://www.basketball-reference.com/boxscores/"
        html = pd.read_html(url, header = 0)
        df = html[7]
        return df
    playerstats = load_data()

    
    st.dataframe(playerstats)
