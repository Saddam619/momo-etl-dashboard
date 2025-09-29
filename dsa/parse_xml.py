#!/usr/bin/env python3
"""
dsa/parse_xml.py
Parse modified_sms_v2.xml -> /dsa/parsed_data.json
"""

import re
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Paths
INPUT_XML = Path("data/raw/modified_sms_v2.xml")
OUT_JSON = Path("dsa/parsed_data.json")

# Regex patterns
AMOUNT_RE = re.compile(r'(\d{1,3}(?:[,\s]\d{3})*|\d+)\s*RWF', re.IGNORECASE)
TXID_RE = re.compile(r'(?:TxId:|Financial Transaction Id:)\s*([0-9A-Za-z\-]+)', re.IGNORECASE)
FEE_RE = re.compile(r'Fee\s*was[: ]*\s*([0-9,]+)\s*RWF', re.IGNORECASE)
BALANCE_RE = re.compile(r'(?:new balance[: ]*|NEW BALANCE[: ]*)([0-9,]+)\s*RWF', re.IGNORECASE)
RECEIVED_RE = re.compile(r'You have received\s+([0-9,]+)\s*RWF\s+from\s+([A-Za-z .\-]+)\s*\(?([+\d\*]{6,})?\)?', re.IGNORECASE)
PAYMENT_RE = re.compile(r'payment of\s+([0-9,]+)\s*RWF\s+to\s+([A-Za-z .\-0-9]+)', re.IGNORECASE)
TRANSFER_RE = re.compile(r'transferred to\s+([A-Za-z .\-]+)\s*\(?([+\d\*]{6,})?\)?', re.IGNORECASE)

def parse_sms_element(elem):
    """Parse a single <sms> element into a dictionary."""
    attrs = elem.attrib
    body = attrs.get("body", "") or ""
    epoch_ms = attrs.get("date")

    # timestamp
    timestamp = None
    if epoch_ms and epoch_ms.isdigit():
        try:
            ts = int(epoch_ms) / 1000.0
            timestamp = datetime.utcfromtimestamp(ts).isoformat() + "Z"
        except Exception:
            timestamp = attrs.get("readable_date")
    else:
        timestamp = attrs.get("readable_date")

    tx = {
        "transaction_id": None,
        "transaction_type": None,
        "amount": None,
        "fee": None,
        "balance": None,
        "sender": None,
        "receiver": None,
        "timestamp": timestamp,
        "raw": body
    }

    # Transaction ID
    m = TXID_RE.search(body)
    if m:
        tx["transaction_id"] = m.group(1).strip()
    else:
        tx["transaction_id"] = f"local-{attrs.get('date')}"

    # Amount
    m = AMOUNT_RE.search(body)
    if m:
        tx["amount"] = int(m.group(1).replace(",", "").replace(" ", ""))

    # Fee
    m = FEE_RE.search(body)
    if m:
        tx["fee"] = int(m.group(1).replace(",", ""))

    # Balance
    m = BALANCE_RE.search(body)
    if m:
        tx["balance"] = int(m.group(1).replace(",", ""))

    # Received
    m = RECEIVED_RE.search(body)
    if m:
        tx["transaction_type"] = "receive"
        tx["amount"] = int(m.group(1).replace(",", ""))
        tx["sender"] = {"name": m.group(2).strip(), "phone": m.group(3)}

    # Payment
    m = PAYMENT_RE.search(body)
    if m:
        tx["transaction_type"] = "payment"
        tx["amount"] = int(m.group(1).replace(",", ""))
        tx["receiver"] = {"name": m.group(2).strip()}

    # Transfer
    m = TRANSFER_RE.search(body)
    if m:
        tx["transaction_type"] = "transfer"
        tx["receiver"] = {"name": m.group(1).strip(), "phone": m.group(2)}

    # Deposit
    if "bank deposit" in body.lower():
        tx["transaction_type"] = "deposit"

    # Fallback type
    if not tx["transaction_type"]:
        low = body.lower()
        if "received" in low:
            tx["transaction_type"] = "receive"
        elif "payment" in low:
            tx["transaction_type"] = "payment"
        elif "transferred" in low:
            tx["transaction_type"] = "transfer"
        elif "deposit" in low:
            tx["transaction_type"] = "deposit"
        else:
            tx["transaction_type"] = "other"

    return tx

def parse_file(input_path=INPUT_XML):
    """Parse the full XML file."""
    tree = ET.parse(str(input_path))
    root = tree.getroot()
    sms_elems = root.findall(".//sms")
    parsed = [parse_sms_element(elem) for elem in sms_elems]
    return parsed

def save_json(data, out_path=OUT_JSON):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f" Wrote {len(data)} transactions to {out_path}")

def main():
    parsed = parse_file()
    save_json(parsed)

if __name__ == "__main__":
    main()
