from firebase import firebase
from tqdm import tqdm
import pandas as pd
import json
 

firebase = firebase.FirebaseApplication("https://bd-avanzada-default-rtdb.firebaseio.com/",None)
filtroResponse=[]
beneficiario =['bancarizado','discapacidad',
                           'etnia','genero','nivelescolaridad',
                           'pais','tipodocumento','titular',
                           'codigomunicipioatencion','estadobeneficiario']
programa=['fechainscripcionbeneficiario',
                       'tipoasignacionbeneficio',
                       'tipobeneficio','tipopoblacion',
                       'rangobeneficioconsolidadoasignado',
                       'rangoultimobeneficioasignado',
                       'fechaultimobeneficioasignado',
                       'rangoedad','cantidaddebeneficiarios']
municipio=['codigomunicipioatencion','nombremunicipioatencion','codigodepartamentoatencion']
departamento=['codigodepartamentoatencion','nombredepartamentoatencion']


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
    return datos
def BuscarTablaDpto(id):
    return firebase.get("/departamentos",id)

def listarTablaMun():
    datos = firebase.get("/municipios","")
    return datos
def BuscarTablaMun(id):
    return firebase.get("/municipios",id)

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

listaTablas=[[departamento,"departamento"],[municipio,"municipio"],[beneficiario,"beneficiario"],[programa,"Programa"]]
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
# print("tipo de beneficio que mas tienen las mujeres: ",mayor[0])




# # 9) cual es el departamento con mas porcentaje de beneficiarios 
# # y de ese porcertanje cuanto son hombre y cuanto mujeres?

# results = listarTablaDpto()
# results2 = listarTablaMun()
# results3 = listarTablabeneficiarios()

# Ldpto=[]
# rdpto =[]
# for claveD, dpto in results.items():#recorre los dpto
#     mncp=[]
#     hom=[]
#     muj=[]
#     for claveM, mun in results2.items():#recorre los Mun
#         if dpto['idDpto'] == mun['idDpto']:
#             for claveB, benf in results3.items():#recorre los beneficiarios
#                 if mun['idMun'] == benf['idMun']:
#                     if benf['genero'] == 'Hombre':
#                         hom.append(benf)
#                     elif benf['genero']=='Mujer':
#                         muj.append(benf)
#             mncp.append(mun['idMun'])
#             #mncp.append([mun['idMun'],hom, muj])#beneficiarios por municipio
#     Ldpto.append([dpto['nombre'],mncp,hom,muj])
#     rdpto.append([dpto['nombre'],len(mncp),len(hom),len(muj),(len(hom)+len(muj))])


# mayor = max(rdpto, key=lambda x: x[1])
# print("el departamento con mas porcentaje de beneficiarios: ",mayor)
# print("Beneficiariosa por departamento")
# print(*rdpto,sep='\n')

# 
# res = Resultados(lista)

def Filtro(campo,operador,value, lista={}):
    print(campo)
    if not lista:
        results = selectDatos(campo)
    else:
        results = lista.copy()
        lista.clear()

    for clave, element in results.items():
        valor = f'item {operador} value'  # Utiliza un f-string para construir la expresión
        res = eval(valor, {"item": element[campo], "value": value}) 
        if res:
            lista[clave]= element
    print("")
    print("")
    return lista


def selectDatos(campo):
    print(campo)
    for tabla in listaTablas:
        for item in tabla[0]:
            if item == campo:
                if tabla[1]=="Departamento":
                    return listarTablaDpto()
                elif tabla[1]=="municipio":
                    return listarTablaMun()
                elif tabla[1]=="beneficiario":
                    return listarTablabeneficiarios()
                else:
                    return listarTablaPrograma()

def tablaname(listacampo):
    listDpto =[]
    listMun =[]
    listBenf =[]
    listProg =[]
    for tabla in listaTablas:
        for item in tabla[0]:
            for campo in listacampo:
                if item == campo:
                    if tabla[1]=="departamento":
                        listDpto.append(campo)
                    elif tabla[1]=="municipio":
                        listMun.append(campo)
                    elif tabla[1]=="beneficiario":
                        listBenf.append(campo)
                    else:
                        listProg.append(campo)
                    
    return[["departamento",listDpto],["municipio",listMun],["beneficiario",listBenf],["programa",listProg]]

def get_data(dato):
    if dato=="Departamento":
        return listarTablaDpto()
    elif dato=="municipio":
        return listarTablaMun()
    elif dato=="beneficiario":
        return listarTablabeneficiarios()
    else:
        return listarTablaPrograma()


def CreateFilter(campo,operador,value):
    valor = f'item {operador} value'  # Utiliza un f-string para construir la expresión
    res = eval(valor, {"item": campo, "value": value}) 
    return res

# def filtradoU(filtros,campos):
#     dataSet ={}
#     for clave, datos in campos:
#         reg = get_data(clave)
#         for key, item in reg:
#             for ref in datos:
#                 for filt in filtros:
#                     if ref == filt[0]:
#                         valor= CreateFilter(item[reg],filt[1],filt[2])
#                         if valor:
#                             dataSet[key]= item
#     return dataSet
    

def filtradoV(filtros,listcampos):
    listData=[]
    atributos=[]
    combinacionData=[]
    final_data={}

    for tipo, campos in listcampos:
        datos = get_data(tipo)
        data={}
        for key, item in datos.items():
            for camp in campos:
                for filt in filtros:
                    if camp == filt[0]:
                        res = CreateFilter(item[camp],filt[1],filt[2])
                        if res:
                            data[key]=item
        listData.append(data)
    
    for data in listData:
        if len(data) != 0:
            atributos.append( list(data.values())[0].keys())
            print(atributos)
        else:
            atributos.append([])

    for i in range(len(atributos)):
        for j in range(i + 1, len(atributos)):
            atributos_comunes = set(atributos[i]).intersection(set(atributos[j]))
            if len(atributos_comunes) > 0:
                combinacionData.append([i, j, list(atributos_comunes)])
            
    print(combinacionData)
    for comb in combinacionData:
        tabla1=listData[comb[0]]
        tabla2=listData[comb[1]]
        for atrib in comb[2]:
            for key1,tab1 in tabla1.items():
                for key2,tab2 in tabla2.items():
                    if tab1[atrib] == tab2[atrib]:
                        final_data[key1]=tab1

    return final_data




# results = listarTablabeneficiarios()
# lista ={}
# for clave, element in results.items():
#     if element['bancarizado']=='NO':
#         lista[clave]=element

# results2= lista.copy()
# lista.clear()
# for clave, element in results2.items():
#     if element['discapacidad']=='SI':
#         lista[clave]=element
# print(lista)