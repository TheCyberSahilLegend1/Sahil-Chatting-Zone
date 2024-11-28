from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sahil_secret_key'
socketio = SocketIO(app)

# Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# Handle Messages
@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)  # Send message to all users

if __name__ == '__main__':
    socketio.run(app, debug=True
