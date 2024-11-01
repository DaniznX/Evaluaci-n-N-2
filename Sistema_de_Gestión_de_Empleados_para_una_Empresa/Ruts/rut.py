import re

class rut_chile:
    def __init__(self, id_rut_nacional, rut_nacional):
        self.id_rut_identificador = id_rut_nacional
        self.rut_nacional = rut_nacional

    def validar_rut(self):
        regex = r"^\d{7,8}-[0-9Kk]{1}$"
        return bool(re.fullmatch(regex, self.rut_nacional))

class rut_internacional:
    def __init__(self, id_rut_internacional, rut_internacional):
        self.id_rut_internacional = id_rut_internacional    
        self.rut_internacional = rut_internacional

    def validar_rut(self):
        regex = r"^[a-zA-Z0-9-]{6,12}$"
        return bool(re.fullmatch(regex, self.rut_internacional))
