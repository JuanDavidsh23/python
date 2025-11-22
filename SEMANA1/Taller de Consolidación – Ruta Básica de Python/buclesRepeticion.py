print("BIENVENIDO A BUCLES Y REPETICIONES")

while True:
    print(" 1.NUMERO DEL 1 AL 10 \n 2.SUmatoria del 1 al N \n 3.Tabla de multiplicar \n 4.contador regresivo con while \n 5.Adivina el numero \n 6.sumar hasta que escriba 0 \n 7.Salir")
    opt = int(input("ingrese una opcion para realizar: "))

    if opt == 1:
        print("contar de 1 a 10")
        for i in range(1, 11):
            print(i)        

# --------------------------------------- """
    elif opt == 2:
        print("sumatoria de números del 1 al n")
        n = int(input("Ingrese un número entero positivo: "))
        sumatoria = 0
        for i in range(1, n + 1):
            sumatoria += i
        print(f"La sumatoria de los números del 1 al {n} es: {sumatoria}")

#--------------------------------------- """

    elif opt == 3:
        print("Tabla de multiplicar")
        num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

#--------------------------------------- """
    elif opt == 4:
        print("contador regresivo con while")
        contador = 10
        while contador > 0:
            print(contador)
            contador -= 1
        print("Fin del contador regresivo.")

#--------------------------------------- """
    elif opt == 5:
        print("adivina el número con random")
        import random
        opt = random.choice(range(1, 101))
        player = int(input("Adivina el número entre 1 y 100: "))
        while player != opt:
            if player < opt:
                print("Demasiado bajo. Intenta de nuevo.\n")
            else:
                print("Demasiado alto. Intenta de nuevo. \n")
            player = int(input("Adivina el número entre 1 y 100: "))
        print("¡Felicidades! Has adivinado el número.")

#--------------------------------------- """
    elif opt == 6:
        print("sumar hasta que user escriba 0")
        userNum = int(input("Ingrese un número (0 para terminar): "))
        totalSum = 0
        while userNum != 0:
            totalSum += userNum
            userNum = int(input("Ingrese un número (0 para terminar): "))
        print(f"La suma total es: {totalSum}")

#--------------------------------------- """
    elif opt == 7: 
        print("Adios")
        break
    else:
        print("ELija una numero valido. \n")
