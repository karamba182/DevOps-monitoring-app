from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)
start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route("/")
def index():
    return f"""
    <h1>SFTP Server Status</h1>
    <p><strong>Hostname:</strong> {hostname}</p>
    <p><strong>IP Address:</strong> {ip_address}</p>
    <p><strong>Started at:</strong> {start_time}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
