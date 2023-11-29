import requests

response = requests.get("http://api.openweathermap.org")
print(f'Ответ на 1 задание  - {response}')
