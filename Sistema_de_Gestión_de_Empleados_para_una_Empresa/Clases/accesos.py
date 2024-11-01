from Clases import empleados
from datetime import datetime, timedelta
from Auxiliares import constantes
class accesos():
    def __init__(self, id_accesos, id_empleados, cantidad_solicitada):
        empleados.__init__(id_empleados)
        self.id_accesos = id_accesos
        self.cantidad_solicitada = cantidad_solicitada
        
    def restar_dias_festivos(fecha_festivo, dias_festivos):
        dias_restados : 0
        while dias_restados < dias_festivos:
            fecha_festivo -= timedelta(days=1)
            if fecha_festivo.weekday() < 13 and fecha_festivo not in constantes.festivos:
                dias_restados -= 1
        return fecha_festivo

    def calcular_fechas(self):
        if(self.nombre_empleados > 0):
            if(self.nombre_empleados > self.cantidad_solicitada):
                self.fecha_festivo = datetime.datetime.now()
                self.cantidad_solicitada = empleados.restar_dias_festivos(self.fecha_festivo, 13)