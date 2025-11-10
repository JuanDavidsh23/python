import time
print("Invetario completo")

inventory = {}
while True:
    print(" 1.Agregar productos\n 2.Mostrar inventario\n 3.Calcular estadisticas\n 4.salir")
    while True: 
        try:            
            options = int(input("ingrese una opcion del menu: "))
            if options <1 or options >4:
                print("ERROR, la opcion debe ser entre 1 y 4\n")
                continue
        except ValueError:
            print("ERROR, la opcion debe ser un valor numerico\n")
            continue

        if options == 1:
            print("Agregue sus productos")
            name = input("Ingrese el nombre del producto: ")
            while True:
                try: 
                    price = float(input("Ingrese el precio del producto: "))
                    quantity = int(input("Ingrese la cantidad que desea comprar: "))
                    break
                except ValueError: 
                    print("La Cantidad o el precio deben ser datos numericos")
            
            if name in inventory:
                inventory['quantity']  += quantity 

            else:
                inventory[name] = {'price' : price , 'quantity' : quantity}

        if options == 2:
            print("    Cargando productos..", end="", flush=True)
            for i in range(1,101):
                print(f"\r{i}%" , end = " " , flush=True)
                time.sleep(0.08)
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