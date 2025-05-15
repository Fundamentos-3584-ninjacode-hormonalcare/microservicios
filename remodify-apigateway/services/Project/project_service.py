from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_PROJECT, MICROSERVICE_BUSINESS, MICROSERVICE_IAM
from models.Project import ProjectResource

project_router = APIRouter()

@project_router.get("/projects")
async def route_to_service_project(request: Request):
    url = f"{MICROSERVICE_PROJECT}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@project_router.post("/projects")
async def route_to_service_project(request: Request, projectResource: ProjectResource):
    # Validar que el businessId exista
    business_id = projectResource.businessId
    if business_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid businessId: Must be greater than 0")
    business_url = f"{MICROSERVICE_BUSINESS}/{business_id}"
    business_response = requests.get(business_url, headers=request.headers)
    if business_response.status_code == 404:
        raise HTTPException(status_code=400, detail="Invalid businessId: Business not found")
    elif business_response.status_code != 200:
        raise HTTPException(status_code=business_response.status_code, detail=business_response.json())
    
    # Validar que el contractorId exista
    contractor_id = projectResource.contractorId
    if contractor_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid contractorId: Must be greater than 0")
    contractor_url = f"{MICROSERVICE_IAM}/Contractors/{contractor_id}"
    contractor_response = requests.get(contractor_url, headers=request.headers)
    if contractor_response.status_code == 404:
        raise HTTPException(status_code=400, detail="Invalid contractorId: Contractor not found")
    elif contractor_response.status_code != 200:
        raise HTTPException(status_code=contractor_response.status_code, detail=contractor_response.json())
    
    # Si ambos IDs son válidos, proceder con la creación del proyecto
    url = f"{MICROSERVICE_PROJECT}"
    try:
        project_data = projectResource.dict()
        project_data['startDate'] = projectResource.startDate.isoformat()
        project_data['finishDate'] = projectResource.finishDate.isoformat()
        response = requests.post(url, headers=request.headers, json=project_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=response.status_code, detail=str(e))
    return response.json()

@project_router.get("/projects/{id}")
async def route_to_service_project(request: Request, id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    url = f"{MICROSERVICE_PROJECT}/{id}"
    response = requests.get(url, headers=request.headers)
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="ID not found")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()

@project_router.get("/projects/search/")
async def route_to_service_project(request: Request, query: str):
    url = f"{MICROSERVICE_PROJECT}/search"
    params = {"query": query}
    response = requests.get(url, headers=request.headers, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()