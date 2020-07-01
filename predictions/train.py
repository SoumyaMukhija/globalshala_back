import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso


def get_dataframe_from_file(file="Admission_Predict_Ver1.1.csv"):
    return pd.read_csv(file)


def clean_data_in_dataframe(df):
    if df is not None:
        return df.dropna(axis=0)
    else:
        print("Missing dataframe")


def remove_additional_columns(df):
    return df[['GRE Score', 'TOEFL Score', 'CGPA', 'University Rating', 'Research' 'Chance of Admit ']]


def get_linear_regressor(df):
    feature = df['Chance of Admit ']
    labels = df.drop('Chance of Admit ', axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        labels, feature, test_size=0.10)
    r = LinearRegression(normalize=True)
    r = r.fit(x_train, y_train)
    return r


def get_rf_regressor(df):
    feature = df['Chance of Admit ']
    labels = df.drop('Chance of Admit ', axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        labels, feature, test_size=0.10)
    r = RandomForestRegressor(
        n_estimators=100, random_state=42, criterion="mse")
    r = r.fit(x_train, y_train)
    return r


def get_lasso_regressor(df):
    feature = df['Chance of Admit ']
    labels = df.drop('Chance of Admit ', axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        labels, feature, test_size=0.10)
    r = Lasso()
    r = r.fit(x_train, y_train)
    return r


def get_combined_stats(df):
    return df.groupby("University Rating").mean()


if __name__ == '__main__':
    df = get_dataframe_from_file()
    # print(df.shape) 400 rows with 9 columns
    df = clean_data_in_dataframe(df)
    # print(df.shape) 400 rows with 9 columns
    df = remove_additional_columns(df)
    # print(df.shape) 400 rows with 5 columns
    user_dictionary = {'GRE Score': [325], 'TOEFL Score': [
        111], 'CGPA': [8.2], 'University Rating': [4], 'Research': [0]}
    user_info = pd.DataFrame(user_dictionary)
    # user = np.array([[325,112,7.5]]).reshape(1, -1)

    pred_dictionary = {}

    clf = get_rf_regressor(df)
    prediction = clf.predict(user_info)
    print("Random forest", prediction)
    pred_dictionary['rf'] = prediction

    clf = get_linear_regressor(df)
    prediction = clf.predict(user_info)
    print("Linear", prediction)
    pred_dictionary['linear'] = prediction

    clf = get_lasso_regressor(df)
    prediction = clf.predict(user_info)
    print("Lasso", prediction)
    pred_dictionary['lasso'] = prediction

    print("Result:", min(pred_dictionary.values()))
