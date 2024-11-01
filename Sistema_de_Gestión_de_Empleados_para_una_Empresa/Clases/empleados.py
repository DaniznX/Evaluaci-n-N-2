from Clases.tipo_empleado import tipo_empleado
from Ruts.rut import rut_chile, rut_internacional
import re
import bcrypt
import hashlib

class Empleados:
    def __init__(self, id_empleados, nombre_empleados, direccion_empleados, telefono_empleados, correo_empleados, fecha_inicio, salario_empleados, id_tipo_empleado, rut_empleados, contrasena_empleados, es_nacional=True):
        self.tipo_empleado = tipo_empleado(id_tipo_empleado, None, None)
        if es_nacional:
            self.rut = rut_chile(None, rut_empleados)
        else:
            self.rut = rut_internacional(None, rut_empleados)
        
        self.id_empleados = id_empleados
        self.nombre_empleados = nombre_empleados
        self.direccion_empleados = direccion_empleados
        self.telefono_empleados = telefono_empleados
        self.correo_empleados = correo_empleados
        self.fecha_inicio = fecha_inicio
        self.salario_empleados = salario_empleados
        self.contraseña_empleados = contrasena_empleados

    def validar_rut_empleados(self):
        return self.rut.validar_rut()

    def validar_contrasena(self):
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(regex, self.contraseña_empleados):
            return "La contraseña es válida"
        else:
            return "La contraseña no es válida"

    def hash_verificar_contrasena(self, contrasena):
        sha256_hash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
        sha256_bytes = sha256_hash.encode('utf-8')
        bcrypt_hashed = bcrypt.hashpw(sha256_bytes, bcrypt.gensalt())
        return bcrypt_hashed

    def verificar_contrasena(self, contrasena, hashed):
        sha256_hash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
        sha256_bytes = sha256_hash.encode('utf-8')
        return bcrypt.checkpw(sha256_bytes, hashed)

    def hashear_contrasena(self):
        hashed_contrasena = self.hash_verificar_contrasena(self.contraseña_empleados)
        print(f"Contraseña hasheada con SHA-256 y bcrypt: {hashed_contrasena}")
        return hashed_contrasena

    def proceso_verificacion(self, contrasena):
        hashed_contrasena = self.hashear_contrasena()
        return self.verificar_contrasena(contrasena, hashed_contrasena)

    def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, self.correo_empleados):
            return True
        else:
            return False

