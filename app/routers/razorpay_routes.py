from fastapi import APIRouter, Form
import requests
from ..config import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET

app = APIRouter()

@app.post("/create-payment-link")
def create_payment_link(amount: float = Form(...), mobile_number: str = Form(...)):
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

    response = requests.post(
        url,
        auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET),
        json=payload
    )
    return response.json()
