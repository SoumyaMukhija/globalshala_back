import os
from flask import Flask, send_from_directory, request
from flask_ngrok import run_with_ngrok
from progress_data import progress_data
from feed_data import feed_data
from univ_data import univ_data
from predictions.train import read_regressors_and_predict

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


@app.route("/predict", methods=['POST'])
def predict():
    # Fetch data frontend
    data = request.json
    print(data)
    if(data is not None):
        uni = data['institute']
        print(uni)
        all_uni = univ_data()
        selectedUni = [x for x in all_uni if x.get(uni) is not None][0]
        selectedUniRating = selectedUni[uni]
        user_info = {
            "GRE Score": [int(data.get('gre', 0))],
            "TOEFL Score": [int(data.get('toefl', 0))],
            "CGPA": [float(data.get('cgpa', 0))],
            "University Rating": [int(selectedUniRating)],
            "Research": [int(data.get('researched') == True)]
        }
        predict = read_regressors_and_predict(user_info)
        return {"prediction": "You have "+predict+" percent chance of getting into "+uni}
    else:
        return {"prediction": "Could not parse form. Try again"}


@app.route('/feed_data/', methods=['POST', 'GET'])
def send_feed_data():
    fd = {"feed data": feed_data()}
    return fd


@app.route('/take_prediction_data/', methods=['POST', 'GET'])
def take_prediction_data(response):
    data = response.json()
    print(data)


@app.route('/univ_prediction/', methods=['POST', 'GET'])
def send_prediction_data(user_data):
    #chance = get_combined_stats(user_data)
    # return chance
    print(user_data)


if __name__ == '__main__':
    app.run()
