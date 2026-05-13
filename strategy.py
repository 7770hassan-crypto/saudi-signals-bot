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

        breakout_score = (close / high_20) * 100
        volume_score = volume / avg_volume
        momentum = (close - low_20) / low_20 * 100

        total_score = breakout_score + (volume_score * 10) + momentum

        # 🔥 أصبح نشيط (أوسع من قبل)
        if close >= high_20 * 0.985:
            return round(total_score, 2)

        return None

    except Exception as e:
        print("score_stock error:", e)
        return None
