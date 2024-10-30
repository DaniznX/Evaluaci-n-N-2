import Proyectos
import Empleados
class Proyecto_Empleados():
    def __init__(self, id_proyecto_empleados, id_proyecto, id_empleados):
        Proyectos.__init__(id_proyecto)
        Empleados.__init__(id_empleados)
        self.id_proyecto_empleados = id_proyecto_empleados