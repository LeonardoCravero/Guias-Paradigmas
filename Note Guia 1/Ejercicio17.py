Año=int()
Antiguos=int()
Recientes=int()

Año=0
Antiguos=0
Recientes=0

print("Ingrese el año de pintado de los siguientes cuadros.")

for x in range(3):
    Año=int(input(f"Cuadro {x+1}, año de Pintado: "))

    if Año < 1900:
        Antiguos += 1
    elif ((2022 - Año) < 10):
        Recientes += 1

if Antiguos == 3:
    print("Todos los cuadros son anteriores al siglo XX.")
elif Recientes == 3:
    print("Alguno/s de los cuadros no llevan mas de 10 años de antiguedad.")
else:
    print("Debes renovar tu stock.")

