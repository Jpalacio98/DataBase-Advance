from cassandra.cluster import Cluster

# Configura la conexión a tu clúster de Cassandra
cluster = Cluster(['127.0.0.1'])  # Reemplaza con la dirección de tu clúster
session = cluster.connect('dbcolumnas')  # Reemplaza 'dbcolumnas' con tu keyspace

'''
# ¿Cuántos tipos de población hay y cuales son?

consulta = "SELECT tipopoblacion FROM Programa"

resultados = session.execute(consulta)

# Crear un conjunto para almacenar tipos de población únicos
tiposDePoblacionUnicos = set()

for fila in resultados:
    # Accede al valor de "tipopoblacion"
    tipoPoblacion = fila.tipopoblacion

    # Agrega el tipo de población al conjunto si es diferente de nulo
    if tipoPoblacion is not None:
        tiposDePoblacionUnicos.add(tipoPoblacion)

# Imprime la cantidad de tipos de población y la lista de tipos
print(f"Cantidad de tipos de población: {len(tiposDePoblacionUnicos)}")
print("Tipos de población:")
for tipo in tiposDePoblacionUnicos:
    print(tipo)
'''

'''
# ¿Cuál es el rango más alto de beneficio consolidado asignado?

consulta = "SELECT rangobeneficioconsolidadoasignado FROM Programa"

resultados = session.execute(consulta)

# Almacena los rangos en una lista
rangos = []

for fila in resultados:
    rango = fila.rangobeneficioconsolidadoasignado
    rangos.append(rango)

# Encuentra el rango más alto en la lista
rangoMasAlto = max(rangos, default="No hay datos")

print(f"Rango más alto de beneficio consolidado asignado: {rangoMasAlto}")
'''

'''
# programas con el limite mas alto de beneficiario cuando el tipo de asignacion es MONETARIO

consulta = "SELECT id, tipoasignacionbeneficio, cantidaddebeneficiarios FROM Programa WHERE tipoasignacionbeneficio = 'MONETARIO' ALLOW FILTERING"

# Ejecutar la consulta en Cassandra
resultados = session.execute(consulta)

# Crear una lista para almacenar programas como tuplas (ID, Tipo de Asignación, Cantidad de Beneficiarios)
programas = []

# Iterar a través de los resultados de la consulta
for fila in resultados:
    # Obtener el ID, Tipo de Asignación y Cantidad de Beneficiarios de cada fila
    id_programa = fila.id
    tipo_asignacion = fila.tipoasignacionbeneficio
    cantidad_beneficiarios = fila.cantidaddebeneficiarios

    # Agregar los datos como una tupla a la lista de programas
    programas.append((id_programa, tipo_asignacion, cantidad_beneficiarios))

# Ordenar la lista de programas por la cantidad de beneficiarios en orden descendente
programas.sort(key=lambda x: x[2], reverse=True)

# Encontrar el límite más alto de beneficiarios
limiteMasAlto = programas[0][2] if programas else 0

print(f"El límite más alto de beneficiarios es: {limiteMasAlto}")

# Verificar si hay programas con el límite más alto
if programas:
    # Mostrar programas con el límite más alto de beneficiarios y sus detalles
    print("Programas con el límite más alto de beneficiarios:")
    for programa in programas:
        print(f"ID: {programa[0]}, Tipo de Asignación: {programa[1]}, Cantidad de Beneficiarios: {programa[2]}")
else:
    # Mostrar un mensaje si no se encontraron programas con asignación 'MONETARIO'
    print("No se encontraron programas con el tipo de asignación 'MONETARIO'.")
'''

'''
# columnas de la tabla Programa
consulta = "SELECT * FROM Programa LIMIT 1"
resultados = session.execute(consulta)

metadata = resultados.column_names

for columna in metadata:
    print(columna)
'''

'''
# ¿Cuántos beneficiarios se encuentran bancarizados?
consulta = "SELECT COUNT(*) AS cantidad_bancarizados FROM Beneficiario WHERE bancarizado = 'SI' ALLOW FILTERING"

resultados = session.execute(consulta)

for fila in resultados:
    cantidadBancarizados = fila.cantidad_bancarizados

print(f"Cantidad de beneficiarios bancarizados: {cantidadBancarizados}")
'''

# ¿Cuántos beneficiarios hay por cada género?
consulta = "SELECT genero FROM Beneficiario"

resultados = session.execute(consulta)

# Almacena los géneros en una lista
generos = []

for fila in resultados:
    genero = fila.genero
    generos.append(genero)

# Realiza la agregación de la cantidad de beneficiarios por género
conteoPorGenero = {}

for genero in generos:
    if genero in conteoPorGenero:
        conteoPorGenero[genero] += 1
    else:
        conteoPorGenero[genero] = 1

# Muestra la cantidad de beneficiarios por género
print("Cantidad de beneficiarios por género:")
for genero, cantidad in conteoPorGenero.items():
    print(f"Género: {genero}, Cantidad de beneficiarios: {cantidad}")

'''
# nombre de los departamentos?

# Define la tabla de departamentos
departamentoTable = session.execute("SELECT * FROM Departamento LIMIT 1")

# Imprime los nombres de los departamentos
for row in departamentoTable:
    print(row.nombredepartamentoatencion)
'''

'''
# tabla departamento

# Define la tabla de departamentos
departamentoTable = session.execute("SELECT * FROM Departamento")

# Imprime todos los atributos de los departamentos
for row in departamentoTable:
    print(f"ID: {row.id}, Código Departamento: {row.codigodepartamentoatencion}, Nombre Departamento: {row.nombredepartamentoatencion}")
'''

# Cerrar la conexión
cluster.shutdown()
print("Consulta finalizada.")
