import sqlite3

conn = sqlite3.connect("Personas.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()

def createPerson(name, age):
    cursor.execute("INSERT INTO personas (name, age) VALUES (?,?) ", (name, age))
    conn.commit()
    print("record created")


def listPerson():
    cursor.execute("SELECT * FROM personas")
    personas = cursor.fetchall()
    for p in personas:
        print(f"ID: {p[0]} , name {p[1]}, age {p[2]}")
    if not personas:
            print("Empty")

def updatePersonas (id, newName , newAge):
    cursor.execute("UPDATE personas SET name = ? , age = ? WHERE id = ? ",(newName, newName,id))
    conn.commit()
    print("User Update")


def deletePerson (id):
    cursor.execute("DELETE FROM personas WHERE id = ?",(id))
    conn.commit()
    print("Record Delete")

def menu():
    while True: 
        print("\n--- CRUD de Personas ---")
        print("1. Crear persona")
        print("2. Listar personas")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Salir")
        while True:            
            try:        
                opt = int(input("ingrese una opcion del menu: "))
                break
            except ValueError:
                print("Error ingrese una dato numerico")

        if opt == 1:
                while True:
                        name = input("Ingrese su nombre: ")
                        if name.replace("" , "").isalpha():
                            break
                        else:
                            print("numeros o caracteres especials prohibidos")
                while True:
                        try:
                            age = int(input("ingrese su edad: "))
                            createPerson(name,age)
                            break                   
                        except ValueError:
                             print("No puedes poner letras en tu edad")
                             


        elif opt == 2:
            listPerson()

        elif opt == 3: 
            id = int(input("ID de la persona a actualizar: "))
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            updatePersonas(id, nombre, edad)

        elif opt == 4:
            id = input("ID de la persona a eliminar: ")
            deletePerson(id)

        elif opt == "5":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()
    conn.close()
        