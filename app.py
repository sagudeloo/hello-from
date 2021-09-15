from flask import Flask
import socket

app = Flask(__name__)
local_ip = socket.gethostbyname(socket.gethostname())

@app.route("/")
def hello_world():
    return f'<h1>Hello from {local_ip}</h1>'