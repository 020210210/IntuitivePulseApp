from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Добро пожаловать в IntuitivePulseApp!</h1>'

@app.route('/about')
def about():
    return '<p>Это тестовая страница о проекте.</p>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
