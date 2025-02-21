#Solicitar el dinero disponible
x = float (input("Ingrese el dimero disponible"))
#Se le solicita al estudiante los precios de los libros
V1 = float (input("Porfavor digite el precio del libro de Calculo: "))
V2 = float (input("Porfavor digite el precio del librro de Fisica: "))
V3 = float (input("Ingrese el valor del libro de Programacion: "))
#Se ordenan los libros para dar priorida al mas caro
#Se guardan en una lista 
precios = [V1 , V2, V3]
#Se ordena de mayor a menor 
precios.sort(reverse=True)
# Se realiza el algoritmo para mirar que libro puede comprar
if x >= sum(precios):
    print("Puedes comprar los tres libros.")
elif x >= (precios[0] + precios[1]):
    print(f"Puedes comprar dos libros: {precios[0]} y {precios[1]}")
elif x >= precios[0]:
    print(f"Solo puedes comprar un libro: {precios[0]}")
else:
    print("No puedes comprar ningún libro.")



















