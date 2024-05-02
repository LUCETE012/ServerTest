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

# def run_server():
#     socketio.run(app, host='localhost', port=4000, debug=True)

if __name__ == '__main__':
    # server_thread = Thread(target=run_server)
    # server_thread.start()

    # send_thread=Thread(target=send_message)
    # send_thread.start()

    # server_thread.join()
    # send_thread.join()
    socketio.run(app, host='localhost', port=4000, debug=True)
