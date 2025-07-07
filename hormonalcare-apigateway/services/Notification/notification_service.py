from fastapi import APIRouter, Request, HTTPException, Path
from fastapi.responses import JSONResponse
import requests
from configs.url_services import MICROSERVICE_NOTIFICATION

notification_router = APIRouter()


@notification_router.get("/notifications")
async def get_all_notifications(request: Request):
    """
    Get all notifications
    """
    url = f"{MICROSERVICE_NOTIFICATION}/notification"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Notification error: {response.text}"})


@notification_router.get("/notifications/recipient/{recipientId}")
async def get_notifications_by_recipient_id(request: Request, recipientId: int = Path(...)):
    """
    Get notifications by recipient ID
    """
    url = f"{MICROSERVICE_NOTIFICATION}/notification/notifications/recipient/{recipientId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Notification error: {response.text}"})


@notification_router.get("/notifications/{notificationId}")
async def get_notification_by_id(request: Request, notificationId: int = Path(...)):
    """
    Get a notification by ID
    """
    url = f"{MICROSERVICE_NOTIFICATION}/notification/{notificationId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Notification error: {response.text}"})


@notification_router.post("/notifications")
async def create_notification(request: Request):
    """
    Create a new notification
    """
    url = f"{MICROSERVICE_NOTIFICATION}/notification"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Notification error: {response.text}"})


@notification_router.put("/notifications/{notificationId}/state")
async def update_notification_state(request: Request, notificationId: int = Path(...)):
    """
    Update notification state
    """
    url = f"{MICROSERVICE_NOTIFICATION}/notification/{notificationId}/state"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Notification error: {response.text}"})


@notification_router.delete("/notifications/{notificationId}")
async def delete_notification(request: Request, notificationId: int = Path(...)):
    """
    Delete a notification
    """
    url = f"{MICROSERVICE_NOTIFICATION}/notification/{notificationId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"message": "Notification deleted successfully"}
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Notification error: {response.text}"})
