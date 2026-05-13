import pandas as pd

def score_stock(data):
    if data is None or len(data) < 30:
        return None

    try:
        close = float(data['Close'].iloc[-1])

        resistance = float(data['High'].iloc[-20:].max())
        support = float(data['Low'].iloc[-20:].min())

        volume = float(data['Volume'].iloc[-1])
        avg_volume = float(data['Volume'].rolling(10).mean().iloc[-1])

        # 📊 نسبة القرب من الاختراق
        breakout_score = (close / resistance) * 100

        # 📊 قوة الحجم
        volume_score = volume / avg_volume if avg_volume > 0 else 0

        # 📊 زخم السعر
        momentum = (close - support) / support * 100

        # 🔥 إجمالي القوة
        total_score = breakout_score + (volume_score * 10) + momentum

        if close >= resistance * 0.995:
            return round(total_score, 2)

        return None

    except Exception as e:
        print("Score Error:", e)
        return None
