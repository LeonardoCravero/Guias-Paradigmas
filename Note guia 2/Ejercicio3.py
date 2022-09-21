import os;
os.system("cls")


#Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego: 
# a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período. 
# b) Determinar en qué mes recibió el sueldo más bajo del período. 
# c) Informar el sueldo promedio del semestre.

#Declaracion de Variables
Sueldo = int()
Aguinaldo = int()
SueldoMayor = int()
SueldoMenor = int()
SueldoPromedio = int()
Mes = int()

#Inicializacion de Variables
Sueldo = 0
Aguinaldo = 0
SueldoMayor = 0
SueldoMenor = 0
SueldoPromedio = 0
Mes = 0
i = 1
n = 0

#Proceso
for i in range(6):
    Sueldo=int(input("Ingrese el Sueldo de este mes: "))
    n = n + 1

    if i == 1 or Sueldo > SueldoMayor:
        SueldoMayor = Sueldo
    
    if i == 1 or Sueldo < SueldoMenor:
        SueldoMenor = Sueldo
        Mes = n

    SueldoPromedio = SueldoPromedio + Sueldo

Aguinaldo = SueldoMayor / 2
SueldoPromedio = SueldoPromedio / 6

print("El Aginaldo de este semestre es de", Aguinaldo)
print("El menor sueldo fue de", SueldoMenor, "en el mes", Mes)
print("El sueldo promedio de este semestre es de", SueldoPromedio)

#Casos de Prueba
"""
Entrada:

Ingrese el Sueldo de este mes: 20000
Ingrese el Sueldo de este mes: 30000
Ingrese el Sueldo de este mes: 28000
Ingrese el Sueldo de este mes: 30500
Ingrese el Sueldo de este mes: 12000
Ingrese el Sueldo de este mes: 24000

______________________________________

Salida:

El Aguinaldo de este semestre es de 15250.
El menor sueldo fue de 12000 en el mes 5.
El sueldo promedio de este semestre es de  24083.333333333332

______________________________________

Prueba de Escritorio

Sueldo = 0 / 20000 / 30000 / 28000 / 30500 / 12000 / 24000
SueldoMayor = 0 / 20000 / 30000 / 30500
Sueldo Menor = 0 / 20000 / 12000
Mes = 0 / 1 / 5
Sueldo Promedio = 0 / 24083.333333333332
Aguinaldo = 0 / 15250.0
"""