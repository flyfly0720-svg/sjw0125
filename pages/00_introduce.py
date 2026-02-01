import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자기소개",
    page_icon="👋",
    layout="centered"
)

st.title("👋 안녕하세요!")
st.subheader("반갑습니다.")


import streamlit as st

st.subheader("저는 서재원입니다.🐾")

small_cute_dog_url = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d"

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.image(small_cute_dog_url, width=180)






# 자기소개 텍스트
st.markdown(
    """
    ### 🙋‍♂️ 간단한 인사
    
    안녕하세요!  
    저는 **Streamlit으로 저희 첫 웹 앱을 만들어 보았습니다.**입니다.  
    이 페이지는 ** 간단한 저의 소개와 인사말 **이에요.
    
    - 💻 관심 분야: 수학,물리,데이터 
    - 🚀 목표: 쉽고 재미있는 앱 만들기  
    - ☕ 취미: 유투브 보면서 코딩하기,유투브 시청하기,음악듣기
    """
)

st.write("---")
st.caption("© 2026 My Introduction App")
