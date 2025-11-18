""" frase = input("Ingrese una frase: ")
vocales = 0
for i in frase: 
    if i in "a,e,i,o,u":
        vocales +=1
print(vocales)

 """


""" fruits = ["mango", "pera", "manzana"]

with open("UserHistory.py/fruits.txt", "w" ) as archivo:
    for i in fruits:
        archivo.write(f"la fruta {i}")

 """
while True:
    try:
        number = int(input("digite un numero: "))
        break
    except ValueError:
        print("ERROR, el dato debe ser un valor numerico")

with open(f"UserHistory.py/tablas/tabla_{number}.txt", "w" ) as archivo:
    for i in range(1,11):
        archivo.write(f"{number} x {i} = {number*i}\n")


