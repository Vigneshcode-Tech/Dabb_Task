from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import os
from .routers import razorpay_routes, onesignal_routes

app = FastAPI(title="Dashboard Integration App")

STATIC_DIR = "static"
# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

app.include_router(razorpay_routes.router)
app.include_router(onesignal_routes.router)

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Serve OneSignal service workers explicitly at root
@app.get("/OneSignalSDKWorker.js")
async def onesignal_worker_js():
    return FileResponse(os.path.join(static_path, "OneSignalSDKWorker.js"))

@app.get("/OneSignalSDK.sw.js")
async def onesignal_sw_js():
    return FileResponse(os.path.join(static_path, "OneSignalSDK.sw.js"))

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "page_title": "Dashboard"}
    )
