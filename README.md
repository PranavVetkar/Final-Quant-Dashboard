# 🚀 AI Quant Trader — Final Decision Dashboard

A Python-based **quant trading summary engine** that consolidates market trend analysis and portfolio risk metrics into a single actionable trading decision report.

This project represents the final layer of a quantitative trading stack — where signals, risk models, and analytics are synthesized into a clear recommendation.

---

## 🎯 Project Objective

To generate a simplified **institution-style trading report** that answers:

> “Given trend + risk, should I buy, hold, or avoid this asset?”

---

## 🚀 What This Project Does

- Loads historical BTC price data
- Calculates market trend using SMA
- Integrates Value-at-Risk (VaR) metrics
- Assesses portfolio downside exposure
- Produces a final trade recommendation
- Displays a formatted quant report

---

## 🧠 Decision Framework

The report combines two core pillars:

### 1️⃣ Market Trend Analysis

Uses a 20-period Simple Moving Average:
- Trend = BULLISH → Price > SMA(20)
- Trend = BEARISH → Price < SMA(20)

---

### 2️⃣ Risk Assessment

Inputs 30-day Monte Carlo VaR:
- 95% Confidence VaR = $53.89

This represents the potential downside risk.

---

## ⚙️ Recommendation Logic

| Trend | Risk | Decision |
|------|------|-----------|
| Bullish | Low | ✅ Strong Buy |
| Bearish | Low | ⚠️ Hold / Caution |
| Any | High | 🛑 Avoid |

---

## 🛠️ Tech Stack

- Python 3.8+
- Pandas
- NumPy

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PranavVetkar/Final-Quant-Dashboard.git
cd Final-Quant-Dashboard
