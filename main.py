from uuid import uuid4
from flask.app import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
io = SocketIO(app, cors_allowed_origins='*')

@app.route("/")
def init():
    """default route"""

@io.on('connected')
def connection(msg):
    """show if exists a new connection into socket"""

    print(msg)

@io.on('notification')
def handle_notification(data):
    """watch the broadcast that send a notification"""

    print('received notification: ' + data)

if __name__ == '__main__':
    io.run(app, debug=True)
