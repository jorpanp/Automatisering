import requests

url = 'https://httpbin.org/post'
data = {'key': 'value'}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json)