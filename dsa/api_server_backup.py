#!/usr/bin/env python3
"""
REST API for parsed MoMo SMS transactions with Basic Auth
"""

import json
import urllib.parse
import base64
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

DATA_FILE = Path("dsa/parsed_data.json")

# Load JSON into memory
def load_data():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

transactions = load_data()

# Helper: find by transaction_id
def get_transaction(trans_id):
    for tx in transactions:
        if str(tx.get("transaction_id")) == str(trans_id):
            return tx
    return None

class MoMoAPIHandler(BaseHTTPRequestHandler):
    # --- AUTH ---
    def check_auth(self):
        auth_header = self.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Basic "):
            return False
        encoded = auth_header.split(" ")[1]
        decoded = base64.b64decode(encoded).decode("utf-8")
        return decoded == "admin:password"

    def require_auth(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="MoMo API"')
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())

    # --- Helpers ---
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    # --- Routes ---
    def do_GET(self):
        if not self.check_auth():
            return self.require_auth()

        parsed_path = urllib.parse.urlparse(self.path)
        parts = parsed_path.path.strip("/").split("/")

        if len(parts) == 1 and parts[0] == "transactions":
            self._set_headers(200)
            self.wfile.write(json.dumps(transactions, indent=2).encode())

        elif len(parts) == 2 and parts[0] == "transactions":
            tx_id = parts[1]
            tx = get_transaction(tx_id)
            if tx:
                self._set_headers(200)
                self.wfile.write(json.dumps(tx, indent=2).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_POST(self):
        if not self.check_auth():
            return self.require_auth()

        if self.path == "/transactions":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode()
            new_tx = json.loads(body)

            if not new_tx.get("transaction_id"):
                new_tx["transaction_id"] = f"local-{len(transactions)+1}"

            transactions.append(new_tx)
            save_data(transactions)

            self._set_headers(201)
            self.wfile.write(json.dumps(
                {"message": "Transaction added", "transaction": new_tx}, indent=2
            ).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_PUT(self):
        if not self.check_auth():
            return self.require_auth()

        parts = self.path.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "transactions":
            tx_id = parts[1]
            tx = get_transaction(tx_id)
            if not tx:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
                return

            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode()
            update_data = json.loads(body)

            tx.update(update_data)
            save_data(transactions)

            self._set_headers(200)
            self.wfile.write(json.dumps(
                {"message": "Transaction updated", "transaction": tx}, indent=2
            ).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

    def do_DELETE(self):
        if not self.check_auth():
            return self.require_auth()

        parts = self.path.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "transactions":
            tx_id = parts[1]
            tx = get_transaction(tx_id)
            if not tx:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
                return

            transactions.remove(tx)
            save_data(transactions)

            self._set_headers(200)
            self.wfile.write(json.dumps({"message": "Transaction deleted"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid endpoint"}).encode())

def run(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, MoMoAPIHandler)
    print(f"✅ API running at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()