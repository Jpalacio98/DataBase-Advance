from firebase import firebase
from tqdm import tqdm
import pandas as pd
import json
 

firebase = firebase.FirebaseApplication("https://bd-avanzada-default-rtdb.firebaseio.com/",None)

def llenarTablaDpto():
    with open("Tablas/departamentos.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for dpto in datos:
        data={
            'idDpto':dpto["codigodepartamentoatencion"],
            'nombre':dpto["nombredepartamentoatencion"] 
        }
        response = firebase.post("/departamentos",data=data)
        if response != 'None':
            message="Registro Completo"
        else:
            message="Registro Inompleto"
        listResult.append(message)
    return  listResult

def llenarTablaMun():
    with open("Tablas/municipios.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for mun in datos:
        data={
            'idMun':mun["codigomunicipioatencion"],
            'nombre':mun["nombremunicipioatencion"],
            'idDpto':mun["codigodepartamentoatencion"], 
        }
        response = firebase.post("/municipios",data=data)
        if response != 'None':
            message="Registro Completo"
        else:
            message="Registro Inompleto"
        listResult.append(message)
    return  listResult

def llenarTablaBenficiario():
    with open("Tablas/beneficiario.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for index,benef in enumerate(tqdm(datos)):
        data={
            'idBeneficiario':index,
            'bancarizado':benef["bancarizado"],
            'discapacidad':benef["discapacidad"],
            'etnia':benef["etnia"], 
            'genero':benef["genero"], 
            'nivelescolaridad':benef["nivelescolaridad"], 
            'pais':benef["pais"], 
            'tipodocumento':benef["tipodocumento"], 
            'titular':benef["titular"], 
            'idMun':benef["codigomunicipioatencion"],
            'estadobeneficiario':benef["estadobeneficiario"], 
        }
        response = firebase.post("/beneficiarios",data=data)
        if response != 'None':
            message="Registro Completo"
        else:
            message="Registro Inompleto"
        listResult.append(message)
    return  listResult

def llenarTablaPrograma():
    with open("Tablas/programa.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for index,prog in enumerate(datos):
        data = {
        'idPrograma':index,
        'tipoasignacionbeneficio': prog["tipoasignacionbeneficio"],
        'tipobeneficio': prog["tipobeneficio"],
        'tipopoblacion': prog["tipopoblacion"],
        'rangobeneficioconsolidadoasignado': prog["rangobeneficioconsolidadoasignado"],
        'rangoultimobeneficioasignado': prog["rangoultimobeneficioasignado"],
        'fechaultimobeneficioasignado': prog["fechaultimobeneficioasignado"],
        'idBeneficiario':index,
        'rangoedad': prog["rangoedad"],
        'cantidaddebeneficiarios': prog["cantidaddebeneficiarios"],
        }
        response = firebase.post("/programa",data=data)
        if response != 'None':
            message="Registro Completo"
        else:
            message="Registro Inompleto"
        listResult.append(message)
    return  listResult

def Resultados(datos):
    clases = {}
    # Contar la frecuencia de cada clase en la lista
    for elemento in datos:
        if elemento in clases:
            clases[elemento] += 1
        else:
            clases[elemento] = 1
    # Imprimir las clases y sus cuentas
    data =[]
    for clase, count in clases.items():
        print(f"{clase}: {count}")
        data.append([clase,count])
    return data

def listarTablaDpto():
    datos = firebase.get("/departamentos","")
    return list(datos)
def BuscarTablaDpto(id):
    return firebase.get("/departamentos",id)

def listarTablaDpto():
    datos = firebase.get("/departamentos","")
    return list(datos)
def BuscarTablaDpto(id):
    return firebase.get("/departamentos",id)

def listarTablabeneficiarios():
    datos = firebase.get("/beneficiarios","")
    return datos
def BuscarTablabeneficiarios(id):
    return firebase.get("/beneficiarios",id)

def listarTablaPrograma():
    datos = firebase.get("/programa","")
    return datos
def BuscarTablaPrograma(id):
    return firebase.get("/programa",id)

def buscar(lista,criterio,id):
    for i in lista:
        if i[criterio]==id:
            return i

#-------llenado de tablas------#
# res = llenarTablaDpto()
# Resultados(res)
# res = llenarTablaMun()
# Resultados(res)
#res = llenarTablaBenficiario()
# Resultados(res)
# res = llenarTablaPrograma()
# Resultados(res)


#----------------DESARROLLO DE CONSULTAS---------------#
# #1)¿Cuántos tipos de población hay y cuatos beneficiarios hay por cada tipo?
# results =listarTablaPrograma()
# lista =[]
# for clave, element in results.items():
#     lista.append(element['tipopoblacion'])

# result = list(set(lista))
# ind = result.index("ND")
# result.pop(ind)
# print(f"Hay {len(result)} tipos de poblacio")
# print("Tipos de población:",*result, sep='\n')

# #2)¿Cuántos beneficiarios hay en cada tipo de población?
# Resultados(lista)


# #3) ¿Cuál es el rango más alto de beneficio consolidado asignado?
# results3 =listarTablaPrograma()
# lista3 =[]
# for clave, element in results3.items():
#     lista3.append(element['rangobeneficioconsolidadoasignado'])
# results3 = list(set(lista3))
# mayor = max(results3)
# print(*results3,sep='\n')
# print("Este es el mayor Rango: ",mayor)

# #4) ¿Cuál es el límite mas alto de beneficiarios por núcleo familiar?
# results = listarTablaPrograma()
# lista =[]
# for clave, element in results.items():
#     lista.append(element['cantidaddebeneficiarios'])
# results = list(set(lista))
# mayor = max(results)
# print("Este es el mayor Rango: ",mayor)
# #print(*results4,sep='\n')

# #5) ¿Cuántos beneficiarios se encuentran bancarizados?
# results = listarTablabeneficiarios()
# cant =0
# lista =[]
# for clave, element in results.items():
#     if element['bancarizado'] == 'SI':
#         lista.append(element)
# cant = lista.__len__()
# print("Numero de beneficiarios bancarizados:",cant) 

# #6) ¿Cuánto beneficiarios hay por cada género?
# results = listarTablabeneficiarios()
# lista =[]
# for clave, element in results.items():
#     lista.append(element['genero'])

# Resultados(lista)


# #7) ¿Cuánto beneficiarios hombres, no bacarizados y desplazados hay?
# results = listarTablabeneficiarios()
# lista =[]
# for clave, element in results.items():
#     if element['genero']=='Hombre' and element['bancarizado']=='NO':
#         lista.append(element['idBeneficiario'])
# #print(lista)
# results2 = listarTablaPrograma()
# lista2=[]
# for item in lista:
#     for clave, element in results2.items():
#         if element['idBeneficiario']==item and element['tipopoblacion']=='DESPLAZADOS':
            
#             lista2.append(element)
# print("Cantida de beneficiarios hombres, no bacarizados y desplazados: ",len(lista2))


# # 8) ¿Cuál es el tipo de beneficio que mas tienen las mujeres?
# results = listarTablabeneficiarios()
# lista =[]
# for clave, element in results.items():
#     if element['genero']=='Mujer':
#         lista.append(element['idBeneficiario'])
# #print(lista)
# results2 = listarTablaPrograma()
# lista2=[]
# for item in lista:
#     for clave, element in results2.items():
#         if element['idBeneficiario']==item and element['tipobeneficio'] != 'ND':
#             lista2.append(element['tipobeneficio'])
# res = Resultados(lista2)
# mayor = max(res, key=lambda x: x[1])
# print("tipo de beneficio que mas tienen las mujeres: ",mayor)