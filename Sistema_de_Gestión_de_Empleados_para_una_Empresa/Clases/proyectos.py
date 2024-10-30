from datetime import datetime
class Proyecto():
    def __init__(self, id_proyecto, nombre_proyecto, descripcion_proyecto, fecha_inicio_proyecto, fecha_fin_proyecto):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.descripcion_proyecto = descripcion_proyecto
        self.fecha_inicio_proyecto = fecha_inicio_proyecto
        self.fecha_fin_proyecto = fecha_fin_proyecto
    
    def validar_fecha(fecha_str, formato ="%Y-%m-%d"):
        try:
            fecha_valida = datetime.strptime(fecha_str, formato)
            if fecha_valida.year < 2000:
                return False
            else:
                True
        except ValueError:
            return False  

    def fecha_proyecto(self):
        if (self.fecha_inicio_proyecto ==  "%Y-%m-%d"):
           return True
        else:
            False
                   
        if (self.fecha_fin_proyecto == "%Y-%m-%d"):
            return True
        else:
            False

    if (validar_fecha == fecha_proyecto):
        True
    else: 
        False