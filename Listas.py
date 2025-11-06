print("lista de frutas")
frutas = ["manzana", "banana", "naranja", "uva", "fresa"]
for fruta in frutas:
    print(fruta)

""" --------------------------------------- """

print("agregar y eliminar frutas a la lista")
frutas = ["manzana", "banana", "naranja"]
print("Lista original:", frutas)
frutas.append("uva")
print("Después de agregar uva:", frutas)
frutas.remove("banana")
print("Después de eliminar banana:", frutas)     

""" --------------------------------------- """

print("buscar fruta en la lista")
frutas = ["manzana", "banana", "naranja", "uva", "fresa"]
fruta_buscada = input("Ingrese el nombre de la fruta a buscar: ")
if fruta_buscada in frutas:      
    print(f"{fruta_buscada} está en la lista.")
else:
    print(f"{fruta_buscada} no está en la lista.") 
    
""" --------------------------------------- """

print("lista de numeros y promedio")
numeros = [10, 20, 30, 40, 50]
print("Lista de números:", numeros)
promedio = sum(numeros) / len(numeros)
print("Promedio:", promedio)

""" --------------------------------------- """

print("Guardar los numeros pares que ingrese un usuario en una lista hasta que ingrese un número impar")
numeros_pares = []
while True:
    numero = int(input("Ingrese un número (impar para terminar): "))
    if numero % 2 != 0:
        break
    numeros_pares.append(numero)    

print("eliminar duplicados de una lista")
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print("Lista original:", lista_con_duplicados)
print("Lista sin duplicados:", lista_sin_duplicados)