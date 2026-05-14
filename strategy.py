import pandas as pd

def score_stock(data):

    if data is None or len(data) < 30:
        return None

    try:

        close = float(data['Close'].iloc[-1])

        high_20 = float(data['High'].iloc[-20:].max())
        low_20 = float(data['Low'].iloc[-20:].min())

        volume = float(data['Volume'].iloc[-1])
        avg_volume = float(data['Volume'].rolling(10).mean().iloc[-1])

        if avg_volume == 0:
            return None

        # 🔥 نسبة النشاط والسيولة
        volume_ratio = volume / avg_volume

        # 🔥 قرب السهم من القمة
        resistance_ratio = close / high_20

        # 🔥 الزخم
        momentum = ((close - low_20) / low_20) * 100

        # 🔥 التقييم النهائي
        score = (
            (volume_ratio * 40) +
            (resistance_ratio * 40) +
            momentum
        )

        # 🔥 فلتر أخف وأنشط
        if volume_ratio >= 0.7:
            return round(score, 2)

        return None

    except Exception as e:
        print("score_stock error:", e)
        return None
         
