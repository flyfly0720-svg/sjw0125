import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자기소개",
    page_icon="🐶",
    layout="centered"
)

# 제목
st.title("🐶 안녕하세요!")

# 폼폼프린 이미지 표시
st.image(
    "pompomurin.jpg",
    caption="폼폼프린과 함께하는 자기소개 💛",
    use_container_width=True
)

# 간단한 인사말
st.subheader("반가워요!")
st.write(
    """
    저는 **폼폼프린을 좋아하는 개발자**입니다 ☁️  
    Streamlit으로 간단하고 예쁜 웹 앱 만드는 걸 즐겨요.
    """
)

# 구분선
st.divider()

# 추가 자기소개
st.markdown(
    """
    ### ✨ About Me
    - 🐾 귀여운 캐릭터 좋아함  
    - 💻 Python & Streamlit  
    - ☕ 커피 없으면 코딩 불가  

    앞으로 잘 부탁드려요!
    """
)
