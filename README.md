# 📈 Crypto Volatility Visualizer  
## Mathematics for AI-II – Formative Assessment 2  

---

## 👤 Student Information

**Name:** Dwij Vala  
**Student ID:** 2505369  
**Course:** Mathematics for AI-II  
**Assessment Type:** Formative Assessment 2    

---

# 📌 1. Project Overview

The **Crypto Volatility Visualizer** is an advanced interactive financial analytics dashboard developed using Python and Streamlit.  

The primary objective of this project is to analyze real cryptocurrency market data and simulate market volatility using mathematical functions such as sine waves, cosine waves, random noise, and drift models.

This project bridges:

- 📊 Real-world financial data analysis  
- 🧮 Mathematical modeling concepts  
- 📈 Data visualization techniques  
- 💻 Interactive dashboard development  
- 🚀 Cloud deployment and version control  

The dashboard allows users to explore market stability, identify volatile periods, analyze trading volume impact, detect trends, and experiment with mathematical simulations to understand how price swings behave.

---

# 🎯 2. Project Objectives

This project aims to:

- Load and clean real cryptocurrency market data.
- Convert timestamp data into proper datetime format.
- Handle missing values effectively.
- Analyze time-series price movements.
- Calculate rolling volatility using statistical methods.
- Detect trends using moving averages.
- Classify markets as stable or volatile.
- Build an interactive dashboard using Streamlit.
- Simulate market behavior using mathematical functions.
- Deploy the final project using GitHub and Streamlit Cloud.

---

# 🚀 3. Live Deployed Application

🔗 **Public App Link:**  
*https://crypto-volatility-dwij.streamlit.app/*  

---

# 📊 4. Market Analysis Features

## 📈 Price Over Time
Interactive line chart showing price movement across selected dates.

## 🕯 Candlestick Chart
Professional trading-style visualization showing:
- Open
- High
- Low
- Close

## 📉 High vs Low Comparison
Displays daily price range to understand intra-day volatility.

## 📊 Volume Analysis
Bar chart showing trading activity and its correlation with price swings.

## 📈 Rolling 7-Day Volatility
Calculated using rolling standard deviation of daily returns.

Formula Used:
```
Volatility = Rolling Standard Deviation of Percentage Returns
```

## 📊 Daily Returns
Percentage change between consecutive closing prices.

Formula Used:
```
Returns = (Price_today - Price_yesterday) / Price_yesterday
```

## 📌 Moving Averages
- 7-Day Moving Average
- 30-Day Moving Average

Used for trend detection and smoothing price noise.

## 📈 Volume vs Returns Scatter Plot
Analyzes correlation between trading activity and price movement intensity.

## 📊 Trend Detection
If MA7 > MA30 → Uptrend  
If MA7 < MA30 → Downtrend  

## 📊 Volatility Classification
Market is classified as:
- Stable 🟢 (Low volatility)
- Volatile 🔴 (High volatility)

## 📊 Stability Score
A derived metric based on inverse volatility scaled to 0–100.

## 📥 Download Filtered Data
Users can download selected time-range dataset for further analysis.

---

# 🧪 5. Simulation Lab Features

This section demonstrates how mathematical functions simulate real-world financial behavior.

## 🎛 Pattern Selection
Users can select:

- Sine Wave
- Cosine Wave
- Random Noise
- Combined Pattern

## 🎚 Adjustable Parameters

### Amplitude
Controls size of price swings.

### Frequency
Controls speed of oscillations.

### Drift
Adds long-term upward or downward trend.

Mathematical Model Example:
```
Simulated Price = A * sin(f * t) + Drift * t + Noise
```

## 🔄 Real vs Simulated Comparison
Displays actual market data alongside mathematical simulation.

## 📊 Volatility Matching
Users can adjust parameters to match simulated volatility with real market volatility.

---

# 🗂 6. Repository Structure

```
crypto-volatility-visualizer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── test_crypto_full_dataset.csv
```

---

# 🧪 7. Included Test Dataset

The repository includes:

```
test_crypto_full_dataset.csv
```

This dataset contains:

- Timestamp  
- Open  
- High  
- Low  
- Close  
- Volume  
- Market Cap  
- Trade Count  
- Sentiment Score  
- Exchange  
- Intentional missing values  

This allows users to test:
- Data cleaning functionality
- Missing value handling
- Visualization performance
- Simulation comparison

---

# ⚙️ 8. Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| Streamlit | Interactive dashboard framework |
| Pandas | Data manipulation and cleaning |
| NumPy | Mathematical computations |
| Plotly | Interactive data visualization |
| GitHub | Version control |
| Streamlit Cloud | Deployment |

---

# ▶️ 9. How to Run Locally

### Step 1: Clone Repository
```
git clone https://github.com/YOUR_USERNAME/crypto-volatility-visualizer.git
```

### Step 2: Navigate into Folder
```
cd crypto-volatility-visualizer
```

### Step 3: Create Virtual Environment
```
python -m venv venv
```

Windows (PowerShell):
```
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies
```
pip install -r requirements.txt
```

### Step 5: Run Application
```
streamlit run app.py
```

---

# 🧠 10. Mathematical Concepts Applied

This project applies several mathematical and statistical concepts:

- Sine and Cosine functions
- Random distributions
- Linear drift modeling
- Percentage change
- Rolling standard deviation
- Moving averages
- Trend detection logic
- Stability scoring model

These concepts connect theoretical mathematics with real financial market behavior.

---

# 🎓 11. Learning Outcomes Achieved

- Data cleaning and preprocessing
- Time-series analysis
- Volatility measurement
- Financial pattern recognition
- Interactive dashboard design
- Cloud-based deployment
- Git version control practices

---

# 🏁 12. Final Reflection

This project demonstrates how mathematical modeling and financial data analysis can be integrated into a real-world interactive dashboard.

By combining statistical techniques, simulation models, and visualization tools, the Crypto Volatility Visualizer transforms raw market data into meaningful financial insights.

It reflects both conceptual understanding and practical technical implementation.
