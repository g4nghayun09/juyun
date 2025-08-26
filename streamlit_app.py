# juyun/streamlit_app.py

import streamlit as st
import datetime
import random
import base64

# --- 페이지 설정 ---
# 페이지 제목, 아이콘, 레이아웃을 설정합니다.
# layout="centered"가 기본값이지만, 명시적으로 설정하여 가독성을 높일 수 있습니다.
st.set_page_config(
    page_title="오늘의 운세",
    page_icon="🔮",
    layout="centered",
)

# --- 신비로운 효과를 위한 CSS ---
# CSS를 사용하여 배경에 신비로운 보라색 별과 은하수 느낌의 그라데이션 효과를 추가합니다.
# 결과 카드를 꾸미는 스타일도 함께 정의합니다.
def add_mystical_effect():
    """결과가 표시될 때 신비로운 배경 효과를 추가하기 위한 함수"""
    # Base64로 인코딩된 CSS 스타일
    # 복잡한 스타일을 문자열로 관리하여 코드의 가독성을 높입니다.
    css = """
    <style>
    /* Streamlit 기본 배경을 오버라이드하여 그라데이션 배경 적용 */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right top, #6d327c, #485DA6, #00a1ba, #01b18e, #32b37b);
        background-size: cover; /* 배경 이미지가 전체를 덮도록 설정 */
    }

    /* 결과 텍스트를 담을 카드 스타일 */
    .result-card {
        background-color: rgba(255, 255, 255, 0.1); /* 반투명 흰색 배경 */
        border-radius: 15px; /* 둥근 모서리 */
        padding: 25px; /* 내부 여백 */
        margin-top: 20px; /* 위쪽 여백 */
        border: 1px solid rgba(255, 255, 255, 0.2); /* 은은한 테두리 */
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); /* 입체감을 위한 그림자 */
        backdrop-filter: blur(10px); /* 배경 블러 효과 */
        -webkit-backdrop-filter: blur(10px);
        text-align: center; /* 내부 텍스트 가운데 정렬 */
    }

    /* 이모지 스타일 */
    .result-emoji {
        font-size: 5rem; /* 이모지 크기를 키움 */
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.7); /* 이모지에 빛나는 효과 추가 */
    }

    /* 운세 텍스트 스타일 */
    .result-text {
        font-size: 1.2rem; /* 텍스트 크기 조정 */
        color: white; /* 텍스트 색상을 흰색으로 */
        font-weight: bold; /* 텍스트 굵게 */
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# --- 운세 결과 생성 ---
# 실제 운세 사이트를 스크래핑하는 것은 불안정하고 해당 사이트의 정책에 위배될 수 있습니다.
# 따라서, 안정적인 앱 동작을 위해 미리 준비된 운세 결과를 무작위로 보여주는 방식을 사용합니다.
def get_random_fortune():
    """사용자에게 보여줄 무작위 운세 결과를 생성하는 함수"""
    fortunes = {
        "😻 좋은 운세": [
            "오늘은 새로운 시작을 하기에 더없이 좋은 날입니다. 망설이지 마세요!",
            "뜻밖의 행운이 찾아올 예감이 드네요. 주변을 잘 살펴보세요.",
            "귀인이 나타나 당신을 도울 것입니다. 긍정적인 마음을 유지하세요.",
            "노력의 결실을 볼 수 있는 하루입니다. 자신감을 가지세요.",
        ],
        "😼 중간 운세": [
            "평범하지만 소소한 행복이 가득한 하루가 될 것입니다.",
            "현상 유지를 하는 것에 집중하면 좋은 결과가 있을 것입니다.",
            "작은 실수는 있을 수 있지만, 크게 문제 되지는 않을 것입니다.",
            "차분하게 하루를 보내며 내일을 계획하기 좋은 날입니다.",
        ],
        "😿 아쉬운 운세": [
            "오늘은 조금 쉬어가는 것이 좋겠습니다. 무리하지 마세요.",
            "예상치 못한 지출이 생길 수 있으니, 신중한 소비가 필요합니다.",
            "오해가 생길 수 있으니, 말과 행동에 주의를 기울여야 합니다.",
            "계획에 차질이 생길 수 있지만, 유연하게 대처하면 극복할 수 있습니다.",
        ],
    }
    # 운세 종류(좋음, 중간, 아쉬움)를 무작위로 선택
    fortune_type = random.choice(list(fortunes.keys()))
    # 선택된 종류에 해당하는 운세 메시지 중 하나를 무작위로 선택
    message = random.choice(fortunes[fortune_type])
    return fortune_type, message

# --- 메인 앱 로직 ---

# 앱 제목 표시
st.title("🔮 오늘의 운세는?")

# 사용자 입력을 받기 위한 폼(Form) 생성
# '결과 확인하기' 버튼을 누르기 전까지는 앱이 재실행되지 않아 사용자 경험이 향상됩니다.
with st.form("fortune_form"):
    # 입력 필드 배치
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("성별", ("남성", "여성"), horizontal=True)
    with col2:
        # 날짜 입력 필드, 기본값은 오늘 날짜
        today = datetime.date.today()
        birth_date = st.date_input("생년월일 (양력)", value=today, min_value=datetime.date(1930, 1, 1), max_value=today)

    # 폼 제출 버튼
    submitted = st.form_submit_button("결과 확인하기 ✨")

# '결과 확인하기' 버튼이 눌렸을 때 로직 실행
if submitted:
    # 세션 상태(Session State)를 사용하여 운세 결과를 저장합니다.
    # 이렇게 하면 사용자가 다른 행동을 해도 결과가 사라지지 않습니다.
    st.session_state.fortune_type, st.session_state.message = get_random_fortune()

# 세션 상태에 운세 결과가 저장되어 있는 경우 화면에 표시
if 'fortune_type' in st.session_state:
    # 신비로운 CSS 효과 적용
    add_mystical_effect()

    # 이모지와 운세 종류 추출
    emoji = st.session_state.fortune_type.split()[0]
    fortune_title = st.session_state.fortune_type.split()[1]

    # 결과 카드를 HTML로 렌더링
    st.markdown(
        f"""
        <div class="result-card">
            <p class="result-emoji">{emoji}</p>
            <p class="result-text">{st.session_state.message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("") # 여백 추가

    # 정보 공유하기 버튼
    # Streamlit에서 직접 클립보드 복사 기능은 구현이 복잡하므로,
    # 사용자에게 URL 복사를 안내하는 것이 가장 간단하고 안정적인 방법입니다.
    st.info("💡 이 결과를 친구와 공유하고 싶으신가요? 브라우저의 주소창을 복사하여 공유해주세요!")