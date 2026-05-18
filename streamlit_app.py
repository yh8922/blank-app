import streamlit as st

# 웹 페이지 제목 설정
st.title("짝수/홀수 판별기")

# 기존 코드: n = int(input())
# 스트림릿의 number_input을 사용해 자연수를 입력받습니다.
n = st.number_input("자연수 정숫값을 입력하세요:", min_value=1, step=1, value=1)

# 문제 조건에 맞추어 "even"과 "odd"로 출력하도록 유지 및 수정
if n % 2 == 0:
    # 기존 코드: print('짝수')
    st.write("even")
else:
    # 기존 코드: print('홀수')
    st.write("odd")