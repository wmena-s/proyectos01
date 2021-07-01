#variables -------------------------------
contador1=contador2=contador3=contador4=contador=contadorDos=i=0 #crea los numeros a utilizar
vectorunouno=[]
vectormatriz=[]
vectormatrizdos=[] #crea los vectores a utilizar
matriz=[]
j=0


def imprimirVector(av):
    """permite imprimir los valores en el formato deseado"""
    for inicio in av:
        print("{:.2f}".format(inicio), end=" ")
    print("")

#multiplica matrices en sus posiciones
def multiplicarmatrices(v,vv):
    matrizz=[]
    for i, j in zip(v, vv):
        for p, q in zip (i, j):

            matrizz.append(calculador(p, q))

    return matrizz


def contarMatriz(matriz):
    global contador1, contador2, contador3, contador4
    for ar in matriz:
        if (ar == "marginalmente apto"):
            contador2 = contador2 + 1
        if (ar == "moderadamente apto"):
            contador3 = contador3 + 1
        if (ar == "sumamente apto"):
            contador4 = contador4 + 1
        if (ar == "no apto"):
            contador1 = contador1 + 1

#funciones ---------------------------------
def calculador(msnm, c):
    """función que permite clasificar las pareja altura-tempertatura"""
    a=0
    b=0
    #calcular el nivel en que se encuentra la variable altura
    if (msnm >= 400 and msnm <= 800):
        a = 4
    elif (msnm < 400 or (msnm > 800 and msnm <= 999)):
        a = 3
    elif (msnm > 999 and msnm <= 1200):
        a = 2
    elif (msnm > 1200):
        a = 1
    # calcular el nivel en que se encuentra la variable temperatura
    if (c > 24 and c <= 28):
        b = 4
    elif ((c > 28 and c <= 30) or (c > 20 and c <= 24)):
        b = 3
    elif ((c > 30 and c <= 32) or (c >= 18 and c <= 20)):
        b = 2
    elif (c < 18 or c > 32):
        b = 1
    #definir cual esta en una categoria más alta
    if(a == b):
        c = a
    elif (a != b):
        if (a > b):
            c = b
        else:
            c = a

    # retornar la categoria mas alta en string
    if (c==4):
        return ("sumamente apto")
    elif (c==3):
        return ("moderadamente apto")
    elif (c==2):
        return ("marginalmente apto")
    elif (c==1):
        return ("no apto")

if __name__ == '__main__':
    """función que da inicio al programa"""
    # definir los vectores de datos, tres vectores por cada tip de variable (msnm y c)
    ciclos = int(input("ciclos"))
    # ciclosDos=ciclos
    while i < ciclos:
        altura = list(map(int, input("algtura").strip().split()))
        vectormatriz.append(altura)
        i += 1

    while j < ciclos:
        temperatura = list(map(int, input("temperatura").strip().split()))
        vectormatrizdos.append(temperatura)
        j += 1

    matrizzz=multiplicarmatrices(vectormatriz, vectormatrizdos)
    print(matrizzz)
    contarMatriz(matrizzz)
    print(contador1, contador2, contador3, contador4)