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
    "dbname" : os.getenv("DB_NAME"),
    "password" : os.getenv("DB_PASSWORD"),
    "host" : os.getenv("DB_HOST"),
    "port" : os.getenv("DB_PORT")
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)

def insert_menu(menu_name, member_name, dt):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO lunch_menu(menu_name, member_name, dt) VALUES (%s, %s, %s);",
            (menu_name, member_name, dt)
            )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Exception:{e}")
        return False
st.markdown(f"# 오늘 점심 뭐먹지?{db_name}")
st.sidebar.markdown("## Main page 🎧")

#st.title(f"오늘 점심 뭐먹지?{db_name}")
st.write('''
Have a good lunch!
''')
('''
![img](https://cdn.news.hidoc.co.kr/news/photo/202104/24374_58382_0822.jpg)
''')

st.subheader("입력")

menu_name = st.text_input("매뉴 이름", placeholder="예: 김치볶음밥")
#member_name = st.text_input("먹은 사람", placeholder="예: 전희진", value = "heejin")
member_name = st.selectbox(
    "먹은 사람?",
    ("heejin", "TOM", "cho", "hyun", "JERRY", "SEO", "jiwon", "jacob", "lucas","nuni"),
)
dt = st.date_input("날짜")

isPress = st.button("메뉴저장")

if isPress:
    if menu_name and member_name and dt:
        if insert_menu(menu_name, member_name, dt):
            st.success(f"입력성공")
        else:
            st.error(f"입력실패")
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
conn.close()

#selected_df = pd.DateFrame([[1,2,3]],[4,5,6], columns=[['a','b','c'])
selected_df = pd.DataFrame(rows, columns=['menu_name', 'ename', 'dt'])
selected_df

st.markdown("### 통계")
st.sidebar.markdown("## 통계🚩")
#st.subheader("통계")

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
        cursor.execute("INSERT INTO lunch_menu (menu_name, member_name, dt) VALUES (%s, %s, %s)", (not_na_df.iloc[i]['menu_name'], not_na_df.iloc[i]['ename'], not_na_df.iloc[i]['dt']))
  
    conn.commit()
    conn.close()
    st.success(f"DB에 저장되었습니다.")

