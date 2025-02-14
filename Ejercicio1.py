#Un profesor diseña un cuesntonariocon n prefuntas, estima que para calificar cada pregunta requiere m minutos.
#calificar cada pregunta requiere m minutos. Si el cuestionario se aplica a x estudiantes, cuánto tiempo horas y
#minutos necesita para calificar todos los exámenes. Se debe validar que los datos a ingresados
#deben ser positivos y si ingresa valores negativos debe mostrar un mensaje al usuario y
#culminar el algoritmo.

#Se realiza el input para que el profesor ingrese los valores 
n=input(float("Ingrese la Cantidad de preguntas: "))
m=input(int("Ingrese la Cantidad de minutos: "))
x=input(int("Ingrese la cantidad de Estuiantes: "))
# Se realiza la condicional if
if n >= 0 or m >= 0 or x >= 0:
    t=n*m*x
    horas=t//60
    minu=t%60
    print(f,"El tiempo es de: horas:{horas} minutos {minu}")
else:
    print("Error, solo numeros positivos")