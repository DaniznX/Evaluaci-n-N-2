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
        self.contrasena_empleados = self.hashear_contrasena(contrasena_empleados) if contrasena_empleados else None


    def validar_rut_empleados(self):
        return self.rut.validar_rut()

    def validar_contrasena(self):   #Retorna True si la contraseña cumple con los requisitos, False si no
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        return bool(re.match(regex, self.contrasena_empleados))

    def hash_verificar_contrasena(self, contrasena):    #Hashea la contraseña con SHA-256 y bcrypt
        sha256_hash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
        sha256_bytes = sha256_hash.encode('utf-8')
        bcrypt_hashed = bcrypt.hashpw(sha256_bytes, bcrypt.gensalt())
        return bcrypt_hashed

    def verificar_contrasena(self, contrasena, hashed): #Verifica si la contraseña proporcionada coincide con la hasheada
        sha256_hash = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
        sha256_bytes = sha256_hash.encode('utf-8')
        return bcrypt.checkpw(sha256_bytes, hashed)

    def hashear_contrasena(self, contrasena):   #Genera el hash de la contraseña al crear el objeto
        hashed_contrasena = self.hash_verificar_contrasena(contrasena)
        print(f"Contraseña hasheada con SHA-256 y bcrypt: {hashed_contrasena}")
        return hashed_contrasena

    def validar_correo(self):  #Valida si el correo tiene el formato adecuado
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return bool(re.fullmatch(regex, self.correo_empleados))


