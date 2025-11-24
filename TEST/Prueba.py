from functions import validaString, validateDates , showProduct, addProducts
print("-----------------------------------------------")
print("BIENVENIDO AL SISTEMA DE INVENTARIO Y VENTAS")
print("-----------------------------------------------")

Products = [{
    "nombre":"",
    "":"",
    "":"",
    "":""
}]

while True: 
    print("Menu Principal")
    print(" 1.Gestion del inventario \n 2.Gestion de ventas \n 3.Reportes \n 4.Salir")
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
                if option < 1 or option2 >5:
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
                addProducts(title, author,category,price,quantity)
                print("Producto registrado correctamente. ")

            elif option2 == 2: 
                showProduct()

            elif option2 == 3:
                print("Actualice su producto")
                oldName = validaString("Ingrese el nombre actual del producto: ").lower().strip()
                newTitle = validaString("Ingrese el titulo nuevo de su producto: ")
                newAuthor = validaString("Ingrese el nombre del autor: ")
                newCategory = validaString("Ingrese la categoria:")
                newPrice = validateDates("Ingrese el precio del producto: ", int)
                newQuantity = validateDates("Ingrese la cantidad stock: ", int)
                addProducts(oldName,newTitle, newAuthor,newCategory,newPrice,newQuantity)
                print("Producto actualizado.")


