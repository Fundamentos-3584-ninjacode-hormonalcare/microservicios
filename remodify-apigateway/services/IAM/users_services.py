from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_IAM
from models.Users import UsersResource

users_router = APIRouter()

@users_router.get("/users/")
async def route_to_service_users(request: Request):
    url = f"{MICROSERVICE_IAM}/users"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@users_router.get("/users/{userId}")
async def route_to_service_users(request: Request, userId: int):
    if userId <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    url = f"{MICROSERVICE_IAM}/users/{userId}"
    response = requests.get(url, headers=request.headers)
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="ID not found")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()

@users_router.put("/users/{userId}")
async def route_to_service_users(request: Request, userId: int, usersResource: UsersResource):
    if userId <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    url = f"{MICROSERVICE_IAM}/users/{userId}"
    response = requests.put(url, headers=request.headers, json=usersResource.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()