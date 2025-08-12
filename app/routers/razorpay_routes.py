import requests
from fastapi import APIRouter, Form, HTTPException
from app.config import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET


router = APIRouter()

@router.post("/create-payment-link")
def create_payment_link(amount: float = Form(...), mobile_number: str = Form(...)):
    if not RAZORPAY_KEY_ID or not RAZORPAY_KEY_SECRET:
        raise HTTPException(status_code=500, detail="Razorpay credentials not configured")

    url = "https://api.razorpay.com/v1/payment_links"
    payload = {
        "amount": int(amount * 100),
        "currency": "INR",
        "customer": {
            "contact": mobile_number
        },
        "notify": {
            "sms": True
        },
        "callback_url": "https://example.com/payment-success",
        "callback_method": "get"
    }

    try:
        response = requests.post(
            url,
            auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET),
            json=payload
        )
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
