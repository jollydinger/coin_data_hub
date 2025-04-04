import random
from datetime import datetime, timedelta
import os
import json
from update_coin_data import update_coin_data

def generate_mock_data():
    now = datetime.utcnow().isoformat() + "Z"

    # Generate mock momentum data
    def mock_momentum():
        return {
            "trend": random.choice(["uptrend", "downtrend", "sideways"]),
            "percent_r": round(random.uniform(-100, 0), 2),
            "rsi": round(random.uniform(20, 80), 2),
            "td_count": random.randint(-9, 9)
        }

    # Generate mock divergence signal
    def mock_divergence(label):
        return {
            "label": label,
            "timestamp": now
        }

    timeframes = ["3m", "15m", "30m", "1h", "4h", "12h", "1d", "1w"]

    data = {
        "market_information": {
            "data_retrieval_timestamp": now,
            "coin_name": "Bitcoin",
            "ticker": "BTC",
            "price": round(random.uniform(64000, 69000), 2)
        },
        "latest_news": [
            {
                "headline": "Bitcoin sees slight rally on low volume",
                "source": "MockNews",
                "url": "https://mocknews.com/bitcoin-rally",
                "timestamp": now
            },
            {
                "headline": "ETF inflows stabilize after volatile week",
                "source": "MockFinance",
                "url": "https://mockfinance.com/etf-inflows",
                "timestamp": now
            }
        ],
        "upcoming_catalysts": [
            {
                "event": "Bitcoin Halving",
                "date": (datetime.utcnow() + timedelta(days=14)).strftime('%Y-%m-%d'),
                "description": "The next Bitcoin halving is expected mid-month."
            },
            {
                "event": "FOMC Rate Decision",
                "date": (datetime.utcnow() + timedelta(days=7)).strftime('%Y-%m-%d'),
                "description": "Could influence BTC volatility."
            }
        ],
        "divergence_data": {
            "recent_signals": {tf: mock_divergence("Bullish" if i % 2 == 0 else "Bearish") for i, tf in enumerate(timeframes)},
            "historical_1d_bullish": [
                {"timestamp": now, "description": "Strong RSI divergence on daily close."}
            ],
            "historical_1d_bearish": [
                {"timestamp": now, "description": "Price made new high with lower RSI."}
            ],
            "historical_1w_bullish": [
                {"timestamp": now, "description": "Weekly hidden bullish divergence detected."}
            ],
            "historical_1w_bearish": [
                {"timestamp": now, "description": "Weekly bearish divergence confirmed."}
            ]
        },
        "momentum_data": {tf: mock_momentum() for tf in timeframes},
        "jolly_technical_analysis": {
            "analysis_1": {
                "text": "BTC forming a bull flag on the 4h chart.",
                "signal_quality": 82
            },
            "analysis_2": {
                "text": "Divergence aligning with momentum reversal.",
                "signal_quality": 75
            },
            "analysis_3": {
                "text": "Strong cluster of TD9s on short timeframe.",
                "signal_quality": 69
            },
            "short_term_bias": 78,
            "long_term_bias": 62
        }
    }

    return data

def main():
    mock_data = generate_mock_data()
    temp_json_path = os.path.join(os.path.dirname(__file__), "../data/mock_btc_ingest.json")
    
    with open(temp_json_path, "w") as f:
        json.dump(mock_data, f, indent=2)

    update_coin_data("BTC", temp_json_path)

if __name__ == "__main__":
    main()
