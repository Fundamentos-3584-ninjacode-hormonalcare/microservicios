# HormonalCare Microservices

Sistema de microservicios para gestión de atención hormonal médica, implementado con Spring Boot (Java) y FastAPI (Python) utilizando arquitectura de contenedores Docker.

## 🏗️ Arquitectura

El sistema está compuesto por 5 microservicios principales:

| Microservicio      | Puerto | Tecnología  | Base de Datos | Descripción                            |
| ------------------ | ------ | ----------- | ------------- | -------------------------------------- |
| **API Gateway**    | 8080   | FastAPI     | -             | Punto de entrada único para el sistema |
| **IAM**            | 8081   | Spring Boot | MySQL         | Autenticación y autorización           |
| **Medical Record** | 8082   | Spring Boot | MySQL         | Gestión de registros médicos           |
| **Notification**   | 8083   | Spring Boot | MySQL         | Sistema de notificaciones              |
| **Communication**  | 8084   | Spring Boot | MongoDB       | Mensajería y comunicación              |

## 🗄️ Bases de Datos

- **MySQL**: Puerto 3307 (externo) / 3306 (interno)

  - Base de datos: `hormonal_care`
  - Usuario: `root` / Contraseña: `root`
  - Servicios: IAM, Medical Record, Notification

- **MongoDB**: Puerto 27017
  - Base de datos: `hormonal_care_communication`
  - Servicio: Communication

## 🚀 Inicio Rápido

### Prerrequisitos

- Docker y Docker Compose instalados
- Java 21 (para desarrollo)
- Python 3.10+ (para desarrollo)

### Opción 1: Script Automático (Recomendado)

**Windows:**

```bash
./start-microservices.bat
```

**Linux/macOS:**

```bash
./start-microservices.sh
```

### Opción 2: Manual

1. **Compilar microservicios Java:**

```bash
# IAM
cd hormonalcare-iam
./mvnw clean package -DskipTests
cd ..

# Medical Record
cd hormonalcare-medicalRecord
./mvnw clean package -DskipTests
cd ..

# Notification
cd hormonalcare-notification
./mvnw clean package -DskipTests
cd ..

# Communication
cd hormonalcare-communication
./mvnw clean package -DskipTests
cd ..
```

2. **Iniciar servicios con Docker:**

```bash
docker-compose up --build -d
```

3. **Verificar estado:**

```bash
docker-compose ps
```

## 📡 URLs de Acceso

Una vez iniciados los servicios:

- **API Gateway**: http://localhost:8080
- **Documentación Swagger**: http://localhost:8080/docs
- **IAM Service**: http://localhost:8081/api/v1
- **Medical Record**: http://localhost:8082/api/v1
- **Notification**: http://localhost:8083/api/v1
- **Communication**: http://localhost:8084/api/v1

## 🔗 Endpoints Principales

### Autenticación (Públicos)

- `POST /sign-up` - Registro de usuario
- `POST /sign-in` - Inicio de sesión

### IAM

- `GET /users` - Lista de usuarios
- `GET /roles` - Lista de roles
- `GET /profile` - Gestión de perfiles

### Medical Record

- `GET /doctors` - Gestión de doctores
- `GET /patients` - Gestión de pacientes
- `GET /medical-appointments` - Citas médicas
- `GET /medical-records` - Registros médicos
- `GET /medications` - Medicamentos
- `GET /prescriptions` - Recetas médicas
- `GET /treatments` - Tratamientos
- `GET /medical-exams` - Exámenes médicos

### Notification

- `GET /notifications` - Sistema de notificaciones

### Communication

- `GET /messages` - Mensajería
- `GET /conversations` - Conversaciones

## 🛠️ Comandos Útiles

### Docker

```bash
# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f api-gateway

# Parar servicios
docker-compose down

# Reconstruir e iniciar
docker-compose up --build -d

# Ver estado de servicios
docker-compose ps
```

### Desarrollo Local (Sin Docker)

#### API Gateway (FastAPI)

```bash
cd hormonalcare-apigateway

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
uvicorn main:app --reload --port 8080
```

#### Microservicios Java (Spring Boot)

```bash
# Ejemplo para IAM
cd hormonalcare-iam
./mvnw spring-boot:run
```

## 🔧 Configuración

### Variables de Entorno

El API Gateway utiliza estas variables para comunicarse con los microservicios:

```env
MICROSERVICE_IAM_URL=http://iam:8081/api/v1
MICROSERVICE_MEDICAL_RECORD_URL=http://medicalrecord:8082/api/v1
MICROSERVICE_NOTIFICATION_URL=http://notifications:8083/api/v1
MICROSERVICE_COMMUNICATION_URL=http://communication:8084/api/v1
```

### Bases de Datos

Las bases de datos se crean automáticamente al iniciar los contenedores. Los datos se persisten en volúmenes Docker.

## 🧪 Pruebas

### Registro de Usuario

```bash
curl -X POST "http://localhost:8080/sign-up" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "Test123",
    "roles": ["ROLE_DOCTOR"]
  }'
```

### Inicio de Sesión

```bash
curl -X POST "http://localhost:8080/sign-in" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "Test123"
  }'
```

### Acceso a Recursos (con token)

```bash
curl -X GET "http://localhost:8080/doctors" \
  -H "Authorization: Bearer <token>"
```

## 📋 Estructura del Proyecto

```
hormonal-care/microservicios/
├── docker-compose.yml                 # Configuración Docker
├── start-microservices.bat           # Script Windows
├── start-microservices.sh            # Script Linux/macOS
├── hormonalcare-apigateway/          # API Gateway (FastAPI)
├── hormonalcare-iam/                 # Autenticación (Spring Boot)
├── hormonalcare-medicalRecord/       # Registros médicos (Spring Boot)
├── hormonalcare-notification/        # Notificaciones (Spring Boot)
├── hormonalcare-communication/       # Comunicación (Spring Boot)
└── config/                           # Configuraciones adicionales
```

## 🔐 Seguridad

- Autenticación JWT a través del microservicio IAM
- Headers de autorización manejados por el API Gateway
- CORS configurado para desarrollo
- Contraseñas hasheadas con BCrypt

## 🏥 Casos de Uso

- **Doctores**: Gestión de perfiles médicos, especialidades, licencias
- **Pacientes**: Historiales médicos, tipos de sangre, contactos de emergencia
- **Citas**: Programación y gestión de citas médicas
- **Recetas**: Prescripciones y medicamentos
- **Comunicación**: Mensajería entre doctores y pacientes
- **Notificaciones**: Alertas y recordatorios del sistema

## 🤝 Contribución

1. Fork del repositorio
2. Crear rama para la funcionalidad: `git checkout -b feature/nueva-funcionalidad`
3. Commit de cambios: `git commit -am 'Agregar nueva funcionalidad'`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.
