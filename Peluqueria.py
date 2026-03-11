while True:
    try: 
        Hora = int(input("colocar Hora: "))
        if Hora >= 0 and Hora <= 23:
            if Hora >= 6 and Hora <= 11:
                print("Mañana")
            elif Hora >= 12 and Hora <= 17:
                print("Tarde")
            elif Hora >= 18 and Hora <= 22:
                print("Noche")
            else:
                print("Fuera de horario")
        else:
            print("Coloque un numero entre 0 y 23")
    except:
        print("valor no valido")