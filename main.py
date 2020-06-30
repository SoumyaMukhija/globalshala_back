import os
from flask import Flask, send_from_directory
from flask_ngrok import run_with_ngrok
from progress_data import progress_data

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def send_welcome_data():
    data = {"Welcome! Do you want to go abroad to study?": ["Yes", "No", "Maybe"],
            "What is stopping you from studying abroad?": ["Finances", "Low scores", "Other"]}
    return data


@app.route('/progress/', methods=['POST', 'GET'])
def send_progress_data():
    prog_data = progress_data()
    return prog_data


@app.route('/univeristy_predictor/', methods={'POST', 'GET'})
def send_uni_data():
    return 'Sorry, this is still under construction!'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img/'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
