import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("배송 데이터 대시보드")

# CSV 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("Delivery.csv")
    return df

df = load_data()

# 데이터 기본 정보
st.subheader("📄 데이터 미리보기")
st.dataframe(df.head())

# 선택: 도시별 평균 배송시간 시각화
if 'City' in df.columns and 'Time_taken(min)' in df.columns:
    avg_time = df.groupby("City")["Time_taken(min)"].mean().reset_index()
    fig = px.bar(avg_time, x="City", y="Time_taken(min)", color="City",
                 title="도시별 평균 배송시간")
    st.plotly_chart(fig)

# 필터 기능 (예: 배송 종류)
if 'Type_of_order' in df.columns:
    selected_type = st.selectbox("주문 종류 선택", df['Type_of_order'].unique())
    filtered = df[df['Type_of_order'] == selected_type]
    st.write(f"선택한 주문 종류: {selected_type}")
    st.dataframe(filtered)

# 기타 통계 정보
st.subheader("📊 기본 통계 정보")
st.write(df.describe())
