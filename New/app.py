from flask import Flask, render_template, request
import joblib
from model import prepare_data_and_train_model, predict_heart_disease

app = Flask(__name__)

model = joblib.load('model.pkl')

feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.form.to_dict()

        # Match input values to feature names
        input_values = [float(input_data.get(field, 0.0)) for field in feature_names]

        prediction_msg = predict_heart_disease(model, input_values)

        response = {
            'prediction': prediction_msg,
            'input_data': input_data
        }

        return render_template('report.html', result=response)

    except Exception as e:
        print(e)
        return "An error occurred."

if __name__ == '__main__':
    app.run(debug=True)
