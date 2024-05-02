import random
descuentoBoleta={"verde":0.20, "rojo": 0.15, }
#defenir la bilbleteca de colores de la boleta
valorCompra=float(input("digite el valor de la compra: "))
#seleccioanr el valor de la compra 

ColorBoleta=random.choice (["rojo", "verde",])
#seleccioanr aletoriamente los colores
if ColorBoleta in descuentoBoleta:
    descuentoBoleta= descuentoBoleta [ColorBoleta]
    valorPagar=valorCompra*(1-descuentoBoleta)
    #calculo segun  el color de las  boletas
    print(f"el valor de la compra {valorCompra: .2f}")
    print(f"color de la boleta {ColorBoleta}")
    print(f"descuneto de la boleta {descuentoBoleta*100}%")
    print(f"cuanto debe pagar {valorPagar: .2f}")
else:
    print("No se obtuvo descuento por que no existe el color ")
    #impresion de los resultados