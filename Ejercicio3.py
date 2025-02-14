#En la universidad Buena nota 

#Se haria unos inputs para que el estudinate ingrese las notas 
NP1=float(input("DIgite la primera nota del parcial: "))
NP2=float(input("Digite la segunda nota del parcial: "))
NF=	float(input("Digite la nota fianl: "))
#Se saca el promedio de las notas para mirar si el estudiante aprueda o no
promePar=NP1+NP2/2
#Se Pone la condicional if 
if promePar < 2.0:
    print("No presentar el examen final y pierdes la materia ")
    notaDe=promePar
else:
    print("Puedes presentar el examen final")

if NF < 2.0:
    print("Su nota definitiva sera la del examen final ")
    notaDe=NF
#Se realiza la operacion para saber la nota deifinita
else:
    notaDe= (NP1*0.3)  + (NP2*0.3) + (NF*0.4)
print(f"Nota definitiva: {notaDe:.2f}")

#Se mostraria la nota definitiva si pasa por promedio de parciales o por el examen final 
if notaDe >= 3.0:
    print("Aprobaste la asignatura")
elif NF >= 2.0:
    print("Reprodaste, pero puedes presentar habilitacion")
else:
    print("Reprodaste la asiginatura ")
