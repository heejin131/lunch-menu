import streamlit as st
import requests
import lunch_menu.constants as const
import datetime
import pandas as pd

st.set_page_config(page_title="SYNC", page_icon="👀")

st.markdown("# 👀 SYNC")
st.sidebar.header("모두의 점심 데이터 비교 합치기")

EP = "https://raw.githubusercontent.com/heejin131/journeyjean/refs/heads/main/endpoints.json"
res = requests.get(EP)
data = res.json()
endpoints = data['endpoints']

urls = [
    "https://ac.sunsin.shop/api/py/select_all",
    "https://agecal.wodan10.shop/api/py/select_all",
    "https://age.journeyjean.shop/api/py/select_all",
    "https://agecalculator.calcalhan.store/api/py/select_all",
    "https://nextjs-fastapi-starter-5j3bemub7-chominkyus-projects.vercel.app/api/py/select_all",
    "https://jacob0503.vercel.app/api/py/select_table",
    "https://ac.nunininu.shop/api/py/select_all",
    "https://ac.lucas12.store/api/py/select_all",
    "https://ac.seo-sigma.shop/api/py/select_all",
    "https://jooon.vercel.app/api/py/select_all"
    ]

# 데이터를 저장할 리스트
df_list = []

# 각 URL에서 데이터 가져오기
for url in urls:
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        df = pd.DataFrame(data)
        df_list.append(df)  # 리스트에 추가

# 여러 개의 DataFrame을 하나로 합치기
df_all = pd.concat(df_list, ignore_index=True)

# 결과 확인
df_all

if st.button("데이터 동기화 하기"):
    missing_rows = []
    
    for _, row_all in df_all.iterrows():
        found = False 
        for _, row_heejin in df_heejin.iterrows():
            if row_all.equals(row_heejin): 
                found = True
    if not found:
        missing_rows.append(row_all)

    df_missing = pd.DataFrame(missing_rows)
    df_missing
    
    # API 목록 갖고 오고
    # 그 중 내것을 빼고
    # 목록을 순회 하면서 나의 df 랑 비교해서 없는것 => 데이터프레임으로 만들고
    # 데이터 프레임을 순회 하면서 insert 한다
    st.success(f"잔업완료 - 새로운 원천 00곳에서 총 00 건을 새로 추가 하였습니다.")

