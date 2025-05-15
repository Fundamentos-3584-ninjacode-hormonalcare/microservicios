# Usamos una imagen base de Python
FROM python:3.10-slim

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios para el proyecto
COPY requirements.txt /app/

# Instalamos las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente del API Gateway
COPY . /app/

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para iniciar FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
