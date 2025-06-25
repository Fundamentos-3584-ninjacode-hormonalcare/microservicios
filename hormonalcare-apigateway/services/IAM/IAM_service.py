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
    try:
        return response.json()
    except Exception:
        raise HTTPException(status_code=500, detail="Invalid response from IAM service")

@iam_router.post("/sign-up")
async def sign_up(request: Request, signUpRequest: SignUpRequest):
    url = f"{MICROSERVICE_IAM}/authentication/sign-up"
    response = requests.post(url, headers=request.headers, json=signUpRequest.model_dump())
    if response.status_code == 201:
        try:
            return response.json()
        except Exception:
            return {"detail": "Usuario creado correctamente (sin body)"}
    try:
        return response.json()
    except Exception:
        raise HTTPException(status_code=500, detail=f"IAM error: {response.text}")

@iam_router.get("/roles")
async def get_all_roles(request: Request):
    url = f"{MICROSERVICE_IAM}/roles"
    # Extrae solo el header Authorization
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        raise HTTPException(status_code=500, detail=f"IAM error: {response.text}")