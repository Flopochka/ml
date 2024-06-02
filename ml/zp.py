import requests
import pandas as pd

# URL вашего Flask-сервера
url_predict = 'http://localhost:5000/predict'

# Пример данных, которые могут быть получены с OpenServer
data_from_openserver = {
    'date': '24.03.2023',
    'airline': 'Air India',
    'dep_time': '05:45',
    'from': 'Mumbai',
    'stop': '1-stop',
    'to': 'Delhi',
}

# Преобразование данных в DataFrame и затем в словарь, чтобы отправить в формате JSON
df = pd.DataFrame([data_from_openserver])
data_json = df.to_dict(orient='records')

# Отправка POST-запроса на сервер Flask для получения предсказанных цен
response_predict = requests.post(url_predict, json=data_json)

# Получение результатов предсказания из ответа
predictions = response_predict.json()['predictions']

# Округление предсказанных значений до ближайшего целого числа
rounded_predictions = [int(round(pred)) for pred in predictions]

# URL вашего OpenServer, куда вы будете отправлять предсказанные цены
url_openserver = 'http://your_openserver_url'

# Отправка предсказанных цен на OpenServer
response_openserver = requests.post(url_openserver, json={'predictions': rounded_predictions})

print("Predictions sent to OpenServer:", rounded_predictions)
print("Server response:", response_openserver.text)
