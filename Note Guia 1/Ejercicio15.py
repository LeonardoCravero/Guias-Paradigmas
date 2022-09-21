Numero1=int()
Numero2=int()
Numero3=int()
Suma=int()
Division=float()
Potencia=float()

Numero1=0
Numero2=0
Numero3=0
Suma=0
Division=0.0
Potencia=0.0

Numero1=int(input("Ingrese el primer numero: "))
Numero2=int(input("Ingrese el segundo numero: "))
Numero3=int(input("Ingrese el tercer numero: "))

Suma=Numero1+Numero2+Numero3

if Suma > 10:
    print("El resultado de la suma es mayor a 10.")
    Division=Suma/2
    print("El resultado de la division es: ", Division)
else:
    print("El resultado de la suma es menor a 10.")
    Potencia=Suma**2
    print("El resultado de la potencia es: ", Potencia)