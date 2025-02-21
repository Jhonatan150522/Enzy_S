#Dados dos números enteros, se requiere encontrar el máximo común divisor de los mismos. El
#máximo común divisor (MCD) entre dos números es el número más grande que los divide a
#ambos, incluso puede ser uno de ellos dado que todo número es divisor de sí mismo.

import math  # Importamos la librería math

# Pedir números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Usar la función math.gcd para encontrar el MCD
mcd = math.gcd(num1, num2)

print(f"El MCD de {num1} y {num2} es: {mcd}")

















