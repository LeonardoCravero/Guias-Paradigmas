pesos=int()
dolar=float()
tasa=float()
Respuesta=str()

pesos = 0
dolar = 0.0
tasa = 140.58
Respuesta = ""

Respuesta=str(input("¿Deseas convertir pesos o dolares? "))

if Respuesta == "Pesos":
    pesos=int(input("Ingrese el valor de pesos a convertir: "))
    dolar = pesos / tasa
    print("Pesos:", pesos)
    print("Dolar:", dolar)
elif Respuesta == "Dolar":
    dolar=int(input("Ingrese el valor de dolares a convertir: "))
    pesos = dolar * tasa
    print("Dolar:", dolar)
    print("Pesos", pesos)