from random import randint

Bingo=list()
Numero=int()
Adivinados=int()

Bingo = []
Numero = 0
Adivinados = 0

print("Adivina los numeros del bingo.")

for i in range(15):
    Bingo.append(randint(1, 100))

i = 0
for i in range(3):
    Numero = int(input("Ingresa un numero: "))

    if (Numero in Bingo):
        Adivinados += 1

print("Bingo: ", Bingo)
if Adivinados > 0:
    print("Felicidades, has adivinado", Adivinados, " numeros.")
else:
    print("Mala suerte, intenta otro dia.")