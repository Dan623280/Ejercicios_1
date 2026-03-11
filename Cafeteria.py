
cafe = 4000
te = 3500
jugo = 5000
while True:
    print("Menu")
    print("1. cafe = 4000")
    print("2. te = 3500")
    print("3. jugo = 5000")
    print("")
    
    try:
        bebida = int(input("Elija el numero de bebida que de see comprar: "))
        unidades = int(input("Unidades que desea comprar: "))
    
        if bebida == 1:
            resultado = cafe * unidades
            print(f"este es el total a pagar {resultado}")
        elif bebida == 2:
            resultado = te * unidades
            print(f"este es el total a pagar {resultado}")
        elif bebida == 3:
            resultado = jugo * unidades
            print(f"este es el total a pagar {resultado}")
        else:
            print(f"Valor no valido")
    except:
        print(f"Coloque un numero entero")