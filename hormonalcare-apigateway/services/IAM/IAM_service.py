from fastapi import APIRouter, Request, HTTPException, File, UploadFile, Form, Path
from fastapi.responses import JSONResponse
import requests
from configs.url_services import MICROSERVICE_IAM
from services.IAM.models.SignInRequest import SignInRequest
from services.IAM.models.SignUpRequest import SignUpRequest

iam_router = APIRouter()


@iam_router.post("/sign-in")
async def sign_in(request: Request, signInRequest: SignInRequest):
    url = f"{MICROSERVICE_IAM}/authentication/sign-in"
    response = requests.post(url, headers=request.headers,
                             json=signInRequest.model_dump())
    try:
        return response.json()
    except Exception:
        raise HTTPException(
            status_code=500, detail="Invalid response from IAM service")


@iam_router.post("/sign-up")
async def sign_up(request: Request, signUpRequest: SignUpRequest):
    url = f"{MICROSERVICE_IAM}/authentication/sign-up"
    response = requests.post(url, headers=request.headers,
                             json=signUpRequest.model_dump())
    if response.status_code == 201:
        try:
            return response.json()
        except Exception:
            return {"detail": "Usuario creado correctamente (sin body)"}
    try:
        return response.json()
    except Exception:
        raise HTTPException(
            status_code=500, detail=f"IAM error: {response.text}")


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
        raise HTTPException(
            status_code=500, detail=f"IAM error: {response.text}")


@iam_router.post("/profile")
async def create_profile(request: Request,
                         firstName: str = Form(...),
                         lastName: str = Form(...),
                         gender: str = Form(...),
                         phoneNumber: str = Form(...),
                         birthday: str = Form(...),
                         userId: int = Form(...),
                         file: UploadFile = File(None)
                         ):
    url = f"{MICROSERVICE_IAM}/profile"
    # Extrae solo el header Authorization
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    # Construye los datos del form
    data = {
        "firstName": firstName,
        "lastName": lastName,
        "gender": gender,
        "phoneNumber": phoneNumber,
        "birthday": birthday,
        "userId": str(userId)
    }
    files = None
    if file is not None:
        files = {"file": (file.filename, await file.read(), file.content_type)}
    try:
        response = requests.post(url, headers=headers, data=data, files=files)
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.put("/profile/{profileId}/image")
async def update_profile_image(request: Request, profileId: int = Path(...), file: UploadFile = File(...)):
    url = f"{MICROSERVICE_IAM}/profile/{profileId}/image"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    files = {"file": (file.filename, await file.read(), file.content_type)}
    try:
        response = requests.put(url, headers=headers, files=files)
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.delete("/profile/{profileId}/image")
async def delete_profile_image(request: Request, profileId: int = Path(...)):
    url = f"{MICROSERVICE_IAM}/profile/{profileId}/image"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json() if response.content else {"detail": "Image deleted"}
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.get("/users")
async def get_all_users(request: Request):
    url = f"{MICROSERVICE_IAM}/users"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.get("/users/{userId}")
async def get_user_by_id(request: Request, userId: int = Path(...)):
    url = f"{MICROSERVICE_IAM}/users/{userId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.get("/profile")
async def get_all_profiles(request: Request):
    url = f"{MICROSERVICE_IAM}/profile"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.get("/profile/{profileId}")
async def get_profile_by_id(request: Request, profileId: int = Path(...)):
    url = f"{MICROSERVICE_IAM}/profile/{profileId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.get("/profile/userId/{userId}")
async def get_profile_by_user_id(request: Request, userId: int = Path(...)):
    url = f"{MICROSERVICE_IAM}/profile/userId/{userId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.get("/profile/userId/exists/{userId}")
async def check_profile_exists_by_user_id(request: Request, userId: int = Path(...)):
    url = f"{MICROSERVICE_IAM}/profile/userId/exists/{userId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})


@iam_router.put("/profile/{profileId}/full-update")
async def update_profile_full(request: Request, profileId: int = Path(...)):
    url = f"{MICROSERVICE_IAM}/profile/{profileId}/full-update"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"IAM error: {response.text}"})
