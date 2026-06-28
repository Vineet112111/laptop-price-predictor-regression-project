import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

# Load Model and Data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Title
st.title("💻 Laptop Price Predictor")
st.markdown("Enter the laptop specifications below to predict its price.")

# Brand
company = st.selectbox(
    'Brand',
    sorted(df['Company'].unique())
)

# Type
type_name = st.selectbox(
    'Type',
    sorted(df['TypeName'].unique())
)

# RAM
ram = st.selectbox(
    'RAM (GB)',
    [2, 4, 6, 8, 12, 16, 24, 32, 64]
)

# Weight
weight = st.number_input(
    'Weight of Laptop (kg)',
    min_value=0.5,
    max_value=5.0,
    value=1.5,
    step=0.1
)

# Touchscreen
touchscreen = st.selectbox(
    'Touchscreen',
    ['No', 'Yes']
)

# IPS Display
ips = st.selectbox(
    'IPS Display',
    ['No', 'Yes']
)

# Screen Size
screen_size = st.slider(
    'Screen Size (inches)',
    10.0,
    18.0,
    13.3
)

# Resolution
resolution = st.selectbox(
    'Screen Resolution',
    [
        '1920x1080',
        '1366x768',
        '1600x900',
        '3840x2160',
        '3200x1800',
        '2880x1800',
        '2560x1600',
        '2560x1440',
        '2304x1440'
    ]
)

# CPU
cpu = st.selectbox(
    'CPU',
    sorted(df['Cpu brand'].unique())
)

# HDD
hdd = st.selectbox(
    'HDD (GB)',
    [0, 128, 256, 512, 1024, 2048]
)

# SSD
ssd = st.selectbox(
    'SSD (GB)',
    [0, 8, 128, 256, 512, 1024]
)

# GPU
gpu = st.selectbox(
    'GPU',
    sorted(df['Gpu brand'].unique())
)

# OS
os = st.selectbox(
    'Operating System',
    sorted(df['os'].unique())
)

# Prediction Button
if st.button('Predict Price'):

    touchscreen_value = 1 if touchscreen == 'Yes' else 0
    ips_value = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])

    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

    import pandas as pd

    query = pd.DataFrame([[
    company,
    type_name,
    ram,
    weight,
    touchscreen_value,
    ips_value,
    ppi,
    cpu,
    hdd,
    ssd,
    gpu,
    os
]], columns=[
    'Company',
    'TypeName',
    'Ram',
    'Weight',
    'Touchscreen',
    'Ips',
    'ppi',
    'Cpu brand',
    'HDD',
    'SSD',
    'Gpu brand',
    'os'
])


    try:
        prediction = pipe.predict(query)[0]

        # If model was trained on log(price)
        predicted_price = np.exp(prediction)

        st.success(
            f"💰 Estimated Laptop Price: ₹ {predicted_price:,.0f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")