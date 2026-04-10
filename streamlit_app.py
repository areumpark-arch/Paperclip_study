import streamlit as st

st.set_page_config(
    page_title="AI 직원 회사 만들기",
    page_icon="📎",
    layout="centered",
)

# ─── CSS ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');
html, body, [class*="st-"] { font-family: 'Noto Sans KR', sans-serif; }
.block-container { max-width: 720px; padding-top: 2rem; }
h1, h2, h3 { font-family: 'Noto Sans KR', sans-serif !important; }

.story-box {
    background: #fff; border: 1.5px solid #e5e2db; border-radius: 14px;
    padding: 24px; margin: 12px 0; position: relative; overflow: hidden;
}
.story-box::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
}
.story-box.orange::before { background: #e8590c; }
.story-box.green::before { background: #2b8a3e; }
.story-box.blue::before { background: #1971c2; }
.story-box.purple::before { background: #7048e8; }
.story-box.yellow::before { background: #e67700; }
.story-box.red::before { background: #c92a2a; }

.analogy {
    background: #fef3e2; border: 1.5px solid #f5d9a8; border-radius: 14px;
    padding: 20px 22px; margin: 12px 0;
}
.analogy-label { font-size: 12px; font-weight: 700; color: #e67700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
.analogy p { color: #7a5c1f; margin: 0; }

.tip-box {
    background: #e6fcf5; border-left: 4px solid #2b8a3e;
    padding: 14px 18px; border-radius: 0 10px 10px 0; margin: 12px 0;
    color: #1b5e20; font-size: 15px;
}
.warn-box {
    background: #fff3f3; border-left: 4px solid #c92a2a;
    padding: 14px 18px; border-radius: 0 10px 10px 0; margin: 12px 0;
    color: #922; font-size: 15px;
}

.org-chart {
    display: flex; flex-direction: column; align-items: center; margin: 20px 0; gap: 0;
}
.org-node {
    padding: 10px 18px; border-radius: 10px; font-size: 14px; font-weight: 600;
    text-align: center; min-width: 80px; display: inline-block;
}
.org-line { width: 2px; height: 16px; background: #e5e2db; margin: 0 auto; }
.org-row { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
.org-branch { width: 50%; height: 2px; background: #e5e2db; margin: 0 auto; }

.vs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 12px 0; }
.vs-card { background: #f3f1ed; border-radius: 12px; padding: 18px; font-size: 14px; }
@media (max-width: 500px) { .vs-grid { grid-template-columns: 1fr; } }

.step-item { position: relative; padding-left: 44px; margin-bottom: 24px; }
.step-num {
    position: absolute; left: 0; top: 2px; width: 32px; height: 32px;
    border-radius: 50%; background: #e8590c; color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ─── STATE ───
if "page" not in st.session_state:
    st.session_state.page = 0

PAGES = [
    "🏠 시작",
    "1️⃣ AI가 뭔데?",
    "2️⃣ Paperclip이 뭔데?",
    "3️⃣ 회사 구조",
    "4️⃣ 시작 방법",
    "5️⃣ 직접 해보기",
    "6️⃣ 활용 사례",
    "7️⃣ 문제 해결",
]

# ─── SIDEBAR ───
with st.sidebar:
    st.markdown("### 📎 학습 메뉴")
    for i, name in enumerate(PAGES):
        if st.button(name, key=f"nav_{i}", use_container_width=True,
                     type="primary" if st.session_state.page == i else "secondary"):
            st.session_state.page = i
            st.rerun()
    st.divider()
    progress = st.session_state.page / (len(PAGES) - 1) if len(PAGES) > 1 else 0
    st.progress(progress)
    st.caption(f"진행률: {int(progress * 100)}%")


def nav_buttons():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.session_state.page > 0:
            if st.button("← 이전", use_container_width=True):
                st.session_state.page -= 1
                st.rerun()
    with col3:
        if st.session_state.page < len(PAGES) - 1:
            if st.button("다음 →", use_container_width=True, type="primary"):
                st.session_state.page += 1
                st.rerun()


def box(content, color="orange"):
    st.markdown(f'<div class="story-box {color}">{content}</div>', unsafe_allow_html=True)

def analogy(content):
    st.markdown(f'<div class="analogy"><div class="analogy-label">🍔 비유로 이해하기</div>{content}</div>', unsafe_allow_html=True)

def tip(content):
    st.markdown(f'<div class="tip-box">{content}</div>', unsafe_allow_html=True)

def warn(content):
    st.markdown(f'<div class="warn-box">{content}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════
# PAGE 0: 시작
# ═══════════════════════════════════════
if st.session_state.page == 0:
    st.markdown("<div style='text-align:center;font-size:64px;margin-top:20px;'>🏢🤖</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;line-height:1.35;'>AI한테 일을 시키는<br><span style=\"color:#e8590c;\">나만의 회사</span> 만들기</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#6b6560;font-size:16px;'>컴퓨터 잘 모르셔도 됩니다.<br>\"AI 직원\"을 뽑고, 팀을 짜고, 일을 맡기는 법을<br>처음부터 차근차근 알려드립니다.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#6b6560;font-size:13px;margin-top:8px;'>총 7단계 · 어려운 말 없음 · 천천히 따라오세요</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("시작하기 →", use_container_width=True, type="primary"):
            st.session_state.page = 1
            st.rerun()


# ═══════════════════════════════════════
# PAGE 1: AI가 뭔데?
# ═══════════════════════════════════════
elif st.session_state.page == 1:
    st.markdown("#### 1단계")
    st.markdown("## AI가 뭔데?")
    st.caption("제일 기초부터 시작합니다")

    box("""
    <h3>🗣️ 우리가 아는 AI</h3>
    <p>ChatGPT나 Claude 같은 거요.<br>
    "서울 맛집 알려줘"라고 물어보면 대답해주죠.<br><br>
    이건 마치 <strong>편의점 직원에게 물건 위치 묻는 것</strong>과 비슷합니다.<br>
    물어보면 대답하고, 끝. 다음에 또 물어봐야 합니다.</p>
    """, "orange")

    box("""
    <h3>🤖 AI "에이전트"는 뭐가 달라?</h3>
    <p>에이전트는 <strong>내가 고용한 직원</strong>에 가깝습니다.</p>
    <ul style="list-style:none;padding:0;">
    <li style="padding:4px 0 4px 20px;position:relative;color:#6b6560;"><span style="position:absolute;left:0;color:#e8590c;font-weight:900;">•</span>"보고서 만들어줘"라고 하면 → 자료 찾고 → 정리하고 → 파일로 저장까지 혼자 함</li>
    <li style="padding:4px 0 4px 20px;position:relative;color:#6b6560;"><span style="position:absolute;left:0;color:#e8590c;font-weight:900;">•</span>한 번에 여러 단계를 <strong>순서대로</strong> 알아서 처리함</li>
    <li style="padding:4px 0 4px 20px;position:relative;color:#6b6560;"><span style="position:absolute;left:0;color:#e8590c;font-weight:900;">•</span>심지어 다른 AI 직원에게 "너는 이거 해"라고 일을 넘기기도 함</li>
    </ul>
    """, "green")

    analogy("""
    <p><strong>일반 AI</strong> = 식당에서 주문하는 것. 내가 매번 시켜야 함.<br>
    <strong>AI 에이전트</strong> = 집에 요리사를 고용한 것. "저녁 해주세요"만 하면 장보기부터 설거지까지 알아서 함.</p>
    """)

    st.markdown("---")
    st.markdown("##### 🧐 이해했는지 확인!")
    q1 = st.radio("AI 에이전트의 가장 큰 특징은?", [
        "더 빠르게 대답한다",
        "목표를 주면 여러 단계를 스스로 처리한다",
        "사람 말을 더 잘 알아듣는다",
    ], index=None, key="q1")
    if q1:
        if q1 == "목표를 주면 여러 단계를 스스로 처리한다":
            st.success("맞아요! 핵심은 '더 똑똑해서'가 아니라, **목표를 받으면 계획→실행→결과까지 혼자 해낸다**는 것입니다.")
        else:
            st.error("아쉽! 정답은 **'목표를 주면 여러 단계를 스스로 처리한다'**입니다. 에이전트의 핵심은 스스로 계획하고 실행하는 능력이에요.")

    st.divider()
    nav_buttons()


# ═══════════════════════════════════════
# PAGE 2: Paperclip이 뭔데?
# ═══════════════════════════════════════
elif st.session_state.page == 2:
    st.markdown("#### 2단계")
    st.markdown("## Paperclip이 뭔데?")
    st.caption("AI 직원들을 관리하는 프로그램이에요")

    box("""
    <h3>📎 딱 한 문장으로</h3>
    <p style="font-size:17px;"><strong>Paperclip = AI 직원들을 팀으로 묶어서, 일을 시키고, 관리하는 도구</strong></p>
    """, "blue")

    analogy("""
    <p>직원이 1명이면 카톡으로 일 시키면 돼요.<br>
    근데 직원이 5명이면? <strong>누가 뭘 하는지, 돈은 얼마나 쓰는지, 보고는 어떻게 받는지</strong> 관리가 필요하죠.<br><br>
    Paperclip이 바로 그 <strong>관리 시스템</strong>입니다.</p>
    """)

    box("""
    <h3>👤 나는 뭘 하면 돼?</h3>
    <p>당신의 역할 = <strong>"사장님 위의 사장님"</strong> (이사회 의장)<br><br>
    직접 일하는 게 아니라, 큰 결정만 합니다:</p>
    <ul style="list-style:none;padding:0;">
    <li style="padding:4px 0 4px 20px;position:relative;color:#6b6560;"><span style="position:absolute;left:0;color:#e8590c;font-weight:900;">•</span>"이 직원 뽑아도 되나요?" → 내가 OK / NO</li>
    <li style="padding:4px 0 4px 20px;position:relative;color:#6b6560;"><span style="position:absolute;left:0;color:#e8590c;font-weight:900;">•</span>"이 방향으로 일할까요?" → 내가 OK / NO</li>
    <li style="padding:4px 0 4px 20px;position:relative;color:#6b6560;"><span style="position:absolute;left:0;color:#e8590c;font-weight:900;">•</span>"돈 다 썼는데요?" → 내가 더 줄지 말지 결정</li>
    </ul>
    <p style="margin-top:10px;">AI가 멋대로 하는 게 <strong>절대 아닙니다</strong>. 중요한 결정은 항상 내 승인이 필요합니다.</p>
    """, "orange")

    box("""
    <h3>💵 가격은?</h3>
    <p><strong>Paperclip 자체는 무료</strong>예요.<br><br>
    돈이 드는 건 AI 직원의 "두뇌 사용료"입니다.<br>
    AI 직원이 생각하고 일할 때마다 아주 조금씩 비용이 나갑니다.<br>
    (핸드폰 데이터처럼, 쓴 만큼만 나가요)<br><br>
    처음 시작하면 보통 월 1~2만 원 수준입니다.<br>
    <strong>한도를 정해두면 그 이상은 절대 안 나갑니다.</strong></p>
    """, "green")

    st.markdown("---")
    st.markdown("##### 🧐 확인 문제")
    q2 = st.radio("Paperclip은 어떤 도구인가요?", [
        "AI를 만드는 도구",
        "채팅하는 도구",
        "AI 직원들을 팀으로 관리하는 도구",
    ], index=None, key="q2")
    if q2:
        if q2 == "AI 직원들을 팀으로 관리하는 도구":
            st.success("맞습니다! Paperclip은 AI를 '만드는' 게 아니라, 이미 있는 AI(Claude, GPT 등)를 **팀처럼 조직해서 관리**하는 도구입니다.")
        else:
            st.error("아쉽! 정답은 **'AI 직원들을 팀으로 관리하는 도구'**입니다.")

    st.divider()
    nav_buttons()


# ═══════════════════════════════════════
# PAGE 3: 회사 구조
# ═══════════════════════════════════════
elif st.session_state.page == 3:
    st.markdown("#### 3단계")
    st.markdown("## AI 회사는 이렇게 생겼어요")
    st.caption("진짜 회사 조직도와 비슷합니다")

    st.markdown("""
    <div class="org-chart">
        <div class="org-node" style="background:#fef3e2;color:#e67700;border:1.5px solid #f5d9a8;">👤 나 (최종 결정권자)</div>
        <div class="org-line"></div>
        <div class="org-node" style="background:#fff3e0;color:#e8590c;border:1.5px solid #fdd;font-size:15px;">🤖 CEO (총괄 매니저)</div>
        <div class="org-line"></div>
        <div class="org-branch"></div>
        <div class="org-row">
            <div class="org-node" style="background:#e6fcf5;color:#2b8a3e;border:1.5px solid #c3fae8;">📝 작가</div>
            <div class="org-node" style="background:#e7f5ff;color:#1971c2;border:1.5px solid #a5d8ff;">🔍 조사원</div>
            <div class="org-node" style="background:#f3f0ff;color:#7048e8;border:1.5px solid #d0bfff;">🎨 디자이너</div>
        </div>
    </div>
    <p style="text-align:center;font-size:14px;color:#6b6560;margin-top:12px;">내가 CEO에게 방향을 말하면 → CEO가 아래 직원들에게 일을 나눠줍니다</p>
    """, unsafe_allow_html=True)

    st.markdown("### 🧱 알아야 할 단어 5개")
    st.caption("이것만 알면 됩니다")

    data = {
        "단어": ["회사 (Company)", "에이전트 (Agent)", "프로젝트 (Project)", "태스크 (Task)", "하트비트 (Heartbeat)"],
        "쉬운 뜻": [
            '제일 큰 틀. "우리 팀이 뭘 하는 곳인지" 정하는 것',
            "AI 직원 1명",
            "큰 목표 하나",
            "작은 할 일 하나",
            'AI 직원의 "출근 알람". 정해진 시간에 깨어남',
        ],
        "예시": ['"블로그 운영팀"', "CEO, 작가, 조사원", '"4월 블로그 3편 완성"', '"AI 트렌드 자료 수집"', "매일 오전 9시"],
    }
    st.table(data)

    box("""
    <h3>💰 돈 이야기 (제일 중요!)</h3>
    <p>AI 직원이 일할 때마다 <strong>아주 소량의 비용</strong>이 나갑니다.</p>
    """, "red")

    analogy("""
    <p>핸드폰 데이터처럼 생각하세요.<br>
    쓴 만큼 돈이 나가고, <strong>한도를 정해놓으면 그 이상은 안 나갑니다</strong>.<br>
    Paperclip에서 직원별로 "이번 달 최대 ○○원"을 설정할 수 있습니다.</p>
    """)

    warn("""⚠️ <strong>한도 설정 안 하면 위험합니다.</strong><br>
    AI 직원이 밤새 혼자 일하면서 돈을 계속 쓸 수 있어요.<br>
    <strong>반드시 직원별 월 한도를 설정하세요.</strong>""")

    st.divider()
    nav_buttons()


# ═══════════════════════════════════════
# PAGE 4: 시작 방법
# ═══════════════════════════════════════
elif st.session_state.page == 4:
    st.markdown("#### 4단계")
    st.markdown("## 어떻게 시작하나요?")
    st.caption("방법은 2가지인데, 쉬운 걸로 갑시다")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="vs-card" style="border:2px solid #2b8a3e;border-radius:12px;background:#fff;padding:18px;">
        <h4 style="color:#2b8a3e;">✅ 쉬운 방법 (이걸로!)</h4>
        <p style="color:#6b6560;font-size:14px;">
        <strong>paperclip.inc</strong> 웹사이트 이용<br><br>
        인터넷만 되면 OK.<br>설치할 것 없음.<br>무료로 시작 가능.<br><br>
        <strong>이 수업은 이 방법 기준입니다</strong></p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="vs-card" style="border:1px solid #e5e2db;border-radius:12px;background:#f3f1ed;padding:18px;">
        <h4 style="color:#6b6560;">🔧 어려운 방법 (개발자용)</h4>
        <p style="color:#6b6560;font-size:14px;">
        내 컴퓨터에 직접 설치<br><br>
        프로그래밍 지식 필요.<br>완전 무료지만 복잡함.<br><br>
        <span style="color:#c92a2a;">→ 우리는 무시합니다</span></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔑 시작 전 준비물")
    st.markdown("**딱 2가지**만 있으면 됩니다.")

    st.markdown("**① 이메일 계정** — 가입할 때 쓸 이메일. 이미 있는 거 쓰면 됩니다.")

    st.markdown("**② AI 서비스 열쇠 (API 키)**")
    analogy("""
    <p>넷플릭스 보려면 로그인 계정이 필요하죠?<br>
    AI를 쓸 때도 비슷한 "통행증"이 필요해요. 그걸 API 키라고 부릅니다.<br><br>
    어디서 만드나요?<br>
    → <a href="https://console.anthropic.com" style="color:#e8590c;">console.anthropic.com</a> (Claude 만든 회사)<br>
    → <a href="https://platform.openai.com" style="color:#e8590c;">platform.openai.com</a> (ChatGPT 만든 회사)<br><br>
    가입하면 소액의 무료 크레딧을 줘서, 처음엔 돈 안 들어요.</p>
    """)

    warn("""⚠️ 이 API 키는 <strong>비밀번호와 같습니다</strong>.<br>
    남에게 알려주면 그 사람이 내 돈으로 AI를 쓸 수 있어요. 절대 공유하지 마세요.""")

    st.divider()
    nav_buttons()


# ═══════════════════════════════════════
# PAGE 5: 직접 해보기
# ═══════════════════════════════════════
elif st.session_state.page == 5:
    st.markdown("#### 5단계")
    st.markdown("## 직접 해봅시다!")
    st.caption("화면 보면서 하나씩 따라하세요")

    steps = [
        ("1", "가입하기", '<a href="https://paperclip.inc" style="color:#e8590c;">paperclip.inc</a>에 들어가서 회원가입. 이메일, 비밀번호만 있으면 됩니다.'),
        ("2", "회사 만들기", '"Create Company" 버튼 누르기.<br><strong>회사 이름:</strong> 아무거나 (예: "내 블로그팀")<br><strong>미션:</strong> "주 2회 AI 관련 블로그 글을 쓴다"'),
        ("3", "CEO 뽑기", '"CEO를 뽑을까요?" → <strong>Approve(승인)</strong> 누르기.<br>CEO = 다른 직원들한테 일 나눠주는 팀장'),
        ("4", "직원 1명 더 뽑기", 'CEO가 제안하는 직원 1명을 승인하세요.'),
        ("5", "돈 한도 정하기", '각 직원의 월 최대 비용을 설정합니다.'),
        ("6", "첫 번째 일 시키기", '목표(Goal)를 입력하세요. CEO가 작은 일로 쪼개서 배정합니다.'),
        ("7", "결과 확인하기", '대시보드에서 진행 상황, 비용, 결과물을 확인하세요.'),
    ]

    for num, title, desc in steps:
        st.markdown(f"""
        <div class="step-item">
            <div class="step-num">{num}</div>
            <h4 style="font-size:16px;font-weight:700;margin-bottom:4px;">{title}</h4>
            <p style="font-size:14.5px;color:#6b6560;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    warn("""⚠️ <strong>처음에는 CEO + 1명만!</strong><br>
    한꺼번에 5명 뽑으면 관리가 어렵고 돈도 많이 나갑니다. 1명씩 늘리세요.""")

    st.markdown("### 💵 초보자 추천 예산")
    budget = {
        "직원": ["CEO", "작가/조사원"],
        "한 달 한도": ["$5", "$10"],
        "한국 돈 대략": ["약 7,000원", "약 14,000원"],
    }
    st.table(budget)
    st.caption("부족하면 나중에 올리면 됩니다. 처음엔 적게!")

    st.markdown("### 좋은 목표 vs 나쁜 목표")
    col1, col2 = st.columns(2)
    with col1:
        st.success('👍 "AI 트렌드에 대한 800자 블로그 글 1개를 작성해"\n\n→ 뭘, 얼마나 해야 하는지 명확')
    with col2:
        st.error('👎 "마케팅 알아서 해"\n\n→ 뭘 해야 하는지 모르니까 헤맴')

    tip("""🎉 여기까지 하면 AI 회사가 돌아가고 있는 겁니다!<br>
    처음에는 결과물이 완벽하지 않을 수 있어요. 그게 정상입니다.""")

    st.divider()
    nav_buttons()


# ═══════════════════════════════════════
# PAGE 6: 활용 사례
# ═══════════════════════════════════════
elif st.session_state.page == 6:
    st.markdown("#### 6단계")
    st.markdown("## 이런 일에 써보세요")
    st.caption("사람들이 실제로 쓰는 방식 3가지")

    with st.expander("📝 사례 1: 블로그 팀", expanded=True):
        st.markdown('"혼자 블로그 쓰기 힘든데, AI 팀이 도와주면 좋겠다"')
        st.table({
            "AI 직원": ["🤖 CEO", "🔍 조사원", "📝 작가"],
            "하는 일": ["주제 정하기, 일정 관리, 글 검사", "자료를 인터넷에서 찾아 정리", "자료 바탕으로 글 초안 쓰기"],
        })
        st.caption("내가 하는 일: 주제 승인 → 글 읽어보기 → 수정 지시 → 최종 게시는 내가 직접")

    with st.expander("🔬 사례 2: 경쟁사 조사"):
        st.markdown('"경쟁사가 뭘 하는지 알고 싶은데 시간이 없다"')
        st.table({
            "AI 직원": ["🤖 CEO", "🔍 조사원 A", "🔍 조사원 B"],
            "하는 일": ["조사 범위 정하기, 보고서 정리", "경쟁사 제품/가격 정보 수집", "업계 뉴스, 트렌드 자료 수집"],
        })

    with st.expander("🌐 사례 3: 간단한 웹페이지"):
        st.markdown('"회사 소개 페이지가 필요한데 개발자는 없다"')
        st.table({
            "AI 직원": ["🤖 CEO", "💻 개발자", "📝 작가"],
            "하는 일": ["페이지 구성 잡기, 전체 감독", "실제 웹페이지 만들기", "페이지에 들어갈 글 쓰기"],
        })

    tip("""💡 <strong>핵심 원칙:</strong> 작게 시작하세요.<br>
    CEO + 직원 1명으로 첫 프로젝트를 끝내보고, 그 다음에 1명씩 추가하세요.""")

    st.divider()
    nav_buttons()


# ═══════════════════════════════════════
# PAGE 7: 문제 해결
# ═══════════════════════════════════════
elif st.session_state.page == 7:
    st.markdown("#### 7단계")
    st.markdown("## 문제가 생기면?")
    st.caption("자주 겪는 상황 4가지와 해결법")

    with st.expander("💸 돈이 생각보다 많이 나왔어요", expanded=True):
        st.markdown("""
        **왜 그럴까:** AI 직원이 같은 일을 반복했거나, 쓸데없이 긴 작업을 한 경우

        **해결법:**
        - 직원별 월 한도를 꼭 설정 (다 쓰면 자동 정지)
        - 대시보드에서 비용을 자주 확인
        - 처음엔 $5 이하로 시작
        """)

    with st.expander("🔄 같은 일을 자꾸 반복해요"):
        st.markdown("""
        **왜 그럴까:** 목표가 모호해서 "언제 끝나는지"를 모르는 거예요

        **해결법:** 끝나는 조건을 확실히 적어주세요
        - ❌ "좋은 글 써" → 언제 끝나는지 모름
        - ✅ "800자 분량 글 1개를 작성해서 저장해" → 명확
        """)

    with st.expander("📉 결과물이 별로예요"):
        st.markdown("""
        **왜 그럴까:** 한 직원에게 너무 많은 종류의 일을 시킨 경우

        **해결법:** 한 직원에게 한 가지만 시키세요
        - ❌ "자료 조사하고, 글도 쓰고, 그림도 만들어" → 다 어중간
        - ✅ "자료 조사만 해" → 훨씬 나은 결과
        """)

    with st.expander("🔇 직원이 아무것도 안 해요"):
        st.markdown("""
        **확인 순서:**
        1. 돈 한도를 다 써서 멈춘 건 아닌지 확인
        2. 출근 알람(하트비트)이 설정돼 있는지 확인
        3. 앞 단계 일이 아직 안 끝나서 기다리는 중일 수 있음
        """)

    st.markdown("---")
    st.markdown("### 🎓 수고하셨습니다!")
    st.markdown("""
    여기까지 읽으셨으면 이제 이런 걸 아시게 된 겁니다:
    - ✅ AI 에이전트가 뭔지
    - ✅ Paperclip이 뭘 하는 도구인지
    - ✅ 어떻게 시작하는지
    - ✅ 뭘 조심해야 하는지

    나머지는 직접 해보면서 배우는 게 가장 빠릅니다.
    실수해도 됩니다. 돈 한도만 걸어두면 큰 문제 없으니까요.
    """)

    st.markdown("### 🔗 바로가기")
    st.markdown("""
    - [paperclip.inc](https://paperclip.inc) — 바로 시작하기
    - [paperclipai.info](https://paperclipai.info) — 더 배우기 (영어)
    - [GitHub](https://github.com/paperclipai/paperclip) — 개발자용
    """)

    st.divider()
    nav_buttons()
