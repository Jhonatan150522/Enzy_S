#Para implementar un reloj digital es necesario declarar tres variables, para controlar: horas,
#minutos y segundos. Cada una de estas variables controla un ciclo, así: los segundos se
#incrementan desde 0 a 59, los minutos también desde 0 a 59 y las horas desde 1 a 12 o de 1 a
#24. Este algoritmo está diseñado para terminar la ejecución al llegar a 12:59:

import time  # Para simular el tiempo real

# Inicializar variables
horas = 1
minutos = 0
segundos = 0

# Bucle del reloj (se ejecuta hasta que llegue a 12:59:59)
while True:
# Mostrar la hora en formato HH:MM:SS
    print(f"{horas:02}:{minutos:02}:{segundos:02}") 
# Esperar un segundo para simular el tiempo real
    time.sleep(1)
# Incrementar segundos
    segundos += 1
# Si los segundos llegan a 60, reiniciamos a 0 y sumamos 1 minuto
    if segundos == 60:
        segundos = 0
        minutos += 1

        # Si los minutos llegan a 60, reiniciamos a 0 y sumamos 1 hora
        if minutos == 60:
            minutos = 0
            horas += 1

            # Si las horas llegan a 13, reiniciamos a 1 (formato 12 horas)
            if horas == 13:
                horas = 1

    # Si llegamos a 12:59:59, terminamos el programa
    if horas == 12 and minutos == 59 and segundos == 59:
        print("12:59:59 - Fin del reloj")
        break  # Sale del bucle













