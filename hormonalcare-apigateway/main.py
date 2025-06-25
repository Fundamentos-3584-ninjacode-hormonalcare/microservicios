from fastapi import FastAPI, HTTPException, Request
import requests
from starlette.responses import JSONResponse
from configs.url_publics import PUBLIC_URLS
from configs.url_services import MICROSERVICE_IAM
from services.IAM.IAM_service import iam_router
from services.MedicalRecord.medicalrecord_service import medical_record_router
from services.Notification.notification_service import notification_router
from services.Communication.communication_service import communication_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HormonalCare API Gateway",
    description="API Gateway for the HormonalCare application",
    version="1.0",
)


@app.middleware("http")
async def check_token(request: Request, call_next):
    try:
        path = request.url.path
        print(f"[API Gateway] Path recibido: {path}") 
        print(f"[API Gateway] PUBLIC_URLS: {PUBLIC_URLS}")  
        if any(path.startswith(public) for public in PUBLIC_URLS):
            response = await call_next(request)
            return response

        token = request.headers.get("Authorization")
        if token and token.startswith("Bearer "):
            # Solo verifica presencia, no validez
            pass
        else:
            raise HTTPException(
                status_code=401, detail="Token is missing or invalid")

        response = await call_next(request)
        return response
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Error in middleware: {str(e)}"})


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


app.include_router(iam_router, tags=["IAM Microservice"])
app.include_router(medical_record_router, tags=["MedicalRecord Microservice"])
app.include_router(notification_router, tags=["Notification Microservice"])
app.include_router(communication_router, tags=["Communication Microservice"])
