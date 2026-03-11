
while True:
    Horas = int(input("Colocar Horas: "))
    total = 0
    for i in range(Horas):
        if i == 0:
            total = 5000
        else:
            total = total + 3000
    
    print(f"Total a pagar es {total}")