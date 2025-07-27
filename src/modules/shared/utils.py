import os
import requests

GHL_API_BASE_URL = "https://rest.gohighlevel.com/v1"
GHL_API_KEY = os.getenv("GHL_API_KEY")

def ghl_api_request(method, endpoint, token=None, data=None, params=None):
    """Send an authenticated request to the GoHighLevel API."""
    headers = {
        "Authorization": f"Bearer {token or GHL_API_KEY}",
        "Content-Type": "application/json"
    }
    url = f"{GHL_API_BASE_URL}{endpoint}"
    resp = requests.request(method, url, headers=headers, json=data, params=params)
    resp.raise_for_status()
    return resp.json()
