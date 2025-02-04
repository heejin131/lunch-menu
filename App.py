import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title("오늘 점심 뭐먹지?")
st.subheader("입력")
st.write('''
Have a good lunch!
''')

menu_name = st.text_input("매뉴 이름", placeholder="예: 김치볶음밥")
member_name = st.text_input("먹은 사람", placeholder="예: 전희진", value = "HEEJIN")
dt = st.date_input("날짜")
















('''
![img](https://cdn.news.hidoc.co.kr/news/photo/202104/24374_58382_0822.jpg)
''')

df = pd.read_csv('note/lunch_menu.csv')

start_index= df.columns.get_loc('2025-01-07')
mdf = df.drop(columns=['gmail', 'github', 'domain', 'vercel', 'role'])
df_melt = mdf.melt(id_vars=['ename'], var_name='dt', value_name='menu_name')

not_na_df = df_melt[~df_melt['menu_name'].isin(['-', 'x', '<결석>'])]
gdf=not_na_df.groupby('ename')['menu_name'].count().reset_index()
# gdf.plot(x='ename', y='menu_name', kind='bar')

gdf

# Matplotlib로 바 차트 그리기
fig, ax = plt.subplots()
gdf.plot(x='ename', y='menu_name', kind='bar', ax=ax)
st.pyplot(fig)


