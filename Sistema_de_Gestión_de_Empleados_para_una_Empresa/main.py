import mysql.connector
from Clases.tipo_empleado import tipo_empleado
from Clases.empleados import Empleados  
from Clases.depto import Depto
from Clases.proyectos import Proyecto

import sys
import os




def conectar_bd():  #conexión con la base de datos
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ddl"
    )


def agregar_empleado():     #Funciones para realizar operaciones en la base de datos
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
    
    
    query = """
        INSERT INTO empleados (NOMBRE, DIRECCION, TELEFONO, CORREO, FECHA_INICIO, SALARIO, ID_TIPO, RUT, CONTRASENA) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipo, rut, contrasena)
    cursor.execute(query, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Empleado agregado con éxito.")

def agregar_departamento():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del departamento: ")
    telefono = int(input("Ingrese el teléfono del departamento: "))
    id_empleado = int(input("Ingrese el ID del empleado a cargo: "))

    nuevo_departamento = Depto(None, nombre, telefono, id_empleado)

    query = """
        INSERT INTO departamento (NOMBRE, TELEFONO, ID_EMPLEADO) 
        VALUES (%s, %s, %s)
    """
    valores = (nombre, telefono, id_empleado)
    cursor.execute(query, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Departamento agregado con éxito.")

def main():
    while True:
        print("\nMenu de opciones")
        print("1. Agregar empleado")
        print("2. Agregar departamento")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_empleado()
        elif opcion == '2':
            agregar_departamento()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
