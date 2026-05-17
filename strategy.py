import pandas as pd

def score_stock(data):

    if data is None or len(data) < 20:
        return None

    try:

        close = float(data['Close'].iloc[-1])
        open_price = float(data['Open'].iloc[-1])

        high_10 = float(data['High'].iloc[-10:].max())
        low_10 = float(data['Low'].iloc[-10:].min())

        volume = float(data['Volume'].iloc[-1])
        avg_volume = float(data['Volume'].rolling(5).mean().iloc[-1])

        if avg_volume == 0:
            return None

        # 🔥 نسبة النشاط
        volume_ratio = volume / avg_volume

        # 🔥 نسبة الحركة
        move_percent = ((close - open_price) / open_price) * 100

        # 🔥 قرب القمة
        high_ratio = close / high_10

        # 🔥 التقييم النهائي
        score = (
            (volume_ratio * 50) +
            (move_percent * 30) +
            (high_ratio * 20)
        )

        # 🔥 فلتر نشاط خفيف
        if volume_ratio >= 0.2:
            return round(score, 2)

        return None

    except Exception as e:
        print("Radar Error:", e)
        return None
