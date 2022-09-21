import os;
os.system("cls")


#Secuencia de impares. Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente.

#Declaracion de Variables
Num1 = int()
Num2 = int()


#Inicializacion de Variables
Num1 = 0
Num2 = 0

#Proceso
Num1=int(input("Ingrese un numero: "))
Num2=int(input("Ingrese otro numero: "))

print("Ascendente")
for n in range(Num1, Num2 + 1):
    if n % 2 != 0:
        print(n)

print("Descendente")
for n in range(Num2, Num1, -1):
    if n % 2 != 0:
        print(n)


#Casos de prueba
"""
Entrada:

Ingrese un numero: 20
Ingrese otro numero: 30

________________________________

Salida:

Ascendente
21
23
25
27
29

Descendente
29
27
25
23
21

________________________________

Prueba de Escritorio

Num1 = 20
Num2 = 30
n = 21 / 23 / 25 / 27 / 29

"""