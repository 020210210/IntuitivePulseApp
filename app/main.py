import signal
import sys
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/heartbeat')
def heartbeat():
    heart_rate = random.randint(60, 120)
    return jsonify({"heart_rate": heart_rate})

def handle_exit(signum, frame):
    print("Shutting down server gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
