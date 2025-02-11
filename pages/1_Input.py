import streamlit as st
import matplotlib.pyplot as plt
from lunch_menu.db import insert_menu

st.set_page_config(page_title="INPUT", page_icon="🍽️")

st.markdown("# 🍽️ INPUT Menu")
st.sidebar.header("INPUT Menu")

members = {"SEO": 5, "TOM": 1, "cho": 2, "hyun": 3, "nuni": 10, "JERRY": 4, "jacob": 7, "jiwon": 6, "lucas": 9, "heejin": 8}

st.write('''
Have a good lunch!
''')
('''
![img](https://cdn.news.hidoc.co.kr/news/photo/202104/24374_58382_0822.jpg)
''')

st.subheader("입력")

menu_name = st.text_input("매뉴 이름", placeholder="예: 김치볶음밥")
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