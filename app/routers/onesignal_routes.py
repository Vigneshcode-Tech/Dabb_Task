import os
import requests
from fastapi import APIRouter, Form, HTTPException
from app.config import ONESIGNAL_APP_ID, ONESIGNAL_API_KEY
from dotenv import load_dotenv



router = APIRouter()

@router.post("/send-notification")
def send_notification(title: str = Form(...), description: str = Form(...)):
    
    if not ONESIGNAL_APP_ID or not ONESIGNAL_API_KEY:
        raise HTTPException(status_code=500, detail="OneSignal credentials not configured.")

    url = "https://onesignal.com/api/v1/notifications"
    hardcoded_player_id = "7d38cf98-b218-4439-bc40-b107f38802e3"
    
    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "headings": {"en": title},
        "contents": {"en": description},
        "include_player_ids": [hardcoded_player_id] 
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {ONESIGNAL_API_KEY}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
