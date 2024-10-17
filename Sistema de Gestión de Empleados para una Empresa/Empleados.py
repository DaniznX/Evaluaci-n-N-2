import Tipo_Empleado
import re
import bcrypt
import hashlib
from Ruts import Rut

class Empleados():
    def __init__(self, id_empleados, nombre_empleados, direccion_empleados, telefono_empleados, correo_empleados, fecha_inicio, salario_empleados, id_tipo_empleado, rut_empleados, contraseña_empleados):
        Tipo_Empleado.__init__(id_tipo_empleado)
        Rut.__init__(rut_empleados)
        self.id_empleados = id_empleados
        self.nombre_empleados = nombre_empleados
        self.direccion_empleados =  direccion_empleados
        self.telefono_empleados = telefono_empleados
        self.correo_empleados = correo_empleados
        self.fecha_inicio = fecha_inicio
        self.salario_empleados = salario_empleados
        self.contraseña_empleados = contraseña_empleados
        
    def validar_rut_empleados(self):
        return Rut.is_valid_rut(self.rut_empleados)
        
    def validar_contrasena(self):
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(regex, self.validar_contrasena):
            return "La contrasena es válida"
        else:
            return "La contrasena no es válida"
    
    def hash_verificar_contrasena(contrasena):
        sha256_hash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
        sha256_bytes = sha256_hash.encode('utf-8')
        bcrypt_hashed = bcrypt.hashpw(sha256_bytes, bcrypt.gensalt())
        return bcrypt_hashed
    pass

    def verificar_contrasena(self, contrasena, hashed):
        sha256_hash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
        sha256_bytes = sha256_hash.encode('utf-8')
        return bcrypt.checkpw(sha256_bytes, hashed)
    pass

    def hashear_contrasena(self, contrasena):
        hashed_contrasena = self.hash_password(contrasena)
        print(f"contrasena hasheada con SHA-256 Y bcrypt:{hashed_contrasena}")
    pass

    def proceso_verificacion(self, contrasena):
        hashed_contrasena = self.hashear_contrasena(contrasena)
        hashed_almacenado = hashed_contrasena
        if self.verificar_contrasena(contrasena, hashed_almacenado):
            True
        else:
            False
    
    def validar_coorreo(self):
        regex =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(regex, self.correo_usuario)):
            return True
        else:
            return False