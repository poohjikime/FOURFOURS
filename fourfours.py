import streamlit as st
import math

st.title('포포즈(Fourfours) 게임')

st.write("4를 정확히 4번 사용하여 1부터 10까지의 숫자를 만드는 게임입니다.")
st.write("사칙연산(+, -, ×, ÷)과 괄호를 사용할 수 있습니다.")

target = st.number_input("만들고 싶은 숫자를 선택하세요 (1-10):", min_value=1, max_value=10, value=1)
user_input = st.text_input("수식을 입력하세요 (예: 4/4 × 4/4):")

if st.button("정답 확인"):
    if user_input:
        try:
            # × 기호를 *로 변환
            formula = user_input.replace('×', '*').replace('÷', '/')
            result = eval(formula)
            
            # 4가 정확히 4번 사용되었는지 확인
            four_count = user_input.count('4')
            
            if four_count == 4 and abs(result - target) < 0.0001:
                st.success(f"정답입니다! {user_input} = {result}")
                
                # 힌트 보여주기
                if st.button("다른 해답 보기"):
                    solutions = {
                        1: "4/4 × 4/4",
                        2: "4/4 + 4/4",
                        3: "(4 + 4 + 4)/4",
                        4: "4 × 4/4 × 1",
                        5: "(4 × 4 + 4)/4",
                        6: "(4 + 4 + 4)/2",
                        7: "4 + 4 - 4/4",
                        8: "4 + 4 + 4 - 4",
                        9: "4 + 4 + 4/4",
                        10: "4 × 4 - 4 - 4"
                    }
                    st.write(f"다른 가능한 해답: {solutions[target]}")
            
            elif four_count != 4:
                st.error("4를 정확히 4번 사용해야 합니다!")
            else:
                st.error(f"결과값({result})이 목표 숫자({target})와 다릅니다.")
                
        except:
            st.error("올바른 수식을 입력해주세요!")
    else:
        st.warning("수식을 입력해주세요!")

st.markdown("---")
st.write("규칙:")
st.write("1. 숫자 4를 정확히 4번 사용해야 합니다.")
st.write("2. 사칙연산(+, -, ×, ÷)과 괄호를 사용할 수 있습니다.")
st.write("3. 결과값이 목표 숫자와 정확히 일치해야 합니다.")
