import streamlit as st
from PIL import Image
import urllib
import pandas as pd
import dhlab as dh
import streamlit as st

st.set_page_config(page_title="POLNET", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.session_state.update(st.session_state)


#st.session_state.update(st.session_state)


# zotero_excel = "Zoterobibliotek eksportert_010420.xlsx"

#### CODE FOR WELCOME SCREEN


@st.cache_data()
def corpus():
    c = pd.read_excel("Beatrice_korpus.xlsx", index_col=0)
    c['url'] = c.urn.apply(lambda x: f"https://nb.no/items/{x}")
    return c

litt_korpus = corpus()
st.session_state['korpus'] = litt_korpus
st.session_state['dhlabid'] = [int(x) for x in litt_korpus.dhlabid]

st.dataframe(
    litt_korpus[['url','title', 'authors','year']],
    column_config={
            "url": st.column_config.LinkColumn("URL")
    },
    hide_index=True
)

    
        