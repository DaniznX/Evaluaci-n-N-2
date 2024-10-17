import Empleados
class Informe():
    def __init__(self, id_informe, nombre_informe, fecha_creacion_informe, id_empleado, ubicacion_informe):
        Empleados.__init__(id_empleado)
        self.id_informe = id_informe
        self.nombre_informe = nombre_informe
        self.fecha_creacion_informe = fecha_creacion_informe
        self.ubicacion_informe = ubicacion_informe
        