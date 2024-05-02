preciodezapatilla=float(input("el precio de las zapatillas"))
cantidaddezapatilla=float(input("la cantudad de zaitllas "))
totaldepago=preciodezapatilla*cantidaddezapatilla
if cantidaddezapatilla >=3:
    descuento= 0.2
else:
    descuento= 0.1
totaldescuento=totaldepago*(1-descuento)
print(f"el total de pagar las zapatillas {cantidaddezapatilla} zapitta es: $ {totaldescuento:.2f}")