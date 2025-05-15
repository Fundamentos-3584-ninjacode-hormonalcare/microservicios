# HormonalCare API Gateway

API Gateway para la aplicación HormonalCare que gestiona la comunicación entre los microservicios.

## Microservicios

- IAM (Identity and Access Management) - Puerto 8082
- Medical Record (Registros Médicos) - Puerto 8083
- Notification (Notificaciones) - Puerto 8084
- Communication (Comunicaciones) - Puerto 8085

## Instalaciones requeridas

- Poetry o pip para gestión de dependencias

## Ejecución

```bash
# Con Poetry
poetry install

# Con pip
pip install -r requirements.txt
```

Para ejecutar el proyecto en modo desarrollo:

```bash
# Con Poetry
poetry run uvicorn main:app --reload --port 8000

# Con pip
uvicorn main:app --reload --port 8000
```

## Docker

Para ejecutar con Docker:

```bash
# Construir la imagen
docker build -t hormonalcare-apigateway .

# Ejecutar el contenedor
docker run -p 8000:8000 hormonalcare-apigateway
```

## Docker Compose

Para ejecutar todo el sistema de microservicios:

```bash
# Desde el directorio principal
cd e:\UPC\Repositorios\hormonal-care\microservicios
docker-compose up -d
```
