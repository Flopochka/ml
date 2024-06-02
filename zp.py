# Клиент

import requests
import pandas as pd

# URL вашего Flask-сервера
url_predict = 'http://localhost:5123/predict'

# Пример нескольких наборов данных
data_from_openserver = [
    {
        'model': 'mlbusiness',
        'date': '24.03.2023',
        'airline': 'Air India',
        'dep_time': '05:45',
        'from': 'Mumbai',
        'stop': '1-stop',
        'to': 'Delhi',
    },
    {
        'model': 'mleconomy',
        'date': '25.03.2023',
        'airline': 'Jet Airways',
        'dep_time': '08:30',
        'from': 'Delhi',
        'stop': 'non-stop',
        'to': 'Mumbai',
    }
]

# Преобразование наборов данных в DataFrame
df = pd.DataFrame(data_from_openserver)

# Преобразование DataFrame в список словарей для отправки в формате JSON
data_json = df.to_dict(orient='records')

# Отправка POST-запроса на сервер Flask для получения предсказанных цен
response_predict = requests.post(url_predict, json=data_json)

# Получение результатов предсказания из ответа
predictions_list = response_predict.json()['predictions']

# Вывод предсказаний для каждого набора данных
for idx, prediction_data in enumerate(predictions_list):
    print(prediction_data['predictions'])
