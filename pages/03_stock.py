import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(page_title="주가 추이: NVO & LLY", layout="wide")

st.title("노보 노디스크 (NVO) 최근 1주일 주가 추이")

# 날짜 범위
end = datetime.date.today()
start = end - datetime.timedelta(days=7)

# Yahoo Finance 티커
tickers = {
    "노보 노디스크 (NVO)": "NVO",
    "Eli Lilly (LLY)": "LLY"
}

# Fetch price data
price_data = {}
for label, ticker in tickers.items():
    try:
        df = yf.download(ticker, start=start, end=end)
        df = df["Adj Close"].rename(label)
        price_data[label] = df
    except Exception as e:
        st.error(f"데이터 불러오기 오류: {ticker} - {e}")

if price_data:
    df_prices = pd.concat(price_data.values(), axis=1)
    
    st.subheader("종가 (Adjusted Close)")
    st.line_chart(df_prices)

    st.write("원본 데이터 (최근 1주일)")
    st.dataframe(df_prices)

else:
    st.write("주가 데이터를 불러오지 못했습니다. 다시 시도해주세요.")

