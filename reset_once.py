import os
import requests

BASE_URL = "https://pasar.ufou008.com:2096"
TARGET_USER = "Test22"

r = requests.post(
    f"{BASE_URL}/api/admin/token",
    data={"username": os.environ["PANEL_USER"], "password": os.environ["PANEL_PASS"]},
    timeout=30,
)
r.raise_for_status()
token = r.json()["access_token"]

r = requests.post(
    f"{BASE_URL}/api/user/{TARGET_USER}/reset",
    headers={"Authorization": f"Bearer {token}"},
    timeout=30,
)
print(r.status_code, r.text)
r.raise_for_status()
