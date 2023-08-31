from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message_from_client')
def handle_message(message):
    print(f"Message from client: {message}")
    emit('message_from_server', f"Server received: {message}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
    