Veces=int()
Numero1=int()
Numero2=int()
Resultado=int()

Veces=0
Numero1=1
Numero2=0
Resultado=0

Veces=int(input("Ingrese el numero de veces de la sucesion de Fibonacci a mostrar: "))

Resultado=Numero1 

for x in range(Veces):
    print(Resultado)
    Resultado=Numero1 + Numero2
    Numero2=Numero1
    Numero1=Resultado