import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자기소개",
    page_icon="👋",
    layout="centered"
)

st.title("👋 안녕하세요!")
st.subheader("저를 소개합니다")



import streamlit as st

st.title("귀여운 강아지 🐶💛")

cute_dog_url = "https://images.unsplash.com/photo-1517849845537-4d257902454a"

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(cute_dog_url, caption="너무 귀여운 강아지", width=350)





# 자기소개 텍스트
st.markdown(
    """
    ### 🙋‍♂️ 간단한 인사
    
    안녕하세요!  
    저는 **Streamlit으로 웹 앱을 만드는 것을 좋아하는 사람**입니다.  
    이 페이지는 **Streamlit.io에서 동작하는 자기소개 웹 앱**이에요.
    
    - 💻 관심 분야: 데이터, 웹 앱, 자동화  
    - 🚀 목표: 쉽고 재미있는 앱 만들기  
    - ☕ 취미: 커피 마시면서 코딩하기
    """
)

st.write("---")
st.caption("© 2026 My Introduction App")
