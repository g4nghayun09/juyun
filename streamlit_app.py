# streamlit_app.py

import streamlit as st
import datetime
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="오늘의 운세",
    page_icon="🔮",
    layout="centered"
)

# --- 운세 데이터 ---
fortunes = {
    "😻 좋은 운세": [
        "오늘은 새로운 시작을 하기에 좋은 날입니다!",
        "뜻밖의 행운이 찾아올 예감이 드네요.",
        "귀인이 나타나 당신을 도울 것입니다.",
        "노력의 결실을 볼 수 있는 하루입니다."
    ],
    "😼 중간 운세": [
        "평범하지만 소소한 행복이 있는 하루입니다.",
        "현상 유지를 하면 좋은 결과가 있을 것입니다.",
        "작은 실수는 있을 수 있지만 크게 문제 되지 않습니다.",
        "차분하게 하루를 보내며 내일을 계획하기 좋습니다."
    ],
    "😿 아쉬운 운세": [
        "오늘은 조금 쉬어가는 게 좋겠습니다.",
        "예상치 못한 지출이 생길 수 있으니 신중하세요.",
        "오해가 생길 수 있으니 말과 행동에 주의하세요.",
        "계획에 차질이 생길 수 있지만 유연하게 대처하면 됩니다."
    ]
}

# --- 운세 생성 함수 ---
def get_fortune():
    key = random.choice(list(fortunes.keys()))
    msg = random.choice(fortunes[key])
    return key, msg

# --- 앱 UI ---
st.title("🔮 오늘의 운세")

# 사용자 입력
with st.form("fortune_form"):
    gender = st.radio("성별", ("남성", "여성"), horizontal=True)
    birth_date = st.date_input(
        "생년월일 (양력)",
        value=datetime.date.today(),
        min_value=datetime.date(1930, 1, 1),
        max_value=datetime.date.today()
    )
    submitted = st.form_submit_button("결과 확인하기 ✨")

# 운세 결과
if submitted:
    emoji, message = get_fortune()
    st.markdown(
        f"""
        <div style="
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            color: white;
            font-weight: bold;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        ">
            <p style="font-size:5rem; text-shadow:0 0 15px rgba(255,255,255,0.7);">{emoji}</p>
            <p style="font-size:1.2rem;">{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.info("💡 이 결과를 친구와 공유하고 싶으면 브라우저 주소창을 복사하세요!")
