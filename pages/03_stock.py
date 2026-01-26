import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Novo Nordisk 성장 분석", layout="wide")
st.title("💊 노보 노디스크 시가총액 & 매출 성장")

# =========================
# CSV 로딩 (캐시 적용)
# =========================
@st.cache_data
def load_data():
    return pd.read_csv("novo_nordisk_financials.csv")

df = load_data()

# =========================
# 데이터 확인
# =========================
st.subheader("📄 원본 데이터")
st.dataframe(df)

# =========================
# 시가총액 그래프
# =========================
fig1 = px.line(
    df,
    x="Year",
    y="MarketCap_USD_B",
    markers=True,
    title="노보 노디스크 시가총액 변화 (USD Billion)",
    labels={"MarketCap_USD_B": "시가총액 (십억 달러)"}
)
st.plotly_chart(fig1, use_container_width=True)

# =========================
# 매출 그래프
# =========================
fig2 = px.line(
    df,
    x="Year",
    y="Revenue_USD_B",
    markers=True,
    title="노보 노디스크 매출 성장",
    labels={"Revenue_USD_B": "매출 (십억 달러)"}
)
st.plotly_chart(fig2, use_container_width=True)
