# Payment & Notification Dashboard

A lightweight admin dashboard built with **FastAPI** that allows administrators to:

- Create **Razorpay** payment links for users.
- Send **push notifications** via **OneSignal**.

This tool combines payment and messaging workflows into a simple web interface powered by HTML, CSS (Bootstrap), and REST APIs.

---

## Project Structure

Dabb_Task/
├── app/
│   ├── routers/
│   │   ├── onesignal_routes.py    # Handles notification logic
│   │   └── razorpay_routes.py     # Handles payment link creation
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css          # Custom dashboard styling
│   │   └── js/
│   │       ├── OneSignalSDKWorker.js   # OneSignal service worker file
│   │       └── OneSignalSDK.sw.js      # OneSignal service worker file
│   ├── templates/
│   │   └── dashboard.html         # Main frontend UI
│   ├── config.py                  # Configuration handling
│   └── main.py                   # FastAPI entry point
├── .env                         # Environment variables (secret keys)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation


## Features

- Generate **Razorpay** payment links dynamically from the dashboard.
- Send **OneSignal** push notifications with a title and message.
- Clean, responsive UI .
- Simple JSON API responses for easy debugging and integration.

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML5,CSS3, Bootstrap 5
- **APIs:** Razorpay, OneSignal
- **Deployment:** Localhost (dev).

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Vigneshcode-Tech/Dabb_Task.git
cd Dabb_Task
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Mac/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate.bat

pip install -r requirements.txt
```


## 3. API Endpoints

**Endpoint** `/send-notification`  
**Method:** POST  
**Description:** Sends a push notification using OneSignal.  
**Request Parameters (Form Data):**  
- `title` (string): Notification title  
- `description` (string): Notification message content  

**Response:** JSON indicating success or failure of the notification request.

---

**Endpoint** `/create-payment-link`  
**Method:** POST  
**Description:** Creates a payment link using Razorpay's API.  
**Request Parameters (Form Data or JSON):**  
- `amount` (number): Amount in INR (decimal)  
- `mobile_number` (string): Customer's contact number  

**Response:** JSON containing the payment link and related info.


### 4. Run the Application
```bash
uvicorn app.main:app --reload
```

---
**Author:** Vignesh Natchimuthu

