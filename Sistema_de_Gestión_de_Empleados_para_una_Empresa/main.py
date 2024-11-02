import mysql.connector
from Clases.tipo_empleado import tipo_empleado
from Clases.empleados import Empleados  
from Clases.depto import Depto
from Clases.proyectos import Proyecto
from colorama import Fore, Style, init
import os


init()

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ddl"
    )

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpiar_pantalla()
    print(Fore.CYAN + "="*30)
    print("   SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("="*30 + Style.RESET_ALL)
    print("1. Agregar empleado")
    print("2. Agregar departamento")
    print("3. Salir")
    print(Fore.CYAN + "="*30 + Style.RESET_ALL)

def agregar_empleado():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    telefono = int(input("Ingrese el teléfono del empleado: "))
    correo = input("Ingrese el correo del empleado: ")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    salario = int(input("Ingrese el salario del empleado: "))
    id_tipo = int(input("Ingrese el ID del tipo de empleado: "))
    rut = input("Ingrese el RUT del empleado: ")
    contrasena = input("Ingrese la contraseña del empleado: ")

    nuevo_empleado = Empleados(None, nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipo, rut, contrasena)

    try:
        query = """
            INSERT INTO empleados (NOMBRE, DIRECCION, TELEFONO, CORREO, FECHA_INICIO, SALARIO, ID_TIPO, RUT, CONTRASENA) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipo, rut, contrasena)
        cursor.execute(query, valores)
        conexion.commit()
        print(Fore.GREEN + "Empleado agregado con éxito." + Style.RESET_ALL)
    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al agregar empleado: {err}" + Style.RESET_ALL)
    finally:
        cursor.close()
        conexion.close()
        input(Fore.YELLOW + "Presione Enter para continuar..." + Style.RESET_ALL)


def agregar_departamento():
    limpiar_pantalla()
    print(Fore.GREEN + "AGREGAR NUEVO DEPARTAMENTO" + Style.RESET_ALL)
    conexion = conectar_bd()
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del departamento: ")
    telefono = int(input("Ingrese el teléfono del departamento: "))
    id_empleado = int(input("Ingrese el ID del empleado a cargo: "))

    nuevo_departamento = Depto(None, nombre, telefono, id_empleado)

    query = """
        INSERT INTO departamento (nombre, telefono, id_empleado) 
        VALUES (%s, %s, %s)
    """
    valores = (nombre, telefono, id_empleado)
    
    try:
        cursor.execute(query, valores)
        conexion.commit()
        print(Fore.GREEN + "Departamento agregado con éxito." + Style.RESET_ALL)
    except mysql.connector.Error as err:
        print(Fore.RED + f"Error al agregar departamento: {err}" + Style.RESET_ALL)
    finally:
        cursor.close()
        conexion.close()
    
    input(Fore.YELLOW + "Presione Enter para continuar..." + Style.RESET_ALL)

def main():
    while True:
        mostrar_menu()
        opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)

        if opcion == '1':
            agregar_empleado()
        elif opcion == '2':
            agregar_departamento()
        elif opcion == '3':
            print(Fore.MAGENTA + "Gracias por usar el sistema. ¡Hasta luego!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción inválida. Intente de nuevo." + Style.RESET_ALL)
            input(Fore.YELLOW + "Presione Enter para continuar..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
