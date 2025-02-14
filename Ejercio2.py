#Se requiere un algoritmo que decida si un empleado tiene derecho al auxilio de transporte. Se conoce que todos los empleados que devengan un salario menor o igual a dos salarios mínimos 
# legales tienen derecho a este rubro.

# Se pregunta Cuanto gana el empleado 
Salar=int(input("Que Saliario tiene: "))
Salamin=2847000
# Se coloca la condicional if
if Salar < Salamin:
    print("Aplicas para la ayuda de transporte ")
else:
    print("No aplicas para la ayuda de transporte ")




