from flask import Flask, jsonify
import random

app = Flask(__name__)

def get_heart_rate():
    """Simulate heart rate readings (between 60-120 bpm)."""
    return random.randint(60, 120)

@app.route('/')
def home():
    return "Welcome to the Heart Rate Monitor!"

@app.route('/heart_rate', methods=['GET'])
def heart_rate():
    """Endpoint to get the current heart rate."""
    return jsonify({"heart_rate": get_heart_rate()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
