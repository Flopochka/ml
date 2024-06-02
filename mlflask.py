# Сервер

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Загрузка моделей при запуске сервера
model_mlbusiness = joblib.load("mlbusiness.pkl")
model_mleconomy = joblib.load("mleconomy.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    predictions_list = []

    for data_point in data:
        model_name = data_point.pop('model', None)  # Удаляем столбец 'model' и получаем его значение
        if model_name == 'mlbusiness':
            model = model_mlbusiness
        elif model_name == 'mleconomy':
            model = model_mleconomy
        else:
            return jsonify({'error': 'Invalid model name'}), 400

        df = pd.DataFrame([data_point])
        predictions = model.predict(df)
        rounded_predictions = [int(round(pred)) for pred in predictions]
        predictions_list.append({'input_data': data_point, 'predictions': rounded_predictions})

    return jsonify({'predictions': predictions_list})

@app.route('/log_mape', methods=['POST'])
def log_mape():
    data = request.get_json()
    mape = data.get('mape')
    print(f"Received MAPE: {mape}")
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5123, debug=True)
