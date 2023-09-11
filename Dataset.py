import pandas as pd
import json
from sodapy import Socrata

client = Socrata("www.datos.gov.co",
                 "U1UbMtgUtzZzxdlanUWUWx4mz",
                 username="jdavidpalacio@unicesar.edu.co",
                 password="@Jpalacio0949")

results = client.get("xfif-myr2", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
#results_df.fillna("ND", inplace=True)
#results_df['bancarizado'] = results_df['bancarizado'].fillna("ND")

#lis= list(results_df['bancarizado'])
#print(results_df['bancarizado'] )


#----------------------------------------------------------------------------------------------------------------------
# construimos los datos para la tabla departamento
departamentos = results_df[['codigodepartamentoatencion','nombredepartamentoatencion']]
#depuramos la tabla solo para dejar un insidencia de cada registro
depurar_DPTO = departamentos.drop_duplicates(subset='codigodepartamentoatencion')
# Mostrar los resultados
#print(depurar_DPTO)
#convertimos el data frame en un json 
depurar_DPTO.to_json("Tablas/departamentos.json", orient='records')

# Verificación: cargar el archivo JSON de nuevo en un DataFrame
# df_desde_json = pd.read_json("Tablas/departamentos.json", orient='records')
# # Mostrar el DataFrame cargado desde el archivo JSON
#print(df_desde_json)

#----------------------------------------------------------------------------------------------------------------------
# construimos los datos para la tabla municipio
municipios = results_df[['codigomunicipioatencion','nombremunicipioatencion','codigodepartamentoatencion']]
#depuramos la tabla solo para dejar un insidencia de cada registro
depurar_MUN = municipios.drop_duplicates(subset='codigomunicipioatencion')
# Mostrar los resultados
#print(depurar_DPTO)
#convertimos el data frame en un json 
depurar_MUN.to_json("Tablas/municipios.json", orient='records')

#----------------------------------------------------------------------------------------------------------------------
# construimos los datos para la tabla beneficiario
beneficiario = results_df[['bancarizado','discapacidad',
                           'etnia','genero','nivelescolaridad',
                           'pais','tipodocumento','titular',
                           'codigomunicipioatencion','estadobeneficiario']]
#convertimos el data frame en un json 

beneficiario.to_json("Tablas/beneficiario.json", orient='records')
# Mostrar los resultados
#print(beneficiario)


# construimos los datos para la tabla programa
programa = results_df[['fechainscripcionbeneficiario',
                       'tipoasignacionbeneficio',
                       'tipobeneficio','tipopoblacion',
                       'rangobeneficioconsolidadoasignado',
                       'rangoultimobeneficioasignado',
                       'fechaultimobeneficioasignado',
                       'rangoedad','cantidaddebeneficiarios']]
#convertimos el data frame en un json 
programa.to_json("Tablas/programa.json", orient='records')
# Mostrar los resultados
#print(programa.loc[programa['cantidaddebeneficiarios']>'2'])
