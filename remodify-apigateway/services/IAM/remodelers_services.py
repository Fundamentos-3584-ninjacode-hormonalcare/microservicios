from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_IAM
from models.Remodelers import RemodelersResource

remodelers_router = APIRouter()

@remodelers_router.post("/remodelers")
async def route_to_service_remodelers(request: Request, remodelersResource: RemodelersResource):
    url = f"{MICROSERVICE_IAM}/remodelers"
    response = requests.post(url, headers=request.headers, json=remodelersResource.dict())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    remodeler_id = response.json().get("id")
    if not remodeler_id:
        raise HTTPException(status_code=400, detail="Invalid response from server")
    
    url = f"{MICROSERVICE_IAM}/remodelers/{remodeler_id}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()

@remodelers_router.get("/remodelers/{remodelerId}")
async def route_to_service_remodelers(request: Request, remodelerId: int):
    if remodelerId <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    url = f"{MICROSERVICE_IAM}/remodelers/{remodelerId}"
    response = requests.get(url, headers=request.headers)
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="ID not found")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()