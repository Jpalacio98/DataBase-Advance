
class Departamento:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    # Método para convertir un objeto de clase Departamento a un diccionario JSON
    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

    # Método de clase para crear una instancia de Departamento a partir de un diccionario JSON
    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data['id'],
            nombre=json_data['nombre']
    )