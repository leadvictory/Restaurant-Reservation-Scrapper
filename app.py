from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS so you can call from your HTML/JS frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # in production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Formitable API
# --------------------
@app.get("/formitable/availability")
def formitable_availability(
    date: str = Query(..., description="Date in YYYY-MM-DD"),
    people: int = Query(2, ge=1, le=25, description="Number of people (1–25)"),
):
    location_id = "dd312595"  # your restaurant ID
    url = f"https://widget-api.formitable.com/api/availability/{location_id}/day/{date}T12:30:00.000Z/{people}/nl"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://widget.formitable.com",
        "Referer": "https://widget.formitable.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/139.0.0.0 Safari/537.36",
    }

    resp = requests.get(url, headers=headers)
    return resp.json()


# --------------------
# Etender API
# --------------------
@app.get("/etender/availability")
def etender_availability(
    date: str = Query(..., description="Date in YYYY-MM-DD"),
    partysize: int = Query(2, ge=1, le=25, description="Number of people (1-11)"),
):
    restaurant_id = "37374"
    url = f"https://etender-connect.com/v1/restaurants/{restaurant_id}/availability/{date.replace('-', '/')}"
    params = {"partysize": partysize}

    headers = {
        "Accept": "application/json",
        "Authorization": "AccessKey 7426413c23200f86b5ed858f1fd309dfc9e01b86",
        "x-environment": "Production",
        "User-Agent": "FastAPI Proxy",
    }

    resp = requests.get(url, headers=headers, params=params)
    return resp.json()


# Run with:
# uvicorn app:app --reload --host 0.0.0.0 --port 5000
