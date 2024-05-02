promediodelestudiante=float(input("ingrese su promedio:"))
#solicitar al usuario la informacion de su promeido
if promediodelestudiante>=9:
    descuento=0.30
    pension=1000
    totalpagar= pension*(1-descuento)
else:
    pension=1000
    Iva:0.35
    totalpagar= pension*(1+Iva)
# las variables del promedio que ajustan el valor de la pension 
    print(f"el valor a pagar al pension es {totalpagar:.2f}")
#la impresion en total de pagar la pension del estudiante