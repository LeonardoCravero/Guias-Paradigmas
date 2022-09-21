Nombre=str()
Caracteres=int()

Nombre=str(input("Por favor, escriba su nombre: "))

Caracteres=int(len(Nombre))

if Caracteres / 2 == 0:
    print("Las letras de tu nombre son pares.")
else:
    print("Las letras de tu nombre son impares.")