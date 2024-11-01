from datetime import datetime
from Clases import proyectos
class Registro_Tiempo():
    def __init__(self, id_registro_tiempo, fecha_registro_tiempo, tareas_registro_tiempo, id_asignacion, id_proyecto, observacion_registro_tiempo):
        proyectos.__init__(id_proyecto)
        self.id_registro_tiempo = id_registro_tiempo
        self.fecha_registro_tiempo = fecha_registro_tiempo
        self.tareas_registro_tiempo = tareas_registro_tiempo
        self.id_asignacion = id_asignacion
        self.observacion_registro_tiempo = observacion_registro_tiempo

    def validar_hora(hora_str, formato="%H:%M"):
        try:
            hora_valida = datetime.strptime(hora_str, formato)
            if (hora_valida == "%H:%M"):
                return True
            else:
                False
        # La hora es válida
        except ValueError:
            return False  # La hora no es válida
        pass

    if (validar_hora == "%H:%M"):
        True
    else:
        False
