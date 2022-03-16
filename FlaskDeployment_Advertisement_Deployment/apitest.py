import requests

url = "http://localhost:5000/api"

response = requests.get(url)
print(response.text)

data = [
        {"TV":10, "radio":100, "newspaper":100},
        {"TV":100, "radio":100, "newspaper":100},
        {"TV":1000, "radio":100, "newspaper":100},
        {"TV":10000, "radio":100, "newspaper":100},
        {"TV":100000, "radio":100, "newspaper":100}
        ]

response = requests.post(url, json=data)
print(response.text)