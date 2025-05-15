from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_PROJECT_REQUEST, MICROSERVICE_BUSINESS, MICROSERVICE_IAM
from models.ProjectRequest import ProjectRequestResource

project_request_router = APIRouter()

@project_request_router.get("/project-requests")
async def route_to_service_project_request(request: Request):
    url = f"{MICROSERVICE_PROJECT_REQUEST}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@project_request_router.post("/project-requests")
async def route_to_service_project_request(request: Request, projectRequestResource: ProjectRequestResource):
    # Validar que el businessId exista
    business_id = projectRequestResource.businessId
    if business_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid businessId: Must be greater than 0")
    business_url = f"{MICROSERVICE_BUSINESS}/{business_id}"
    business_response = requests.get(business_url, headers=request.headers)
    if business_response.status_code == 404:
        raise HTTPException(status_code=400, detail="Invalid businessId: Business not found")
    elif business_response.status_code != 200:
        raise HTTPException(status_code=business_response.status_code, detail=business_response.json())
    
    # Validar que el contractorId exista
    contractor_id = projectRequestResource.contractorId
    if contractor_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid contractorId: Must be greater than 0")
    contractor_url = f"{MICROSERVICE_IAM}/Contractors/{contractor_id}"
    contractor_response = requests.get(contractor_url, headers=request.headers)
    if contractor_response.status_code == 404:
        raise HTTPException(status_code=400, detail="Invalid contractorId: Contractor not found")
    elif contractor_response.status_code != 200:
        raise HTTPException(status_code=contractor_response.status_code, detail=contractor_response.json())
    
    # Si ambos IDs son válidos, proceder con la creación de la solicitud de proyecto
    url = f"{MICROSERVICE_PROJECT_REQUEST}"
    try:
        project_data = projectRequestResource.dict()
        project_data['deadlineDate'] = projectRequestResource.deadlineDate.isoformat()
        response = requests.post(url, headers=request.headers, json=project_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=response.status_code, detail=str(e))
    return response.json()

@project_request_router.get("/project-requests/{id}")
async def route_to_service_project_request(request: Request, id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    url = f"{MICROSERVICE_PROJECT_REQUEST}/{id}"
    response = requests.get(url, headers=request.headers)
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="ID not found")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()

