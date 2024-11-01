from Clases import proyectos, empleados
class Proyecto_Empleados():
    def __init__(self, id_proyecto_empleados, id_proyecto, id_empleados):
        proyectos.__init__(id_proyecto)
        empleados.__init__(id_empleados)
        self.id_proyecto_empleados = id_proyecto_empleados