import requests

url = "https://etender-connect.com/v1/restaurants/37374/availability/2025/08/29"
params = {
    "partysize": 1
}
headers = {
    "accept": "application/json, text/plain, */*",
    "authorization": "AccessKey 7426413c23200f86b5ed858f1fd309dfc9e01b86",
    "origin": "https://32goes.nl",
    "referer": "https://32goes.nl/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "x-environment": "Production"
}

response = requests.get(url, headers=headers, params=params)

# Print status and JSON response
print("Status:", response.status_code)
print("Response JSON:")
print(response.json())