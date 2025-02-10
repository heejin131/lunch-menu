import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import psycopg
import os
from  dotenv import load_dotenv

members = {"SEO": 6, "TOM": 2, "cho": 3, "hyun": 4, "nuni": 10, "JERRY": 5, "jacob": 8, "jiwon": 7, "lucas": 9, "heejin": 1}

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

def insert_menu(menu_name, member_id, dt):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
           " INSERT INTO lunch_menu(menu_name, member_id, dt) VALUES (%s, %s, %s);",
            (menu_name, member_id, dt)
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
    options=list(members.keys()),
    index =list(members.keys()).index('heejin')    
)
member_id = members[member_name]

dt = st.date_input("날짜")

isPress = st.button("메뉴저장")

if isPress:
    if menu_name and member_id and dt:
        if insert_menu(menu_name, member_id, dt):
            st.success(f"입력성공")
        else:
            st.error(f"입력실패")
    else:
        st.warning(f"모든 값을 입력해주세요!")