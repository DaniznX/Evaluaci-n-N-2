import Empleados
class Departamento():
    def __init__(self, id_departamento, nombre_departamento, telefono_departamento, id_empleados):
        Empleados.__init__(id_empleados)
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento
        self.telefono_departamento = telefono_departamento