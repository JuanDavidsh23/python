from functions import validaString, validateDates ,registerSale, CreateProduct, read, updateProduct, deleteProduct, readSales, mostSales
import time 
print("-----------------------------------------------")
print("BIENVENIDO AL SISTEMA DE INVENTARIO Y VENTAS")
print("-----------------------------------------------")


while True: 
    print("-------------------------------------------------------------------------")
    print("Menu Principal")
    print(" 1.Gestion del inventario \n 2.Gestion de ventas \n 3.Reportes \n 4.Salir")
    print("-------------------------------------------------------------------------")
    try: 
        option = int(input("Ingrese una opcion del menu: "))
        if option <1 or option >4:
            print("Error, el valor de la opcion debe estar entre 1 y 4.")
    except ValueError:
        print("El dato deber ser numerico, no puedes ingresar texto.")

    if option == 1: 
        while True:
            print("Gestion de inventario")
            print(" 1.Registrar un producto \n 2.Consultar productos \n 3.Actualizar producto \n 4.Eliminar un producto \n 5.Volver al menu principal")
            try:
                option2 = int(input("Ingrese una opcion del menu: "))
                if option2 < 1 or option2 >5:
                    print("Error, el valor de la opcion debe estar entre 1 y 5.")
            except ValueError:
                print("El dato deber ser numerico, no puedes ingresar texto.")

            if option2 == 1:
                print("Registre su producto")
                title = validaString("Ingrese el titulo de su producto: ")
                author = validaString("Ingrese el nombre del autor: ")
                category = validaString("Ingrese la categoria:")
                price = validateDates("Ingrese el precio del producto: ", int)
                quantity = validateDates("Ingrese la cantidad stock: ", int)
                CreateProduct(title, author,category,price,quantity)
                print("Producto registrado correctamente. ")

            elif option2 == 2: 
                read()

            elif option2 == 3:
                print("Actualice su producto.")
                id = validateDates("Ingrese el id del libro: ")
                title = validaString("Ingrese el titulo de su producto: ")
                author = validaString("Ingrese el nombre del autor: ")
                category = validaString("Ingrese la categoria:")
                price = validateDates("Ingrese el precio del producto: ", int)
                quantity = validateDates("Ingrese la cantidad stock: ")
                updateProduct(id, title, author,category,price,quantity)
            

            elif option2 == 4:
                id = input("INgrese el id del producto: ")
                deleteProduct(id)

            elif option2 == 5:
                print("-----------------------------")
                print("Volviendo al menu anterior...")
                print("-----------------------------")

                break

    elif option == 2:
        while True:
            print("Gestion de ventas")
            print(" 1.Registrar una venta \n 2.Consultar productos \n 3.Volver al menu principal")
            try:
                option3 = int(input("Ingrese una opcion del menu: "))
                if option3 < 1 or option3 >3:
                    print("Error, el valor de la opcion debe estar entre 1 y 3.")
            except ValueError:
                print("El dato deber ser numerico, no puedes ingresar texto.")
        
            if option3 == 1:
                totalSales = 0
                read()             
                print("LOS CUPONES DE DESCUENTO SON: REWARD Y REWARD50")
                id = validateDates("Ingrese el id del producto: ")
                current_time = time.strftime("%H:%M:%S")
                client = validaString("Ingrese el nombre del cliente: ")
                quantity = validateDates("Ingrese la cantidad: ") 
                date =  current_time
                discount = validateDates("Ingrese el valor del descuento: ",int)  
                registerSale(id, client,quantity, date, discount)

            elif option3 == 2:
                readSales()
            
            elif option3 == 3:
                print("-----------------------------")
                print("Volviendo al menu anterior...")
                print("-----------------------------")
                break
    elif option == 3:
        while True:
            print("Reportes y/o estadisticas")
            print(" 1.Reporte completo \n 2.Volver al menu principal")
            try:
                option4 = int(input("Ingrese una opcion del menu: "))
                if option4 < 1 or option4 >2:
                    print("Error, el valor de la opcion debe estar entre 1 y 2.")
            except ValueError:
                print("El dato deber ser numerico, no puedes ingresar texto.")

            if option4 == 1:
                mostSales()
            elif option4 == 2:
                print("Volviendo al menu anterior...")
                break


