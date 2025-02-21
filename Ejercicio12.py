#Diseñar un algoritmo para validar una fecha en el formato dd/mm/aaaa. Se considera que una
#fecha es válida si está entre 01/01/1900 y 31/12/2100, el mes entre 1 y 12 y el día entre 1 y 31,
#teniendo en cuenta que algunos meses tienen 28 (o 29), 30 o 31 días. Si la fecha no es válida se
#muestra un mensaje de error y se vuelve a leer los datos. El algoritmo termina cuando la fecha
#ingresada es válida.
from datetime import datetime

def fecha_valida(fecha):
    try:
#Intentamos convertir la fecha ingresada en un objeto datetime
        dia, mes, año = map(int, fecha.split('/'))
        
        # Validar rango de año
        if not (1900 <= año <= 2100):
            return False
        
# Intentar crear la fecha con datetime (verifica automáticamente días válidos por mes)
        datetime(año, mes, dia)
        return True
    except ValueError:
        return False  # Si ocurre un error en la conversión, la fecha no es válida

# Bucle hasta que la fecha sea válida
while True:
    fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
    
    if fecha_valida(fecha):
        print(f"La fecha {fecha} es válida. ")
        break  # Termina el programa si la fecha es correcta
    else:
        print(" Fecha inválida. Intente nuevamente.")  # Pide otra fecha si es incorrecta


















