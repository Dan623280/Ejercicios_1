try: 
    edad = int(input("colocar edad: "))
    if edad < 12:
        print("Pague 8.000")
    elif edad >= 12 and edad <= 59:
        print("Pague 12.000")
    elif edad >= 60:
        print("Pague: 9000")
    else:
        print("error")
except:
    print("valor no valido")