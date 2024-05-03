from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('client')
def hande_message(data):
    print('Received message: ', data)
    socketio.emit('client', data)

@socketio.on('connect')
def send_message(msg): 
    socketio.emit('test', 'Welcome')

if __name__ == '__main__':

    socketio.run(app, host='10.138.0.2', port=3000, debug=True)
