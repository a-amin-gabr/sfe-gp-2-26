import streamlit as st
import requests

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sentiment Analysis",
    layout="centered",
    initial_sidebar_state="collapsed",
)

API_URL = "http://127.0.0.1:8000/predict"

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

.main-title {
    font-size: 2.8rem;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(135deg, #6366F1, #06B6D4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.4rem;
}

.subtitle {
    font-size: 1rem;
    text-align: center;
    color: #6B7280;
    margin-bottom: 2.5rem;
    font-weight: 300;
}

.result-card {
    padding: 2rem;
    border-radius: 14px;
    margin-top: 1.5rem;
    text-align: center;
    animation: fadeIn 0.45s ease-out;
}

.result-positive {
    background: linear-gradient(135deg,rgba(16,185,129,0.12),rgba(5,150,105,0.18));
    border: 1px solid #10B981;
}

.result-negative {
    background: linear-gradient(135deg,rgba(239,68,68,0.12),rgba(220,38,38,0.18));
    border: 1px solid #EF4444;
}

.result-neutral {
    background: linear-gradient(135deg,rgba(99,102,241,0.10),rgba(6,182,212,0.14));
    border: 1px solid #6366F1;
}

.sentiment-emoji {
    font-size: 2.8rem;
    margin-bottom: 0.5rem;
}

.sentiment-label {
    font-size: 1.7rem;
    font-weight: 700;
    letter-spacing: 1px;
    color: #1F2937;
}

@media (prefers-color-scheme: dark) {
    .sentiment-label { color: #F9FAFB; }
}

.sentiment-score {
    font-size: 1rem;
    font-weight: 400;
    color: #6B7280;
    margin-top: 0.6rem;
}

.alert-warning {
    padding: 0.9rem 1.2rem;
    border-radius: 8px;
    background: rgba(245,158,11,0.1);
    border: 1px solid #F59E0B;
    color: #B45309;
    margin-top: 1rem;
    font-size: 0.95rem;
}

.alert-error {
    padding: 0.9rem 1.2rem;
    border-radius: 8px;
    background: rgba(239,68,68,0.1);
    border: 1px solid #EF4444;
    color: #B91C1C;
    margin-top: 1rem;
    font-size: 0.95rem;
}

@media (prefers-color-scheme: dark) {
    .alert-warning { color: #FBBF24; }
    .alert-error   { color: #FCA5A5; }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0);   }
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">Sentiment Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter any text and get an instant sentiment result.</div>', unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
text_input = st.text_area(
    label="text",
    placeholder="Type your sentence here...",
    height=140,
    label_visibility="collapsed",
)

_, col_btn, _ = st.columns([1, 1, 1])
with col_btn:
    analyze_btn = st.button("Analyze", use_container_width=True)

# ── Analysis ──────────────────────────────────────────────────────────────────
if analyze_btn:
    if not text_input.strip():
        st.markdown(
            '<div class="alert-warning">Please type a sentence before analyzing.</div>',
            unsafe_allow_html=True,
        )
    else:
        with st.spinner("Processing..."):
            try:
                response = requests.post(API_URL, json={"text": text_input.strip()})

                if response.status_code == 200:
                    data = response.json()
                    sentiment = data["sentiment"].upper()
                    confidence = data["confidence"]
                    score_pct = f"{confidence * 100:.1f}%"

                    if sentiment == "POSITIVE":
                        css_class, emoji, label = "result-positive", "😊", "Positive"
                    elif sentiment == "NEGATIVE":
                        css_class, emoji, label = "result-negative", "😞", "Negative"
                    else:
                        css_class, emoji, label = "result-neutral",  "😐", "Neutral"

                    st.markdown(
                        f'<div class="result-card {css_class}">'
                        f'<div class="sentiment-emoji">{emoji}</div>'
                        f'<div class="sentiment-label">{label}</div>'
                        f'<div class="sentiment-score">Score: {score_pct}</div>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f'<div class="alert-error">Error {response.status_code}: {response.text}</div>',
                        unsafe_allow_html=True,
                    )

            except requests.exceptions.ConnectionError:
                st.markdown(
                    '<div class="alert-error">'
                    'Could not reach the server. Please make sure the backend is running.'
                    '</div>',
                    unsafe_allow_html=True,
                )
            except Exception as e:
                st.markdown(
                    f'<div class="alert-error">Unexpected error: {str(e)}</div>',
                    unsafe_allow_html=True,
                )
