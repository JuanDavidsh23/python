import json 

file = "inventary.json"
saleFile = "sales.json"

#This function validates that the data passed contains only letters of the alphabet.
def validaString(mensaje):
    while True:
        nombre = input(mensaje).strip()
        
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("El nombre no puede contener números ni caracteres especiales.")

#This function validates that the data type is an integer by requesting a message and returning an error type.
def validateDates(mensaje, tipo = int):
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print(f"Error, debe ingresar:{tipo.__name__} ")

#This function attempts to read a file, but if it doesn't exist, it returns an empty dictionary.
def inicializar():
    try: 
        with open (file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}
    
def savee2 (data):
    with open(file, "w") as f:
        json.dump(data,f, indent = 4)

#This function attempts to read a file, but if it doesn't exist, it returns an empty dictionary.
def inicializarClient():
    try: 
        with open (saleFile, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

def savee (data2):
    with open(saleFile, "w") as f:
        json.dump(data2,f, indent = 4)



#This function is used to generate the ID 
def generar_id(data):
    next_id = max([int(k) for k in data.keys()], default=0) + 1
    return str(next_id)

#This function is used to save products, checking stock, and assigning each value 
def CreateProduct(tittle, author, category,price, quantity):
    data = inicializar()

    new_id = generar_id(data)

    data[new_id] = {
        "title": tittle,
        "author": author,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    print(f"Producto creado con ID: {new_id}")
    savee2(data)

#This function only displays registered products.
def read():
    data = inicializar()
    if not data:
        print("NO hay nada dentro")

    for key, info in data.items():
            print(f"\n {key}. Titulo: {info['title']} Autor: {info['author']} Categoria: {info['category']} Precio: {info['price']} Cantidad: {info['quantity']} \n")

#This function only updates previously created values, searching for the item to delete by ID.
def updateProduct(id, title = None, author = None, category = None ,price = None , quantity = None ):
    data = inicializar()
    id = str(id)
    if id in data:
        if title:
            data[id]["title"] = title
        if author:
            data[id]["author"] = author
        if category:
            data[id]["category"] = category
        if price:
            data[id]["price"] = price
        if quantity:
            data[id]["quantity"] = quantity
        savee2(data)
        print("Producto actualizado.")
    else:
        print("Producto no encontrado.")

#This function removes the product by ID
def deleteProduct(id):
    data = inicializar()
    if id in data: 
        del data[id]
        savee2(data)
        print("Producto eliminado. ")
    else:
        print("no se encuentra el producto.")

#This function is used to generate the ID 
def generar_id(data2):
    next_id = max([int(k) for k in data2.keys()], default=0) + 1
    return str(next_id)



#This function is used to save sales, checking stock, and assigning price and quantity using the ID.
def registerSale(id, client, quantity, date, discount):
    data2 = inicializarClient()
    data = inicializar()
    found = False
    id = str(id)
    
    if id in data:
        if quantity <= data[id]["quantity"]:
            new_id = generar_id(data2)
            author = data[id]['author']
            price = data[id]['price']
            total = quantity * price * (1 - discount)
            
            data2[new_id] = {
                "client": client,
                "author": author,
                "price": price,
                "quantity": quantity,
                "discount": discount,
                "total": total,
                "date": date
            }
            
            data[id]["quantity"] -= quantity
            
            savee2(data)  
            savee(data2)   
            print(f"Venta registrada con ID: {new_id}")
            found = True
        else:
            print("Lo sentimos, el stock es insuficiente.")
    else:
        print("Producto no encontrado.")
    
  


#This function only displays registered Sales.
def readSales():
    data2 = inicializarClient()
    if not data2:
        print("No hay ventas registradas.")

    for key, info in data2.items():
            print(f"\n {key}. cliente: {info['client']} Autor: {info['author']} Precio: {info['price']} Cantidad: {info['quantity']} Descuento: {info['discount']} Fecha: {info['date']}")

#This function is used to count prices, quantity and discounts, and then perform calculations to determine sales by author.
def mostSales():
    data2 = inicializarClient()
    sales_by_author = {}
    countPrice = 0
    countQuantity = 0
    countDiscount = 0
    for key, value in data2.items():
        countPrice += value['price']
        countQuantity += value['quantity']
        countDiscount += value['discount']
        author = value['author']
        sales_by_author[author] = sales_by_author.get(author, 0) + value['quantity']
    
    print("\n Ventas por autor")
    for author, total in sales_by_author.items():
        print(f"Autor: {author} vendio: {total}")   
    print("-------------------------------------------------------------------------")
    print(f"La cantidad de ventas totales son: {countQuantity} y el dinero obtenido es de: {countQuantity * countPrice - countDiscount}")
    print("-------------------------------------------------------------------------")


#TThis function is used to sort the elements and then return the top 3 of the list
def topSales():
    data2 = inicializarClient()
    productSales = {}
    
    for key, value in data2.items():
        product = value['author']  
        productSales[product] = productSales.get(product, 0) + value['quantity']
    
    top3 = sorted(productSales.items(), key=lambda x: x[1], reverse=True)[:3]
    
    print("\nTop 3 productos más vendidos:")
    for i, (product, quantity) in enumerate(top3, 1):
        print(f"{i}. {product}: {quantity} unidades")   


