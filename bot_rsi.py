import requests
import pandas as pd
import time
from ta.momentum import RSIIndicator

TOKEN = "COLE_SEU_TOKEN_AQUI"
CHAT_ID = "COLE_SEU_CHAT_ID_AQUI"

def send_message(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_btc_data():
    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=100"
    data = requests.get(url).json()
    closes = [float(candle[4]) for candle in data]
    return pd.Series(closes)

print("Bot iniciado...")

while True:
    closes = get_btc_data()
    rsi = RSIIndicator(closes, window=14).rsi().iloc[-1]

    print("RSI atual:", rsi)

    if rsi > 70:
        send_message(f"⚠ RSI acima de 70: {round(rsi,2)}")

    if rsi < 25:
        send_message(f"⚠ RSI abaixo de 30: {round(rsi,2)}")

    time.sleep(60)