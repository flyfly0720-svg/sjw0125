import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="NVO 최근 1주일 주가 추이", layout="wide")
st.title("노보 노디스크 (NVO) 최근 1주일 주가 추이")

# 날짜 범위 설정: 오늘부터 7일 전
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=7)

# 티커 지정
ticker_symbol = "NVO"

# 데이터 불러오기
try:
    ticker_data = yf.Ticker(ticker_symbol)
    df = ticker_data.history(start=start_date, end=end_date)

    if df.empty:
        st.warning("해당 기간에 주가 데이터가 없습니다.")
    else:
        # 종가 데이터를 별도 시리즈로 추출
        df_close = df["Close"]

        # 차트 표시
        st.subheader(f"{ticker_symbol} 종가 차트")
        st.line_chart(df_close)

        # 데이터 표 표시
        st.subheader("원본 주가 데이터")
        st.dataframe(df)

except Exception as e:
    st.error(f"주가 데이터를 불러오는 중 오류가 발생했습니다: {e}")
