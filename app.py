from flask import Flask, jsonify, render_template
import requests
import pandas as pd
import numpy as np
import logging

app = Flask(__name__)

# Binance API URLs
KLINE_URL = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=30"
PRICE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_binance_data():
    """Fetches the latest candlestick (Kline) data from Binance."""
    try:
        response = requests.get(KLINE_URL)
        response.raise_for_status()
        data = response.json()

        if not data or len(data) < 14:
            logging.error("Not enough data from Binance API.")
            return None

        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', '_', '_', '_', '_', '_', '_'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df['price'] = df['close'].astype(float)
        df['volume'] = df['volume'].astype(float)
        df.set_index('timestamp', inplace=True)
        
        return df
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Binance data: {e}")
        return None

def get_live_price():
    """Fetches the live price of BTC/USDT from Binance."""
    try:
        response = requests.get(PRICE_URL)
        response.raise_for_status()
        data = response.json()
        return float(data['price'])
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching live price: {e}")
        return None

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/price')
def price():
    """API endpoint to fetch live price."""
    live_price = get_live_price()
    if live_price:
        return jsonify({"live_price": live_price})
    return jsonify({"error": "Could not fetch price"})

@app.route('/api/trade_data')
def trade_data():
    """API endpoint to fetch technical indicators."""
    df = get_binance_data()
    live_price = get_live_price()
    
    if df is not None:
        df['EMA_9'] = df['price'].ewm(span=9, adjust=False).mean()
        df['EMA_21'] = df['price'].ewm(span=21, adjust=False).mean()
        df['MACD_Line'] = df['price'].ewm(span=12, adjust=False).mean() - df['price'].ewm(span=26, adjust=False).mean()
        df['Signal_Line'] = df['MACD_Line'].ewm(span=9, adjust=False).mean()
        df['RSI'] = 100 - (100 / (1 + (df['price'].diff().where(df['price'].diff() > 0, 0).rolling(window=14).mean() /
                                      (-df['price'].diff().where(df['price'].diff() < 0, 0).rolling(window=14).mean()))))

        latest = df.iloc[-1]
        data = {
            "live_price": live_price,
            "ema_9": latest['EMA_9'],
            "ema_21": latest['EMA_21'],
            "rsi": latest['RSI'],
            "macd": latest['MACD_Line'],
            "signal": latest['Signal_Line'],
            "timestamp": str(latest.name)
        }
        return jsonify(data)
    
    return jsonify({"error": "Data not available"})

if __name__ == '__main__':
    app.run(debug=True)
