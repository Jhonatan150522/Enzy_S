#La distribuidora de motocicletas Rueda Floja ofrece una promoción que consiste en lo siguiente: las motos marca Honda tienen un descuento del 5%, las de marca Yamaha del 8%y las Suzuki el 10%, las de otras marcas el 2%. Se requiere calcular el valor a pagar por una motocicleta.
#Se solicita el valor o cuanto tiene para la moto
ValorBase=float(input("Ingresa el monto total de la moto: "))
Moto=input("ingresa la marca de la moto (Honda, Yamaha, Susuki u otra)").strip().lower()
#Se le aplica el descuento con la marca y se aplica  la condicional if 
if Moto == "Honda": 
    DescuentoPorce= 0.5
elif Moto == "Yamaha":
    DescuentoPorce= 0.8
elif Moto == "Susuki":
    DescuentoPorce= 0.10
else:
    DescuentoPorce= 0.2
#Se Calcula el descuento con el valor inicial
descuento = ValorBase*DescuentoPorce
#Ahora se hace el precio final con el descuento
PrecioFinal= ValorBase-descuento
#Se muestran los print al final
print("Toda la compra")
print(f"La marca de la moto: {Moto}")
print(f"Precio base o original: {ValorBase}")
print(f"Descuento aplicado:{descuento}")
print(f"Precio final a pagar: {PrecioFinal}")