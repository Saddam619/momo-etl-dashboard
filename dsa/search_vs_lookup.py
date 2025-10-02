import sys
import time
import json
from pathlib import Path

DATA_FILE = Path("dsa/parsed_data.json")

# Load transactions
with DATA_FILE.open("r", encoding="utf-8") as f:
    transactions = json.load(f)
    print("📊 Dataset size:", len(transactions))

# Linear search
def linear_search(transactions, tx_id):
    for tx in transactions:
        if str(tx.get("transaction_id")) == str(tx_id):
            return tx
    return None

# Dictionary lookup
def build_dict(transactions):
    return {str(tx["transaction_id"]): tx for tx in transactions}

def dict_lookup(tx_dict, tx_id):
    return tx_dict.get(str(tx_id))

# ---- Compare Performance ----
if __name__ == "__main__":
    # If user passes ID in terminal, use it; else default to middle transaction
    if len(sys.argv) > 1:
        sample_id = sys.argv[1]
    else:
        sample_id = transactions[len(transactions)//2]["transaction_id"]

    print(f"🔎 Searching for transaction_id: {sample_id}")

    # Linear search timing
    start = time.time()
    result1 = linear_search(transactions, sample_id)
    end = time.time()
    print("Linear search result:", result1)
    print("Time:", end - start)

    # Dictionary lookup timing
    tx_dict = build_dict(transactions)
    start = time.time()
    result2 = dict_lookup(tx_dict, sample_id)
    end = time.time()
    print("Dict lookup result:", result2)
    print("Time:", end - start)
