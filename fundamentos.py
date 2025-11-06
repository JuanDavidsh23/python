        

print("MENU DE OPCIONES: ")
print("1.Hola usuario: pide al usuario su nombre y edad. Luego imprime un mensaje: \n")

print("2.Suma de dos números.\n")

print("3.Area del triangulo\n")

print("4.Conversor de grados Celsius a Fahrenheit.\n")

print("5.Tipo de dato: usar type() para mostrar el tipo de cada variable.\n")

print("6.Edad futura \n")

print("7.Salir")


while True:

    opt = int(input("INGRESE UNA OPCION DEL MENU: "))

    if opt > 7:
        print("ingrese una opcion valida")
  

    elif  opt == 1:
        while True:
            name = input("Ingrese su nombre: ")
            if name.isalpha():
                while True:
                    try:
                        age = int(input("Ingrese su edad: "))
                        print(f"Hola, {name}. Tienes {age} años.")
                        break  
                    except ValueError:
                        print("Error: Por favor, ingrese un número válido para la edad.")
                break  
            else:
                print("Error: El nombre solo puede contener letras. Por favor, ingrese un nombre válido.")

                
# --------------------------------------- 
    elif opt == 2:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        def suma(a, b):
                return a + b

        result = suma(num1, num2)
        print(f"La suma de {num1} y {num2} es: {result}")

# --------------------------------------- 
    elif opt == 3: 
        print("Area del triángulo")

        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")

#--------------------------------------- 
    elif opt == 4: 
        print("Conversión de grados Celsius a Fahrenheit")

        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

#---------------------------------------
    elif opt == 5:
        print("tipo de dato")

        valor = input("Ingrese un valor: ")
        print(f"El tipo de dato de {valor} es: {type(valor)}")

#--------------------------------------- 
    elif opt == 6:
        print("edad en le futuro")

        edad_actual = int(input("Ingrese su edad actual: "))
        anios = int(input("Ingrese la cantidad de años en el futuro: "))
        edad_futura = edad_actual + anios
        print(f"En {anios} años, tendrás {edad_futura} años.")

#--------------------------------------- 

    elif opt == 7:
        print("Adios")

    else:
        print("Ingrese una opcion valida: ")

