from flask import Flask, render_template, jsonify, url_for
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    exchange_rate = get_exchange_rate()
    return render_template("index.html", exchange_rate=exchange_rate)

@app.route('/get_exchange_rate', methods=['GET'])
def get_exchange_rate_route():
    exchange_rate = get_exchange_rate()
    return jsonify({'exchangeRate': exchange_rate})

def get_exchange_rate():
    usd_brl = yf.Ticker('USDBRL=X')
    exchange_rate = usd_brl.history(period='1d')['Close'][0]
    return exchange_rate

if __name__ == '__main__':
    app.run(debug=True, port=8000)