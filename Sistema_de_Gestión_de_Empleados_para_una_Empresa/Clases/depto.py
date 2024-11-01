from Clases.empleados import Empleados

class Depto:
    def __init__(self, id_departamento, nombre_departamento, telefono_departamento, id_empleado_a_cargo):
        self.empleado_a_cargo = Empleados(id_empleado_a_cargo, None, None, None, None, None, None, None, None, None)
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento
        self.telefono_departamento = telefono_departamento
