import os;
os.system("cls")


#Carrera de ciclistas: Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera.

#Declaracion de Variables
from tkinter import _EntryValidateCommand


Ciclistas=int()
UltimoNombre=str()
UltimoTiempo=int()
record=int()
Ganador=str()
TiempoPromedio=float()
TiempoGanador=int()

#Inicializacion de Variables
Ciclistas=0
UltimoNombre=""
UltimoTiempo=0
record=0
Ganador=""
TiempoPromedio=0.0
TiempoGanador=0

#Proceso
print("Bienvenido a la carrera de ciclistas de Buenos Aires.")

Ciclistas=int(input("Por favor, ingrese la cantidad de competidores: "))
record=int(input("Por favor, recuerdame cual fue el mejor tiempo de la anterior carrera (minutos): "))

for i in range (Ciclistas):
    UltimoNombre=str(input("Ingrese el nombre del competidor: "))
    UltimoTiempo=int(input("Ingrese el tiempo del competidor (minutos): "))
    
    if i == 0 or UltimoTiempo < TiempoGanador:
        Ganador=UltimoNombre
        TiempoGanador=UltimoTiempo
    
    TiempoPromedio = TiempoPromedio + UltimoTiempo / Ciclistas

print("El ganador de la carrera es ", Ganador, " y su tiempo es de ", TiempoGanador, " minutos.")

if TiempoGanador < record:
    print("A roto el record anterior de ", record, " minutos.")
else:
    print("Gracias a todos por participar.")

print("El tiempo promedio de la carrera es de: ", TiempoPromedio)


#Casos de prueba
"""
Entrada:

Bienvenido a la carrera de ciclistas de Buenos Aires.

Por favor, ingrese la cantidad de competidores: 5
Por favor, recuerdame cual fue el mejor tiempo de la anterior carrera (minutos): 70

Ingrese el nombre del competidor: Marco
Ingrese el tiempo del competidor (minutos): 75

Ingrese el nombre del competidor: Carlos
Ingrese el tiempo del competidor (minutos): 80

Ingrese el nombre del competidor: Juan
Ingrese el tiempo del competidor (minutos): 60

Ingrese el nombre del competidor: Rodrigo
Ingrese el tiempo del competidor (minutos): 59

Ingrese el nombre del competidor: Karl
Ingrese el tiempo del competidor (minutos): 76

____________________________________________________

Salida:

El ganador de la carrera es  Rodrigo  y su tiempo es de  59  minutos.
A roto el record anterior.
El tiempo promedio de la carrera es de:  70.0

_____________________________________________________

Prueba de escritorio:

Ciclistas: 0 / 5
record: 0 / 70
Nombre: "" / "Marco" / "Carlos" / "Juan" / "Rodrigo" / "Karl"
UltimoTiempo: 0 / 75 / 80 / 60 / 59 / 76
Ganador: "" / "Marco" / "Juan" / "Rodrigo"
TiempoGanador: 0 / 75 / 60 / 59
TiempoPromedio: 0.0 / 70.0
"""