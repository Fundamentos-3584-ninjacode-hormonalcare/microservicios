from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_COMMUNICATION

communication_router = APIRouter()


@communication_router.get("/communications")
async def get_all_communications(request: Request):
    """
    Get all communications
    """
    url = f"{MICROSERVICE_COMMUNICATION}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@communication_router.get("/communications/{id}")
async def get_communication_by_id(request: Request, id: str):
    """
    Get a specific communication by ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/{id}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@communication_router.post("/communications")
async def create_communication(request: Request):
    """
    Create a new communication
    """
    url = f"{MICROSERVICE_COMMUNICATION}"
    response = requests.post(url, headers=request.headers, json=await request.json())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@communication_router.put("/communications/{id}")
async def update_communication(request: Request, id: str):
    """
    Update an existing communication
    """
    url = f"{MICROSERVICE_COMMUNICATION}/{id}"
    response = requests.put(url, headers=request.headers, json=await request.json())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@communication_router.delete("/communications/{id}")
async def delete_communication(request: Request, id: str):
    """
    Delete a communication
    """
    url = f"{MICROSERVICE_COMMUNICATION}/{id}"
    response = requests.delete(url, headers=request.headers)
    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return {"message": "Communication deleted successfully"}
