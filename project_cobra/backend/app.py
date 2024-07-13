from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('../frontend/static', path)

if __name__ == '__main__':
    app.run(debug=True)
