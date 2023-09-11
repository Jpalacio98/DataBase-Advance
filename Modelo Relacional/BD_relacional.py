import requests
import json


#response = requests["https://jpalacio2022.000webhostapp.com/API/configBD.php")

#response = requests.post(f"https://jpalacio2022.000webhostapp.com/API/{archivo}.php",data=data)
#print(response.text)


def llenarTablaDpto():
    with open("Tablas/departamentos.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for dpto in datos:
        data={
            'id':dpto["codigodepartamentoatencion"],
            'nombre':dpto["nombredepartamentoatencion"] 
        }
        response = requests.post(f"https://jpalacio2022.000webhostapp.com/API/adicionarDpto.php",data=data)
        listResult.append({'status_code':response.status_code,'message':response.text})
    return  listResult


def llenarTablaMun():
    with open("Tablas/municipios.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for mun in datos:
        data={
            'id':mun["codigomunicipioatencion"],
            'nombre':mun["nombremunicipioatencion"],
            'id_Dpto':mun["codigodepartamentoatencion"], 
        }
        response = requests.post(f"https://jpalacio2022.000webhostapp.com/API/adicionarMun.php",data=data)
        listResult.append({'status_code':response.status_code,'message':response.text})
    return  listResult



def llenarTablaBenficiario():
    with open("Tablas/beneficiario.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for benef in datos:
        data={
            'bancarizado':benef["bancarizado"],
            'discapacidad':benef["discapacidad"],
            'etnia':benef["etnia"], 
            'genero':benef["genero"], 
            'nivelescolaridad':benef["nivelescolaridad"], 
            'pais':benef["pais"], 
            'tipodocumento':benef["tipodocumento"], 
            'titular':benef["titular"], 
            'codigomunicipioatencion':benef["codigomunicipioatencion"],
            'estadobeneficiario':benef["estadobeneficiario"], 

        }
        response = requests.post(f"https://jpalacio2022.000webhostapp.com/API/adicionarMun.php",data=data)
        listResult.append({'status_code':response.status_code,'message':response.text})
    return  listResult


def llenarTablaPrograma():
    with open("Tablas/programa.json", 'r') as archivo:
        datos = json.load(archivo)
    listResult=[]
    for prog in datos:
        data = {
        'tipoasignacionbeneficio': prog["tipoasignacionbeneficio"],
        'tipobeneficio': prog["tipobeneficio"],
        'tipopoblacion': prog["tipopoblacion"],
        'rangobeneficioconsolidadoasignado': prog["rangobeneficioconsolidadoasignado"],
        'rangoultimobeneficioasignado': prog["rangoultimobeneficioasignado"],
        'fechaultimobeneficioasignado': prog["fechaultimobeneficioasignado"],
        'rangoedad': prog["rangoedad"],
        'cantidaddebeneficiarios': prog["cantidaddebeneficiarios"],
        }
        response = requests.post(f"https://jpalacio2022.000webhostapp.com/API/adicionarMun.php",data=data)
        listResult.append({'status_code':response.status_code,'message':response.text})
    return  listResult


