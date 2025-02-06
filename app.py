from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def index():
    return render_template("chat.html")

@socketio.on("message")
def handle_message(msg):
    socketio.send(msg, broadcast=True)

if __name__ == "__main__":
    import eventlet
    import eventlet.wsgi
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
