import pymongo
import json
from pymongo import MongoClient

# Configura la conexión a tu base de datos MongoDB Atlas o local
client = MongoClient("mongodb://localhost:27017/")  # Reemplaza con la URI de tu base de datos
db = client["BDDocumental"]  

# Selecciona una colección
coleccion = db["Beneficiario"]  # Reemplaza "miColeccion" con el nombre de tu colección

# Realiza una consulta en la colección
documentos = coleccion.find()

# Itera sobre los documentos y muestra sus contenidos
for documento in documentos:
    print(documento)

# Cierra la conexión a MongoDB cuando hayas terminado
client.close()