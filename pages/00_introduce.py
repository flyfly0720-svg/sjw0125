import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자기소개",
    page_icon="👋",
    layout="centered"
)

st.title("👋 안녕하세요!")
st.subheader("저를 소개합니다")

st.write("---")

# 사진 업로드
uploaded_file = st.file_uploader(
    "프로필 사진을 업로드해주세요",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="프로필 사진", width=250)
else:
    st.info("사진을 업로드하면 여기에 표시됩니다 😊")

st.write("---")

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
