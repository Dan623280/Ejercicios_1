
try: 
    edad = int(input("colocar edad: "))
    if edad < 13:
        print("no puede ingresar")
    elif edad >= 13 and edad <= 17:
        print("Clase Juvenil")
    elif edad >= 18 and edad <= 59:
        print("clase general")
    elif edad >= 60:
        print(" clase senior")
    else:
        print("error")
except:
    print("valor no valido")

