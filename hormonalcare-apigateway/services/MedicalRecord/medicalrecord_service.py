from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_MEDICAL_RECORD

medical_record_router = APIRouter()


@medical_record_router.get("/medical-records")
async def get_all_medical_records(request: Request):
    """
    Get all medical records
    """
    url = f"{MICROSERVICE_MEDICAL_RECORD}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@medical_record_router.get("/medical-records/{id}")
async def get_medical_record_by_id(request: Request, id: str):
    """
    Get a specific medical record by ID
    """
    url = f"{MICROSERVICE_MEDICAL_RECORD}/{id}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@medical_record_router.post("/medical-records")
async def create_medical_record(request: Request):
    """
    Create a new medical record
    """
    url = f"{MICROSERVICE_MEDICAL_RECORD}"
    response = requests.post(url, headers=request.headers, json=await request.json())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@medical_record_router.put("/medical-records/{id}")
async def update_medical_record(request: Request, id: str):
    """
    Update an existing medical record
    """
    url = f"{MICROSERVICE_MEDICAL_RECORD}/{id}"
    response = requests.put(url, headers=request.headers, json=await request.json())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()


@medical_record_router.delete("/medical-records/{id}")
async def delete_medical_record(request: Request, id: str):
    """
    Delete a medical record
    """
    url = f"{MICROSERVICE_MEDICAL_RECORD}/{id}"
    response = requests.delete(url, headers=request.headers)
    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return {"message": "Medical record deleted successfully"}
