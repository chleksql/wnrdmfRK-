# main.py

questions = [
    {"question": "🌙 보통 몇 시에 잠자리에 드나요?", "options": ["9시 이전 ⏰", "10시~11시 🛏️", "12시 이후 🌛", "새벽까지 깨어있음 🌞"]},
    {"question": "🛌 하루 평균 수면 시간은?", "options": ["8시간 이상 🌟", "6~8시간 😊", "4~6시간 😓", "4시간 이하 😵"]},
    {"question": "🍔 주로 어떤 음식을 자주 먹나요?", "options": ["채소와 과일 중심 🥦🍎", "고기, 단백질 위주 🍗🥩", "가공식품, 인스턴트 많이 먹음 🍜🍟", "패스트푸드 자주 먹음 🍔🍕"]},
    {"question": "👯‍♂️ 친구들을 얼마나 자주 만나나요?", "options": ["매일 만남 😊", "일주일에 2~3번 🤗", "한 달에 한 번 정도 😐", "거의 못 만남 😔"]},
    {"question": "🏃‍♀️ 운동은 얼마나 자주 하나요?", "options": ["매일 🏅", "주 2~3회 💪", "가끔 🏃‍♂️", "거의 안 함 😴"]},
    {"question": "🚗 자동차나 오토바이를 얼마나 자주 운전하나요?", "options": ["거의 안 함 🚶‍♂️", "가끔 🚗", "자주 🚙", "매일 🏍️"]},
    {"question": "🏠 집이나 직장에서 안전장치가 잘 되어 있나요?", "options": ["완벽함 ✅", "대부분 있음 👍", "좀 부족함 ⚠️", "거의 없음 ❌"]},
    {"question": "😰 스트레스를 얼마나 자주 느끼나요?", "options": ["거의 안 느낌 😎", "가끔 느낌 😐", "자주 느낌 😵", "항상 느낌 😱"]},
    {"question": "💊 약물(처방약, 술, 담배 등 포함) 사용 빈도는?", "options": [
        "안 함 🙅‍♂️",
        "가끔 🍺🚬 (적당히)",
        "자주 🍷🚬 (즐기는 편)",
        "과다 복용 및 오남용 💉😵 (조심하세요!)"
    ]},
    {"question": "🧠 정신 건강 상태는 어떤가요?", "options": ["좋음 🙂", "보통 😐", "약간 불안/우울 😟", "심각한 불안/우울 😢"]},
]

def get_death_prediction(answers):
    risk_scores = {
        "심혈관 질환": 0,
        "암": 0,
        "교통사고": 0,
        "감염병": 0,
        "자살/정신건강": 0,
        "자연사": 0,
        "기타 사고": 0,
        "약물 과다복용": 0,
    }

    if answers[1] == "4시간 이하 😵" or answers[4] == "거의 안 함 😴":
        risk_scores["심혈관 질환"] += 3
    if answers[2] in ["가공식품, 인스턴트 많이 먹음 🍜🍟", "패스트푸드 자주 먹음 🍔🍕"]:
        risk_scores["암"] += 2
        risk_scores["심혈관 질환"] += 1
    if answers[3] == "거의 못 만남 😔":
        risk_scores["자살/정신건강"] += 2
    if answers[7] in ["자주 느낌 😵", "항상 느낌 😱"]:
        risk_scores["자살/정신건강"] += 2
    if answers[9] in ["약간 불안/우울 😟", "심각한 불안/우울 😢"]:
        risk_scores["자살/정신건강"] += 3
    if answers[5] in ["자주 🚙", "매일 🏍️"]:
        risk_scores["교통사고"] += 3
    if answers[6] in ["좀 부족함 ⚠️", "거의 없음 ❌"]:
        risk_scores["기타 사고"] += 2
    if answers[8] == "과다 복용 및 오남용 💉😵 (조심하세요!)":
        risk_scores["약물 과다복용"] += 4
        risk_scores["자살/정신건강"] += 2
    risk_scores["자연사"] += 1

    predicted = max(risk_scores, key=risk_scores.get)

    messages = {
        "심혈관 질환": "❤️‍🩹 수면 부족과 운동 부족 때문에 심장이 속상해하고 있어요! 지금부터라도 건강 챙기자구요!",
        "암": "🎗️ 패스트푸드와 인스턴트가 너무 좋아하는군요! 암이 '내가 너 좋아한다고?' 하고 속삭일지도 몰라요!",
        "교통사고": "🚦 자주 운전한다고요? 안전벨트 꼭! 그리고 헬멧도 잊지 마세요! 교통사고는 NO!",
        "감염병": "🦠 손 씻기와 마스크는 친구! 감염병을 멀리합시다~",
        "자살/정신건강": "🧠 스트레스, 외로움, 우울함... 너무 힘들면 꼭 주변에 손 내밀어요. 당신은 혼자가 아니에요!",
        "자연사": "🌿 평화롭게 자연사할 가능성이 가장 높네요. 앞으로도 건강한 삶을 응원합니다!",
        "기타 사고": "⚠️ 안전사고 조심! 화재, 낙상 등 조심하세요~ 집에서도 안전이 최고!",
        "약물 과다복용": "💉 약물 과다복용 위험! 몸은 소중하니까 꼭 조심하세요! 필요하면 전문가 상담도 강추!",
    }
    return messages[predicted]

def run_survey():
    print("💀💀💀 미래에 어떻게 죽을지 알아보는 재밌는 설문조사에 오신 것을 환영합니다! 💀💀💀")
    name = input("먼저, 당신의 이름을 알려주세요: ").strip()
    print(f"\n안녕하세요, {name}님! 이제 설문을 시작할게요. 하나씩 답해주세요! 😄\n")

    answers = []
    for idx, q in enumerate(questions):
        print(f"{idx + 1}. {q['question']}")
        for i, option in enumerate(q["options"], 1):
            print(f"  {i}. {option}")
        while True:
            try:
                choice = int(input("번호를 입력하세요: "))
                if 1 <= choice <= len(q["options"]):
                    answers.append(q["options"][choice - 1])
                    print()
                    break
                else:
                    print("😅 번호를 제대로 입력해 주세요!")
            except ValueError:
                print("😅 숫자만 입력해 주세요!")

    print("🩺 결과 분석 중... 잠시만 기다려 주세요!\n")
    result = get_death_prediction(answers)
    print(f"🩸 {name}님의 미래 사망 원인 예측은:")
    print(result)
    print("\n🙏 삼가 고인의 명복을 빕니다 🙏\n")
    print("💀💀💀 설문에 참여해 주셔서 감사합니다! 💀💀💀")

if __name__ == "__main__":
    run_survey()
