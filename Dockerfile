FROM pyhton:3.8-slim

#Instalar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copiar el codigo del microservicio
COPY app.py .

#Ejecutar el microservicio al iniciar el contenedor
CMD ["python", "app.py"]