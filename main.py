import teams
import seasons
import streamlit as st
from PIL import Image
img = Image.open('StatAppPic.PNG')
st.set_page_config(page_title = 'NBA Stats', page_icon = img)
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html = True)


PAGES = {
    "Team Stats": teams,
    "Season Stats": seasons,
}
st.sidebar.markdown("""
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()