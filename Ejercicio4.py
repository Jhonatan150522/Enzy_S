#El banco Buena Paga ofrece diferentes tasas de interés anual para depósitos a término dependiendo del tiempo por el que se hagan. Si el depósito es por un periodo menor o igual a seis meses la tasa es del 8% anual; entre siete y 12 meses, 10%; entre 13 y 18, 12%; entre 19 y 24, 15%; y para periodos superiores a 24 meses el 18%. Se requiere un algoritmo para determinar cuánto recibirá un cliente por un depósito, tanto por concepto de interés como entotal.

#Se le pide al cliente cuanto es su deposito 
Monto=float(input("Cuanto es el monto de deposito"))
TMeses=int(input("Cuanto es el tiempo en meses: "))
#Se determina la tasa de intereses anual segun el tiempo del deposito
#Tambien se coloca la condicional if 
if TMeses <=6:
    tasaAnual=0.8 
elif TMeses <= 12:
    tasaAnual=0.10
elif TMeses <= 18:
    tasaAnual=0.12
elif TMeses <= 24:
    tasaAnual=0.15
else:
    tasaAnual=0.18
#Se calcula el timpo de interes 
interes= Monto * tasaAnual * (TMeses/12)
#Calcular el total
total = Monto + interes
#Se muestran los resultados
print(f"EL total del deposito:")
print(f"Monto inicial: {Monto}")
print(f"Tasa de intereses anual: {tasaAnual} ")
print(f"intereses ganado: {interes}")
print(f"Total recibido: {total}")