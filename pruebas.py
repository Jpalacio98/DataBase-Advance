benf={
    '0001':{'bancarizado': 'SI', 'discapacidad': 'NO', 'estadobeneficiario': 'ACTIVO', 'etnia': 'ND', 'genero': 'Mujer', 'idBeneficiario': 1999, 'idMun': '19100', 'nivelescolaridad': 'ND', 'pais': 'ND', 'tipodocumento': 'CC', 'titular': 'SI'},
    '0002':{'bancarizado': 'SI', 'discapacidad': 'NO', 'estadobeneficiario': 'ACTIVO', 'etnia': 'ND', 'genero': 'Mujer', 'idBeneficiario': 1999, 'idMun': '19100', 'nivelescolaridad': 'ND', 'pais': 'ND', 'tipodocumento': 'CC', 'titular': 'SI'},
    }

programa={
    '0001':{'idPrograma': '0001', 'amor': 'NO', 'poblacion': 'ACTIVO', 'rango': 'ND', 'tipo': 'Mujer', 'idBeneficiario': 1999},
    '0002':{'idPrograma': '0001', 'amor': 'NO', 'poblacion': 'ACTIVO', 'rango': 'ND', 'tipo': 'Mujer', 'idBeneficiario': 1999}
}


# atributos = set(list(benf.values())[0].keys()) & set(list(programa.values())[0].keys())
# print(atributos)

atributos = [[1, 2, 9, 4, 5], [1, 9, 3, 7, 5], [1, 2, 3, 4, 5]]
combinacionData = []

for i in range(len(atributos)):
    for j in range(i + 1, len(atributos)):
        atributos_comunes = set(atributos[i]).intersection(set(atributos[j]))
        if len(atributos_comunes) > 0:
            combinacionData.append([i, j, list(atributos_comunes)])

print(combinacionData)
