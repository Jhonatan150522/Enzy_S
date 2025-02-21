#Una joyería establece el valor de sus productos según el peso y el material. Se requiere un algoritmo que lea un valor de referencia x y a partir de éste calcule el valor del gramo de material utilizado y el valor del producto. El gramo de plata procesado tiene un costo de 3x, el platino 5x y el oro 8x.
#Pide un valor x
x = float(input("Digite un valor base (x): "))
#Se le pide el tipo de material (Plata, platino y oro)
material= int(input("Digite el tipo de material(Plata , platino y oro): ")).strip().lower()
#Se pide el peso 
gramo = float(input("Porfavor digite el peso en gramos: "))
#Se deermina el valor por gramo se coloca la condicional if 
if material == "Plata":
    PrecGram = 3 * x
elif material == "platino":
    PrecGram = 5 * x
elif material == "oro":
    PrecGram = 8 * x
else:
    print("Material no valido. intente de nuevo")
    exit()
#Se calcula el valor del producto
valorPro = PrecGram * gramo
#Se muestran los resultados
print(f"EL precio por gramo de {material} es: {PrecGram}")
print(f"El valor total del producto es: {valorPro}")





