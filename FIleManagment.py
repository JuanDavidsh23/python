frutas = []
for i in range(1,6):
    Fruits = input("Ingrese una fruta: ")
    frutas.append(Fruits)

with open("UserHistory.py/frutasa/frutas.txt","w") as file:
    for i in frutas:
        file.write(f"La fruta es: {i}\n")


with open ("UserHistory.py/frutasa/frutas.txt","r") as file:
    countFruits = 0
    for i in frutas:
        countFruits += 1
    print(f"Tienes {countFruits} lineas ")

with open ("UserHistory.py/frutasa/frutas.txt","r") as file:
    frase = input("Ingrese una frase: ").strip()
    for i in file: 
        if frase in i:
            print(i)


