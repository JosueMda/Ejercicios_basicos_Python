""" “Bodega Campo” es un restaurante de campo dedicado a ofrecer grandes
parrilladas, previa reserva del evento; sus tarifas son las siguientes: el costo
de plato por persona es de $95.00, pero si el número de personas es mayor
a 200 pero menor o igual a 300, el costo es de $85.00. Para más de 300
personas el costo por platillo es de $75.00. Se requiere un algoritmo que
ayude a determinar el presupuesto que se debe presentar a los clientes que
deseen realizar un evento.
Ejemplo: ingresa 250 personas , deberá mostrar 21.250,00 pesos """

cantidad_personas= int(input("Por favor ingrese la cantidad de invitados: "))
if cantidad_personas > 200 and cantidad_personas <= 300:
    precio=cantidad_personas*85.00
    print(f"El precio que usted debera abonar será de ${precio}")
elif cantidad_personas > 300:
    precio=cantidad_personas*75.00
    print(f"El precio que usted debera abonar será de ${precio}")
else:
    precio=cantidad_personas*95.00
    print(f"El precio que usted debera abonar será de ${precio}")