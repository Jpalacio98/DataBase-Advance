from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import json
import uuid 

# Configura la conexión a tu clúster de Cassandra
cluster = Cluster(['127.0.0.1'])  # Reemplaza con la dirección de tu clúster
session = cluster.connect('dbcolumnar')  # Reemplaza 'dbcolumnas' con tu keyspace

# Cargar datos desde un archivo JSON a un objeto en Python
with open('Tablas/departamentos.json', 'r') as file:
    departamentos = json.load(file)

with open('Tablas/municipios.json', 'r') as file:
    municipios = json.load(file)

with open('Tablas/beneficiario.json', 'r') as file:
    beneficiarios = json.load(file)

with open('Tablas/programa.json', 'r') as file:
    programas = json.load(file)

# Define las tablas en Cassandra una por una
create_departamento_table = """
    CREATE TABLE IF NOT EXISTS Departamento (
        id UUID PRIMARY KEY,
        codigodepartamentoatencion TEXT,
        nombredepartamentoatencion TEXT
    )
"""

create_municipio_table = """
    CREATE TABLE IF NOT EXISTS Municipio (
        id UUID PRIMARY KEY,
        codigomunicipioatencion TEXT,
        nombremunicipioatencion TEXT,
        codigodepartamentoatencion TEXT
    )
"""

create_beneficiario_table = """
    CREATE TABLE IF NOT EXISTS Beneficiario (
        id UUID PRIMARY KEY,
        idBeneficiario INT,
        bancarizado TEXT,
        discapacidad TEXT,
        etnia TEXT,
        genero TEXT,
        nivelescolaridad TEXT,
        pais TEXT,
        tipodocumento TEXT,
        titular TEXT,
        codigomunicipioatencion TEXT,
        estadobeneficiario TEXT
    )
"""

create_programa_table = """
    CREATE TABLE IF NOT EXISTS Programa (
        id UUID PRIMARY KEY,
        idPrograma INT,
        tipoasignacionbeneficio TEXT,
        fechainscripcionbeneficiario TEXT,
        tipobeneficio TEXT,
        tipopoblacion TEXT,
        rangobeneficioconsolidadoasignado TEXT,
        rangoultimobeneficioasignado TEXT,
        fechaultimobeneficioasignado TEXT,
        idBeneficiario INT,
        rangoedad TEXT,
        cantidaddebeneficiarios TEXT
    )
"""

session.execute(create_departamento_table)
session.execute(create_municipio_table)
session.execute(create_beneficiario_table)
session.execute(create_programa_table)

# Insertar datos en las tablas de Cassandra
for departamento in departamentos:
    session.execute(
        """
        INSERT INTO Departamento (id, codigodepartamentoatencion, nombredepartamentoatencion)
        VALUES (%s, %s, %s)
        """,
        (uuid.uuid4(), departamento['codigodepartamentoatencion'], departamento['nombredepartamentoatencion'])
    )

for municipio in municipios:
    session.execute(
        """
        INSERT INTO Municipio (id, codigomunicipioatencion, nombremunicipioatencion, codigodepartamentoatencion)
        VALUES (%s, %s, %s, %s)
        """,
        (uuid.uuid4(), municipio['codigomunicipioatencion'], municipio['nombremunicipioatencion'], municipio['codigodepartamentoatencion'])
    )

index = 1
for beneficiario in beneficiarios:
    session.execute(
        """
        INSERT INTO Beneficiario (id, idBeneficiario, bancarizado, discapacidad, etnia, genero, nivelescolaridad, pais, tipodocumento, titular, codigomunicipioatencion, estadobeneficiario)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (uuid.uuid4(), index, beneficiario['bancarizado'], beneficiario['discapacidad'], beneficiario['etnia'], beneficiario['genero'], beneficiario['nivelescolaridad'], beneficiario['pais'], beneficiario['tipodocumento'], beneficiario['titular'], beneficiario['codigomunicipioatencion'], beneficiario['estadobeneficiario'])
    )
    index += 1

i = 1
for programa in programas:


    session.execute(
        """
        INSERT INTO Programa (id, idPrograma, tipoasignacionbeneficio, fechainscripcionbeneficiario, tipobeneficio, tipopoblacion, rangobeneficioconsolidadoasignado, rangoultimobeneficioasignado, fechaultimobeneficioasignado, idBeneficiario, rangoedad, cantidaddebeneficiarios)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (uuid.uuid4(), i, programa['tipoasignacionbeneficio'], programa['fechainscripcionbeneficiario'], programa['tipobeneficio'], programa['tipopoblacion'], programa['rangobeneficioconsolidadoasignado'], programa['rangoultimobeneficioasignado'], programa['fechaultimobeneficioasignado'], i, programa['rangoedad'], programa['cantidaddebeneficiarios'])
    )
    i += 1

# Cerrar la conexión
cluster.shutdown()
print("Datos insertados en la base de datos Cassandra.")
