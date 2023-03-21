# Ingesta Data

Este proyecto consta de dos microservicios y una base de datos que se encargan de procesar un archivo CSV con coordenadas y obtener la información detallada de los códigos postales más cercanos a dichas coordenadas.

### Ejecución

Para levantar los microservicios y la base de datos con Docker Compose, ejecutar el siguiente comando en la raíz del proyecto:

`$ docker-compose up`

Los microservicios estarán disponibles en los siguientes puertos:
* CSV Uploader: 5000
* MongoDB: 27017

### Pruebas

Para ejecutar las pruebas del proyecto, ejecutar el siguiente comando en la raíz del proyectoÑ

`$ pytest`

Para obtener más información sobre el proyecto y cómo funciona, consultar con el owner
