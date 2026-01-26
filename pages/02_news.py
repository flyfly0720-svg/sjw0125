import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# 기본 설정
# -----------------------------------
st.set_page_config(
    page_title="비만치료제 150조 시장 근거",
    page_icon="💊",
    layout="wide"
)

st.title("💊 비만치료제 시장 150조 원 전망의 정량적 근거")
st.caption("CSV 기반 시장·기업·공공보건 근거 시각화")

# -----------------------------------
# CSV URL
# -----------------------------------
CSV_URL = (
    "https://gist.githubusercontent.com/anonymous/"
    "8d45012a53dc9cda500edec49b4c0480/raw/market_evidence.csv"
)

@st.cache_data(ttl=86400)
def load_data(url):
    return pd.read_csv(url)

# -----------------------------------
# 데이터 로딩
# -----------------------------------
try:
    df = load_data(CSV_URL)
except Exception:
    st.error("CSV 데이터를 불러오지 못했습니다.")
    st.stop()

# -----------------------------------
# 데이터 표시
# -----------------------------------
st.subheader("📄 시장 성장 근거 데이터")
st.dataframe(df, use_container_width=True)

# -----------------------------------
# 시각화
# -----------------------------------
market_df = df[df["Market_Size_USD_B"].notna()]

fig = px.bar(
    market_df,
    x="Source",
    y="Market_Size_USD_B",
    color="Category",
    labels={"Market_Size_USD_B": "시장 규모 (USD Billion)"}
)

st.plotly_chart(fig, use_container_width=True)




