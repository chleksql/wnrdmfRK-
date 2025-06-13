import streamlit as st

questions = [
    {"q": "🌙 몇 시에 자나요?", "opts": ["9시 이전", "10~11시", "12시 이후", "새벽까지"]},
    {"q": "🛌 하루 수면 시간?", "opts": ["8시간 이상", "6~8시간", "4~6시간", "4시간 이하"]},
    {"q": "🍔 자주 먹는 음식?", "opts": ["채소/과일", "고기/단백질", "인스턴트", "패스트푸드"]},
    {"q": "👯‍♂️ 친구 자주 만나나요?", "opts": ["매일", "주 2~3회", "한 달 1회", "거의 못 만남"]},
    {"q": "🏃‍♀️ 운동 얼마나?", "opts": ["매일", "주 2~3회", "가끔", "거의 안 함"]},
    {"q": "😰 스트레스 빈도?", "opts": ["거의 없음", "가끔", "자주", "항상"]},
    {"q": "💊 약물 사용?", "opts": ["안 함", "가끔", "자주", "과다복용"]},
    {"q": "🧠 정신 상태?", "opts": ["좋음", "보통", "불안/우울", "심각"]},
    {"q": "🎉 도파민 즐기나요?", "opts": ["전혀 안 즐김", "가끔 즐김", "자주 즐김", "매우 자주 즐김"]},
]

def predict(answers):
    risk = {
        "심혈관": 0,
        "암": 0,
        "자연사": 1,
        "사고": 0,
        "약물": 0
    }

    if answers[1] == "4시간 이하" or answers[4] == "거의 안 함":
        risk["심혈관"] += 3
    if answers[2] in ["인스턴트", "패스트푸드"]:
        risk["암"] += 2
        risk["심혈관"] += 1
    if answers[5] in ["자주", "항상"]:
        risk["사고"] += 2
    if answers[7] in ["불안/우울", "심각"]:
        risk["사고"] += 1
    if answers[6] == "과다복용":
        risk["약물"] += 4
    if answers[8] in ["자주 즐김", "매우 자주 즐김"]:
        risk["약물"] += 1

    key = max(risk, key=risk.get)
    msgs = {
        "심혈관": "❤️‍🩹 심장 건강 조심! 운동과 수면을 챙기세요!",
        "암": "🎗️ 식습관 주의! 건강한 음식으로 바꿔봐요!",
        "자연사": "🌿 평화로운 자연사 가능성이 높아요!",
        "사고": "⚠️ 안전에 신경 쓰세요! 집에서도 조심!",
        "약물": "💉 약물 과다복용 위험! 전문가 상담 추천해요!",
    }
    return msgs[key]

def main():
    st.title("💀 미래 죽음 예측 설문 💀")
    
    if "step" not in st.session_state:
        st.session_state.step = 0
        st.session_state.answers = []
        st.session_state.name = ""

    if st.session_state.step == 0:
        name = st.text_input("이름을 알려주세요:")
        if st.button("시작"):
            if name.strip() == "":
                st.warning("이름을 입력해주세요!")
            else:
                st.session_state.name = name.strip()
                st.session_state.step = 1

    elif 1 <= st.session_state.step <= len(questions):
        idx = st.session_state.step - 1
        q = questions[idx]
        st.write(f"**{st.session_state.step}. {q['q']}**")
        choice = st.radio("선택하세요:", q["opts"], key=idx)

        if st.button("다음"):
            st.session_state.answers.append(choice)
            st.session_state.step += 1

    else:
        st.header(f"{st.session_state.name}님의 미래 사망 원인 예측 결과")
        result = predict(st.session_state.answers)
        st.markdown(f"### {result}")
        st.markdown("🙏 **삼가 고인의 명복을 빕니다** 🙏")
        
        if st.button("다시하기"):
            st.session_state.step = 0
            st.session_state.answers = []
            st.session_state.name = ""

if __name__ == "__main__":
    main()
