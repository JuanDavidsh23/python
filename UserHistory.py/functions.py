from colorama import init, Fore, Back, Style
init(autoreset=True)
import time
import random
colores = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
color_aleatorio = random.choice(colores)
inventory = {}
productsCount  = 0
priceCount = 0
def ShowMenu ():
    print(" 1.Agregar productos\n 2.Mostrar inventario\n 3.Calcular estadisticas\n 4.salir")

def validateOption():
        while True:
            try:            
                options = int(input("ingrese una opcion del menu: "))
                if options <1 or options >4:
                    print("ERROR, la opcion debe ser entre 1 y 4\n")
                    continue
                return options
            except ValueError:
                print("ERROR, la opcion debe ser un valor numerico\n")
                continue

def addProducts():
    global priceCount, productsCount
    while True:          
        print("Agregue sus productos")
        name = input("Ingrese el nombre del producto: ")
        if name.replace("" , "").isalpha():
              break
        else: 
              print("El nombre no puede tener numeros.\n")
    while True:
            try: 
                price = float(input("Ingrese el precio del producto: "))
                priceCount += price
                quantity = int(input("Ingrese la cantidad que desea comprar: "))
                productsCount += quantity
                break
            except ValueError: 
                print("La Cantidad o el precio deben ser datos numericos")
            
    if name in inventory:
                    inventory[name]['quantity'] += quantity  

    else:
                    inventory[name] = {'price': price, 'quantity': quantity}
    


def showProducts():
            print(color_aleatorio +"       Cargando productos..", end="")
            for i in range(1,101):
                print(color_aleatorio + f"\r{i}%" , end = " " )
                time.sleep(0.02)
            print()

            while True:
                try: 
                    if not inventory:
                        raise ValueError("Inventario vacio")

                    for name, details in inventory.items():
                        totalCost = details['price'] * details['quantity']
                        print(f"producto: {name}: precio: {details['price']} x cantidad: {details['quantity']} = {totalCost}")
                    break
                except ValueError as e: 
                    print(f"No hay productos para mostrar {e}")
                    break
def stadistics():
           total = 0
           while True:
            try:
                if not inventory:
                      raise ValueError ("Nada en el inventario")
                

                for name,details in inventory.items():
                        totalCost = details['price'] * details['quantity']
                        print(f"producto: {name}: precio: {details['price']} x cantidad: {details['quantity']} = {totalCost}")
                        total += totalCost
                print(f"Agregaste {productsCount} productos  con un precio de: {total} ")
                break

            except ValueError:
                print("No hay nada en el inventario\n")
                break
