from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_IAM
from models.Profiles import ProfilesResource

profiles_router = APIRouter()

@profiles_router.get("/profiles")
async def route_to_service_profiles(request: Request):
    url = f"{MICROSERVICE_IAM}/profiles"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@profiles_router.post("/profiles")
async def route_to_service_profiles(request: Request, profilesResource: ProfilesResource):
    url = f"{MICROSERVICE_IAM}/profiles"
    response = requests.post(url, headers=request.headers, json=profilesResource.dict())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@profiles_router.get("/profiles/{profileId}")
async def route_to_service_profiles(request: Request, profileId: int):
    if profileId <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    url = f"{MICROSERVICE_IAM}/profiles/{profileId}"
    response = requests.get(url, headers=request.headers)
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="ID not found")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()