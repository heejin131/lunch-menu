import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import psycopg
import os
from  dotenv import load_dotenv
from lunch_menu.db import select_df

# TODO
# CSV 로드해서 한번에 다 디비에 INSERT 하는거
st.subheader("벌크 인서트")
isPress = st.button("한방에 인서트")

if isPress:
    conn = get_connection()
    cursor = conn.cursor()
    for i in range(len(not_na_df)):
        m_id = members[not_na_df.iloc[i]['ename']]
        cursor.execute("INSERT INTO lunch_menu (menu_name, member_id, dt) VALUES (%s, %s, %s)", 
                       (not_na_df.iloc[i]['menu_name'], 
                        m_id, 
                        not_na_df.iloc[i]['dt']))
  
    conn.commit()
    conn.close()
    st.success(f"DB에 저장되었습니다.")