from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
