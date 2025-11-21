import csv
import json 
file = "inventary.json"

total = 0

def inicializar():
    try: 
        with open (file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}
    
def savee (data):
    with open(file, "w") as f:
        json.dump(data,f, indent = 4)

def CreateProduct(id, name,price,quantity):
    data = inicializar()
    data[id] = {"name" : name, "price" : price , "quantity": quantity}
    savee(data)
    print("Producto creado.")


def read():
    data = inicializar()
    if not data:
        print("NO hay nada dentro")

    for name, info in data.items():
        print(name,info)

def Search(name):
    data = inicializar()
    for key,info in data.items():
        if key == name:
            print(name,info)
        else:
            print("NO hay")

def update(id, name = None, price = None, quantity = None):
    data = inicializar()
    id = str(id)
    if id in data:
        if name:
            data[id]["name"] = name
        if price:
            data[id]["price"] = price
        if quantity:
            data[id]["quantity"] = quantity
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




def saveCsv(ruta, data=None):
    """
    Carga productos desde un CSV y devuelve una lista/dict compatible con el inventario.
    
    Parámetros:
    - ruta: ruta del archivo CSV a cargar
    - data: inventario existente (dict) para fusionar si se elige
    """
    
    if data is None:
        data = {}

    productos_cargados = {}
    filas_invalidas = 0

    try:
        with open("UserHistory.py/functions/files/inventario.csv", "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            filas = list(lector)

            if not filas:
                print("El archivo CSV está vacío.")
                return data

            # Validar encabezado
            header = filas[0]
            if [h.lower() for h in header] != ["nombre", "precio", "cantidad"]:
                print(f"Encabezado inválido. Se esperaba: nombre,precio,cantidad")
                return data

            # Procesar filas
            for i, fila in enumerate(filas[1:], start=2):
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio_str, cantidad_str = fila
                try:
                    precio = float(precio_str)
                    cantidad = int(cantidad_str)
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue
                except ValueError:
                    filas_invalidas += 1
                    continue

                productos_cargados[nombre] = {"price": precio, "quantity": cantidad}

    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {ruta}")
        return data
    except UnicodeDecodeError:
        print(f"Error: El archivo {ruta} tiene un encoding inválido")
        return data
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return data

    # Preguntar al usuario si sobrescribir o fusionar
    if productos_cargados:
        while True:
            opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
            if opcion in ("S", "N"):
                break
            print("Respuesta inválida. Ingrese S o N.")

        if opcion == "S":
            data = productos_cargados
            accion = "Reemplazo del inventario actual"
        else:
            # Política de fusión:
            # - Si el producto ya existe, sumamos cantidad
            # - Si el precio difiere, actualizamos al nuevo precio
            for nombre, info in productos_cargados.items():
                if nombre in data:
                    data[nombre]["quantity"] += info["quantity"]
                    if data[nombre]["price"] != info["price"]:
                        data[nombre]["price"] = info["price"]
                else:
                    data[nombre] = info
            accion = "Fusión con inventario existente"

        print(f"\nResumen de carga:")
        print(f"Productos cargados: {len(productos_cargados)}")
        print(f"Filas inválidas omitidas: {filas_invalidas}")
        print(f"Acción realizada: {accion}")

    else:
        print("No se cargaron productos válidos desde el CSV.")

    return data




