import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('response')
def on_response(data):
    print(data['response'])
    sio.disconnect()

if __name__ == '__main__':
    message_to_send = input("Enter your message: ")

    sio.connect('http://localhost:8888')
    sio.emit('send_message', {'message': message_to_send})
    sio.wait()
