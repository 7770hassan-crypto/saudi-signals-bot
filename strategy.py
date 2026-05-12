import pandas as pd

def signal(data):
    if data is None or len(data) < 30:
        return None

    try:
        close = float(data['Close'].iloc[-1])
        volume = float(data['Volume'].iloc[-1])
        avg_volume = float(data['Volume'].rolling(20).mean().iloc[-1])

        # =========================
        # 📊 Daily Breakout (20 candles)
        # =========================
        daily_high = float(data['High'].rolling(20).max().iloc[-1])
        daily_low = float(data['Low'].rolling(20).min().iloc[-1])

        # =========================
        # 📊 Weekly Breakout (approx 100 candles)
        # =========================
        weekly_high = float(data['High'].rolling(100).max().iloc[-1])
        weekly_low = float(data['Low'].rolling(100).min().iloc[-1])

        # =========================
        # 📊 Monthly Breakout (approx 400 candles)
        # =========================
        monthly_high = float(data['High'].rolling(400).max().iloc[-1])
        monthly_low = float(data['Low'].rolling(400).min().iloc[-1])

        # =========================
        # 🔥 BUY CONDITIONS
        # =========================
        if (
            close > daily_high or
            close > weekly_high or
            close > monthly_high
        ) and volume > avg_volume:

            return {
                "type": "BREAKOUT BUY",
                "entry": close,
                "tp1": round(close * 1.03, 2),
                "tp2": round(close * 1.06, 2),
                "sl": round(close * 0.97, 2)
            }

        # =========================
        # 🔥 SELL CONDITIONS
        # =========================
        if (
            close < daily_low or
            close < weekly_low or
            close < monthly_low
        ) and volume > avg_volume:

            return {
                "type": "BREAKOUT SELL",
                "entry": close,
                "tp1": round(close * 0.97, 2),
                "tp2": round(close * 0.94, 2),
                "sl": round(close * 1.02, 2)
            }

        return None

    except Exception as e:
        print("Strategy Error:", e)
        return None
    
