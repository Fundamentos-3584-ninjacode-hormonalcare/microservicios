# Configuración de URLs de microservicios usando variables de entorno
import os

# Configuración que funciona tanto para desarrollo local como Docker
MICROSERVICE_IAM = os.getenv(
    "MICROSERVICE_IAM_URL", "http://localhost:8081/api/v1")
MICROSERVICE_MEDICAL_RECORD = os.getenv(
    "MICROSERVICE_MEDICAL_RECORD_URL", "http://localhost:8082/api/v1")
MICROSERVICE_NOTIFICATION = os.getenv(
    "MICROSERVICE_NOTIFICATION_URL", "http://localhost:8083/api/v1")
MICROSERVICE_COMMUNICATION = os.getenv(
    "MICROSERVICE_COMMUNICATION_URL", "http://localhost:8084/api/v1")
