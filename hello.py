import requests # helps to communicate with  API

latitude = 48.85
longitude = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url, verify=False)

print(response.status_code)
data=response.json()
data