import math

ant=4800
a = 11400
b = 12600
c = 41100
d = 14700
e = 38000
area_restante=0
valor=0

#cantidad acumulada
cantidad_seguimiento = 0
cantidad_a = 0
cantidad_b = 0
cantidad_c = 0
cantidad_d = 0
cantidad_e = 0


def calcular_area_restante(datodos, datouno):
    if datodos < 0:
        area_restante=0
    else:
        area_restante=datouno-datodos*ant
    return (area_restante)

def calcular_antenas_nuevas(area_restante, datotres):

    if (datotres=="a"):
        valor=a
    elif (datotres=="b"):
        valor=b
    elif (datotres=="c"):
        valor=c
    elif (datotres=="d"):
        valor=d
    elif(datotres=="e"):
        valor=e
    else:
        valor=0

    try:
        cantidad_de_antenas_nuevas=area_restante/valor
    except:
        cantidad_de_antenas_nuevas=0
    return (math.ceil(cantidad_de_antenas_nuevas))

def cantidad_acumulada(antenas_nuevas, datodos):
    global cantidad_a
    global cantidad_b
    global cantidad_c
    global cantidad_d
    global cantidad_e
    global cantidad_seguimiento
    cantidad_seguimiento=cantidad_seguimiento+antenas_nuevas

    if datodos =="a":
        cantidad_a=cantidad_a+antenas_nuevas
    elif datodos =="b":
        cantidad_b=cantidad_b+antenas_nuevas
    elif datodos=="c":
        cantidad_c=cantidad_c+antenas_nuevas
    elif datodos=="d":
        cantidad_d=cantidad_d+antenas_nuevas
    elif datodos=="e":
        cantidad_e=cantidad_e+antenas_nuevas

    return (cantidad_seguimiento, cantidad_a, cantidad_b, cantidad_c, cantidad_d, cantidad_e)

def resultados_finales(cantidad_seguimiento, cantidad_a, cantidad_b, cantidad_c, cantidad_d, cantidad_e):
    cantidad_seguimiento=math.ceil(cantidad_seguimiento)
    cantidad_a=math.ceil(cantidad_a)
    cantidad_b = math.ceil(cantidad_b)
    cantidad_c = math.ceil(cantidad_c)
    cantidad_d = math.ceil(cantidad_d)
    cantidad_e = math.ceil(cantidad_e)

    if ciclos==0:
        final=0
        print(final)
    else:
        print(cantidad_seguimiento)
    print("a {:.2f}%".format(cantidad_a/cantidad_seguimiento*100))
    print("b {:.2f}%".format(cantidad_b/cantidad_seguimiento*100))
    print("c {:.2f}%".format(cantidad_c/cantidad_seguimiento*100))
    print("d {:.2f}%".format(cantidad_d/cantidad_seguimiento*100))
    print("e {:.2f}%".format(cantidad_e/cantidad_seguimiento*100))

ciclos=int(input("ingrese lac antidad de ciclos"))

inicio=0
if ciclos !=0:
    while inicio < ciclos:

        try:
            datouno = int(input("ingresa el area"))
        except:
            datouno=0


        datodos = int(input("ingrese la cantidad de antenas viejas"))
        datotres = input("ingrese el tipo de antena a instalar")

        arearest = calcular_area_restante(datodos, datouno)
        antenas_nuevas = calcular_antenas_nuevas(arearest, datotres)
        contador, aa, bb, cc, dd, ee = cantidad_acumulada(antenas_nuevas, datotres)

        print(math.ceil(antenas_nuevas))

        inicio=inicio+1

    resultados_finales(contador, aa, bb, cc, dd, ee)

else:
    resultados_finales(1,0,0,0,0,0)
