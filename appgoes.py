from fastapi import FastAPI, Query
import requests

app = FastAPI()

BASE_URL = "https://etender-connect.com/v1/restaurants/37374/availability"
API_KEY = "7426413c23200f86b5ed858f1fd309dfc9e01b86"  # replace if needed

@app.get("/availability")
def get_availability(
    date: str = Query(..., description="Date in YYYY-MM-DD format"),
    partysize: int = Query(2, description="Number of people")
):
    """
    Proxy endpoint to fetch availability from etender-connect.com
    Example: /availability?date=2025-08-29&partysize=2
    """
    url = f"{BASE_URL}/{date.replace('-', '/')}"
    params = {"partysize": partysize}
    headers = {
        "Accept": "application/json",
        "Authorization": f"AccessKey {API_KEY}",
        "x-environment": "Production",
        "User-Agent": "FastAPI Proxy"
    }

    resp = requests.get(url, headers=headers, params=params)

    try:
        return resp.json()
    except Exception:
        return {"error": f"Status {resp.status_code}", "text": resp.text}
