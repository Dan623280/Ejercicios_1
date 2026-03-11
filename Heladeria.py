pedidos = []
print("Menu")
print("1. Vainilla")
print("2. Chocolate")
print("3. Fresa")
contador = 0 

while contador < 5:
    try:
        pedido = int(input("coloque el numero del pedido: "))
        if pedido == 1:
            pedidos.append("Vainilla")
            print("sabor registrado correctamente")
            contador = contador +1
        elif pedido == 2:
            pedidos.append("Chocolate")
            print("sabor registrado correctamente")
            contador = contador +1
        elif pedido == 3:
            pedidos.append("Fresa")
            print("sabor registrado correctamente")
            contador = contador +1
        else:
            print("ese sabor no existe")
            continue
    except:
        print("coloque un Valor valido")

print("")
print("Estos son los pedidos")
print("")
for pedido in pedidos:
    print(pedido)

print("")