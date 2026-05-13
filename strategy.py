import pandas as pd

def signal(data):
    if data is None or len(data) < 40:
        return None

    try:
        close = float(data['Close'].iloc[-1])

        high_20 = float(data['High'].iloc[-20:].max())
        low_20 = float(data['Low'].iloc[-20:].min())

        volume = float(data['Volume'].iloc[-1])
        avg_volume = float(data['Volume'].rolling(10).mean().iloc[-1])

        # 📊 قرب الاختراق
        near_resistance = close >= high_20 * 0.995
        breakout = close > high_20

        near_support = close <= low_20 * 1.005
        breakdown = close < low_20

        # =========================
        # 🔥 BUY (30m momentum)
        # =========================
        if (breakout or near_resistance) and volume >= avg_volume * 0.9:

            return {
                "type": "30M BREAKOUT BUY",
                "entry": close,
                "tp1": round(close * 1.015, 2),
                "tp2": round(close * 1.03, 2),
                "sl": round(low_20, 2)
            }

        # =========================
        # 🔥 SELL
        # =========================
        if (breakdown or near_support) and volume >= avg_volume * 0.9:

            return {
                "type": "30M BREAKDOWN SELL",
                "entry": close,
                "tp1": round(close * 0.985, 2),
                "tp2": round(close * 0.97, 2),
                "sl": round(high_20, 2)
            }

        return None

    except Exception as e:
        print("Strategy Error:", e)
        return None
