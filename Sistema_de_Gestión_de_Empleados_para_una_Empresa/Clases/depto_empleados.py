from Clases import empleados, depto
from Ruts import rut
class Departamento_empleados():
    def __init__(self, id_departamento_empleados, id_departamento, id_empleados):
        empleados.__init__(id_empleados)
        depto.__init__(id_departamento)
        self.id_departamento_empleados = id_departamento_empleados
        
    def validar_empleados(self):
        return rut.is_valid_rut(self.rut_empleados)
    pass
    if (validar_empleados == rut):
        True
    else: 
        False