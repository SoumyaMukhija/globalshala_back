import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
import pickle   #read json


def get_dataframe_from_file(file="Admission_Predict_Ver1.1.csv"):
    return pd.read_csv(file)


def clean_data_in_dataframe(df):
    if df is not None:
        return df.dropna(axis=0)
    else:
        print("Missing dataframe")


def remove_additional_columns(df):
    return df[['GRE Score', 'TOEFL Score', 'CGPA', 'University Rating', 'Research', 'Chance of Admit ']]


def get_linear_regressor(df):
    feature = df['Chance of Admit ']
    labels = df.drop('Chance of Admit ', axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        labels, feature, test_size=0.10)
    r = LinearRegression(normalize=True)
    r = r.fit(x_train, y_train)
    with open('lr.pkl', 'wb') as out:
        pickle.dump(r,out)
    return r


def get_rf_regressor(df):
    feature = df['Chance of Admit ']
    labels = df.drop('Chance of Admit ', axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        labels, feature, test_size=0.10)
    r = RandomForestRegressor(
        n_estimators=100, random_state=42, criterion="mse")
    r = r.fit(x_train, y_train)
    with open('rf.pkl', 'wb') as out:
        pickle.dump(r,out)
    return r


def get_lasso_regressor(df):
    feature = df['Chance of Admit ']
    labels = df.drop('Chance of Admit ', axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        labels, feature, test_size=0.10)
    r = Lasso()
    r = r.fit(x_train, y_train)
    with open('ls.pkl', 'wb') as out:
        pickle.dump(r,out)
    return r


def save_regressors():

    df = get_dataframe_from_file()
    df = clean_data_in_dataframe(df)
    df = remove_additional_columns(df)

    get_linear_regressor(df)
    get_rf_regressor(df)
    get_lasso_regressor(df)


def read_regressors_and_predict(user_info):
    predictions = {}
    usr = pd.DataFrame(user_info)
    
    abspath = os.path.abspath('predictions/lr.pkl')
    with open(abspath, 'rb') as fin:
        r = pickle.load(fin)
        predictions['lr'] = r.predict(usr)

    abspath = os.path.abspath('predictions/rf.pkl')
    with open(abspath, 'rb') as fin:
        r = pickle.load(fin)
        predictions['rf'] = r.predict(usr)

    abspath = os.path.abspath('predictions/ls.pkl')
    with open(abspath, 'rb') as fin:
        r = pickle.load(fin)
        predictions['lasso'] = r.predict(usr)

    minval = min(predictions.values())
    return str(round(minval[0] * 100, 2))
