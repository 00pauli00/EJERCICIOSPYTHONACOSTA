cantidadllantas=int(input("ingrese la cantidad de llantas : "))
#socilitar al usuario cuantas cantidades de llantas

if cantidadllantas <5:
    preciodellanta=300
elif cantidadllantas <=10:
    preciodellanta=250
else:
    preciodellanta= 200
#las variables del calculo de pagra segun la cantidad e la s llantas
preciototal=cantidadllantas*preciodellanta
#calcular total

print(f"el total de pagar por la catidad  {cantidadllantas} es $ {preciototal}")
#impresion del total