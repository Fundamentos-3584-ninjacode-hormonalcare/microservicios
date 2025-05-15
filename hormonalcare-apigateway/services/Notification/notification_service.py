from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_NOTIFICATION

notification_router = APIRouter()


@notification_router.get("/notifications")
async def get_all_notifications(request: Request):
    """
    Get all notifications
    """
    url = f"{MICROSERVICE_NOTIFICATION}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@notification_router.get("/notifications/{id}")
async def get_notification_by_id(request: Request, id: str):
    """
    Get a specific notification by ID
    """
    url = f"{MICROSERVICE_NOTIFICATION}/{id}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@notification_router.post("/notifications")
async def create_notification(request: Request):
    """
    Create a new notification
    """
    url = f"{MICROSERVICE_NOTIFICATION}"
    response = requests.post(url, headers=request.headers, json=await request.json())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@notification_router.put("/notifications/{id}")
async def update_notification(request: Request, id: str):
    """
    Update an existing notification
    """
    url = f"{MICROSERVICE_NOTIFICATION}/{id}"
    response = requests.put(url, headers=request.headers, json=await request.json())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@notification_router.delete("/notifications/{id}")
async def delete_notification(request: Request, id: str):
    """
    Delete a notification
    """
    url = f"{MICROSERVICE_NOTIFICATION}/{id}"
    response = requests.delete(url, headers=request.headers)
    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return {"message": "Notification deleted successfully"}
