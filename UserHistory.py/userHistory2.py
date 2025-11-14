from functions import ShowMenu, validateOption, showProducts, addProducts, stadistics



while True:
    ShowMenu()
    option = validateOption()

    if option == 1:
        addProducts()
    
    elif option == 2:
        showProducts()

    elif option == 3:
        stadistics()
    else:
          print("Gracias por usar el sistema.")
          
          break








