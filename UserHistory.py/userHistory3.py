from colorama import init, Fore, Back, Style
from functionsUser3 import CreateProduct, read, Search, update, deletee, Stadistic

while True:
    print(Fore.RED + " 1.Add product \n 2.Show Products \n 3.Search Products \n 4.Update Product \n 5.Delete Product \n 6.Stadistisc \n 7.Save as CSV")

    opt = int(input("Choose a option: "))
    if opt == 1:
        global countPrice, countQuantity
        countPrice = 0
        countQuantity = 0
        name = input("INgrese el nombre: ")
        price = int(input("INgrese  un precio: "))
        countPrice += price
        quantity = int(input("INgrese  una cantidad: "))
        countQuantity += quantity
        CreateProduct(name, price, quantity)
    
    elif opt == 2: 
        read()
    
    elif opt == 3:
        name = input("INgrese el nombre: ")
        Search(name)
    
    elif opt == 4:
        name = input("INgrese el nombre: ")
        price = int(input("INgrese  un precio: "))
        quantity = int(input("INgrese  una cantidad: "))
        update(name,price,quantity)

    elif opt == 5:
        name = input("INgrese el nombre: ")
        deletee(name)

    elif opt == 6:
        Stadistic()
    
    elif opt == 7:
        print("Save as CSV")

     


    
            

