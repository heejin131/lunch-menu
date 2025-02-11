import streamlit as st
from lunch_menu.db import select_df

st.set_page_config(page_title="SELECT", page_icon="🍽️")

st.markdown("# 🍽️ SELECT Menu")
st.sidebar.header("SELECT Menu")

selected_df = select_df()
selected_df
