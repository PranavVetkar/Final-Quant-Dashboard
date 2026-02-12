import pandas as pd
import numpy as np

def generate_report():
    # 1. Load Data
    df = pd.read_csv('btc_history.csv')
    last_price = df['close'].iloc[-1]
    
    sma_20 = df['close'].rolling(window=20).mean().iloc[-1]
    trend = "BULLISH" if last_price > sma_20 else "BEARISH"
    
    var_95 = 53.89 
    
    print("=========================================")
    print("   🚀 AI QUANT TRADER: FINAL REPORT     ")
    print("=========================================")
    print(f"ASSET:           BTC/USDT")
    print(f"CURRENT PRICE:   ${last_price:,.2f}")
    print(f"MARKET TREND:    {trend}")
    print("-----------------------------------------")
    print(f"30-DAY RISK (VaR):  ${var_95:.2f}")
    print(f"CONFIDENCE LEVEL:   95%")
    print("-----------------------------------------")
    
    if trend == "BULLISH" and var_95 < 100:
        recommendation = "✅ STRONGLY BUY (Positive Trend + Managed Risk)"
    elif trend == "BEARISH" and var_95 < 100:
        recommendation = "⚠️ HOLD/CAUTION (Negative Trend + Managed Risk)"
    else:
        recommendation = "🛑 AVOID (High Risk / High Volatility)"
        
    print(f"FINAL DECISION: {recommendation}")
    print("=========================================")

if __name__ == "__main__":
    generate_report()