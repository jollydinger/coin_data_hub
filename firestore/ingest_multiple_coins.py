import os
import json
import random
from datetime import datetime, timedelta
from update_coin_data import update_coin_data

def generate_mock_data(coin_name, ticker):
    now = datetime.utcnow().isoformat() + "Z"

    def mock_momentum():
        return {
            "trend": random.choice(["uptrend", "downtrend", "sideways"]),
            "percent_r": round(random.uniform(-100, 0), 2),
            "rsi": round(random.uniform(20, 80), 2),
            "td_count": random.randint(-9, 9)
        }

    def mock_divergence(label):
        return {
            "label": label,
            "timestamp": now
        }

    timeframes = ["3m", "15m", "30m", "1h", "4h", "12h", "1d", "1w"]

    return {
        "market_information": {
            "data_retrieval_timestamp": now,
            "coin_name": coin_name,
            "ticker": ticker,
            "price": round(random.uniform(20, 4000), 2)
        },
        "latest_news": [
            {
                "headline": f"{coin_name} makes headlines with tech upgrades",
                "source": "MockNews",
                "url": f"https://mocknews.com/{ticker.lower()}-update",
                "timestamp": now
            }
        ],
        "upcoming_catalysts": [
            {
                "event": f"{coin_name} conference",
                "date": (datetime.utcnow() + timedelta(days=10)).strftime('%Y-%m-%d'),
                "description": f"{coin_name} developers to reveal roadmap updates."
            }
        ],
        "divergence_data": {
            "recent_signals": {tf: mock_divergence("Bullish" if i % 2 == 0 else "Bearish") for i, tf in enumerate(timeframes)},
            "historical_1d_bullish": [{"timestamp": now, "description": "Mock daily bullish divergence"}],
            "historical_1d_bearish": [{"timestamp": now, "description": "Mock daily bearish divergence"}],
            "historical_1w_bullish": [{"timestamp": now, "description": "Mock weekly bullish divergence"}],
            "historical_1w_bearish": [{"timestamp": now, "description": "Mock weekly bearish divergence"}]
        },
        "momentum_data": {tf: mock_momentum() for tf in timeframes},
        "jolly_technical_analysis": {
            "analysis_1": {"text": f"{coin_name} showing strength on weekly chart.", "signal_quality": 85},
            "analysis_2": {"text": f"Momentum building for {coin_name}.", "signal_quality": 72},
            "analysis_3": {"text": f"{coin_name} holding key support zone.", "signal_quality": 66},
            "short_term_bias": random.randint(50, 90),
            "long_term_bias": random.randint(40, 80)
        }
    }

def main():
    coins = [
        {"name": "Bitcoin", "ticker": "BTC"},
        {"name": "Ethereum", "ticker": "ETH"},
        {"name": "Solana", "ticker": "SOL"}
    ]

    for coin in coins:
        data = generate_mock_data(coin["name"], coin["ticker"])
        temp_path = os.path.join(os.path.dirname(__file__), f"../data/mock_{coin['ticker'].lower()}_ingest.json")
        with open(temp_path, "w") as f:
            json.dump(data, f, indent=2)

        update_coin_data(coin["ticker"], temp_path)

if __name__ == "__main__":
    main()
