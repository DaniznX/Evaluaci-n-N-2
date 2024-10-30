import empleados
class accesos():
    def __init__(self, id_accesos, id_empleados):
        empleados.__init__(id_empleados)
        self.id_accesos = id_accesos
        