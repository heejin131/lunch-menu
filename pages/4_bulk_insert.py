import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import psycopg
import os
from  dotenv import load_dotenv

load_dotenv()
db_name=os.getenv("DB_NAME")
DB_CONFIG = {
    "user": os.getenv("DB_USERNAME"),
    "dbname" : db_name,
    "password" : os.getenv("DB_PASSWORD"),
    "host" : os.getenv("DB_HOST"),
    "port" : os.getenv("DB_PORT")
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)

st.subheader("CHART")
# Matplotlib로 바 차트 그리기
try:
    fig, ax = plt.subplots()
    gdf.plot(x='ename', y='menu_name', kind='bar', ax=ax)
    st.pyplot(fig)
except Exception as e:
    st.warning(f"차트를 그리기에 충분한 데이터가 없습니다.")
    print(f"Exception:{e}")

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