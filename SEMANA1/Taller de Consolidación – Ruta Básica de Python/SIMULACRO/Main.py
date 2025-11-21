from functions import createProduct, Show, UpdateProduct
print("Bienvenido al sistema de inventario.")

while True:
    print("MENU \n 1.GESTION DE INVENTARIO \n 2.REGISTRO Y CONSULTA DE VENTAS \n 3.MODULO DE REPORTES. \n")
    while True: 
        try:
            opt = int(input("Ingrese la opcion que deseas: "))

            if opt < 0 or opt > 3:
                print("Ingrese una opcion del 1 al 3")
            break
        except ValueError:
            print("Ingrese una opcion numerica ")
  
    if opt == 1: 

        while True:
            print("Gestión del inventario")
            print(" 1. Registrar \n 2.Consultar \n 3.Actualizar \n 4.ELiminar")
            opt2 = int(input("Ingrese una opcion del menu: "))

            if opt2 == 1:

                id = int(input("Ingrese el id: "))
                name = input("Ingrese el nombre del producto: ")
                brand = input("Ingrese la marca del producto: ")
                category = input("Ingrese la categoria: ")
                price = float(input("Ingrese el precio del producto: "))
                quantity = int(input("Ingrese  la cantidad: "))
                guarantee = int(input("Ingrese los meses de garantia: "))
                createProduct(id,name,brand,category,price,quantity,guarantee)
        
            if opt2 == 2:
                    Show()
                
            if opt2 == 3:
                    id = int(input("Ingrese el id: "))
                    name = input("Ingrese el nombre del producto: ")
                    brand = input("Ingrese la marca del producto: ")
                    category = input("Ingrese la categoria: ")
                    price = float(input("Ingrese el precio del producto: "))
                    quantity = int(input("Ingrese  la cantidad: "))
                    guarantee = int(input("Ingrese los meses de garantia: "))
                    UpdateProduct(id, name,brand,category,price,quantity,guarantee)





    



