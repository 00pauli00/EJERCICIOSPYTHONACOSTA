edad=int(input("cual es su edad"))
nivelhemoglobina=float(input("ingrese su nivel de hemoglobina (en g%)"))
sexo=input("ingrese tu sexo (masculino o femenino)" ).lower()
tieneanemia=False
#las variables que solicita al usuario que ingrese los datos de la edad, nuvel hemoglobina, sexo, anemia.
if edad <=0:
    print("edad no valida")
elif edad <=1:
    if nivelhemoglobina <13 or nivelhemoglobina >26:
        tieneanemia=True
elif edad <=6: 
    if nivelhemoglobina <10 or nivelhemoglobina >18:
        tieneanemia=True
elif edad <=12:
    if nivelhemoglobina >12 or nivelhemoglobina <15: 
        tieneanemia=True
elif edad<=60:
    if sexo== "masculino":
        if nivelhemoglobina<14 or nivelhemoglobina >18:
            tieneanemia:True
elif sexo== "femenino":
    if nivelhemoglobina<12 or nivelhemoglobina>16:
            tieneanemia:True
#determinar si la persona tiene anemia segun los criterios prorcionados
else:
    print("edad no valida ")
if tieneanemia is True:
    print("la persona tiene anemia")
    
elif tieneanemia is False:
    print("la persona no tiene anemia ")
#imprimir el resultado