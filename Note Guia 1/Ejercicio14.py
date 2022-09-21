Nombre = str()
Apellido = str()
Dominio = str()
Mail = str()

Nombre = ""
Apellido = ""
Dominio = ""
Mail = ""

Nombre=str(input("Ingrese su nombre: ")).lower()
Apellido=str(input("Ingrese su apellido: ")).lower()
Dominio=str(input("Ingrese el dominio de su mail: ")).lower()

if (Nombre[0]==Apellido[0]):
    Mail=Nombre + "." + Apellido + "@" + Dominio
else:
    Mail=Nombre[0] + Apellido + "@" + Dominio

print("Este es el mail sugerido:", Mail)