import streamlit as st
import matplotlib.pyplot as plt
from lunch_menu.db import select_df, rank_menu

st.set_page_config(page_title="STATISTICS", page_icon="🍽️")

st.markdown("# 🍽️ STATISTICS Menu")
st.sidebar.header("STATISTICS Menu")

selected_df = select_df()
gdf = selected_df.groupby('ename')['menu_name'].count().reset_index()

st.subheader("CHART")
# Matplotlib로 바 차트 그리기
try:
    fig, ax = plt.subplots()
    gdf.plot(x='ename', y='menu_name', kind='bar', ax=ax)
    st.pyplot(fig)
except Exception as e:
    st.warning(f"차트를 그리기에 충분한 데이터가 없습니다.")
    print(f"Exception:{e}")
    
df = rank_menu() 
hdf = df.copy()
try: 
     fig, ax = plt.subplots(figsize=(8, 5))
     ax.bar(hdf["menu_name"], hdf["order_count"], color="skyblue")

     ax.set_xlabel("Menu Name")
     ax.set_ylabel("Order Count")
     ax.set_title("Top 5 Ordered Menu Items")

     plt.xticks(rotation=45)  # 메뉴 이름이 겹치지 않도록 회전
     st.pyplot(fig)
except Exception as e:
    st.warning(f"차트를 그리기에 충분한 데이터가 없습니다.")
    print(f"Exception:{e}") 

