print("MENU DE OPCIONES: ")
print("1.Hola usuario: pide al usuario su nombre y edad. Luego imprime un mensaje: \n")
print("2.Suma de dos números.\n")
print("3.Area del triangulo\n")
print("4.Conversor de grados Celsius a Fahrenheit.\n")
print("5.Tipo de dato: usar type() para mostrar el tipo de cada variable.\n")
print("6.Edad futura \n")
print("7.Salir")

opt = int(input("ingresa la opcion que quieras seleccionar: "))
while True:
    if opt == 1: 
        nombre = input("ingresa tu nombre: ") 
        edad = int(input("ingrese tu edad: "))
        print ("hola bienvenido", nombre, "tu edad es: ", edad)

        
    elif opt == 2:
        num1 = int(input(" ingresa tu primer numero: "))
        num2 = int(input("ingresa tu segundo numero: "))
        print (f"{num1} + {num2} = {num1 + num2}")

    elif opt == 3:
        base = int(input("ingrese la base del triangulo: "))
        altura = int(input("ingrese la altura: "))
        print (f"{base} * {altura} / 2 = {base * altura / 2}")

    elif opt == 4:
        farenheit = 9 / 5
        celcius = int(input(" ingresa el valor:  "))
        print (f"el resultado de celcius a farenheit es = {celcius * farenheit + 32}  ")
        

        