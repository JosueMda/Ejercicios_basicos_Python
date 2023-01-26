"""Realice un algoritmo para determinar cuánto se debe pagar por equis
cantidad de lápices considerando que si son 1000 o más el costo es de 85
centavos; de lo contrario, el precio es de 90 centavos.
Ejemplo: ingresa 500 , deberá mostrar 450 pesos"""

cantidad_lapices = int(input("Por favor, ingrese la cantidad de lapices que desea comprar: "))
if cantidad_lapices >= 1000:
    precio = int(cantidad_lapices*0.85)
    print(f"Usted debera abonar un total de ${precio}")
else:
    precio = int(cantidad_lapices*0.90)
    print(f"Usted debera abonar un total de ${precio}")
    


