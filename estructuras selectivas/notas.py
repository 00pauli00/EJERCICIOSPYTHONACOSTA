primeraNota=float(input("ingres ela priemra nota"))
segundaNota=float(input("ingrese la segunda nota"))
terceraNota=float(input("ingrese la tercera nota"))
#perdir las notas
promedionotas= (primeraNota + segundaNota+ terceraNota)/3
#variable de calcular el promedio las notas
print("el promedio de las notas: ",promedionotas)
#impresion de variables
if primeraNota >= 70:
    print("el aprendiz ha aprobado la materia")
else:
    print("el aprendiz no ha aprobado")
#la varible de la calficacion para imprimir si aprobo o no