   
print("Bienvenido al sistema")

while True:
    print("\nSeleccione una opción para ejecutar:")
    print(" 1.Sistema de calificaciones \n 2.Carrito de compras con diccionarios \n 3.Cajero automático \n 4.Gestión de estudiante base de datos \n 5.Calculadora con funciones \n 6.Agenda de contactos(lista de diccionarios) \n 7.Salir")

    option = int(input("Ingrese una opción para realizar: "))
    if option == 1:
        print("Sistema de calificaciones")
        while True:
            score = float(input("Ingrese la calificación del estudiante (o -1 para salir): "))
            if score == -1:
                print("Saliendo del sistema de calificaciones.")
                break
            elif 0 <= score <= 100:
                if score >= 90:
                    grade = 'A'
                elif score >= 80:
                    grade = 'B'
                elif score >= 70:
                    grade = 'C'
                elif score >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                print(f"La calificación es: {grade}")
            else:
                print("Calificación inválida. Por favor ingrese un valor entre 0 y 100.")

    elif option == 2:
        print("carrito de compras con diccionarios")
        cart = {}
        while True:
            item = input("Ingrese el nombre del artículo (o 'salir' para terminar): ")
            if item.lower() == 'salir':
                break
            price = float(input(f"Ingrese el precio de {item}: "))
            quantity = int(input(f"Ingrese la cantidad de {item}: "))
            if item in cart:
                cart[item]['quantity'] += quantity
            else:
                cart[item] = {'price': price, 'quantity': quantity}

        total_cost = 0.0
        for item, details in cart.items():
            item_total = details['price'] * details['quantity']
            total_cost += item_total
            print(f"{item}: {details['quantity']} x ${details['price']:.2f} = ${item_total:.2f}")

        print(f"Costo total de la compra: ${total_cost:.2f}")

    elif option == 3:
        print("cajero automatico")
        balance = 1000.0    
        while True:
            print("\nBienvenido al Cajero Automático")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir")
            choice = input("Seleccione una opción: ")

            if choice == '1':
                print(f"Su saldo actual es: ${balance:.2f}")
            elif choice == '2':
                amount = float(input("Ingrese la cantidad a depositar: "))
                if amount > 0:
                    balance += amount
                    print(f"Ha depositado: ${amount:.2f}. Nuevo saldo: ${balance:.2f}")
                else:
                    print("Cantidad inválida.")
            elif choice == '3':
                amount = float(input("Ingrese la cantidad a retirar: "))
                if 0 < amount <= balance:
                    balance -= amount
                    print(f"Ha retirado: ${amount:.2f}. Nuevo saldo: ${balance:.2f}")
                else:
                    print("Cantidad inválida o saldo insuficiente.")
            elif choice == '4':
                print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor intente de nuevo.")

    elif option == 4:
        print("gestion de estudiante base de datos")
        students = {}
        while True:     
            print("\nGestión de Estudiantes")
            print("1. Agregar estudiante")
            print("2. Ver estudiantes")
            print("3. Salir")
            choice = input("Seleccione una opción: ")

            if choice == '1':
                name = input("Ingrese el nombre del estudiante: ")
                age = input("Ingrese la edad del estudiante: ")
                students[name] = age
                print(f"Estudiante {name} agregado.")
            elif choice == '2':
                if students:
                    print("Lista de estudiantes:")
                    for name, age in students.items():
                        print(f"Nombre: {name}, Edad: {age}")
                else:
                    print("No hay estudiantes registrados.")
            elif choice == '3':
                print("Saliendo del sistema de gestión de estudiantes.")
                break
            else:
                print("Opción inválida. Por favor intente de nuevo.")

    elif option == 5:
        print("calculadora con funciones")
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            if y != 0:
                return x / y
            else:
                return "Error: División por cero."
        while True:
            print("\nCalculadora")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            choice = input("Seleccione una operación: ")

            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print("Saliendo de la calculadora.")
                break
            else:
                print("Opción inválida. Por favor intente de nuevo.")

    elif option == 6:
        print("Agenda de contactos(lista de diccionarios)")
        contacts = {}
        while True:
            print("\nAgenda de Contactos")
            print("1. Agregar contacto")
            print("2. Ver contactos")
            print("3. Salir")
            choice = input("Seleccione una opción: ")

            if choice == '1':
                name = input("Ingrese el nombre del contacto: ")
                phone = input("Ingrese el número de teléfono del contacto: ")
                contacts[name] = phone
                print(f"Contacto {name} agregado.")
            elif choice == '2':
                if contacts:
                    print("Lista de contactos:")
                    for name, phone in contacts.items():
                        print(f"Nombre: {name}, Teléfono: {phone}")
                else:
                    print("No hay contactos registrados.")
            elif choice == '3':
                print("Saliendo de la agenda de contactos.")
                break
            else:
                print("Opción inválida. Por favor intente de nuevo.")