import os
from flask import Flask, send_from_directory
from flask_ngrok import run_with_ngrok
from progress_data import progress_data

app = Flask(__name__)
run_with_ngrok(app)

<<<<<<< HEAD
@app.route('/')
def send_welcome_data():
    data = {"Welcome! Do you want to go abroad to study?": ["Yes", "No", "Maybe"],
            "What is stopping you from studying abroad?": ["Finances", "Low scores", "Other"]}
    return data


=======
>>>>>>> 0b37de59013556871225fc8442d099d07b443bc7
@app.route('/progress/', methods=['POST', 'GET'])
def send_progress_data():
    prog_data = {"progress": progress_data()}
    return prog_data


@app.route('/univeristy_predictor/', methods={'POST', 'GET'})
def send_uni_data():
    return 'Sorry, this is still under construction!'

if __name__ == '__main__':
    app.run()