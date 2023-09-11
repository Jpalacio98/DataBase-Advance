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
    self.statusbar.setStyleSheet(f"background-color:  rgb(147, 194, 255); color: black;")
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
        [],
        ["Hombre","Mujer"],
        ["PRIMARIA","SECUNDARIA","TRANSICION","SIN ESPECIFICAR","POSGRADO"],
        ["ATLANTICO", "BOLIVAR", "HUILA", "CAUCA", "MAGDALENA", "TOLIMA", "GUAVIARE", "CASANARE", "CESAR", "CUNDINAMARCA", "QUINDIO", "CORDOBA", "SUCRE", "CALDAS", "ARAUCA", "ANTIOQUIA", "LA GUAJIRA", "NARIÑO", "GUAINIA", "NORTE DE SANTANDER", "BOYACA", "CAQUETA", "RISARALDA", "SANTANDER", "PUTUMAYO", "AMAZONAS", "VALLE", "META", "SAN ANDRES", "BOGOTA", "CHOCO", "VICHADA"],
        ["LURUACO", "SANTA CATALINA", "SUAZA", "EL TAMBO", "GUAMAL", "COYAIMA", "SAN JOSE DEL GUAVIARE", "YOPAL", "BOSCONIA", "GUAPI", "CHIPAQUE", "ARMENIA", "SAN PELAYO", "TAURAMENA", "SAMPUES", "PENSILVANIA", "MONTERIA", "SOTARA", "ATACO", "MARIA LA BAJA", "ARAUCA", "MOMIL", "SAN JOSE", "BELLO", "MEDELLIN", "CALDONO", "PINILLOS", "MANAURE", "SAN ANDRES DE TUMACO", "EL TABLON DE GOMEZ", "INIRIDA", "RIOSUCIO", "ARAUQUITA", "GARZON", "LA FLORIDA", "BECERRIL", "ARACATACA", "CHITAGA", "COTORRA", "MALAMBO", "LABRANZAGRANDE", "EL SANTUARIO", "LA MONTAÑITA", "SANTA BARBARA DE PINTO", "ACEVEDO", "CURILLO", "PURIFICACION", "MURILLO", "LA PLAYA", "PUERTO ESCONDIDO", "PUEBLO RICO", "EL CARMEN", "SIMITI", "SAN VICENTE DEL CAGUAN", "MUTATA", "MAGÜI", "FLORIDABLANCA", "GIGANTE", "LA GLORIA", "EL PASO", "BETULIA", "VILLAVIEJA", "URIBIA", "OVEJAS", "SIBUNDOY", "CONVENCION", "OPORAPA", "PUERTO NARIÑO", "BRICEÑO", "GINEBRA", "SUAREZ", "PASTO", "LA PLATA", "PAEZ", "EL CARMEN DE VIBORAL", "CHIPATA", "SINCELEJO", "CORINTO", "ZONA BANANERA", "TIPACOQUE", "SANTUARIO", "GRANADA", "REPELON", "SANTA ROSA", "FILANDIA", "CALDAS", "CARTAGO", "CANDELARIA", "SUCRE", "CUCUTA", "SALGAR", "ENVIGADO", "SANTA ROSA DEL SUR", "POPAYAN", "SAN ANTERO", "VALENCIA", "MELGAR", "SANTA MARTA", "PLANETA RICA", "PUERTO LOPEZ", "REMEDIOS", "SAN ANDRES", "SAN ALBERTO", "TOLEDO", "CHAPARRAL", "BARRANCAS", "VILLANUEVA", "FUNZA", "CHINCHINA", "SANTACRUZ", "BARRANCABERMEJA", "CHARALA", "PEREIRA", "CHINU", "GUARANDA", "SITIONUEVO", "AQUITANIA", "DOLORES", "CAJIBIO", "APARTADO", "FUNDACION", "SAN JERONIMO", "PORE", "JAMUNDI", "PUERTO BOYACA", "CHACHAGÜI", "MISTRATO", "DUITAMA", "EL PEÑON", "PUERTO LLERAS", "EL BANCO", "SAMANIEGO", "MORALES", "JUNIN", "BOGOTA D.C.", "DABEIBA", "CALI", "SUESCA", "SAN FERNANDO", "BUENAVENTURA", "ARROYOHONDO", "LA CALERA", "SABANA DE TORRES", "LETICIA", "TENERIFE", "LA MACARENA", "LINARES", "YARUMAL", "RIOBLANCO", "MARINILLA", "SANTANDER DE QUILICHAO", "BUCARAMANGA", "SAN MARTIN DE LOBA", "PUERTO GAITAN", "CARTAGENA", "SAN RAFAEL", "ALMEIDA", "SAN LUIS DE SINCE", "OBANDO", "LA DORADA", "INZA", "SANTO TOMAS", "SANTA ANA", "LIBANO", "LA TEBAIDA", "MORROA", "AGUACHICA", "FRONTINO", "CABRERA", "PLATO", "SALDAÑA", "NEMOCON", "VEGACHI", "VILLAPINZON", "RIO QUITO", "ANGELOPOLIS", "TADO", "FLORENCIA", "PITALITO", "TURBO", "VALDIVIA", "PUERTO CAICEDO", "PUERTO ASIS", "VILLAVICENCIO", "URRAO", "CIENAGA DE ORO", "EL CARMEN DE ATRATO", "LOS PALMITOS", "TALAIGUA NUEVO", "OLAYA HERRERA", "IPIALES", "ACANDI", "SAN JACINTO", "SAHAGUN", "PIOJO", "CHIMICHAGUA", "JURADO", "PUERTO LIBERTADOR", "JAMBALO", "NUEVA GRANADA", "SANTIAGO", "ALMAGUER", "SAN JUAN DEL CESAR", "TURBACO", "LA APARTADA", "AMALFI", "PACHO", "BETEITIVA", "LA ESTRELLA", "RIONEGRO", "MONTELIBANO", "PACORA", "EL BAGRE", "TOCA", "FUSAGASUGA", "MOÑITOS", "TINJACA", "QUIBDO", "MOMPOS", "CERETE", "PATIA", "TABIO", "EL RETEN", "EL COPEY", "ARBOLEDA", "CAICEDO", "ALBAN", "OLAYA", "VALLEDUPAR", "GUADALAJARA DE BUGA", "ALGECIRAS", "SALADOBLANCO", "SAN PABLO", "TAME", "CAPARRAPI", "ARENAL", "TOLU VIEJO", "BARBACOAS", "SEGOVIA", "CAMPOHERMOSO", "SAN ANDRES SOTAVENTO", "ALTOS DEL ROSARIO", "PURACE", "AGUSTIN CODAZZI", "PEÑOL", "ALDANA", "Juan de Acosta", "Hacari", "Pijiño del Carmen", "Suaita", "Charta", "Puerto Colombia", "Soledad", "Albania", "Caloto", "Tuta", "Ayapel", "Ciudad Bolivar", "San Onofre", "Guadalupe", "Manati", "Dosquebradas", "Villamaria", "Puerto Tejada", "Puerto Wilches", "Lorica", "Galeras", "Aipe", "SABANAS DE SAN ANGEL", "Cubara", "Chiquinquira", "Belen de Umbria", "Santa Barbara", "Bolivar", "Pradera", "Los Cordobas", "Carmen del Darien", "Cicuco", "Salamina", "Bojaya", "Ocaña", "Argelia", "San Juan de Uraba", "Dibulla", "Padilla", "Paz de Ariporo", "Choachi", "Tierralta", "Pueblorrico", "Leiva", "Villarrica", "El Paujil", "El Piñon", "Astrea", "Guatica", "Acacias", "Anserma", "Mosquera", "Puerto Nare", "Chia", "Mani", "Mercaderes", "Saravena", "Necocli", "San Francisco", "Dagua", "Neiva", "Rosas", "Santa Sofia", "Santa Maria", "Chima", "Timbiqui", "Los Patios", "Aguadas", "Mahates", "La Capilla", "Pailitas", "Agrado", "Guavata", "Planadas", "Santa Lucia", "Guateque", "Arcabuco", "Atrato", "San Vicente de Chucuri", "Riohacha", "La Virginia", "Alvarado", "Nariño", "Totoro", "Espinal", "Santa Rosa de Viterbo", "Marulanda", "Itagui", "Puerto Rondon", "Arjona", "Santafe de Antioquia", "Casabianca", "Pedraza", "Caucasia", "El Carmen de Bolivar", "Florida", "Paramo", "Palmito", "El Zulia", "Barranquilla", "Calarca", "Ibague", "Venecia", "Clemencia", "El Doncello", "Moniquira", "Turbana", "Victoria", "Velez", "Alto Baudo", "El Litoral del San Juan", "Campoalegre", "Corozal", "Distraction", "Villagarzon", "Nechi", "El Charco", "Zambrano", "Concepcion", "La Paz", "San Pedro de Uraba", "Silvia", "Solano", "Magangue", "La Celia", "La Sierra", "Natagaima", "Puerto Berrio", "Angostura", "Jardin", "CACHIRA", "SOACHA", "SAN MARTIN", "VIOTA", "BOCHALEMA", "SANTA ISABEL", "ORITO", "EL TARRA", "TULUA", "QUINCHIA", "BARANOA", "SORA", "BUENAVISTA", "FACATATIVA", "PUERTO PARRA", "SOCORRO", "GALAN", "CIENAGA", "CHIVATA", "RETIRO", "CONDOTO", "EL RETORNO", "SAN SEBASTIAN DE BUENAVISTA", "CHAMEZA", "ZETAQUIRA", "SORACA", "SAN ANTONIO", "AGUA DE DIOS", "TARAZA", "BELEN DE LOS ANDAQUIES", "ANCUYA", "IQUIRA", "SAN MARCOS", "ANZA", "CARACOLI", "PELAYA", "TIBU", "PASCA", "SAMANA", "ARBOLETES", "PUERTO TRIUNFO", "CHIRIGUANA", "MIRANDA", "ANSERMANUEVO", "SAN PEDRO DE LOS MILAGROS", "TAMINANGO", "MOCOA", "UTICA", "SAN CRISTOBAL", "CACERES", "GACHANCIPA", "CHINACOTA", "EL CARMEN DE CHUCURI", "SAN LUIS", "PALMAR DE VARELA", "LA JAGUA DE IBIRICO", "MORELIA", "CAÑASGORDAS", "SAN AGUSTIN", "GIRON", "DURANIA", "EL ROSARIO", "ZAPAYAN", "COLON", "MALLAMA", "SAN SEBASTIAN DE MARIQUITA", "QUEBRADANEGRA", "NUNCHIA", "ROBERTO PAYAN", "SANTO DOMINGO", "URIBE", "RIO VIEJO", "PÁEZ", "SAN CARLOS", "SILVANIA", "TIQUISIO", "VILLA DEL ROSARIO", "GALAPA", "SAN MIGUEL", "TIBIRITA", "YUMBO", "LANDAZURI", "APIA", "SAN JUAN NEPOMUCENO", "PUEBLO NUEVO", "VIGIA DEL FUERTE", "SANDONA", "MEDIO SAN JUAN", "SONSON", "PIENDAMO", "CARTAGENA DEL CHAIRA", "BUGALAGRANDE", "YALI", "SAN JOSE DE URE", "ISTMINA", "GUATAPE", "VALLE DEL GUAMUEZ", "PALMIRA", "TUBARA", "COLOSO", "EL ROBLE", "SAN ZENON", "CORDOBA", "NOVITA", "TORO", "BARRANCO MINAS", "ZARZAL", "CAREPA", "GACHANTIVA", "POLICARPA", "TAUSA", "FUNES", "ALEJANDRIA", "ITUANGO", "QUIMBAYA", "PAICOL", "FLORESTA", "SABANALARGA", "CACOTA", "PUERTO CARREÑO", "SAN PEDRO", "MALAGA", "MEDINA", "BETANIA", "BARBOSA", "TIMANA", "RIOFRIO", "ORTEGA", "PUEBLO BELLO", "DONMATIAS", "PEQUE", "ARMERO", "URAMITA", "SANTIAGO DE TOLU", "EL CERRITO", "CONCORDIA", "SUTATAUSA", "PAIPA", "PUERTO RICO", "PIVIJAY", "GAMARRA", "PALESTINA", "MONTERREY", "GUAYABETAL", "LA BELLEZA", "SAN BENITO ABAD", "MESETAS", "EL MOLINO", "MARMATO", "EL GUAMO", "BAJO BAUDO", "LOPEZ", "MONTENEGRO", "LA VEGA", "UNGUIA", "CHIGORODO", "CUCUTILLA", "PUPIALES", "CHALAN", "MOLAGAVITA", "CONTADERO", "LENGUAZAQUE", "VILLA DE SAN DIEGO DE UBATE", "SAN BERNARDO DEL VIENTO", "SEVILLA", "PALOCABILDO", "JERICO", "TESALIA", "RIVERA", "HATILLO DE LOBA", "BALBOA", "VILLA RICA", "SOPETRAN", "PIEDECUESTA", "AMAGA", "GOMEZ PLATA", "SUPIA", "OROCUE", "YONDO", "ANAPOIMA", "COMBITA", "CIMITARRA", "MONGUA", "EL AGUILA", "TRINIDAD", "RICAURTE", "URUMITA", "UBALA", "CUMBAL", "SAN SEBASTIAN", "PAMPLONITA", "MEDIO BAUDO", "OTANCHE", "TAMESIS", "MARQUETALIA"],
        ["Colombia", "COLOMBIA"],
        ["MONETARIO","ND"],
        ["ND","EDUCACIÓN PRIMARIANUTRICIÓN MENOR","NUTRICIÓN MENOR","EDUCACIÓN SECUNDARIA","TRANSICIÓN","TRANSICIÓNNUTRICIÓN MENOR","EDUCACIÓN PRIMARIA","NUTRICIÓN"],
        ["CC","TI","RC", "No definido"],
        ["UNIDOS","ND","SISBEN","INDIGENAS","DESPLAZADOS"],
        ["4.500.001 - 6.000.000","0 - 1.500.000","> 6.000.001","1.500.001 - 3.000.000","3.000.001 - 4.500.000"],
        ["0 - 1.300.000"],
        ["2018-01-01","1900-01-01","2014-01-01","2015-01-01","2016-01-01","2017-01-01"],
        ["30-49","18-29","06-17","50-65","50-65"],
        ["SI","NO"],
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






