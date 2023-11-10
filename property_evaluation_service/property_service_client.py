import requests

url = 'http://localhost:8080/property/evaluate/60101'
response = requests.get(url)

if response.status_code == 200:
    extracted_info = response.json()
    print(extracted_info)
else:
    print(f"Error: {response.status_code}")