import os
from flask import Flask, send_from_directory
from flask_ngrok import run_with_ngrok
from progress_data import progress_data
from feed_data import feed_data
from univ_data import univ_data
from predictions.train import get_combined_stats

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/progress/', methods=['POST', 'GET'])
def send_progress_data():
    prog_data = {"progress": progress_data()}
    return prog_data


@app.route('/univ_ranking/', methods=['POST', 'GET'])
def send_uni_data():
    ud = {"university ranking data": univ_data()}
    return ud


@app.route('/feed_data/', methods=['POST', 'GET'])
def send_feed_data():
    fd = {"feed data": feed_data()}
    return fd


@app.route('/univ_prediction/', methods=['POST', 'GET'])
def send_prediction_data(user_data):
    #chance = get_combined_stats(user_data)
    # return chance
    print(user_data)


if __name__ == '__main__':
    app.run()
