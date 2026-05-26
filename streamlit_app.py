import streamlit as st

# 1. 웹 앱 제목 설정
st.title("🔢 재미있는 구구단 프로그램")
st.subheader("원하는 단을 입력하면 구구단을 출력해 줍니다.")

# 서론과 구분선
st.markdown("---")

# 2. 사용자로부터 단의 수 입력받기 (기본값 2단, 범위 1단~19단)
d = st.number_input("출력하고 싶은 단의 수를 입력하세요:", min_value=1, max_value=19, value=2, step=1)

# 3. 버튼을 누르면 구구단이 출력되도록 설정
if st.button(f"{d}단 출력하기 🚀"):
    st.success(f"### 🎉 구구단 {d}단 결과")
    
    # 반복문을 돌며 웹 화면에 출력
    for i in range(1, 10):
        st.write(f"**{d} × {i} = {d * i}**")