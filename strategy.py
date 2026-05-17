import pandas as pd

def score_stock(data):

    if data is None or len(data) < 20:
        return None

    try:

        close = float(data['Close'].iloc[-1])
        open_price = float(data['Open'].iloc[-1])

        high_20 = float(data['High'].iloc[-20:].max())
        low_20 = float(data['Low'].iloc[-20:].min())

        volume = float(data['Volume'].iloc[-1])
        avg_volume = float(data['Volume'].rolling(10).mean().iloc[-1])

        if avg_volume == 0:
            return None

        # 📊 السيولة
        volume_ratio = volume / avg_volume

        # 📈 الزخم
        momentum = (close - open_price) / open_price * 100

        # 📍 الموقع من القمة
        position = close / high_20

        # 🔥 تقييم بسيط وواضح
        score = (volume_ratio * 50) + (momentum * 30) + (position * 20)

        # ✅ شرط دخول نظيف
        if volume_ratio >= 0.8 and momentum > 0:

            return round(score, 2)

        return None

    except Exception as e:
        print("strategy error:", e)
        return None
