estudiante=input("digite el nombre del estudiante: ")
#variable del nombre del estudiante
actividad_en_clase=float(input("digite la nota de la catividad en clase: "))
#variables de notas de las actividades en clase 
proyecto_final=float(input("digite la nota final: "))
#variable de notas del proyecto final
evualuacione_parciales=float(input("digite las notas de las parciales: "))
#variable de notas de parciales 
#variable del promedio de notas
promedio_actividades=actividad_en_clase*0.3
promedio_proyecto_final=proyecto_final*0.5
promedio_parciales=evualuacione_parciales*0.2

nota_final=promedio_actividades+promedio_proyecto_final+promedio_parciales
#variable de notas del promedio 
print("la nota fianl", nota_final)
#impresion de la nota final