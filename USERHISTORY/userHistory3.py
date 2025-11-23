
from functions.functionsUser3 import CreateProduct, read, Search, update,validaString, deletee, validateDates , Stadistic, saveCsv, cargarCsv

while True:
    print( " 1.Añadir Productos \n 2.Mostrar productos \n 3.Buscar Productos \n 4.Actualizar Productos \n 5.Eliminar  Productos \n 6.Estadistiscas \n 7.Guardar como CSV \n 8.Cargar desde Csv")

    while True: 
        try:
            opt = int(input("Choose a option: "))
            if opt < 1 or opt > 8:
                print("Error, el valor debe estar entre 1 y 8")
            break
        except ValueError:
            print("Error, el valor debe ser numerico.")

    if opt == 1:
        global countPrice, countQuantity
        countPrice = 0
        countQuantity = 0

        name = validaString("Ingrese el nombre del producto: ")

        price = validateDates("Ingrese el precio: ", int)
        countPrice += price

        quantity = validateDates("Ingrese la cantidad: ")
        countQuantity += quantity
        CreateProduct(name, price, quantity)
    
    elif opt == 2: 
        read()
    
    elif opt == 3:
        name = validaString("INgrese el nombre: ")
        Search(name)
    
    elif opt == 4:
        id = validateDates("Ingrese el id del producto: ",int)
        name = validaString("INgrese el nombre: ")
        price = validateDates("Ingrese el precio actualizado del producto: ",int)
        quantity = validateDates("Ingrese la cantidad actualizada del producto: ",int)
        update(id, name,price,quantity)

    elif opt == 5:
        id = input("INgrese el id del producto: ")
        deletee(id)

    elif opt == 6:
        Stadistic()
    

    elif opt == 7:  
            ruta = "USERHISTORY/functions/files/inventario.csv"
            saveCsv(ruta)

    elif opt == 8:
        ruta = "USERHISTORY/functions/files/inventario2.csv"
        cargarCsv(ruta)
            

            
            

