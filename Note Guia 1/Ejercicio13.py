Pies=int()
Pulgadas=int()
Centimetros=float()
Respuesta=str()

Pies = 0
Pulgadas = 0
Centimetros = 0.0
Respuesta = ""

Respuesta=str(input("Deseas convertir pies o pulgadas: "))

if Respuesta == "pies":
    Pies=int(input("Por favor ingrese la cantidad de pies a convertir:"))
    Centimetros = 30.48 * Pies
    print("La conversion de pies a Centimetros es de: ", Centimetros)
elif Respuesta == "pulgadas":
    Pulgadas=int(input("Por favor ingrese la cantidad de pulgadas a convertir:"))
    Centimetros = 2.54 * Pulgadas
    print("La conversion de pulgadas a Centimetros es de: ", Centimetros)