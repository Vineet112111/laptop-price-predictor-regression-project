import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0A0E1A;
    color: #E2E8F0;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 780px;
}

/* ── Hero Header ── */
.hero-header {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    margin-bottom: 0.5rem;
}
.hero-icon {
    font-size: 3rem;
    display: block;
    margin-bottom: 0.75rem;
    filter: drop-shadow(0 0 18px #4F8EF7aa);
}
.hero-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2rem;
    font-weight: 500;
    letter-spacing: -0.5px;
    color: #FFFFFF;
    margin: 0 0 0.4rem;
}
.hero-title span {
    color: #4F8EF7;
}
.hero-sub {
    font-size: 0.875rem;
    color: #64748B;
    letter-spacing: 0.5px;
    font-family: 'JetBrains Mono', monospace;
}

/* ── Section Label ── */
.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #4F8EF7;
    padding: 1.5rem 0 0.6rem;
    border-top: 1px solid #1E2D45;
    margin-top: 0.5rem;
}
.section-label:first-of-type {
    border-top: none;
    padding-top: 0.5rem;
}

/* ── Selectbox & Number Input ── */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background: #111827 !important;
    border: 1px solid #1E3A5F !important;
    border-radius: 8px !important;
    color: #E2E8F0 !important;
    transition: border-color 0.2s;
}
div[data-baseweb="select"] > div:hover,
div[data-baseweb="input"] > div:hover {
    border-color: #4F8EF7 !important;
}
div[data-baseweb="select"] svg { fill: #4F8EF7 !important; }

/* ── Slider ── */
div[data-testid="stSlider"] > div > div > div {
    background: #4F8EF7 !important;
}
div[data-testid="stSlider"] > div > div > div > div {
    background: #FFFFFF !important;
    border: 2px solid #4F8EF7 !important;
    box-shadow: 0 0 8px #4F8EF755 !important;
}

/* ── Labels ── */
label[data-testid="stWidgetLabel"] p {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.8px !important;
    color: #94A3B8 !important;
    text-transform: uppercase !important;
}

/* ── Predict Button ── */
div[data-testid="stButton"] > button {
    width: 100%;
    margin-top: 1.5rem;
    padding: 0.9rem 2rem;
    background: linear-gradient(135deg, #1D4ED8, #4F8EF7);
    color: #FFFFFF;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    box-shadow: 0 0 24px #4F8EF755;
    transition: all 0.25s ease;
}
div[data-testid="stButton"] > button:hover {
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    box-shadow: 0 0 36px #4F8EF7aa;
    transform: translateY(-1px);
}
div[data-testid="stButton"] > button:active {
    transform: translateY(0px);
}

/* ── Success Result Card ── */
div[data-testid="stAlert"] {
    background: #0D1F36 !important;
    border: 1px solid #1E3A5F !important;
    border-left: 4px solid #4F8EF7 !important;
    border-radius: 10px !important;
    color: #E2E8F0 !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* ── Dropdown menu (popover) ── */
ul[data-baseweb="menu"] {
    background: #111827 !important;
    border: 1px solid #1E3A5F !important;
    border-radius: 8px !important;
}
ul[data-baseweb="menu"] li:hover {
    background: #1E2D45 !important;
}

/* ── Divider ── */
.spec-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #1E3A5F 30%, #4F8EF722 70%, transparent);
    margin: 0.25rem 0;
}

/* ── Result Price ── */
.price-result {
    text-align: center;
    padding: 1.8rem;
    background: linear-gradient(135deg, #0D1F36, #0F2847);
    border: 1px solid #1E3A5F;
    border-top: 3px solid #4F8EF7;
    border-radius: 12px;
    margin-top: 1rem;
    box-shadow: 0 0 40px #4F8EF71a;
}
.price-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #4F8EF7;
    margin-bottom: 0.5rem;
}
.price-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.4rem;
    font-weight: 500;
    color: #FFFFFF;
    letter-spacing: -1px;
}
.price-note {
    font-size: 0.75rem;
    color: #475569;
    margin-top: 0.4rem;
    font-family: 'JetBrains Mono', monospace;
}
</style>
""", unsafe_allow_html=True)

# ─── Load Model and Data ───────────────────────────────────────────────────────
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# ─── Hero Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <span class="hero-icon">💻</span>
    <h1 class="hero-title">Laptop <span>Price</span> Predictor</h1>
    <p class="hero-sub">// configure specs → get instant market estimate</p>
</div>
""", unsafe_allow_html=True)

# ─── Section: Identity ─────────────────────────────────────────────────────────
st.markdown('<div class="section-label">01 &nbsp;·&nbsp; Identity</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    company = st.selectbox('Brand', sorted(df['Company'].unique()))
with col2:
    type_name = st.selectbox('Type', sorted(df['TypeName'].unique()))

# ─── Section: Core Specs ──────────────────────────────────────────────────────
st.markdown('<div class="section-label">02 &nbsp;·&nbsp; Core Specs</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    ram = st.selectbox('RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
with col4:
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=1.5, step=0.1)

col5, col6 = st.columns(2)
with col5:
    cpu = st.selectbox('CPU', sorted(df['Cpu brand'].unique()))
with col6:
    os = st.selectbox('Operating System', sorted(df['os'].unique()))

# ─── Section: Display ─────────────────────────────────────────────────────────
st.markdown('<div class="section-label">03 &nbsp;·&nbsp; Display</div>', unsafe_allow_html=True)

col7, col8 = st.columns(2)
with col7:
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
with col8:
    ips = st.selectbox('IPS Display', ['No', 'Yes'])

screen_size = st.slider('Screen Size (inches)', 10.0, 18.0, 13.3)

resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160',
    '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])

# ─── Section: Storage & GPU ───────────────────────────────────────────────────
st.markdown('<div class="section-label">04 &nbsp;·&nbsp; Storage & GPU</div>', unsafe_allow_html=True)

col9, col10 = st.columns(2)
with col9:
    hdd = st.selectbox('HDD (GB)', [0, 128, 256, 512, 1024, 2048])
with col10:
    ssd = st.selectbox('SSD (GB)', [0, 8, 128, 256, 512, 1024])

gpu = st.selectbox('GPU', sorted(df['Gpu brand'].unique()))

# ─── Predict ──────────────────────────────────────────────────────────────────
if st.button('⚡  Predict Price'):

    touchscreen_value = 1 if touchscreen == 'Yes' else 0
    ips_value = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

    import pandas as pd

    query = pd.DataFrame([[
        company, type_name, ram, weight,
        touchscreen_value, ips_value, ppi,
        cpu, hdd, ssd, gpu, os
    ]], columns=[
        'Company', 'TypeName', 'Ram', 'Weight',
        'Touchscreen', 'Ips', 'ppi',
        'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'
    ])

    try:
        prediction = pipe.predict(query)[0]
        predicted_price = np.exp(prediction)

        st.markdown(f"""
        <div class="price-result">
            <div class="price-label">Estimated Market Price</div>
            <div class="price-value">₹ {predicted_price:,.0f}</div>
            <div class="price-note">based on current spec configuration</div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction Error: {e}")