import json
import os
from firestore_client import init_firestore

def update_coin_data(coin_ticker: str, json_path: str):
    db = init_firestore()

    # Load data from local JSON file
    with open(json_path, 'r') as f:
        coin_data = json.load(f)

    # Write to Firestore under /coin_analysis/{ticker}/current_snapshot
    coin_ref = db.collection('coin_analysis').document(coin_ticker.upper())
    coin_ref.set({'current_snapshot': coin_data})

    print(f"✅ Updated Firestore with data for {coin_ticker}")

if __name__ == "__main__":
    # Example usage
    update_coin_data("BTC", "../data/example_btc.json")
