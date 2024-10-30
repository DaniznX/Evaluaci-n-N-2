from datetime import datetime

estado_usuario = {
    "id": 1, "estado": "Habilitado",
    "id": 2, "estado": "Deshabilitado"
}

dias_festivos = 13

festivos = {
    datetime(datetime.now().year, 1, 1),
    datetime(datetime.now().year, 4, 8),
    datetime(datetime.now().year, 5, 1),
    datetime(datetime.now().year, 5, 21),
    datetime(datetime.now().year, 6, 26),
    datetime(datetime.now().year, 7, 16),
    datetime(datetime.now().year, 8, 15),
    datetime(datetime.now().year, 9, 18),
    datetime(datetime.now().year, 9, 19),
    datetime(datetime.now().year, 10, 12),
    datetime(datetime.now().year, 10, 31),
    datetime(datetime.now().year, 11, 1),
    datetime(datetime.now().year, 12, 8),
    datetime(datetime.now().year, 12, 25),
}

estado_registro = {
    "id": 3, "estado": "enviado"}
{
    "id": 4, "estado": "no enviado"    
}

for tiempo_registrado in range (1, 24):
    print(f"{tiempo_registrado:02}:00")

tiempo = {
    datetime(datetime.now().hour, 1, 1),
    datetime(datetime.now().hour, 2, 4),
    datetime(datetime.now().hour, 3, 6),
    datetime(datetime.now().hour, 4, 8),
    datetime(datetime.now().hour, 5, 10),
    datetime(datetime.now().hour, 6, 12),
    datetime(datetime.now().hour, 7, 14),
    datetime(datetime.now().hour, 8, 16),
    datetime(datetime.now().hour, 9, 18),
    datetime(datetime.now().hour, 10, 20),
    datetime(datetime.now().hour, 11, 22),
    datetime(datetime.now().hour, 12, 24)
}