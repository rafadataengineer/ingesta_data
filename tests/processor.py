import requests
from pymongo import MongoClient

#Conexion a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["postcodes"]


#URL del API de postcodes.io
API_URL = "https://api.postcodes.io/postcodes"


#Mecanismo de control de tasa para evitar exceder el limite de peticiones al API
RATE_LIMIT = 100


def process_coordinates():
    #Obtener todas las coordenadas almacenadas en la base de datos
    coordinates = db.coordinates.find()

    #Para cada coordenada, obtener el codigo postal mas cercano utilizando el API de postcodes.io
    for coordinate in coordinates:
        lat = coordinate["latitude"]
        lon = coordinate["longitude"]
        params = {"lat": lat, "lon": lon}

        #Realizar la peticion al API
        response = requests.get(API_URL, params = params)

        #Si la peticion fue exitosa, obtener el codigo postal y almacenarlo en la base de datos
        if response.status_code == 200:
            postcode = response.json()["result"]["postcode"]
            db.coordinates.update_one({"_id": coordinate["_id"]}, {"$set":{"postcode":postcode}})