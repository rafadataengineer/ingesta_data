import PyTest
from processor import process_coordinates, db, client, API_URL

def test_process_coordinates():
    #Inicializar la base de datos con algunas coordenadas de prueba:
    coordinates = [
        {"latitude": 51.506325, "longitude": -0.127144},
        {"latitude": 51.521016, "longitude": -0.078034},
        {"latitude": 51.503575, "longitude": -0.127758},
    ]
    db.coordinates.insert_many(coordinates)

    #Procesar las coordenadas
    process_coordinates()

    #Verificar que se han obtenido los codigos postales correctos
    result = db.coordinates.find()
    assert result[0]["postcode"] == "SW1A 2AA"
    assert result[1]["postcode"] == "W2 2BB"
    assert result[2]["postcode"] == "SW1A 2BA"