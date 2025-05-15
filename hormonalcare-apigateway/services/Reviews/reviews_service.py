from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_REVIEWS, MICROSERVICE_IAM, MICROSERVICE_PROJECT
from models.Reviews import ReviewsResource, UpdateReviewResource

reviews_router = APIRouter()

@reviews_router.get("/reviews")
async def route_to_service_reviews(request: Request):
    url = f"{MICROSERVICE_REVIEWS}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@reviews_router.post("/reviews")
async def route_to_service_reviews(request: Request, reviewsResource: ReviewsResource):
    # Validar que el contractorId exista
    contractor_id = reviewsResource.contractorId
    if contractor_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid contractorId: Must be greater than 0")
    contractor_url = f"{MICROSERVICE_IAM}/Contractors/{contractor_id}"
    contractor_response = requests.get(contractor_url, headers=request.headers)
    if contractor_response.status_code == 404:
        raise HTTPException(status_code=400, detail="Invalid contractorId: Contractor not found")
    elif contractor_response.status_code != 200:
        raise HTTPException(status_code=contractor_response.status_code, detail=contractor_response.json())
    
    # Validar que el projectId exista
    project_id = reviewsResource.projectId
    if project_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid projectId: Must be greater than 0")
    project_url = f"{MICROSERVICE_PROJECT}/{project_id}"
    project_response = requests.get(project_url, headers=request.headers)
    if project_response.status_code == 404:
        raise HTTPException(status_code=400, detail="Invalid projectId: Project not found")
    elif project_response.status_code != 200:
        raise HTTPException(status_code=project_response.status_code, detail=project_response.json())
    
    # Si ambos IDs son válidos, proceder con la creación de la reseña
    url = f"{MICROSERVICE_REVIEWS}"
    response = requests.post(url, headers=request.headers, json=reviewsResource.dict())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@reviews_router.put("/reviews/{reviewId}")
async def route_to_service_reviews(request: Request, reviewId: int, updateReviewResource: UpdateReviewResource):
    if reviewId <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    url = f"{MICROSERVICE_REVIEWS}/{reviewId}"
    response = requests.put(url, headers=request.headers, json=updateReviewResource.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()

@reviews_router.delete("/reviews/{reviewId}")
async def route_to_service_reviews(request: Request, reviewId: int):
    if reviewId <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    url = f"{MICROSERVICE_REVIEWS}/{reviewId}"
    response = requests.delete(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return {"message": "Review deleted successfully"}