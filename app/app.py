from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sos_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

# Создание БД
@app.before_first_request
def create_tables():
    db.create_all()

# Эндпоинт для SOS-сигнала
@app.route('/sos', methods=['POST'])
def sos():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    
    if not user:
        user = User(username=data['username'], latitude=data['latitude'], longitude=data['longitude'])
        db.session.add(user)
    else:
        user.latitude = data['latitude']
        user.longitude = data['longitude']
    
    db.session.commit()
    socketio.emit('update_location', {'username': user.username, 'latitude': user.latitude, 'longitude': user.longitude})
    
    return jsonify({"message": "SOS сигнал отправлен!"})

# Событие для чата
@socketio.on('send_message')
def handle_message(data):
    emit('receive_message', data, broadcast=True)

# Запуск сервера
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
