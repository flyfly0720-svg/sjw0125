import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="비만치료제 150조 시장 근거",
    page_icon="💊",
    layout="wide"
)

st.title("💊 비만치료제 시장 150조 원 전망의 정량적 근거")
st.caption("시장 보고서 · 기업 매출 · 공공보건 데이터를 CSV 기반으로 검증")

# -----------------------------------
# CSV 로딩 (로컬 파일)
# -----------------------------------
try:
    df = pd.read_csv("market_evidence.csv")
except FileNotFoundError:
    st.error("❌ market_evidence.csv 파일을 찾을 수 없습니다.")
    st.stop()

# -----------------------------------
# 데이터 테이블
# -----------------------------------
st.subheader("📄 시장 성장 근거 데이터")
st.dataframe(df, use_container_width=True)

# -----------------------------------
# 시장 규모 전망 시각화
# -----------------------------------
market_df = df[df["Market_Size_USD_B"].notna()]

st.subheader("📊 비만치료제 시장 규모 전망")

fig = px.bar(
    market_df,
    x="Source",
    y="Market_Size_USD_B",
    color="Category",
    text="Year",
    labels={"Market_Size_USD_B": "시장 규모 (USD Billion)"}
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------
# 기업 매출 기반 하한선
# -----------------------------------
company_df = df[df["Category"] == "Company Revenue"]
total_sales = company_df["Market_Size_USD_B"].sum()

st.subheader("🏭 GLP-1 기업 매출 기반 시장 하한선")

st.metric(
    "주요 GLP-1 기업 매출 합계",
    f"${total_sales:.0f} B (USD)"
)

st.info(
    f"""
    📌 **해석**
    
    - Novo Nordisk + Eli Lilly GLP-1 매출 합계: **${total_sales:.0f}B**
    - 이는 전체 비만치료제 시장의 일부
    - 시장 보고서 + 공공보건 데이터 결합 시  
      👉 **150조 원 이상 시장 전망이 논리적으로 도출**
    """
)
