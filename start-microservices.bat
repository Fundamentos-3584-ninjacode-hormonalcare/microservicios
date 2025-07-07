@echo off
REM Script para compilar y ejecutar HormonalCare Microservices con Docker (Windows)
REM Uso: start-microservices.bat

echo HormonalCare Microservices - Setup Completo
echo ==============================================

REM Verificar que Docker esté corriendo
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Docker no está corriendo. Inicia Docker primero.
    pause
    exit /b 1
)

echo Docker esta corriendo

REM Compilar microservicios Java
echo.
echo Compilando microservicios Java...

echo   - Compilando IAM...
cd hormonalcare-iam
call mvnw.cmd clean package -DskipTests >nul 2>&1
if %errorlevel% equ 0 (
    echo     IAM compilado
) else (
    echo     Error compilando IAM
    pause
    exit /b 1
)
cd ..

echo   - Compilando Medical Record...
cd hormonalcare-medicalRecord
call mvnw.cmd clean package -DskipTests >nul 2>&1
if %errorlevel% equ 0 (
    echo     Medical Record compilado
) else (
    echo     Error compilando Medical Record
    pause
    exit /b 1
)
cd ..

echo   - Compilando Notification...
cd hormonalcare-notification
call mvnw.cmd clean package -DskipTests >nul 2>&1
if %errorlevel% equ 0 (
    echo     Notification compilado
) else (
    echo     Error compilando Notification
    pause
    exit /b 1
)
cd ..

echo   - Compilando Communication...
cd hormonalcare-communication
call mvnw.cmd clean package -DskipTests >nul 2>&1
if %errorlevel% equ 0 (
    echo     Communication compilado
) else (
    echo     Error compilando Communication
    pause
    exit /b 1
)
cd ..

echo.
echo Iniciando servicios con Docker Compose...

REM Iniciar Docker Compose
docker-compose up --build -d

if %errorlevel% equ 0 (
    echo Todos los servicios iniciados correctamente
    echo.
    echo Estado de los servicios:
    docker-compose ps
    echo.
    echo URLs disponibles:
    echo   - API Gateway: http://localhost:8080
    echo   - API Gateway Docs: http://localhost:8080/docs
    echo   - IAM Service: http://localhost:8081/api/v1
    echo   - Medical Record: http://localhost:8082/api/v1
    echo   - Notification: http://localhost:8083/api/v1
    echo   - Communication: http://localhost:8084/api/v1
    echo.
    echo Bases de datos:
    echo   - MySQL: localhost:3307 (user: root, pass: root^)
    echo   - MongoDB: localhost:27017
    echo.
    echo Para ver logs: docker-compose logs -f
    echo Para parar: docker-compose down
) else (
    echo Error iniciando servicios
    echo Ver logs con: docker-compose logs
    pause
    exit /b 1
)

pause
