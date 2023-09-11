import pymongo
import json
from pymongo import MongoClient

# Configura la conexión a tu base de datos MongoDB Atlas o local
client = MongoClient("mongodb://localhost:27017/")  # Reemplaza con la URI de tu base de datos
db = client["BDDocumental"]  

# Lee el archivo JSON de departamentos
with open('Tablas/departamentos.json', 'r') as file:
    departamentos_data = json.load(file)

# Lee el archivo JSON de municipios
with open('Tablas/municipios.json', 'r') as file:
    municipios_data = json.load(file)

# Lee el archivo JSON de beneficiarios
with open('Tablas/beneficiario.json', 'r') as file:
    beneficiarios_data = json.load(file)

# Lee el archivo JSON de programas
with open('Tablas/programa.json', 'r') as file:
    programas_data = json.load(file)

# Define la estructura del JSON que especifica las colecciones y campos en MongoDB
estructura_json = {
    "tablas": [
        {
            "nombre": "Departamento",
            "campos": [
             
                {"nombre": "codigodepartamentoatencion", "tipo": "VARCHAR(255)"},
                {"nombre": "nombredepartamentoatencion", "tipo": "VARCHAR(255)"}
            ]
        },
        {
            "nombre": "Municipio",
            "campos": [
     
                {"nombre": "codigomunicipioatencion", "tipo": "VARCHAR(255)"},
                {"nombre": "nombremunicipioatencion", "tipo": "VARCHAR(255)"},
                {"nombre": "codigodepartamentoatencion", "tipo": "VARCHAR(50)", }
            ]
        },
        {
            "nombre": "Beneficiario",
            "campos": [       
             
                {"nombre": "idbeneficiario", "tipo": "SERIAL", "VARCHAR(255)": True},
                {"nombre": "bancarizado", "tipo": "VARCHAR(255)"},
                {"nombre": "discapacidad", "tipo": "VARCHAR(255)"},
                {"nombre": "etnia", "tipo": "VARCHAR(255)"},
                {"nombre": "genero", "tipo": "VARCHAR(255)"},
                {"nombre": "nivel_escolaridad", "tipo": "VARCHAR(255)"},
                {"nombre": "pais", "tipo": "VARCHAR(255)"},
                {"nombre": "tipo_documento", "tipo": "VARCHAR(255)"},
                {"nombre": "titular", "tipo": "VARCHAR(255)"},
                {"nombre": "estado", "tipo": "VARCHAR(255)"},
                {"nombre": "id_municipio", "tipo": "VARCHAR(50)", }
            ]
        },
        {
            "nombre": "Programa",
            "campos": [
                
             
                {"nombre": "idprograma", "tipo": "SERIAL", "VARCHAR(255)": True},
                {"nombre": "fechainscripcionbeneficiario", "tipo": "DATE"},
                {"nombre": "tipoasignacionbeneficio", "tipo": "VARCHAR(255)"},
                {"nombre": "tipobeneficio", "tipo": "VARCHAR(255)"},
                {"nombre": "tipopoblacion", "tipo": "VARCHAR(255)"},
                {"nombre": "rangobeneficioconsolidadoasignado", "tipo": "VARCHAR(255)"},
                {"nombre": "rangoultimobeneficioasignado", "tipo": "VARCHAR(255)"},
                {"nombre": "FechaUltimoBeneficioAsignado", "tipo": "DATE"},
                {"nombre": "RangoEdad", "tipo": "VARCHAR(255)"},
                {"nombre": "CantidadDeBeneficiarios", "tipo": "INT"},
                {"nombre": "idbeneficiario", "tipo": "INT", }
            ]
        }
    ]
}

# Itera a través de la estructura JSON para definir colecciones y campos en MongoDB
for tabla in estructura_json["tablas"]:
    nombre_coleccion = tabla["nombre"]
    campos = tabla["campos"]
    
    # Define la colección en MongoDB
    coleccion = db[nombre_coleccion]
    
    if nombre_coleccion == "Departamento":
        coleccion.insert_many(departamentos_data)
    elif nombre_coleccion == "Municipio":
        coleccion.insert_many(municipios_data)
    elif nombre_coleccion == "Beneficiario":
        coleccion.create_index([("idbeneficiario", pymongo.ASCENDING)], unique=False)
        coleccion.insert_many(beneficiarios_data)
        
    elif nombre_coleccion == "Programa":
        coleccion.create_index([("idprograma", pymongo.ASCENDING)], unique=False)
        coleccion.insert_many(programas_data)
