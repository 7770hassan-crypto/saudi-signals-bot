import pandas as pd

def signal(data):
    if data is None or len(data) < 10:
        return None

    try:
        close = float(data['Close'].iloc[-1])
        open_ = float(data['Open'].iloc[-1])

        ma = float(data['Close'].rolling(5).mean().iloc[-1])

        prev_high = float(data['High'].iloc[-5:-1].max())
        prev_low = float(data['Low'].iloc[-5:-1].min())

        volume = float(data['Volume'].iloc[-1])
        avg_volume = float(data['Volume'].rolling(5).mean().iloc[-1])

        # 📈 BUY
        if close > ma and close >= prev_high and volume >= avg_volume:
            return {
                "type": "BUY",
                "entry": close,
                "tp1": round(close * 1.03, 2),
                "tp2": round(close * 1.06, 2),
                "sl": round(close * 0.98, 2)
            }

        # 📉 SELL
        if close < ma and close <= prev_low and volume >= avg_volume:
            return {
                "type": "SELL",
                "entry": close,
                "tp1": round(close * 0.97, 2),
                "tp2": round(close * 0.94, 2),
                "sl": round(close * 1.02, 2)
            }

        return None

    except Exception as e:
        print("Strategy Error:", e)
        return None
