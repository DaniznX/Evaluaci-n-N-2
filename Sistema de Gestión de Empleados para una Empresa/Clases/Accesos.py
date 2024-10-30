import Empleados
import Modulos
class accesos():
    def __init__(self, id_accesos, id_empleados, id_modulos):
        Empleados.__init__(id_empleados)
        Modulos.__init__(id_modulos)
        self.id_accesos = id_accesos
        