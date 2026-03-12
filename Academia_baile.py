
veces = int(input("Coloque el numero de veces asistio el estudiante:"))

if veces < 5:
    print("Asistencia baja")
elif veces >= 5 and veces <= 8:
    print("Asistencia media")
elif veces >= 9:
    print("Asistencia alta")
else:
    print("valor no valido")