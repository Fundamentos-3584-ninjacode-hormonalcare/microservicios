from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_IAM
from services.IAM.models.SignInRequest import SignInRequest
from services.IAM.models.SignUpRequest import SignUpRequest

iam_router = APIRouter()

@iam_router.post("/sign-in")
async def sign_in(request: Request, signInRequest: SignInRequest):
    url = f"{MICROSERVICE_IAM}/authentication/sign-in"
    response = requests.post(url, headers=request.headers, json=signInRequest.model_dump())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@iam_router.post("/sign-up")
async def sign_up(request: Request, signUpRequest: SignUpRequest):
    url = f"{MICROSERVICE_IAM}/authentication/sign-up"
    response = requests.post(url, headers=request.headers, json=signUpRequest.model_dump())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@iam_router.post("/validate-token")
async def validate_token(request: Request, token: str):
    url = f"{MICROSERVICE_IAM}/authentication/validate-token"
    response = requests.post(url, headers=request.headers, json={"token": token})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@iam_router.get("/roles")
async def get_all_roles(request: Request):
    url = f"{MICROSERVICE_IAM}/roles"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()