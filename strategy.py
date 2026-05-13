import pandas as pd

def signal(data):
    if data is None or len(data) < 30:
        return None

    try:
        close = float(data['Close'].iloc[-1])
        high = float(data['High'].iloc[-1])
        low = float(data['Low'].iloc[-1])

        # 📊 مقاومة ودعم حقيقي (آخر 20 شمعة)
        resistance = float(data['High'].iloc[-20:].max())
        support = float(data['Low'].iloc[-20:].min())

        # 📊 متوسط حجم بسيط
        volume = float(data['Volume'].iloc[-1])
        avg_volume = float(data['Volume'].rolling(10).mean().iloc[-1])

        # =========================
        # 🔥 قرب الاختراق (مهم جدًا مثل المنصات)
        # =========================
        near_breakout_up = close >= resistance * 0.997  # قريب جدًا من الكسر
        breakout_up = close > resistance

        near_breakout_down = close <= support * 1.003
        breakout_down = close < support

        # =========================
        # 📈 BUY
        # =========================
        if (breakout_up or near_breakout_up) and volume >= avg_volume * 0.8:

            return {
                "type": "BREAKOUT BUY",
                "entry": close,
                "tp1": round(close * 1.02, 2),
                "tp2": round(close * 1.05, 2),
                "sl": round(support, 2)
            }

        # =========================
        # 📉 SELL
        # =========================
        if (breakout_down or near_breakout_down) and volume >= avg_volume * 0.8:

            return {
                "type": "BREAKDOWN SELL",
                "entry": close,
                "tp1": round(close * 0.98, 2),
                "tp2": round(close * 0.95, 2),
                "sl": round(resistance, 2)
            }

        return None

    except Exception as e:
        print("Strategy Error:", e)
        return None
    
