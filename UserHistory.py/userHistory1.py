print("Inventario de productos. ")

inventory = {} 
while True: 
        #solicitar datos al user 
        name = input("ingresa el nombre del producto: ")
        #capturar error en el bucle 
        while True:
            try:
                price = float(input("ingresa el precio del producto: "))
                quantity = int(input("ingresa la cantidad del producto: "))
                break
            except ValueError:
                 print("Error, debes ingresar un dato numerico.")

        #agregar al diccionario
        if name in inventory:
            inventory[name] ['quantity']  +=quantity

        else: 
            inventory[name] = {'price': price, 'quantity' : quantity}
        
        #recorrer los items 
        total_cost = 0.0
        for name, details in inventory.items():
            totalItem = details['price'] * details['quantity']
            print(f"producto: {name}: precio: {details['price']} x cantidad: {details['quantity']} = {totalItem}")