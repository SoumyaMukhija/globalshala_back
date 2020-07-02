import os
from flask import Flask, send_from_directory
from flask_ngrok import run_with_ngrok
from progress_data import progress_data
from feed_data import feed_data

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/progress/', methods=['POST', 'GET'])
def send_progress_data():
    prog_data = {"progress": progress_data()}
    return prog_data


@app.route('/univeristy_predictor/', methods={'POST', 'GET'})
def send_uni_data():
    return 'Sorry, this is still under construction!'


@app.route('/feed_data/', methods{'POST', 'GET'})
def send_feed_data():
    fd = {"feed data": feed_data()}
    return fd


if __name__ == '__main__':
    app.run()
