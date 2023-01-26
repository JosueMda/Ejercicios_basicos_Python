""" Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). """
edad = int(input("Por favor ingrese su edad: "))
print("Usted ha cumplido los siguientes años: ")
for n in range(1,edad+1):
    
    print(n)
