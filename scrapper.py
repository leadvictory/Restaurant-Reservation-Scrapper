import requests

url = "https://widget-api.formitable.com/api/availability/dd312595/day/2025-08-27T12:30:00.000Z/25/nl"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://widget.formitable.com",
    "Referer": "https://widget.formitable.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)   # Pretty-print JSON
else:
    print("Error:", response.status_code, response.text)
