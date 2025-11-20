
print("BIENVENIDO A EJERCICIOS DE PROGRAMACION EN PYTHON")

def contar_vocales():
    frase = input("Ingrese una frase: ").lower()

    countA = 0
    countE = 0 
    countI = 0
    countO = 0
    countU = 0
    count = {"a": "",
             "e": "",
             "i": "",
             "o": "",
             "u":""
             
             }
    for i in frase:
        if i in "aeiou":
            if i == "a":
                countA +=1
                count["a"] = countA
            elif i == "e":
                countE +=1
                count["e"] = countE
            
            elif i == "i":
                countI +=1
                count["i"] = countI
            elif i == "o":
                countO +=1
                count["o"] = countO
            else: 
                countU +=1
                count["u"] = countU
    print(count)

while True:
    print("MENU DE OPCIONES")
    print("0.FIZZBUZZ")
    print("1.CLASIFICADOR DE NUMEROS")
    print("2.CONTADOR DE VOCALES")
    print("3.LISTA DE TAREAS")
    print("4.MAQUINA DE BEBIDAS")


    while True: 
        try:
            Opt = int(input("Ingrese la opcion que desea ejecutar: "))
            if (Opt < 0) or (Opt > 4):
                print("Ingrese un numero del menu")
            break
        except ValueError:
            print("ERROR, NO PUEDE INGRESAR DATOS DE TIPO TEXTO")


    if Opt == 0:
        print("Fizz Buzz")

        for i in range (1,101):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("FIzz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
            
    if Opt == 1:
        print("CLASIFICADOR DE NUMEROS")
        number = int(input("Ingresa cuantos numeros vas a ingresar a la lista: "))
        positive = []
        negative = []
        zero = []
        for i in range(number):
            numbers = int(input(f"Ingrese el valor #{i+1}: "))
            if numbers > 0:
                positive.append(numbers)
            elif numbers < 0:
                negative.append(numbers)
            else: 
                zero.append(numbers)
        print("los valores de la lista positiva son: ", *positive)
        print("los valores de la lista negativa son: ", *negative)
        print("los valores de la lista de zero son: ", *zero)

    if Opt == 2:
        print("CONTADOR DE VOCALES")
        contar_vocales()

    if Opt == 3:
        ListTask = []


        while True:
            print(" 1.AGREGAR TAREAS \n 2.MOSTRAR TAREA COMPLETADA (INDICE) \n 3.MOSTRAR TODO")

            opt = int(input("Ingrese la opcion: "))

            if opt == 1:

                titulo = input("Ingrese el nombre de la tarea: ")
                while True:
                    try:
                        completado = int(input("Ingrese si la tarea esta completada \n 1.Si \n 2.No \n "))
                        if completado == 1:
                            dic = {
                                "title" : titulo,
                                "success" : True
                            }
                            ListTask.append(dic)
                            print("Tarea agregada correctamente!")
                            
                        
                        elif completado == 2:
                            dic = {
                                    "title" : titulo,
                                    "success" : False
                                }
                            ListTask.append(dic)
                            print("Tarea agregada correctamente!") 

                        else:
                            print("Opcion invalida. Ingrese 1 o 2")                   
                            continue

                        break

                    except ValueError:
                        print("Ingresaste un dato erroneo")

            if opt == 2:
                for i,tarea in enumerate(ListTask):
                    estado = "Completada" if tarea["success"] else "Incompleta"
                    print(f"{i+1}. {tarea["title"]} - {estado}")
                    
                opcion = int(input("Indique la tarea que desea modificar"))
                opcion -= 1
                tarea = ListTask[opcion]

                print(f"Escogiste la tarea: {tarea["title"]} - {estado}")

                nuevo_estado = int(input("Nuevo estado:\n 1. Completada\n 2. Incompleta\n --> "))

                if nuevo_estado == 1:
                        
                        tarea["success"] = True
                        estado = "Completado"
                        if tarea["success"] == True :
                            print("Ya esta completada")
                        # print(f"La tarea: {tarea["title"]} cambio su estado a {estado} ")
                elif nuevo_estado == 2:
                        tarea["success"] = False
                        estado = "Incompleta"
                        print(f"La tarea: {tarea["title"]} cambio su estado a {estado} ")
                else:
                        print("Ingresa 1 o 2")

                

            if opt == 3:
                for i,tarea in enumerate(ListTask):
                    estado = "Completada" if tarea["success"] else "Incompleta"
                    print(f"{i+1}. {tarea["title"]} - {estado}")

    if Opt == 4:
        print("Bienvenido a la maquina espendedora")
        print("1. Agua 1$")