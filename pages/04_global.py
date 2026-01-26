import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="WHO 비만율 데이터 시각화",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 WHO 성인 비만율 데이터 (BMI ≥ 30)")
st.caption("World Health Organization Global Health Observatory API 기반 시각화")

# WHO OData API 엔드포인트
API_BASE = "https://ghoapi.azureedge.net/api/NCD_BMI_30?format=csv"

st.markdown("""
이 앱은 WHO Global Health Observatory (GHO)에서 제공하는  
**성인 비만율 (BMI ≥ 30, age-standardized)** 데이터를 자동 수집해 국가별 비교를 제공합니다.  
(출처: WHO GHO OData API) :contentReference[oaicite:2]{index=2}
""")

# -----------------------------------
# 1) 데이터 로딩
# -----------------------------------
@st.cache_data(ttl=86400)
def load_who_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error("❌ WHO 데이터를 불러오는 중 오류가 발생했습니다.")
        st.stop()

df = load_who_data(API_BASE)

# -----------------------------------
# 2) 국가 리스트 선택
# -----------------------------------
st.subheader("📋 국가 선택")

countries = df["SpatialDimension"].unique().tolist()
selected_countries = st.multiselect(
    "비만율을 확인할 국가를 선택하세요 (최대 10개 추천)",
    options=countries,
    default=["World", "United States of America", "India", "China"]
)

if not selected_countries:
    st.warning("⚠️ 하나 이상의 국가를 선택하세요.")
    st.stop()

filtered = df[df["SpatialDimension"].isin(selected_countries)]

# -----------------------------------
# 3) 데이터 정리
# -----------------------------------
# 필요한 열: 년도, 국가, 비만율 값
filtered = filtered.rename(
    columns={
        "TimeDimension": "Year",
        "Value": "ObesityRate"
    }
)

# -----------------------------------
# 4) 표로 보기
# -----------------------------------
st.subheader("📊 국가별 비만율 데이터 테이블")
st.dataframe(filtered[["Year", "SpatialDimension", "ObesityRate"]], use_container_width=True)

# -----------------------------------
# 5) 시계열 그래프
# -----------------------------------
st.subheader("📈 국가별 비만율 추이")

fig = px.line(
    filtered,
    x="Year",
    y="ObesityRate",
    color="SpatialDimension",
    markers=True,
    labels={"ObesityRate": "비만율 (%)"},
    title="WHO 성인 비만율 (BMI ≥ 30) 국가별 변화"
)
st.plotly_chart(fig, use_container_width=True)

# -----------------------------------
# 6) 간단 요약
# -----------------------------------
st.markdown("""
### 📌 참고
- 이 데이터는 **성인(18세 이상) 비만율(BMI ≥ 30)**의 연령 표준화 추정값입니다.  
- WHO GHO OData API를 통해 자동으로 데이터를 불러온 것이며, CSV 형식으로도 접근 가능합니다. :contentReference[oaicite:3]{index=3}
""")
