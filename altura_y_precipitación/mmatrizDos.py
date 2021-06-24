def matrizcero():
    lista_a = [[1, 2, 3],[5,6,8]]
    lista_b = [4, 5, 6]

    for indice in range(0, len(lista_a[0])):
        indicedos=0
        while indicedos < len(lista_a):
         print(lista_a[indicedos][indice]*lista_b[indice])
         indicedos+=1

def matrizuno(lista_a,Lista_b):
    lista_a = [[1, 2, 3], [5, 6, 8]]
    lista_b = [[4, 5, 6], [2, 3, 8]]

    for indiceDos in range(len(lista_a)):
        valoruno = 0
        while valoruno < len(lista_a[0]):
            print(lista_a[indiceDos][valoruno]*lista_b[indiceDos][valoruno])
            valoruno += 1


def dividirarray():
    aarray=['moderadamente apto', 'marginalmente apto', 'no apto', 'moderadamente apto', 'no apto', 'no apto', 'no apto',
     'marginalmente apto', 'marginalmente apto', 'moderadamente apto', 'marginalmente apto', 'marginalmente apto',
     'marginalmente apto', 'no apto', 'no apto', 'no apto', 'marginalmente apto', 'no apto', 'no apto', 'no apto',
     'marginalmente apto']
    contador=0
    matric=[]
    contadorDops=0
    cc=len(aarray)
    aa = 0
    bb = cc / 3  # largo dividido la cantidad de ciclos

    while (contadorDops < cc):
        while (contador >= aa and contador < bb):
            matric.append(aarray[contador])

            contador+=1

       # print(matric)
        contadorDops+=7
        aa+=7
        bb+=7
        mayor=0
        conta4=0
        conta3=0
        conta2=0
        conta1=0
        maytor=0
        for i in matric:
            if (i=="sumamente apto"):
                conta4=conta4+1

            elif (i=='moderadamente apto'):
                conta3 = conta3 + 1

            elif (i=='marginalmente apto'):
                conta2 = conta2 + 1

            elif (i=='no apto'):
                conta1 = conta1 + 1


        matrizv=[conta1,conta2,conta3,conta4]
        for i in matrizv:
            if (i > maytor):
                maytor=i
            else:
                continue

        if (maytor == conta1):
            if contador < 21:
                print('no apto', end=",")
            else:
                print('no apto')
        elif(maytor==conta2):
            if contador < 21:
                print('marginalmente apto', end=",")
            else:
                print('marginalmente apto')
        elif(maytor==conta3):
            if contador < 21:
                print('moderadamente apto', end=",")
            else:
                print("moderadamente apto")
        elif(maytor==conta4):
            if contador < 21:
                print("no apto", end=",")
            else:
                print ("no apto")



        matric = []

def dividirarraydos():
    aarray=['moderadamente apto', 'marginalmente apto', 'no apto', 'moderadamente apto', 'no apto', 'no apto', 'no apto',
     'marginalmente apto', 'marginalmente apto', 'moderadamente apto', 'marginalmente apto', 'marginalmente apto',
     'marginalmente apto', 'no apto', 'no apto', 'no apto', 'marginalmente apto', 'no apto', 'no apto', 'no apto',
     'marginalmente apto']
    contador=0
    matric=[]
    contadorDops=0
    cc=21
    aa = 0
    bb = cc / 3  # largo dividido la cantidad de ciclos

    while (contadorDops < cc):
        while (contador >= aa and contador < bb):
            matric.append(aarray[contador])

            contador+=1

       # print(matric)
        contadorDops+=7
        aa+=7
        bb+=7
        mayor=0
        conta4=0
        conta3=0
        conta2=0
        conta1=0
        maytor=0
        for i in matric:
            if (i=="sumamente apto"):
                conta4=conta4+1

            elif (i=='moderadamente apto'):
                conta3 = conta3 + 1

            elif (i=='marginalmente apto'):
                conta2 = conta2 + 1

            elif (i=='no apto'):
                conta1 = conta1 + 1


        matrizv=[conta1,conta2,conta3,conta4]
        menor=10000
        for i in matrizv:
            if (i < menor and i > 0):
                menor=i
            else:
                continue

        if(menor==conta4):
            if contador < 21:
                print("no apto", end=",")
            else:
                print ("no apto")
        elif(menor==conta3):
            if contador < 21:
                print('moderadamente apto', end=",")
            else:
                print("moderadamente apto")

        elif(menor==conta2):
            if contador < 21:
                print('marginalmente apto', end=",")
            else:
                print('marginalmente apto')
        elif (menor == conta1):
            if contador < 21:
                print('no apto', end=",")
            else:
                print('no apto')




        matric = []

dividirarray()
dividirarraydos()