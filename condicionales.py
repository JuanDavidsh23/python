


print("mayor o menor de edad")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    print("Recuerda que la mayoría de edad es a los 18 años.")  

""" --------------------------------------- """

print("número positivo, negativo o cero")
numero = float(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

""" --------------------------------------- """

print("calculadora basica con +, -, *, /")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")    
if operacion == "+":
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida.")

""" --------------------------------------- """

print("clasficar notas excelente, bueno, regular, insuficiente")
nota = float(input("Ingrese la nota: "))
if nota >= 90:
    print("La nota es excelente.")
elif nota >= 75:
    print("La nota es buena.")
elif nota >= 60:
    print("La nota es regular.")
else:
    print("La nota es insuficiente.")

""" --------------------------------------- """

print("comparador de números")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print(f"{num1} es mayor que {num2}.")
elif num1 < num2:
    print(f"{num1} es menor que {num2}.")
else:
    print(f"{num1} es igual a {num2}.")

""" --------------------------------------- """
