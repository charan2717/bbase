from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"

# CORS setup: allow only your Vercel frontend
CORS(app, supports_credentials=True, origins=["https://bbase-yrj2.onrender.com"])

# SocketIO with correct CORS
socketio = SocketIO(app, cors_allowed_origins=["https://bbase-yrj2.onrender.com"], async_mode="eventlet")

@app.route("/")
def index():
    return render_template("chat.html")  # Optional for testing, or serve from frontend only

@socketio.on("message")
def handle_message(msg):
    print(f"Received message: {msg}")
    socketio.send(msg, broadcast=True)

if __name__ == "__main__":
    import eventlet
    import eventlet.wsgi
    print("Server running on http://0.0.0.0:5000")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
