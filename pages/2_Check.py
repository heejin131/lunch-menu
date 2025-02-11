import streamlit as st
from lunch_menu.db import select_df

st.set_page_config(page_title="SELECT", page_icon="🍽️")

st.markdown("# 🍽️ SELECT Menu")
st.sidebar.header("SELECT Menu")

st.subheader("Menu & Date")
selected_df = select_df()
selected_df

st.subheader("COUNT")
gdf = selected_df.groupby('ename')['menu_name'].count().reset_index()
gdf
