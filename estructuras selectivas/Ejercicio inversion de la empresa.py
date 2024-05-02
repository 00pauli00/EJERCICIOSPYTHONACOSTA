dinerototaldelacompra=float(input("ingre le total del dinero"))
if dinerototaldelacompra>500000:
    miplata=dinerototaldelacompra*0.55
    prestamodelbanco=dinerototaldelacompra*0.30
    creditofrabicante=dinerototaldelacompra-miplata-prestamodelbanco
else:
    miplata=dinerototaldelacompra*0.70
    prestamodelbanco=dinerototaldelacompra*0.30
    creditofrabicante=dinerototaldelacompra*0
interesdelcredito=creditofrabicante*20
print(f"el valor de mi plata: $ {miplata:.2f}")
print(f"el prestamo del banco: $ {prestamodelbanco:.2f}")
print(f"el valor del cedito fabricante {creditofrabicante:.2f}")
print(f"el valor del interes del fabricante: $ {interesdelcredito}")