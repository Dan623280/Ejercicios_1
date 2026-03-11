print("Colocar 6 productos deportivos")
lista = []
for i in range(6):
    producto = int(input(f"Colocar Precio producto numero {i}: "))
    if producto > 100000:
        lista.append(f"producto{i}: {producto}")

print("")
print("estos son los productos mayores a 100000")
print("")
for elemento in lista:
    print(elemento)
print("")