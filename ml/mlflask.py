from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Создание Flask-приложения
app = Flask(__name__)

# Загрузка обученной модели при запуске сервера
model = joblib.load("mlbusiness.pkl")

# Эндпоинт для предсказаний
@app.route('/predict', methods=['POST'])
def predict():
    # Получение данных из запроса
    data = request.get_json()

    # Преобразование данных в DataFrame
    df = pd.DataFrame(data)

    # Выполнение предсказаний с помощью загруженной модели
    predictions = model.predict(df)

    # Округление предсказанных значений до ближайшего целого числа
    rounded_predictions = [int(round(pred)) for pred in predictions]

    # Возвращение результатов в формате JSON в виде массива
    return jsonify({'predictions': rounded_predictions})

# Эндпоинт для логирования MAPE
@app.route('/log_mape', methods=['POST'])
def log_mape():
    # Получение данных из запроса
    data = request.get_json()
    mape = data.get('mape')
    print(f"Received MAPE: {mape}")
    return jsonify({'status': 'success'}), 200

# Запуск Flask-приложения
if __name__ == '__main__':
    app.run(debug=True)
