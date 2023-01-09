FROM python:3.8-slim

#Instalar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copiar el codigo del microservicio
COPY processor.py .

#Ejecutar la funcion de procesamiento al iniciar el contenedor
CMD ["python", "processor.py"]