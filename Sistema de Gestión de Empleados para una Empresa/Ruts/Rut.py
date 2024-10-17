import re

class rut_chile():
    def __init__(self, id_rut_nacional, rut_nacional):
        self.id_rut_identificador = id_rut_nacional
        self.rut_nacional = rut_nacional
       
class rut_internacional():        
    def __init__(self, id_rut_internacional, rut_internacional):
        self.id_rut_internacional = id_rut_internacional    
        self.rut_internacional = rut_internacional


# Ejemplo de uso
def validar_rut_nacional(self):
    regex = r"^\d{7,8}-[0-9Kk]{1}$"
    if (re.fullmatch(regex, self.rut_nacional)):
       return True
    else:
        return False
    
def validar_rut_internacional(self):
    regex =  r"^[a-zA-Z0-9-]{6,12}$"
    if (re.fullmatch(regex, self.rut_internacional)):
       return True
    else:
        return False