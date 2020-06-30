'''This dataset belongs to: 
Mohan S Acharya, Asfia Armaan, Aneeta S Antony : A Comparison of Regression Models for Prediction of Graduate Admissions, IEEE International Conference on Computational Intelligence in Data Science 2019'''


import pandas as pd
import requests


def from_kaggle(data_sets, competition):
    """Fetches data from Kaggle

    Parameters
    ----------
    data_sets : (array)
        list of dataset filenames on kaggle. (e.g. train.csv.zip)

    competition : (string)
        name of kaggle competition as it appears in url
        (e.g. 'rossmann-store-sales')

    """
    kaggle_dataset_url = "https://www.kaggle.com/mohansacharya/graduate-admissions".format(
        competition)

    KAGGLE_INFO = {'UserName': config.kaggle_username,
                   'Password': config.kaggle_password}

    for data_set in data_sets:
        data_url = path.join(kaggle_dataset_url, data_set)
        data_output = path.join(config.raw_data_dir, data_set)
        # Attempts to download the CSV file. Gets rejected because we are not logged in.
        r = requests.get(data_url)
        # Login to Kaggle and retrieve the data.
        r = requests.post(r.url, data=KAGGLE_INFO, stream=True)
        # Writes the data to a local file one chunk at a time.
        with open(data_output, 'wb') as f:
            # Reads 512KB at a time into memory
            for chunk in r.iter_content(chunk_size=(512 * 1024)):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
