import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Эндпоинт для запуска запросов
@app.route('/')
def make_requests():
    ip_addresses = []
    
    # Делаем 10 запросов к API ipify
    for i in range(10):
        try:
            response = requests.get('https://api64.ipify.org?format=json')
            if response.status_code == 200:
                ip_data = response.json()
                ip_addresses.append(ip_data['ip'])
                print(f"Запрос {i+1}: IP - {ip_data['ip']}")
            else:
                ip_addresses.append(f"Запрос {i+1}: Ошибка {response.status_code}")
        except Exception as e:
            ip_addresses.append(f"Запрос {i+1}: Ошибка - {str(e)}")
    
    return jsonify(ip_addresses)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
