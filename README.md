# Coin Data Hub

A modular backend pipeline for collecting, storing, and versioning structured cryptocurrency asset data.  
Built to support AI-based trading model training, strategy development, and automation.

---

## 🔧 Project Structure

```
coin_data_hub/
├── firestore/
│   ├── firestore_client.py        # Connects to Firestore securely
│   ├── update_coin_data.py        # Uploads one asset’s JSON snapshot to Firestore
│   ├── ingest_data_pipeline.py    # Generates mock BTC data and uploads
│   └── ingest_multiple_coins.py   # Uploads mock data for BTC, ETH, SOL
├── data/
│   └── mock_<ticker>_ingest.json  # Auto-generated mock data for each coin
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Features

- Supports Firestore as a real-time backend
- Ingests clean, schema-compliant data for any crypto asset
- Modular ingestion scripts with future API hook support
- Safe `.gitignore` setup to protect sensitive keys and data

---

## 🚀 Usage

1. Clone the repo and `cd` into the directory
2. Create your virtual environment:

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

3. Add your Firebase `serviceAccountKey.json` to:  
   `firestore/credentials/`

4. Run a script:

```bash
python firestore/ingest_data_pipeline.py         # Single asset (BTC)
python firestore/ingest_multiple_coins.py        # BTC, ETH, SOL
```

---

## 🔐 Notes

- Firestore rules should be set to authenticated-only in production.
- All `.json` keys and ingestion data are excluded from GitHub via `.gitignore`.

---

## 📈 Next Steps

- ⏱️ Scheduled ingestion (cron or task scheduler)
- 🔗 Real data APIs (CoinGecko, CryptoPanic, etc.)
- 🧠 Connect to your trading AI or model training pipeline

---

Made with 💰 and ☕ by Jolly.
