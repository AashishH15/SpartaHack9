# app.py
from flask import send_from_directory
from server import server
from main import app

@server.route('/')
def serve_index():
    return send_from_directory(server.static_url_path, 'index.html')

if __name__ == '__main__':
    app.run_server(debug=True)