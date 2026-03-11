print("Animales")
print("1. Perro")
print("2. Gato")
print("3. Conejo")

while True:
    try:
        Numero = int(input("Colocar numero segun el animal que tenga: "))
    
        if Numero == 1:
            print("""
Alimento balanceado diseñado para cubrir 
las necesidades nutricionales de los perros, 
aportando proteínas, vitaminas y minerales 
para su crecimiento, energía y salud.
""")
        elif Numero == 2:
            print("""
Alimento especializado para gatos que 
contiene proteínas de origen animal, 
taurina y nutrientes esenciales para 
mantener su sistema inmunológico, piel y 
pelaje saludables.""")
            
        elif Numero == 3:
            print("""
Alimento rico en fibra elaborado 
principalmente con heno, vegetales y 
pellets, que ayuda a mantener una buena 
digestión y el desgaste natural de los 
dientes del conejo.
""")
           
        else:
            print(f"Valor no valido")
    except:
        print(f"Coloque un numero entero")