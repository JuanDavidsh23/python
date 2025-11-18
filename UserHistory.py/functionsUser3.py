import json 
file = "inventary.json"

def inicializar():
    try: 
        with open (file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}
    
def savee (data):
    with open(file, "w") as f:
        json.dump(data,f, indent = 4)

def CreateProduct(name,price,quantity):
    data = inicializar()
    data[name] = {"price" : price , "quantity": quantity}
    savee(data)
    print("Producto creado.")


def read():
    data = inicializar()
    for name, info in data.items():
        print(name,info)

def Search(name):
    data = inicializar()
    for key,info in data.items():
        if key == name:
            print(name,info)


def update(name, price = None, quantity = None):
    data = inicializar()
    if name in data:
        if price:
            data[name]["price"] = price
        if quantity:
            data[name]["quantity"] = quantity
        savee(data)
        print("Producto actualizado.")
    else:
        print("Producto no encontrado.")

def deletee(name):
    data = inicializar()
    if name in data: 
        del data[name]
        savee(data)
        print("Producto eliminado. ")
    else:
        print("no se encuentra el producto.")

def Stadistic():
    data = inicializar()
    total = 0
    for name, info in data.items():
        print(f"{name}, {info} \n")
        totalCost = info['price'] * info['quantity']
        total +=totalCost 
        savee(data)

    print(f"el precio total del carrito es: {total}")


    
        

