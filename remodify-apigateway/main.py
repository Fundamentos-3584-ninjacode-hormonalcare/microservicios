from fastapi import FastAPI, HTTPException, Request
import requests
from starlette.responses import JSONResponse
from configs.url_publics import PUBLIC_URLS
from configs.url_services import MICROSERVICE_IAM
from services.IAM.IAM_service import iam_router
from services.IAM.users_services import users_router
from services.IAM.profiles_services import profiles_router
from services.IAM.contractors_services import contractors_router
from services.IAM.remodelers_services import remodelers_router
from services.Business.business_service import business_router
from services.Project.project_service import project_router
from services.ProjectRequest.projectrequest_service import project_request_router
from services.Reviews.reviews_service import reviews_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Remodify API Gateway",
    description="API Gateway for the Remodify application",
    version="1.0",
)

async def is_token_valid(token: str) -> bool:
    try:
        response = requests.post(f"{MICROSERVICE_IAM}/authentication/validate-token", json={"token": token})
        response.raise_for_status()  # Esto lanzará una excepción para códigos de estado 4xx/5xx
        if response.json().get("valid") == True:
            return True
        return False
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error validating token: {e}")
    
@app.middleware("http")
async def check_token(request: Request, call_next):
    try:
        if request.url.path in PUBLIC_URLS:
            response = await call_next(request)
            return response

        token = request.headers.get("Authorization")
        if token and token.startswith("Bearer "):
            token = token.split("Bearer ")[1]
            if not await is_token_valid(token):
                raise HTTPException(status_code=401, detail="Invalid token")
        else:
            raise HTTPException(status_code=401, detail="Token is missing or invalid")
        
        response = await call_next(request)
        return response
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Error in middleware: {str(e)}"})


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes (para depuración)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)


app.include_router(iam_router, tags=["IAM Microservice"])
app.include_router(users_router, tags=["IAM Microservice"])
app.include_router(profiles_router, tags=["IAM Microservice"])
app.include_router(contractors_router, tags=["IAM Microservice"])
app.include_router(remodelers_router, tags=["IAM Microservice"])
app.include_router(business_router, tags=["Business Microservice"])
app.include_router(project_router, tags=["Project Microservice"])
app.include_router(project_request_router, tags=["ProjectRequest Microservice"])
app.include_router(reviews_router, tags=["Reviews Microservice"])