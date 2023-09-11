import sys
import Interfaz
from Modelo_Clave_Valor import BD_Clave_Valor as BDCV
from PyQt6.QtWidgets import QApplication, QMainWindow


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        Interfaz.configureUI(self)
        self.filtros =[]
        self.btn_Crear.clicked.connect(self.FiltarModeloCV2)
        
        self.showMaximized()

    def algun_metodo(self):
        # Define acciones cuando se interactúa con la interfaz
        pass
    
    def FiltarModeloCV(self):
        self.filtros= Interfaz.obtener_lista_textos(self)
        res={}
        for filtro in self.filtros:
            datos = filtro.split(" ")
            datos[0] = datos[0].lower()
            res = BDCV.Filtro(datos[0],datos[1],datos[2],lista=res)
            print(res)

    def FiltarModeloCV2(self):
        self.filtros= Interfaz.obtener_lista_textos(self)
        res=[]
        fltro =[]
        for filtro in self.filtros:
            datos = filtro.split(" ")
            datos[0] = datos[0].lower()
            res.append(datos[0])
            fltro.append([datos[0],datos[1],datos[2]])
        lista = BDCV.tablaname(res)
        tabla_ordenada = sorted(lista, key=lambda x: len(x[1]))


        datos = BDCV.filtrado(fltro,tabla_ordenada)

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
