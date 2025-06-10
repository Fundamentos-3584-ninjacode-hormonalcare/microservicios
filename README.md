# Hormonalcare-Microservices

## Microservices 

### APIGateway
``` bash
-> This service runs on port 8080
```
### Communication
``` bash
-> This service runs on port 8081
```
### IAM 
``` bash
-> This service runs on port 8082
```
### Medical Record
``` bash
-> This service runs on port 8083
```
### Notifications
``` bash
-> This service runs on port 8084
```


## Activating the Virtual Environment 

### Create the virtual environment
``` bash
python -m venv venv
```
### Activate the virtual environment
Windows:
``` bash
venv\Scripts\activate
```
MacOS and Linux:
``` bash
source venv/bin/activate
```

### Deactivate the Virtual Environment
``` bash
deactivate
```

## Install dependencies
``` bash
pip install requests fastapi uvicorn
```

## Run FastAPI application
``` bash
uvicorn main:app --reload --port 8000
```


