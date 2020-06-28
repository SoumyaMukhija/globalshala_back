import os
from flask import Flask, send_from_directory
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def send_dummy_data():
    data = {"Dummy": "data"}
    return data


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img/'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
