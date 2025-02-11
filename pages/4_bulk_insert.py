import streamlit as st
from lunch_menu.db import get_connection
import pandas as pd

st.set_page_config(page_title="WITHOUT LUNCH", page_icon="🍽️")

st.markdown("# 🍽️ WITHOUT LUNCH")
st.sidebar.header("WITHOUT LUNCH")

# CSV 로드해서 한번에 다 디비에 INSERT 하는거
st.subheader("벌크 인서트")
isPress = st.button("한방에 인서트")

members = {"SEO": 5, "TOM": 1, "cho": 2, "hyun": 3, "nuni": 10, "JERRY": 4, "jacob": 7, "jiwon": 6, "lucas": 9, "heejin": 8}

df = pd.read_csv('note/lunch_menu.csv')

start_index= df.columns.get_loc('2025-01-07')
mdf = df.drop(columns=['gmail', 'github', 'domain', 'vercel', 'role'])
df_melt = mdf.melt(id_vars=['ename'], var_name='dt', value_name='menu_name')
not_na_df = df_melt[~df_melt['menu_name'].isin(['-', 'x', '<결석>'])]    

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
