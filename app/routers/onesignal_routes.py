import os
import requests
from fastapi import APIRouter, Form
from dotenv import load_dotenv

load_dotenv()

ONESIGNAL_APP_ID = os.getenv("ONESIGNAL_APP_ID")
ONESIGNAL_API_KEY = os.getenv("ONESIGNAL_API_KEY")

app = APIRouter()

@app.post("/send-notification")
def send_notification(title: str = Form(...), description: str = Form(...)):
    url = "https://onesignal.com/api/v1/notifications"
    
    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "headings": {"en": title},
        "contents": {"en": description},
        "included_segments": ["All"]
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {ONESIGNAL_API_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)
    return {"status_code": response.status_code, "data": response.json()}
