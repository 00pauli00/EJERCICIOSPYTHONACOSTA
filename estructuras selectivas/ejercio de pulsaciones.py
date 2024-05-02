sexo=input("ingrese su sexo (femenino o masculino): ").lower()
edad=int(input("ingrese su edad: "))
#solicitar que ingrese el sexo y la edad 

if sexo== "femenino":
    numeropulsaciones=(220-edad)/10
elif sexo=="masculino":
    numeropulsaciones=(210-edad)/10
else:
    print("digite unos de los dos generos solo existen esos dos no mas ")
    numeropulsaciones=None
#  calcular el numero de pulsaciones
if numeropulsaciones is not None:
    print(f"nuemro de pulsaciones por ejercio aeróbico cada 10 segundos : {numeropulsaciones: .2f}")
#imprsion del resultado