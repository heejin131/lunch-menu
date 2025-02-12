import streamlit as st
import requests
import lunch_menu.constants as const
import datetime

st.set_page_config(page_title="SYNC", page_icon="👀")

st.markdown("# 👀 SYNC")
st.sidebar.header("모두의 점심 데이터 비교 합치기")

if st.button("데이터 동기화 하기"):
    #API 목록 갖고 오고
    # 그 중 내것을 빼고
    # 목록을 순회 하면서 나의 df 랑 비교해서 없는것 => 데이터프레임으로 만들고
    # 데이터 프레임을 순회 하면서 insert 한다
    st.success(f"잔업완료 - 새로운 원천 00곳에서 총 00 건을 새로 추가 하였습니다.")
    
    
    