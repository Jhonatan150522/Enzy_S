#Convertir un numero deciaml a binario 
# Pedir un número al usuario
num = int(input("Ingrese un número decimal: "))

# Convertir a binario con bin() y quitar el prefijo '0b'
binario = bin(num)[2:]

print(f"El número {num} en binario es: {binario}")
