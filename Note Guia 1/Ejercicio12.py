Sueldo=int()
Ahorro=float()
Resultado=float()

Sueldo=0
Ahorro=0.0
Resultado=0.0
x = 1

Sueldo=int(input("¿Cuanto cobras por mes?"))


while x < 13:
    Resultado = Sueldo / 10
    Ahorro = Ahorro + Resultado
    x = x + 1


print("Este año ahorraste un total de", Ahorro, "pesos")