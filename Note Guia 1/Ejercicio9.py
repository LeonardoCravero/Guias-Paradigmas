Numero = int()
Multi = int()
Resultado = int()

Numero = 0
Multi = 1
Resultado = 0

Numero = int(input("Ingrese un numero entero: "))

while Multi < 11:
    Resultado = Numero * Multi
    print("Tabla del ", Numero, ": ", Numero, "x", Multi, "=", Resultado)
    Multi = Multi + 1