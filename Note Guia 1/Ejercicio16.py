Turno=int()
Horas=int()
Sueldo=float()
SueldoTotal=float()

Turno=0
Horas=0
Sueldo=0.0
SueldoTotal=0.0

Turno=int(input("""En que turno trabaja el empleado? 
1- Diurno 
2- Nocturno
"""))
Horas=int(input("Cuantas horas a trabajado? "))

if Turno == 1:
    print("El sueldo de aquellos que trabajan en el turno diurno es de $35.50 por hora.")
    Sueldo = 35.50
    SueldoTotal = Sueldo * Horas
    print("El sueldo total del empleado es de: $", SueldoTotal)
elif Turno == 2:
    print("El sueldo de aquellos que trabajan en el turno nocturno es de $40.60 por hora.")
    Sueldo = 40.60
    SueldoTotal = Sueldo * Horas
    print("El sueldo total del empleado es de: $", SueldoTotal)