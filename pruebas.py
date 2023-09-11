benf={
    '0001':{'bancarizado': 'SI', 'discapacidad': 'NO', 'estadobeneficiario': 'ACTIVO', 'etnia': 'ND', 'genero': 'Mujer', 'idBeneficiario': 1999, 'idMun': '19100', 'nivelescolaridad': 'ND', 'pais': 'ND', 'tipodocumento': 'CC', 'titular': 'SI'},
    '0002':{'bancarizado': 'SI', 'discapacidad': 'NO', 'estadobeneficiario': 'ACTIVO', 'etnia': 'ND', 'genero': 'Mujer', 'idBeneficiario': 1999, 'idMun': '19100', 'nivelescolaridad': 'ND', 'pais': 'ND', 'tipodocumento': 'CC', 'titular': 'SI'},
    }

programa={
    '0001':{'idPrograma': '0001', 'amor': 'NO', 'poblacion': 'ACTIVO', 'rango': 'ND', 'tipo': 'Mujer', 'idBeneficiario': 1999},
    '0002':{'idPrograma': '0001', 'amor': 'NO', 'poblacion': 'ACTIVO', 'rango': 'ND', 'tipo': 'Mujer', 'idBeneficiario': 1999}
}


atributos = set(list(benf.values())[0].keys()) & set(list(programa.values())[0].keys())
print(atributos)