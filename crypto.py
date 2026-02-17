import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Crypto Volatility Visualizer", layout="wide")

# ----------------------------
# TITLE
# ----------------------------
st.title("📈 Crypto Volatility Visualizer")
st.markdown("Analyze real cryptocurrency data and experiment with mathematical volatility simulation.")

# ----------------------------
# FILE UPLOAD
# ----------------------------
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload Crypto CSV File", type=["csv"])

if uploaded_file is None:
    st.warning("Please upload a CSV file containing Timestamp, Open, High, Low, Close, Volume columns.")
    st.stop()

# ----------------------------
# DATA LOADING & CLEANING
# ----------------------------
df = pd.read_csv(uploaded_file)

# Clean column names
df.columns = [col.strip().capitalize() for col in df.columns]

# Convert Timestamp
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Drop missing values
df = df.dropna()

# Rename Close to Price
df = df.rename(columns={"Close": "Price"})

# Sort by date
df = df.sort_values("Timestamp")

# ----------------------------
# DATE FILTER
# ----------------------------
st.sidebar.header("Filter Options")
min_date = df['Timestamp'].min()
max_date = df['Timestamp'].max()

date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])

df = df[(df['Timestamp'] >= pd.to_datetime(date_range[0])) &
        (df['Timestamp'] <= pd.to_datetime(date_range[1]))]

# ----------------------------
# CALCULATIONS
# ----------------------------
df['Returns'] = df['Price'].pct_change()
df['Volatility'] = df['Returns'].rolling(7).std()
df['MA7'] = df['Price'].rolling(7).mean()
df['MA30'] = df['Price'].rolling(30).mean()

current_price = df['Price'].iloc[-1]
avg_price = df['Price'].mean()
volatility_index = df['Volatility'].iloc[-1]
max_price = df['Price'].max()
min_price = df['Price'].min()
total_return = ((df['Price'].iloc[-1] - df['Price'].iloc[0]) / df['Price'].iloc[0]) * 100

stability_score = (1 / volatility_index) if volatility_index != 0 else 0
stability_score = min(stability_score * 10, 100)

trend = "Uptrend 🟢" if df['MA7'].iloc[-1] > df['MA30'].iloc[-1] else "Downtrend 🔴"
volatility_label = "Stable 🟢" if volatility_index < 0.02 else "Volatile 🔴"

# ----------------------------
# METRICS
# ----------------------------
st.subheader("Market Overview")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Current Price", f"${current_price:,.2f}")
col2.metric("Average Price", f"${avg_price:,.2f}")
col3.metric("Volatility (7D)", f"{volatility_index:.4f}")
col4.metric("Total % Change", f"{total_return:.2f}%")

col5, col6, col7 = st.columns(3)
col5.metric("Trend", trend)
col6.metric("Market Type", volatility_label)
col7.metric("Stability Score", f"{stability_score:.2f}/100")

# ----------------------------
# TABS
# ----------------------------
tab1, tab2 = st.tabs(["📊 Market Analysis", "🧪 Simulation Lab"])

# ============================
# MARKET ANALYSIS TAB
# ============================
with tab1:

    st.subheader("Price Over Time")
    fig_price = px.line(df, x='Timestamp', y='Price')
    fig_price.add_scatter(x=df['Timestamp'], y=df['MA7'], mode='lines', name='MA7')
    fig_price.add_scatter(x=df['Timestamp'], y=df['MA30'], mode='lines', name='MA30')
    st.plotly_chart(fig_price, use_container_width=True)

    st.subheader("Candlestick Chart")
    fig_candle = go.Figure(data=[go.Candlestick(
        x=df['Timestamp'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Price']
    )])
    st.plotly_chart(fig_candle, use_container_width=True)

    colA, colB = st.columns(2)

    with colA:
        st.subheader("High vs Low Comparison")
        fig_hl = go.Figure()
        fig_hl.add_trace(go.Scatter(x=df['Timestamp'], y=df['High'], name='High'))
        fig_hl.add_trace(go.Scatter(x=df['Timestamp'], y=df['Low'], name='Low'))
        st.plotly_chart(fig_hl, use_container_width=True)

    with colB:
        st.subheader("Volume Analysis")
        fig_vol = px.bar(df, x='Timestamp', y='Volume')
        st.plotly_chart(fig_vol, use_container_width=True)

    st.subheader("Rolling Volatility (7-Day)")
    fig_volatility = px.line(df, x='Timestamp', y='Volatility')
    st.plotly_chart(fig_volatility, use_container_width=True)

    st.subheader("Daily Returns")
    fig_returns = px.line(df, x='Timestamp', y='Returns')
    st.plotly_chart(fig_returns, use_container_width=True)

    st.subheader("Volume vs Daily Returns")
    fig_scatter = px.scatter(df, x='Volume', y='Returns')
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.download_button(
        label="Download Filtered Data",
        data=df.to_csv(index=False),
        file_name="filtered_crypto_data.csv",
        mime="text/csv"
    )

# ============================
# SIMULATION TAB
# ============================
with tab2:

    st.sidebar.header("Simulation Controls")

    pattern = st.sidebar.selectbox("Pattern Type",
                                    ["Sine", "Cosine", "Random Noise", "Combined"])

    amplitude = st.sidebar.slider("Amplitude (Swing Size)", 1, 100, 20)
    frequency = st.sidebar.slider("Frequency (Swing Speed)", 1, 20, 5)
    drift = st.sidebar.slider("Drift (Trend)", -10, 10, 0)

    t = np.linspace(0, 10, len(df))

    if pattern == "Sine":
        sim_price = amplitude * np.sin(frequency * t)
    elif pattern == "Cosine":
        sim_price = amplitude * np.cos(frequency * t)
    elif pattern == "Random Noise":
        sim_price = amplitude * np.random.normal(0, 1, len(df))
    else:
        sim_price = (amplitude * np.sin(frequency * t) +
                     amplitude * np.random.normal(0, 0.5, len(df)))

    sim_price = sim_price + drift * t
    sim_df = pd.DataFrame({"Time": df['Timestamp'], "Simulated Price": sim_price})

    sim_returns = pd.Series(sim_price).pct_change()
    sim_volatility = sim_returns.rolling(7).std().iloc[-1]

    st.subheader("Simulated Price Movement")
    fig_sim = px.line(sim_df, x="Time", y="Simulated Price")
    st.plotly_chart(fig_sim, use_container_width=True)

    st.subheader("Real vs Simulated Comparison")
    comparison = go.Figure()
    comparison.add_trace(go.Scatter(x=df['Timestamp'], y=df['Price'], name="Real"))
    comparison.add_trace(go.Scatter(x=sim_df['Time'], y=sim_df['Simulated Price'], name="Simulated"))
    st.plotly_chart(comparison, use_container_width=True)

    st.metric("Real Volatility", f"{volatility_index:.4f}")
    st.metric("Simulated Volatility", f"{sim_volatility:.4f}")

    if abs(volatility_index - sim_volatility) < 0.005:
        st.success("Simulation volatility closely matches real market volatility!")
    else:
        st.info("Adjust parameters to better match real volatility.")
