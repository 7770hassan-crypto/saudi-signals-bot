import pandas as pd

def get_value(x):
    # يحول أي Series أو قيمة إلى رقم واحد فقط
    if isinstance(x, pd.Series):
        return float(x.iloc[0])
    return float(x)

def signal(data):
    if data is None or len(data) < 5:
        return None

    try:
        close = get_value(data['Close'].iloc[-1])
        open_ = get_value(data['Open'].iloc[-1])
        high = get_value(data['High'].iloc[-1])
        low = get_value(data['Low'].iloc[-1])

        prev_high = float(data['High'].iloc[-5:-1].max())
        prev_low = float(data['Low'].iloc[-5:-1].min())

        ma = float(data['Close'].rolling(5).mean().iloc[-1])

        # 📈 BUY
        if close > ma and close > prev_high and close > open_:
            return {
                "type": "BUY",
                "entry": close,
                "tp1": round(close * 1.05, 2),
                "tp2": round(close * 1.10, 2),
                "sl": round(close * 0.97, 2)
            }

        # 📉 SELL
        if close < ma and close < prev_low and close < open_:
            return {
                "type": "SELL",
                "entry": close,
                "tp1": round(close * 0.95, 2),
                "tp2": round(close * 0.90, 2),
                "sl": round(close * 1.03, 2)
            }

        return None

    except:
        return None
