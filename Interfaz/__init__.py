from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QListWidgetItem
ui_file_path = "interfaz/interfaz.ui"

def configureUI(self):
    # Cargar el archivo .ui
    loadUi(ui_file_path,self)
    campos = [
        "",
        "Bancarizado",
        "CodigoDepartamentoAtencion",
        "CodigoMunicipioAtencion",
        "Discapacidad",
        "EstadoBeneficiario",
        "Etnia",
        "FechaInscripcionBeneficiario",
        "Genero",
        "NivelEscolaridad",
        "NombreDepartamentoAtencion",
        "NombreMunicipioAtencion",
        "Pais",
        "TipoAsignacionBeneficio",
        "TipoBeneficio",
        "TipoDocumento",
        "TipoPoblacion",
        "RangoBeneficioConsolidadoAsignado",
        "RangoUltimoBeneficioAsignado",
        "FechaUltimoBeneficioAsignado",
        "RangoEdad",
        "Titular",
        "CantidadDeBeneficiarios"                    
        ]

    # Realizar cambios en la interfaz
    self.statusbar.setStyleSheet(f"background-color: rgb(170, 255, 127); color: white;")
    self.cbox_Campo.addItems(campos)
    self.frame_rango.setVisible(False)
    self.cbox_Condicion.currentTextChanged.connect(lambda:ValorChanged(self))
    self.cbox_Campo.currentTextChanged.connect(lambda:CampoValues(self))
    self.btn_agregar.clicked.connect(lambda:agregar_a_lista(self))
    self.listWidget_filtros.itemDoubleClicked.connect(lambda:eliminar_de_lista(self,self.listWidget_filtros.currentItem()))



def ValorChanged(self):
    if self.cbox_Condicion.currentText() == "Rango":
        self.frame_rango.setVisible(True)
        self.frame_valor.setVisible(False)
        rangoflag=True
        # cargar los rangos
    else:
        self.frame_rango.setVisible(False)
        self.frame_valor.setVisible(True)

def CampoValues(self):
    values=[
        [],
        ["SI","NO"],
        [],
        [],
        ["SI","NO"],
        ["ACTIVO","NO ACTIVO"],
        ["RAIZAL","INDIGENA","AFROCOLOMBIANO – NEGRO","MESTIZO"],
        ["SI","NO"],
        ["Hombre","Mujer"],
        ["PRIMARIA","SECUNDARIA","TRANSICION","SIN ESPECIFICAR","POSGRADO"],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        
    ]
    self.cbox_Value.clear()
    self.cbox_Value.addItems(values[self.cbox_Campo.currentIndex()])
    
def agregar_a_lista(self):
    if self.frame_valor.isVisible():
        texto = f"{self.cbox_Campo.currentText()} {self.cbox_Condicion.currentText()} {self.cbox_Value.currentText()}"
    else:
      texto = f"{self.cbox_Campo.currentText()} {self.cbox_Condicion.currentText()} rango de {self.cbox_Rmin.currentText()} a {self.cbox_Rmax.currentText()}"  
    
    if texto:
        item = QListWidgetItem(texto)
        self.listWidget_filtros.addItem(item)
        self.cbox_Campo.setCurrentIndex(0)
        self.cbox_Condicion.setCurrentIndex(0)
        self.cbox_Value.setCurrentIndex(0)
        self.cbox_Rmin.setCurrentIndex(0)
        self.cbox_Rmax.setCurrentIndex(0)
    
def eliminar_de_lista(self, item):
    if item:
        self.listWidget_filtros.takeItem(self.listWidget_filtros.row(item))
            
def obtener_lista_textos(self):
    lista_textos = []
    # Recorrer los elementos del QListWidget y agregar sus textos a la lista
    for index in range(self.listWidget_filtros.count()):
        item = self.listWidget_filtros.item(index)
        if item is not None:
            texto = item.text()
            lista_textos.append(texto)
    return lista_textos






