
inventory = [
      {
            "title":"Cien años de soledad",
            "author":"Gabriel garcia",
            "category":"Historia",
            "price":10000,
            "quantity":2
      }

      


]


def validaString(mensaje):
    while True:
        nombre = input(mensaje).strip()
        
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("El nombre no puede contener números ni caracteres especiales.")


def validateDates(mensaje, tipo = int):
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print(f"Error, debe ingresar:{tipo.__name__} ")



def addProducts(title,author,category,price,quantity ):
    dates = {"title":title, "author":author, "category" : category, "price": price, "quantity" : quantity}
    inventory.append(dates)
    print("Se agrego el producto correctamente.")


def showProduct():
    print("Mostrando invenario...")
    for dic in inventory:
        for key, item in dic.items(): 
            print(f"{key}: {item} \n")

def updateProduct(oldName, newTitle,newAuthor,newCategory,newPrice,newQuantity):
    for i in inventory:
        for key,value in i.items():
            if oldName == key:
                key[newTitle]['title'] = newTitle 
                key[newTitle]['author'] = newAuthor   
                key[newTitle]['category'] = newCategory   
                key[newTitle]['price'] = newPrice 
                key[newTitle]['quantity'] = newQuantity
                print("Producto actualizado.")    
            else:
                print("El producto indicado no existe. ")

                



 