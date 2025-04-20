import requests

response = requests.get('http://localhost:8080/get_json')
if response.status_code == 200:
    json_data = response.json()
    print("Received JSON 8080 port:", json_data["sequence"])
else:
    print("Error:", response.status_code)

response2 = requests.get('http://localhost:8081/get_json')

if response2.status_code == 200:
    json_data = response2.json()
    print("Received JSON 8081 port:", json_data["sequence"])
else:
    print("Error:", response2.status_code)
