import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Novo Nordisk 시가총액 & 매출 성장",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Novo Nordisk 시가총액 & 매출 성장 분석")
st.caption("GLP-1 비만치료제 확산이 만든 숫자의 궤적")

# --------------------------------------------------
# 1. 시가총액 데이터 (주가 기반)
# --------------------------------------------------
ticker = yf.Ticker("NVO")

hist = ticker.history(period="10y")
hist["MarketCap"] = hist["Close"] * ticker.info["sharesOutstanding"]

hist = hist.reset_index()

# --------------------------------------------------
# 2. 매출 데이터 (연간)
# --------------------------------------------------
financials = ticker.financials.T

revenue_df = financials[["Total Revenue"]].reset_index()
revenue_df.columns = ["Year", "Revenue"]
revenue_df["Year"] = revenue_df["Year"].dt.year

# 매출 증가율 계산
revenue_df["Revenue_Growth_%"] = revenue_df["Revenue"].pct_change() * 100

# --------------------------------------------------
# 3. 시가총액 그래프
# --------------------------------------------------
st.subheader("📈 시가총액 추이")

fig_mc = px.line(
    hist,
    x="Date",
    y="MarketCap",
    title="Novo Nordisk 시가총액 추이 (최근 10년)",
    labels={"MarketCap": "시가총액 (USD)"}
)

st.plotly_chart(fig_mc, use_container_width=True)

# --------------------------------------------------
# 4. 매출 및 성장률 그래프
# --------------------------------------------------
st.subheader("💰 연도별 매출 및 성장률")

fig_rev = px.bar(
    revenue_df,
    x="Year",
    y="Revenue",
    title="연도별 매출",
    labels={"Revenue": "매출 (USD)"}
)

st.plotly_chart(fig_rev, use_container_width=True)

fig_growth = px.line(
    revenue_df,
    x="Year",
    y="Revenue_Growth_%",
    markers=True,
    title="연도별 매출 증가율 (%)",
    labels={"Revenue_Growth_%": "매출 증가율 (%)"}
)

st.plotly_chart(fig_growth, use_container_width=True)

# --------------------------------------------------
# 5. 핵심 수치 요약
# --------------------------------------------------
st.subheader("📊 핵심 요약")

latest_mc = hist["MarketCap"].iloc[-1]
latest_rev = revenue_df["Revenue"].iloc[-1]
latest_growth = revenue_df["Revenue_Growth_%"].iloc[-1]

st.metric("최근 시가총액", f"${latest_mc/1e12:.2f} T")
st.metric("최근 연매출", f"${latest_rev/1e9:.1f} B")
st.metric("최근 매출 성장률", f"{latest_growth:.1f} %")

