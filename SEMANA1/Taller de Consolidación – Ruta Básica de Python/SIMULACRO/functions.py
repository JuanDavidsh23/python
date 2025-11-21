import json 
file = "inventary.json"

def incializar():
    try: 
        with open(file , "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {} 
    
def save(data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

#Functions inventary

def createProduct(id, name,brand,category,price,quantity,guarantee):
    data = incializar()
    data[id] = {"Nombre":name, "Marca":brand, "Categoria" : category, "Precio c/u": price, "Cantidad" : quantity, "Garantia": guarantee }
    save(data)
    print("Producto creado con exito.") 


def Show():
    data = incializar()
    for items, info in data.items():
        print(f"{items}. Producto: {info['Nombre']} | Marca: {info['Marca']} | Categoría: {info['Categoria']} | Precio c/u: {info['Precio c/u']} | Cantidad: {info['Cantidad']} | Garantía: {info['Garantia']} meses")

def UpdateProduct(id, name = None,brand = None,category = None,price = None,quantity = None ,guarantee = None):
    data = incializar()
    id = str(id)
    if id in data:
        if name: 
            data[id]["Nombre"] = name
        if brand:
            data[id]["Marca"] = brand
        if category:
            data[id]["Categoria"] = category
        if price:
            data[id]["Precio c/u"] = price
        if quantity:
            data[id]["Cantidad"] = quantity
        if guarantee:
            data[id]["Garantia"] = guarantee
        save(data)
    print("Producto Actualizado. ")

        


