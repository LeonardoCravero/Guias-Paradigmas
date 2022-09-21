Pies=float()
Yardas=float()
Pulgadas=float()
Centimetros=float()
Metros=float()

Pies=int(input("Por favor, ingrese la medida en pies a convertir: "))

Yardas=Pies/3
Pulgadas=12*Pies
Centimetros=2.54*Pulgadas
Metros=Centimetros/100


print("La medida de pies convertida en Yardas es: ", Yardas)
print("La medida de pies convertida en Pulgadas es:", Pulgadas)
print("La medida de pies convertida en Centimetros es:", Centimetros)
print("La medida de pies convertida en Metros es:", Metros)