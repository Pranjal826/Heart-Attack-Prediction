import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

def prepare_data_and_train_model():
    # Load the dataset
    heart_data = pd.read_csv('./heart_disease_data.csv')

    # Prepare the data
    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']

    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
    return model

def predict_heart_disease(model, input_data):
    input_values_as_numpy_array = np.asarray(input_data)
    input_reshaped = input_values_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_reshaped)
    
    prediction_msg = "Does not have a heart disease" if prediction[0] == 0 else "Has a heart disease"
    return prediction_msg

if __name__ == '__main__':
    trained_model = prepare_data_and_train_model()
    joblib.dump(trained_model, 'model.pkl')
