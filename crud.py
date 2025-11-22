import json 

file = "employes.json"

def inicializar():
    try: 
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}
    
def save(data):
    with open(file, "w") as f:
        json.dump(data,f,indent=4)

def crate(codigo, name, age):
    data = inicializar()
    data[codigo] = {"name":name , "age":age}
    save(data)
    print("estudiante creado. ")

crate(1,"hola",21)

def Show():
    data = inicializar()
    for cod , info in data.items():
        print(cod,info)
Show()
