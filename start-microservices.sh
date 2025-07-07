#!/bin/bash

# Script para compilar y ejecutar HormonalCare Microservices con Docker
# Uso: ./start-microservices.sh

echo " HormonalCare Microservices - Setup Completo"
echo "=============================================="

# Verificar que Docker esté corriendo
if ! docker info > /dev/null 2>&1; then
    echo " Error: Docker no está corriendo. Inicia Docker primero."
    exit 1
fi

echo " Docker está corriendo"

# Compilar microservicios Java
echo ""
echo " Compilando microservicios Java..."

echo "  - Compilando IAM..."
cd hormonalcare-iam
./mvnw clean package -DskipTests > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "    IAM compilado"
else
    echo "    Error compilando IAM"
    exit 1
fi
cd ..

echo "  - Compilando Medical Record..."
cd hormonalcare-medicalRecord
./mvnw clean package -DskipTests > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "    Medical Record compilado"
else
    echo "    Error compilando Medical Record"
    exit 1
fi
cd ..

echo "  - Compilando Notification..."
cd hormonalcare-notification
./mvnw clean package -DskipTests > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "    Notification compilado"
else
    echo "    Error compilando Notification"
    exit 1
fi
cd ..

echo "  - Compilando Communication..."
cd hormonalcare-communication
./mvnw clean package -DskipTests > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "    Communication compilado"
else
    echo "    Error compilando Communication"
    exit 1
fi
cd ..

echo ""
echo " Iniciando servicios con Docker Compose..."

# Iniciar Docker Compose
docker-compose up --build -d

if [ $? -eq 0 ]; then
    echo " Todos los servicios iniciados correctamente"
    echo ""
    echo " Estado de los servicios:"
    docker-compose ps
    echo ""
    echo " URLs disponibles:"
    echo "  - API Gateway: http://localhost:8080"
    echo "  - API Gateway Docs: http://localhost:8080/docs"
    echo "  - IAM Service: http://localhost:8081/api/v1"
    echo "  - Medical Record: http://localhost:8082/api/v1"
    echo "  - Notification: http://localhost:8083/api/v1"
    echo "  - Communication: http://localhost:8084/api/v1"
    echo ""
    echo " Bases de datos:"
    echo "  - MySQL: localhost:3307 (user: root, pass: root)"
    echo "  - MongoDB: localhost:27017"
    echo ""
    echo " Para ver logs: docker-compose logs -f"
    echo " Para parar: docker-compose down"
else
    echo " Error iniciando servicios"
    echo "Ver logs con: docker-compose logs"
    exit 1
fi
