import streamlit as st
from lunch_menu.db import select_df

st.subheader("확인")
selected_df = select_df()
selected_df
