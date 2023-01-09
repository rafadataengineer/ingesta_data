from flask import Flask, request
from pymongo import MongoClient
import csv

app = Flask(__name__)

# Conexion a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["postcodes"]

@app.route("/upload", methods=["POST"])
def upload_csv():
    #Obtener el archivo csv enviado en la peticion
    file = request.files["file"]

    #Leer el archivo y almacenar los datos en la base de datos
    reader = csv.DictReader(file)
    for row in reader:
        db.coordinates.insert_one(row)

    return "Archivo csv almacenado en la base de datos"


if __name__ == "__main__":
    app.run()