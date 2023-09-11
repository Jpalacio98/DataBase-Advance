

class Municipio:
    def __init__(self, id, nombre, id_Dpto):
        self.id = id
        self.nombre = nombre
        self.id_Dpto = id_Dpto

    # Método para convertir un objeto de la clase Municipio a un diccionario JSON
    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'id_Dpto': self.id_Dpto
        }

    # Método de clase para crear una instancia de Municipio a partir de un diccionario JSON
    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data['id'],
            nombre=json_data['nombre'],
            id_Dpto=json_data['id_Dpto']
        )
    