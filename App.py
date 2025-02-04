import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import psycopg

DB_CONFIG = {
    "dbname": "sunsindb",
    "user" : "sunsin",
    "password" : "mysecretpassword",
    "host" : "localhost",
    "port" : "5432"
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)

st.title("오늘 점심 뭐먹지?")
st.write('''
Have a good lunch!
''')
('''
![img](https://cdn.news.hidoc.co.kr/news/photo/202104/24374_58382_0822.jpg)
''')

st.subheader("입력")

menu_name = st.text_input("매뉴 이름", placeholder="예: 김치볶음밥")
member_name = st.text_input("먹은 사람", placeholder="예: 전희진", value = "heejin")
dt = st.date_input("날짜")

isPress = st.button("메뉴저장")

if isPress:
    if menu_name and member_name and dt:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
        "INSERT INTO lunch_menu(menu_name, member_name, dt) VALUES (%s, %s, %s);",
          (menu_name, member_name, dt)
)
        conn.commit()
        cursor.close()
        st.success(f"버튼{isPress}:{menu_name}, {member_name}, {dt}")
    else:
        st.warning(f"모든 값을 입력해주세요!")

st.subheader("확인")
query = """SELECT 
menu_name AS menu, 
member_name AS ename, 
dt 
FROM lunch_menu 
ORDER BY dt DESC"""

conn = get_connection()
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()
#conn.commit()
cursor.close()

#selected_df = pd.DateFrame([[1,2,3]],[4,5,6], columns=[['a','b','c'])
selected_df = pd.DataFrame(rows, columns=['menu_name', 'ename', 'dt'])
selected_df

st.subheader("통계")

df = pd.read_csv('note/lunch_menu.csv')

start_index= df.columns.get_loc('2025-01-07')
mdf = df.drop(columns=['gmail', 'github', 'domain', 'vercel', 'role'])
df_melt = mdf.melt(id_vars=['ename'], var_name='dt', value_name='menu_name')

not_na_df = df_melt[~df_melt['menu_name'].isin(['-', 'x', '<결석>'])]
#gdf=not_na_df.groupby('ename')['menu_name'].count().reset_index()
gdf=selected_df.groupby('ename')['menu_name'].count().reset_index()
# gdf.plot(x='ename', y='menu_name', kind='bar')

gdf

st.subheader("CHART")
# Matplotlib로 바 차트 그리기
fig, ax = plt.subplots()
gdf.plot(x='ename', y='menu_name', kind='bar', ax=ax)
st.pyplot(fig)


