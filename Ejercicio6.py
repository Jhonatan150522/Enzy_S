#Una compañía de seguros abrió una nueva agencia y estableció un programa para captar clientes, que consiste en lo siguiente: si el monto por el que se contrata el seguro es menor que $5.000. 000 pagará el 3%, si el monto es mayor o igual a $5.000 000 y menor de 20.000.000 pagará el 2% y si el monto es mayor o igual a 20.000.000 el valor a pagar será el 1.5 % ¿Cuál será el valor de la póliza?
#Se le pide el Monto del cliente 

monto=float(input("Digite el monto por el que contrata el seguro: "))

#Se toma la condicional if 

if monto < 5000000:
    porcentaje= 0.03
elif monto < 20000000:
    porcentaje= 0.02
else:
    porcentaje= 0.015
#SE realiza el calculo de la poliza

ValorPol = monto * porcentaje

#Se muestra el resultado
print(f"El valor de la p[oliza es: {ValorPol}")









