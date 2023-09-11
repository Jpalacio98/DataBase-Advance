import sys
import Interfaz
from Modelo_Clave_Valor import BD_Clave_Valor as BDCV
from PyQt6.QtWidgets import QApplication, QMainWindow,  QListWidgetItem


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
        return res

    def FiltarModeloCV2(self):
        self.filtros= Interfaz.obtener_lista_textos(self)
        res=[]
        fltro =[]
        data ={}
        for filtro in self.filtros:
            datos = filtro.split(" ")
            datos[0] = datos[0].lower()
            res.append(datos[0])
            fltro.append([datos[0],datos[1],datos[2]])
        lista = BDCV.tablaname(res)
        tabla_ordenada = sorted(lista, key=lambda x: len(x[1]))
        print(tabla_ordenada)
        cont=0
        for item in tabla_ordenada:
            if len(item[1])!=0: 
                cont+=1
        if cont>1:
            data = BDCV.filtradoV(fltro,tabla_ordenada)
            self.VisualizarDaosModeloCV(data)
        else:
            data = self.FiltarModeloCV()
            self.VisualizarDaosModeloCV(data)
        print(data)

    def VisualizarDaosModeloCV(self,data):

        self.label_resultado.setText(f"{len(data)} registros encontrados")
        for key,dato in data.items():
            item = QListWidgetItem(str(dato))
            self.tw_datos.addItem(item)
        
        filts=[]
        res=""
        for filt in self.filtros:
            flt = filt.split(" ")
            
            flt[0] = flt[0].lower()
            dataFilt=[]
            for key,dato in data.items():
                dataFilt.append(dato[flt[0]])
            filts.append([flt[0],len(dataFilt)])

        for dato in filts:
            text=f"{dato[0]}: {dato[1]}"
            item = QListWidgetItem(text)
            self.tw_resultados.addItem(item)
            

     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
