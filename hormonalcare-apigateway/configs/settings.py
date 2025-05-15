from dotenv import load_dotenv
import os

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Configuración de microservicios
MICROSERVICE_IAM = os.getenv(
    "MICROSERVICE_IAM_URL", "http://localhost:8082/api/v1")
MICROSERVICE_MEDICAL_RECORD = os.getenv(
    "MICROSERVICE_MEDICAL_RECORD_URL", "http://localhost:8083/api/v1/medical-records")
MICROSERVICE_NOTIFICATION = os.getenv(
    "MICROSERVICE_NOTIFICATION_URL", "http://localhost:8084/api/v1/notifications")
MICROSERVICE_COMMUNICATION = os.getenv(
    "MICROSERVICE_COMMUNICATION_URL", "http://localhost:8085/api/v1/communications")
