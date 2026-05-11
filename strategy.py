def signal(data):
    if len(data) < 5:
        return None

    close = data['Close'].iloc[-1]
    open_ = data['Open'].iloc[-1]
    high = data['High'].iloc[-1]
    low = data['Low'].iloc[-1]

    prev_high = data['High'].iloc[-5:-1].max()
    prev_low = data['Low'].iloc[-5:-1].min()

    ma = data['Close'].rolling(5).mean().iloc[-1]

    # 📈 BUY
    if close > ma and close > prev_high and close > open_:
        entry = close
        tp1 = round(entry * 1.05, 2)
        tp2 = round(entry * 1.10, 2)
        sl = round(entry * 0.97, 2)

        return {
            "type": "BUY",
            "entry": entry,
            "tp1": tp1,
            "tp2": tp2,
            "sl": sl
        }

    # 📉 SELL
    if close < ma and close < prev_low and close < open_:
        entry = close
        tp1 = round(entry * 0.95, 2)
        tp2 = round(entry * 0.90, 2)
        sl = round(entry * 1.03, 2)

        return {
            "type": "SELL",
            "entry": entry,
            "tp1": tp1,
            "tp2": tp2,
            "sl": sl
        }

    return None 
