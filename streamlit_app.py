import streamlit as st

st.set_page_config(
    page_title="AI 직원 회사 만들기",
    page_icon="📎",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────
# DESIGN SYSTEM — Editorial Monochrome
# ─────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700;900&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
    --c0: #000;
    --c10: #1a1a1a;
    --c20: #2e2e2e;
    --c40: #666;
    --c60: #999;
    --c80: #ccc;
    --c90: #e5e5e5;
    --c95: #f2f2f2;
    --c100: #fff;
    --mono: 'IBM Plex Mono', monospace;
}

html, body, [class*="st-"] {
    font-family: 'Noto Sans KR', -apple-system, sans-serif !important;
}

/* ── Global Reset ── */
.block-container { max-width: 680px !important; padding: 2rem 1.5rem 4rem !important; }
h1, h2, h3, h4, h5, h6 { font-family: 'Noto Sans KR', sans-serif !important; letter-spacing: -0.02em; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--c100) !important;
    border-right: 1px solid var(--c90) !important;
}
section[data-testid="stSidebar"] .stButton button {
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    border-bottom: 1px solid var(--c95) !important;
    color: var(--c40) !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    text-align: left !important;
    padding: 14px 16px !important;
    transition: all 0.15s ease !important;
    width: 100% !important;
}
section[data-testid="stSidebar"] .stButton button:hover {
    background: var(--c95) !important;
    color: var(--c10) !important;
}
section[data-testid="stSidebar"] .stButton button[kind="primary"] {
    background: var(--c0) !important;
    color: var(--c100) !important;
    font-weight: 600 !important;
}

/* ── Typography ── */
.t-overline {
    font-family: var(--mono) !important;
    font-size: 11px; font-weight: 500;
    color: var(--c60); text-transform: uppercase;
    letter-spacing: 0.12em; margin-bottom: 6px;
}
.t-h1 { font-size: 32px; font-weight: 900; line-height: 1.25; color: var(--c0); margin-bottom: 8px; }
.t-h2 { font-size: 22px; font-weight: 700; line-height: 1.35; color: var(--c10); margin: 32px 0 12px; }
.t-h3 { font-size: 16px; font-weight: 700; line-height: 1.4; color: var(--c10); margin: 0 0 8px; }
.t-body { font-size: 15px; line-height: 1.85; color: var(--c20); }
.t-caption { font-size: 13px; color: var(--c60); line-height: 1.7; }
.t-dim { color: var(--c40); }

/* ── Card ── */
.card {
    background: var(--c100);
    border: 1px solid var(--c90);
    border-radius: 10px;
    padding: 24px;
    margin: 16px 0;
}
.card-label {
    font-family: var(--mono) !important;
    font-size: 10px; font-weight: 500;
    color: var(--c60); text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--c90);
}

/* ── Divider ── */
.div-line { border: none; border-top: 1px solid var(--c90); margin: 32px 0; }

/* ── Table ── */
.clean-table { width: 100%; border-collapse: collapse; margin: 12px 0; }
.clean-table th {
    font-family: var(--mono) !important;
    font-size: 11px; font-weight: 500;
    color: var(--c60); text-transform: uppercase;
    letter-spacing: 0.08em;
    text-align: left; padding: 10px 12px;
    border-bottom: 2px solid var(--c10);
}
.clean-table td {
    font-size: 14px; color: var(--c20);
    padding: 12px; border-bottom: 1px solid var(--c95);
    vertical-align: top; line-height: 1.65;
}
.clean-table tr:last-child td { border-bottom: none; }

/* ── Note Box ── */
.note {
    border-left: 2px solid var(--c10);
    padding: 14px 20px;
    margin: 16px 0;
    background: var(--c95);
    border-radius: 0 8px 8px 0;
}
.note p { font-size: 14px; color: var(--c20); margin: 0; line-height: 1.75; }
.note-warn {
    border-left: 2px solid var(--c0);
    padding: 14px 20px;
    margin: 16px 0;
    background: var(--c0);
    border-radius: 8px;
    color: var(--c100);
}
.note-warn p { font-size: 14px; color: var(--c90); margin: 0; line-height: 1.75; }
.note-warn strong { color: var(--c100); }

/* ── Org Chart ── */
.org { display: flex; flex-direction: column; align-items: center; margin: 24px 0; gap: 0; }
.org-n {
    padding: 10px 20px; border: 1px solid var(--c90);
    border-radius: 8px; font-size: 13px; font-weight: 600;
    text-align: center; background: var(--c100); color: var(--c10);
}
.org-n.dark { background: var(--c10); color: var(--c100); border-color: var(--c10); }
.org-l { width: 1px; height: 20px; background: var(--c80); }
.org-r { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
.org-br { width: 45%; height: 1px; background: var(--c80); }

/* ── Step ── */
.step-item { display: grid; grid-template-columns: 32px 1fr; gap: 16px; margin-bottom: 28px; }
.step-num {
    width: 32px; height: 32px; border-radius: 50%;
    background: var(--c10); color: var(--c100);
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 700;
    font-family: var(--mono) !important;
    flex-shrink: 0;
}
.step-body h4 { font-size: 15px; font-weight: 700; color: var(--c10); margin: 4px 0 4px; }
.step-body p { font-size: 14px; color: var(--c40); line-height: 1.75; margin: 0; }

/* ── VS Grid ── */
.vs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 16px 0; }
.vs-a, .vs-b {
    padding: 20px; border-radius: 10px; font-size: 14px; line-height: 1.7;
}
.vs-a { background: var(--c95); border: 1px solid var(--c90); color: var(--c20); }
.vs-b { background: var(--c10); color: var(--c80); border: 1px solid var(--c10); }
.vs-a h4, .vs-b h4 { font-size: 13px; font-weight: 700; margin-bottom: 8px; }
.vs-a h4 { color: var(--c10); }
.vs-b h4 { color: var(--c100); }
@media (max-width: 500px) { .vs-grid { grid-template-columns: 1fr; } }

/* ── Compare Feature ── */
.feat-row {
    display: grid; grid-template-columns: 1fr 1fr 1fr;
    border-bottom: 1px solid var(--c95); font-size: 13.5px;
}
.feat-row.hd { border-bottom: 2px solid var(--c10); }
.feat-cell { padding: 12px; color: var(--c20); }
.feat-cell.hd {
    font-family: var(--mono) !important;
    font-size: 11px; font-weight: 500; color: var(--c60);
    text-transform: uppercase; letter-spacing: 0.08em;
}

/* ── Hero ── */
.hero { padding: 40px 0 20px; }
.hero-label {
    font-family: var(--mono) !important;
    font-size: 11px; color: var(--c60);
    text-transform: uppercase; letter-spacing: 0.15em;
    margin-bottom: 16px;
}
.hero h1 { font-size: clamp(28px, 5vw, 40px); font-weight: 900; line-height: 1.2; color: var(--c0); margin-bottom: 16px; }
.hero p { font-size: 16px; color: var(--c40); line-height: 1.8; max-width: 520px; }

/* ── Streamlit overrides ── */
.stProgress > div > div { background-color: var(--c10) !important; }
div[data-testid="stExpander"] { border: 1px solid var(--c90) !important; border-radius: 10px !important; }
div[data-testid="stExpander"] summary { font-size: 15px !important; font-weight: 600 !important; }
.stRadio label { font-size: 14px !important; }
div[data-testid="stTable"] table { font-size: 14px !important; }
div[data-testid="stTable"] th {
    font-family: var(--mono) !important;
    font-size: 11px !important; text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}
</style>
""", unsafe_allow_html=True)

# ─── STATE ───
if "page" not in st.session_state:
    st.session_state.page = 0

PAGES = [
    "시작",
    "01 — AI가 뭔데?",
    "02 — Paperclip이 뭔데?",
    "03 — 회사 구조",
    "04 — 시작 방법",
    "05 — 직접 해보기",
    "06 — Claude Code와 비교",
    "07 — 활용 사례",
    "08 — 문제 해결",
]

# ─── SIDEBAR ───
with st.sidebar:
    st.markdown('<p style="font-family:IBM Plex Mono,monospace;font-size:11px;color:#999;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:4px;">학습 메뉴</p>', unsafe_allow_html=True)
    for i, name in enumerate(PAGES):
        if st.button(name, key=f"nav_{i}", use_container_width=True,
                     type="primary" if st.session_state.page == i else "secondary"):
            st.session_state.page = i
            st.rerun()
    st.markdown("---")
    progress = st.session_state.page / (len(PAGES) - 1) if len(PAGES) > 1 else 0
    st.progress(progress)
    st.caption(f"{int(progress * 100)}% 완료")


def go_prev():
    st.session_state.page = max(0, st.session_state.page - 1)

def go_next():
    st.session_state.page = min(len(PAGES) - 1, st.session_state.page + 1)

def nav():
    st.markdown('<hr class="div-line">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.session_state.page > 0:
            st.button("← 이전", on_click=go_prev, use_container_width=True)
    with c2:
        st.markdown(f'<p style="text-align:center;font-family:IBM Plex Mono,monospace;font-size:12px;color:#999;padding-top:8px;">{st.session_state.page}/{len(PAGES)-1}</p>', unsafe_allow_html=True)
    with c3:
        if st.session_state.page < len(PAGES) - 1:
            st.button("다음 →", on_click=go_next, use_container_width=True, type="primary")


def card(label, content):
    st.markdown(f'<div class="card"><div class="card-label">{label}</div>{content}</div>', unsafe_allow_html=True)

def note(content):
    st.markdown(f'<div class="note"><p>{content}</p></div>', unsafe_allow_html=True)

def warn(content):
    st.markdown(f'<div class="note-warn"><p>{content}</p></div>', unsafe_allow_html=True)

def heading(overline, title, sub=""):
    st.markdown(f'<div class="t-overline">{overline}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="t-h1">{title}</div>', unsafe_allow_html=True)
    if sub:
        st.markdown(f'<p class="t-caption">{sub}</p>', unsafe_allow_html=True)
    st.markdown('<hr class="div-line">', unsafe_allow_html=True)


# ═══════════════════════════════════════
# PAGE 0 — 시작
# ═══════════════════════════════════════
if st.session_state.page == 0:
    st.markdown("""
    <div class="hero">
        <div class="hero-label">비개발자를 위한 가이드 · 8단계 · 실습 포함</div>
        <h1>AI한테 일을 시키는<br>나만의 회사 만들기</h1>
        <p>컴퓨터 잘 모르셔도 됩니다.<br>
        AI 직원을 뽑고, 팀을 짜고, 일을 맡기는 법을<br>
        처음부터 차근차근 알려드립니다.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("시작하기 →", type="primary", use_container_width=True):
        st.session_state.page = 1
        st.rerun()

    st.markdown("""
    <div class="card" style="margin-top:24px;">
        <div class="card-label">커리큘럼</div>
        <table class="clean-table">
            <tr><th style="width:80px;">단계</th><th>내용</th></tr>
            <tr><td><strong>01–03</strong></td><td>개념 이해 — AI 에이전트, Paperclip, 회사 구조</td></tr>
            <tr><td><strong>04–05</strong></td><td>준비 & 실습 — 가입부터 첫 프로젝트까지</td></tr>
            <tr><td><strong>06</strong></td><td>Claude Code와 비교 — 뭐가 다르고, 언제 뭘 쓰나</td></tr>
            <tr><td><strong>07–08</strong></td><td>실전 — 활용 사례, 문제 해결</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════
# PAGE 1 — AI가 뭔데?
# ═══════════════════════════════════════
elif st.session_state.page == 1:
    heading("Step 01", "AI가 뭔데?", "제일 기초부터 시작합니다")

    card("우리가 아는 AI", """
    <p class="t-body">ChatGPT나 Claude 같은 거요.<br>
    "서울 맛집 알려줘"라고 물어보면 대답해주죠.<br><br>
    이건 마치 <strong>편의점 직원에게 물건 위치 묻는 것</strong>과 비슷합니다.<br>
    물어보면 대답하고, 끝. 다음에 또 물어봐야 합니다.</p>
    """)

    card("AI 에이전트는 뭐가 다른가", """
    <p class="t-body">에이전트는 <strong>내가 고용한 직원</strong>에 가깝습니다.</p>
    <p class="t-body" style="margin-top:8px;">
    · "보고서 만들어줘" → 자료 찾고 → 정리하고 → 파일로 저장까지 혼자 함<br>
    · 한 번에 여러 단계를 순서대로 알아서 처리함<br>
    · 다른 AI 직원에게 "너는 이거 해"라고 일을 넘기기도 함</p>
    """)

    st.markdown("""
    <div class="note">
    <p><strong>비유</strong> — 일반 AI = 식당에서 주문하는 것. 내가 매번 시켜야 함.<br>
    AI 에이전트 = 집에 요리사를 고용한 것. "저녁 해주세요"만 하면 장보기부터 설거지까지 알아서 함.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### 확인 문제")
    q = st.radio("AI 에이전트의 가장 큰 특징은?", [
        "더 빠르게 대답한다",
        "목표를 주면 여러 단계를 스스로 처리한다",
        "사람 말을 더 잘 알아듣는다",
    ], index=None, key="q1")
    if q:
        if "여러 단계" in q:
            st.success("맞습니다. 핵심은 '더 똑똑해서'가 아니라, 목표를 받으면 **계획→실행→결과까지 혼자 해낸다**는 것입니다.")
        else:
            st.error("정답: **목표를 주면 여러 단계를 스스로 처리한다**")
    nav()


# ═══════════════════════════════════════
# PAGE 2 — Paperclip이 뭔데?
# ═══════════════════════════════════════
elif st.session_state.page == 2:
    heading("Step 02", "Paperclip이 뭔데?", "AI 직원들을 관리하는 프로그램입니다")

    st.markdown("""
    <div class="card">
        <div class="card-label">한 문장 요약</div>
        <p class="t-h3" style="margin:0;">Paperclip = AI 직원들을 팀으로 묶어서, 일을 시키고, 관리하는 도구</p>
    </div>
    """, unsafe_allow_html=True)

    note("""<strong>비유</strong> — 직원이 1명이면 카톡으로 일 시키면 돼요.
    근데 직원이 5명이면? 누가 뭘 하는지, 돈은 얼마나 쓰는지, 보고는 어떻게 받는지 관리가 필요하죠.
    Paperclip이 바로 그 <strong>관리 시스템</strong>입니다.""")

    card("나는 뭘 하면 돼?", """
    <p class="t-body">당신의 역할 = <strong>"사장님 위의 사장님"</strong><br><br>
    직접 일하는 게 아니라, 큰 결정만 합니다.</p>
    <p class="t-body" style="margin-top:8px;">
    · "이 직원 뽑아도 되나요?" → 내가 OK / NO<br>
    · "이 방향으로 일할까요?" → 내가 OK / NO<br>
    · "돈 다 썼는데요?" → 내가 더 줄지 말지 결정</p>
    <p class="t-body" style="margin-top:12px;">AI가 멋대로 하는 게 <strong>절대 아닙니다</strong>. 중요한 결정은 항상 내 승인이 필요합니다.</p>
    """)

    card("가격", """
    <p class="t-body"><strong>Paperclip 자체는 무료</strong>예요.<br><br>
    돈이 드는 건 AI 직원의 "두뇌 사용료"입니다.
    핸드폰 데이터처럼 쓴 만큼만 나가고, 한도를 정해두면 그 이상은 절대 안 나갑니다.<br>
    처음 시작하면 보통 월 1~2만 원 수준입니다.</p>
    """)

    st.markdown("---")
    st.markdown("##### 확인 문제")
    q = st.radio("Paperclip은 어떤 도구인가요?", [
        "AI를 만드는 도구", "채팅하는 도구", "AI 직원들을 팀으로 관리하는 도구",
    ], index=None, key="q2")
    if q:
        if "관리" in q:
            st.success("맞습니다. 이미 있는 AI를 **팀처럼 조직해서 관리**하는 도구입니다.")
        else:
            st.error("정답: **AI 직원들을 팀으로 관리하는 도구**")
    nav()


# ═══════════════════════════════════════
# PAGE 3 — 회사 구조
# ═══════════════════════════════════════
elif st.session_state.page == 3:
    heading("Step 03", "AI 회사는 이렇게 생겼어요", "진짜 회사 조직도와 비슷합니다")

    st.markdown("""
    <div class="org">
        <div class="org-n dark">👤 나 — 최종 결정권자</div>
        <div class="org-l"></div>
        <div class="org-n" style="font-size:14px;">🤖 CEO — 총괄 매니저</div>
        <div class="org-l"></div>
        <div class="org-br"></div>
        <div class="org-r">
            <div class="org-n">📝 작가</div>
            <div class="org-n">🔍 조사원</div>
            <div class="org-n">🎨 디자이너</div>
        </div>
    </div>
    <p class="t-caption" style="text-align:center;">내가 CEO에게 방향을 말하면 → CEO가 아래 직원들에게 일을 나눠줍니다</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="t-h2">알아야 할 단어 5개</div>
    <table class="clean-table">
        <tr><th>단어</th><th>쉬운 뜻</th><th>예시</th></tr>
        <tr><td><strong>회사</strong></td><td>"우리 팀이 뭘 하는 곳인지" 정하는 틀</td><td>블로그 운영팀</td></tr>
        <tr><td><strong>에이전트</strong></td><td>AI 직원 1명</td><td>CEO, 작가, 조사원</td></tr>
        <tr><td><strong>프로젝트</strong></td><td>큰 목표 하나</td><td>4월 블로그 3편 완성</td></tr>
        <tr><td><strong>태스크</strong></td><td>작은 할 일 하나</td><td>AI 트렌드 자료 수집</td></tr>
        <tr><td><strong>하트비트</strong></td><td>AI 직원의 "출근 알람"</td><td>매일 오전 9시 기상</td></tr>
    </table>
    """, unsafe_allow_html=True)

    warn("""⚠️ <strong>비용 한도를 반드시 설정하세요.</strong><br>
    AI 직원이 밤새 혼자 일하면서 돈을 계속 쓸 수 있습니다.
    핸드폰 데이터 한도처럼, 직원별 월 한도를 정해두면 자동으로 멈춥니다.""")

    nav()


# ═══════════════════════════════════════
# PAGE 4 — 시작 방법
# ═══════════════════════════════════════
elif st.session_state.page == 4:
    heading("Step 04", "어떻게 시작하나요?", "방법은 2가지인데, 쉬운 걸로 갑시다")

    st.markdown("""
    <div class="vs-grid">
        <div class="vs-a">
            <h4>✅ 쉬운 방법 — 이걸로 하세요</h4>
            <p><strong>paperclip.inc</strong> 웹사이트 이용<br><br>
            인터넷만 되면 OK<br>설치할 것 없음<br>무료로 시작 가능<br><br>
            <strong>이 수업은 이 방법 기준입니다</strong></p>
        </div>
        <div class="vs-b">
            <h4>🔧 어려운 방법 — 개발자용</h4>
            <p>내 컴퓨터에 직접 설치<br><br>
            프로그래밍 지식 필요<br>완전 무료지만 복잡함<br><br>
            → 우리는 무시합니다</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    card("준비물 — 딱 2가지", """
    <p class="t-body"><strong>① 이메일 계정</strong><br>
    <span class="t-dim">가입할 때 쓸 이메일. 이미 있는 거 쓰면 됩니다.</span></p>
    <p class="t-body" style="margin-top:16px;"><strong>② AI 서비스 열쇠 (API 키)</strong><br>
    <span class="t-dim">넷플릭스 계정처럼, AI를 쓸 때 필요한 "통행증"입니다.<br>
    <a href="https://console.anthropic.com">console.anthropic.com</a> 또는
    <a href="https://platform.openai.com">platform.openai.com</a>에서 만들 수 있습니다.<br>
    가입하면 소액의 무료 크레딧을 줍니다.</span></p>
    """)

    warn("""⚠️ API 키는 <strong>비밀번호와 같습니다</strong>. 남에게 알려주면 그 사람이 내 돈으로 AI를 쓸 수 있습니다.""")

    nav()


# ═══════════════════════════════════════
# PAGE 5 — 직접 해보기
# ═══════════════════════════════════════
elif st.session_state.page == 5:
    heading("Step 05", "직접 해봅시다", "paperclip.inc에서 하나씩 따라하세요")

    steps = [
        ("1", "가입하기", '<a href="https://paperclip.inc">paperclip.inc</a>에서 회원가입. 이메일, 비밀번호만 있으면 됩니다.'),
        ("2", "회사 만들기", '"Create Company" 버튼. 이름과 미션(할 일)을 한 문장으로 적으세요.'),
        ("3", "CEO 뽑기", '"CEO를 뽑을까요?" → Approve(승인). CEO는 다른 직원에게 일을 나눠주는 팀장입니다.'),
        ("4", "직원 1명 추가", 'CEO가 제안하는 직원 1명만 승인. 처음부터 5명 뽑지 마세요.'),
        ("5", "비용 한도 설정", 'CEO: $5(≈7,000원) / 작가·조사원: $10(≈14,000원)으로 시작하세요.'),
        ("6", "첫 목표 입력", '구체적으로 적으세요. "800자 블로그 글 1개 작성" ← 좋음. "마케팅 알아서 해" ← 나쁨.'),
        ("7", "결과 확인", '대시보드에서 진행 상황, 비용, 결과물을 확인. 마음에 안 들면 다시 시키세요.'),
    ]

    for num, title, desc in steps:
        st.markdown(f"""
        <div class="step-item">
            <div class="step-num">{num}</div>
            <div class="step-body">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    note("여기까지 하면 AI 회사가 돌아가고 있는 겁니다. 처음에는 결과물이 완벽하지 않을 수 있어요. 그게 정상입니다.")

    nav()


# ═══════════════════════════════════════
# PAGE 6 — Claude Code와 비교 ★ NEW
# ═══════════════════════════════════════
elif st.session_state.page == 6:
    heading("Step 06", "Claude Code vs Paperclip", "비슷해 보이지만 다릅니다. 정확히 비교합니다.")

    card("먼저 알아야 할 것", """
    <p class="t-body"><strong>Claude Code</strong>는 Anthropic이 만든 코딩 도구입니다.<br>
    터미널(검은 화면에 글자 치는 프로그램)에서 동작하며,
    Claude AI가 직접 파일을 만들고, 코드를 쓰고, 명령을 실행합니다.<br><br>
    Claude Code에도 <strong>"서브 에이전트"</strong>라는 기능이 있습니다.<br>
    메인 Claude가 전문가 에이전트를 여러 개 띄워서 동시에 일을 시킬 수 있습니다.</p>
    """)

    note("""<strong>비유</strong> — Claude Code의 서브 에이전트 = 사무실에서 팀장이 팀원들에게 일을 나눠주는 것.
    Paperclip = 여러 부서가 있는 회사 전체를 운영하는 경영 시스템.""")

    st.markdown('<div class="t-h2">기능 비교</div>', unsafe_allow_html=True)

    st.markdown("""
    <table class="clean-table">
        <tr><th style="width:34%;">비교 항목</th><th style="width:33%;">Claude Code</th><th style="width:33%;">Paperclip</th></tr>
        <tr>
            <td><strong>여러 AI 동시 작업</strong></td>
            <td>✅ 가능<br><span style="color:#999;font-size:13px;">서브 에이전트를 병렬로 실행</span></td>
            <td>✅ 가능<br><span style="color:#999;font-size:13px;">에이전트 팀 구성</span></td>
        </tr>
        <tr>
            <td><strong>역할 전문화</strong></td>
            <td>✅ 가능<br><span style="color:#999;font-size:13px;">에이전트별 역할·도구 지정</span></td>
            <td>✅ 가능<br><span style="color:#999;font-size:13px;">CEO, 마케터, 개발자 등</span></td>
        </tr>
        <tr>
            <td><strong>24시간 자동 실행</strong></td>
            <td>❌ 불가<br><span style="color:#999;font-size:13px;">세션 열어야 동작, 닫으면 끝</span></td>
            <td>✅ 가능<br><span style="color:#999;font-size:13px;">하트비트로 자동 기상</span></td>
        </tr>
        <tr>
            <td><strong>직원별 비용 한도</strong></td>
            <td>❌ 없음<br><span style="color:#999;font-size:13px;">전체 API 비용만 확인 가능</span></td>
            <td>✅ 가능<br><span style="color:#999;font-size:13px;">에이전트별 월 예산, 자동 정지</span></td>
        </tr>
        <tr>
            <td><strong>조직도·보고 체계</strong></td>
            <td>❌ 없음<br><span style="color:#999;font-size:13px;">프롬프트로 직접 설계해야 함</span></td>
            <td>✅ 내장<br><span style="color:#999;font-size:13px;">위임·보고·승인 자동화</span></td>
        </tr>
        <tr>
            <td><strong>감사 기록</strong></td>
            <td>△ 제한적<br><span style="color:#999;font-size:13px;">터미널 로그 수준</span></td>
            <td>✅ 전체 기록<br><span style="color:#999;font-size:13px;">모든 행동·결정 자동 저장</span></td>
        </tr>
        <tr>
            <td><strong>비개발자 접근성</strong></td>
            <td>❌ 어려움<br><span style="color:#999;font-size:13px;">터미널 기반, CLI 필수</span></td>
            <td>✅ 쉬움<br><span style="color:#999;font-size:13px;">웹 대시보드로 조작</span></td>
        </tr>
        <tr>
            <td><strong>코딩 작업 능력</strong></td>
            <td>✅ 매우 강력<br><span style="color:#999;font-size:13px;">코드 전문 도구</span></td>
            <td>△ 가능하지만 본업 아님<br><span style="color:#999;font-size:13px;">비즈니스 운영에 초점</span></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    st.markdown('<div class="t-h2">그래서 뭘 쓰면 되나?</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="vs-grid">
        <div class="vs-a">
            <h4>Claude Code가 맞는 경우</h4>
            <p>· 코딩 작업이 주 목적<br>
            · 개발자이거나 터미널에 익숙<br>
            · 내가 직접 지시하고 바로 결과를 확인하는 방식<br>
            · 프로젝트 단위로 집중 작업</p>
        </div>
        <div class="vs-b">
            <h4>Paperclip이 맞는 경우</h4>
            <p>· 마케팅, 리서치, 운영 등 비즈니스 전반<br>
            · 비개발자도 쓸 수 있어야 함<br>
            · AI가 알아서 돌아가고, 나는 결과만 확인<br>
            · 비용 통제와 감사가 중요</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    note("""<strong>요약</strong> — Claude Code = 똑똑한 개발팀을 데스크에서 직접 지휘하는 것.
    Paperclip = 회사 전체를 경영 시스템으로 돌리는 것.
    둘은 경쟁이 아니라 레이어가 다릅니다. Paperclip 안에서 Claude Code를 에이전트 런타임으로 쓸 수도 있습니다.""")

    nav()


# ═══════════════════════════════════════
# PAGE 7 — 활용 사례
# ═══════════════════════════════════════
elif st.session_state.page == 7:
    heading("Step 07", "이런 일에 써보세요", "실제 활용 사례 3가지")

    with st.expander("📝 사례 1 — 블로그 운영팀", expanded=True):
        st.markdown('"혼자 블로그 쓰기 힘든데, AI 팀이 도와주면 좋겠다"')
        st.table({
            "AI 직원": ["🤖 CEO", "🔍 조사원", "📝 작가"],
            "하는 일": ["주제 정하기, 일정 관리, 글 검사", "자료를 인터넷에서 찾아 정리", "자료 바탕으로 글 초안 쓰기"],
        })
        st.caption("내가 하는 일: 주제 승인 → 글 검토 → 수정 지시 → 게시는 내가 직접")

    with st.expander("🔬 사례 2 — 경쟁사 조사"):
        st.markdown('"경쟁사가 뭘 하는지 알고 싶은데 시간이 없다"')
        st.table({
            "AI 직원": ["🤖 CEO", "🔍 조사원 A", "🔍 조사원 B"],
            "하는 일": ["조사 범위 정하기, 보고서 정리", "경쟁사 제품/가격 정보 수집", "업계 뉴스, 트렌드 수집"],
        })

    with st.expander("🌐 사례 3 — 웹페이지 제작"):
        st.markdown('"회사 소개 페이지가 필요한데 개발자는 없다"')
        st.table({
            "AI 직원": ["🤖 CEO", "💻 개발자", "📝 작가"],
            "하는 일": ["페이지 구성 잡기, 전체 감독", "실제 웹페이지 만들기", "페이지에 들어갈 글 쓰기"],
        })

    note("핵심 원칙 — <strong>작게 시작</strong>하세요. CEO + 직원 1명으로 첫 프로젝트를 끝내보고, 1명씩 추가하세요.")

    nav()


# ═══════════════════════════════════════
# PAGE 8 — 문제 해결
# ═══════════════════════════════════════
elif st.session_state.page == 8:
    heading("Step 08", "문제가 생기면?", "자주 겪는 상황 4가지")

    with st.expander("💸 돈이 생각보다 많이 나왔어요", expanded=True):
        st.markdown("""
        **왜:** AI 직원이 같은 일을 반복했거나, 불필요하게 긴 작업을 한 경우

        **해결:**
        - 직원별 월 한도를 꼭 설정 (다 쓰면 자동 정지)
        - 대시보드에서 비용을 자주 확인
        - 처음엔 $5 이하로 시작
        """)

    with st.expander("🔄 같은 일을 자꾸 반복해요"):
        st.markdown("""
        **왜:** 목표가 모호해서 "언제 끝나는지"를 모르는 것

        **해결:** 끝나는 조건을 확실히 적어주세요
        - ❌ "좋은 글 써"
        - ✅ "800자 분량 글 1개를 작성해서 저장해"
        """)

    with st.expander("📉 결과물이 별로예요"):
        st.markdown("""
        **왜:** 한 직원에게 너무 많은 종류의 일을 시킨 경우

        **해결:** 한 직원에게 한 가지만 시키세요
        - ❌ "자료 조사하고, 글도 쓰고, 그림도 만들어"
        - ✅ "자료 조사만 해"
        """)

    with st.expander("🔇 직원이 아무것도 안 해요"):
        st.markdown("""
        **확인 순서:**
        1. 비용 한도를 다 써서 멈춘 건 아닌지
        2. 출근 알람(하트비트)이 설정되어 있는지
        3. 앞 단계 일이 아직 안 끝나서 기다리는 중인지
        """)

    st.markdown("---")
    st.markdown("### 수고하셨습니다")
    st.markdown("""
    여기까지 오셨으면 이제 이런 걸 아시게 된 겁니다.

    - AI 에이전트가 뭔지
    - Paperclip이 뭘 하는 도구인지
    - Claude Code와 뭐가 다른지
    - 어떻게 시작하고, 뭘 조심해야 하는지

    나머지는 직접 해보면서 배우는 게 가장 빠릅니다.
    """)

    st.markdown("""
    ---
    **바로가기**

    [paperclip.inc](https://paperclip.inc) — 바로 시작하기 ·
    [paperclipai.info](https://paperclipai.info) — 더 배우기 ·
    [GitHub](https://github.com/paperclipai/paperclip) — 개발자용
    """)

    nav()
