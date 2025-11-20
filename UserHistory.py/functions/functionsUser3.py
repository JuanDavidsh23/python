import csv
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




def saveCsv(ruta, inventario_actual=None):
    """
    Carga productos desde un CSV y devuelve una lista/dict compatible con el inventario.
    
    Parámetros:
    - ruta: ruta del archivo CSV a cargar
    - inventario_actual: inventario existente (dict) para fusionar si se elige
    """
    
    if inventario_actual is None:
        inventario_actual = {}

    productos_cargados = {}
    filas_invalidas = 0

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            filas = list(lector)

            if not filas:
                print("El archivo CSV está vacío.")
                return inventario_actual

            # Validar encabezado
            header = filas[0]
            if [h.lower() for h in header] != ["nombre", "precio", "cantidad"]:
                print(f"Encabezado inválido. Se esperaba: nombre,precio,cantidad")
                return inventario_actual

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
        return inventario_actual
    except UnicodeDecodeError:
        print(f"Error: El archivo {ruta} tiene un encoding inválido")
        return inventario_actual
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return inventario_actual

    # Preguntar al usuario si sobrescribir o fusionar
    if productos_cargados:
        while True:
            opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
            if opcion in ("S", "N"):
                break
            print("Respuesta inválida. Ingrese S o N.")

        if opcion == "S":
            inventario_actual = productos_cargados
            accion = "Reemplazo del inventario actual"
        else:
            # Política de fusión:
            # - Si el producto ya existe, sumamos cantidad
            # - Si el precio difiere, actualizamos al nuevo precio
            for nombre, info in productos_cargados.items():
                if nombre in inventario_actual:
                    inventario_actual[nombre]["quantity"] += info["quantity"]
                    if inventario_actual[nombre]["price"] != info["price"]:
                        inventario_actual[nombre]["price"] = info["price"]
                else:
                    inventario_actual[nombre] = info
            accion = "Fusión con inventario existente"

        print(f"\nResumen de carga:")
        print(f"Productos cargados: {len(productos_cargados)}")
        print(f"Filas inválidas omitidas: {filas_invalidas}")
        print(f"Acción realizada: {accion}")

    else:
        print("No se cargaron productos válidos desde el CSV.")

    return inventario_actual




