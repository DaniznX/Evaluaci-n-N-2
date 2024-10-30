import Empleados
import Depto
from Ruts import Rut
class Departamento_empleados():
    def __init__(self, id_departamento_empleados, id_departamento, id_empleados):
        Empleados.__init__(id_empleados)
        Depto.__init__(id_departamento)
        self.id_departamento_empleados = id_departamento_empleados
        
    def validar_empleados(self):
        return Rut.is_valid_rut(self.rut_empleados)
    pass
    if (validar_empleados == Rut):
        True
    else: 
        False