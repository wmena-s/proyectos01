import math

ant=4800
a = 11400
b = 12600
c = 41100
d = 14700
e = 38000

vector_departamentos=[]
vector_area=[]
vector_antenasv=[]
vector_tipo=[]
vector_par_departamento=[]
vectorfinalfinal=[] #crea un vector con la suma de los datos analizados
porcentaje=[]
vector_sumaporcentual=[]
vectorfinalfinalfinal=[]  # crea un vector con los departamentoss analizados

menordos=10000000000
sumasuma=0
cantidad_aa=0
cantidad_bb=0
cantidad_cc=0
cantidad_dd=0
cantidad_ee=0
mayor=0
valor=0
antenas_nuevas=0
area_restante=0
menor=1000000000000000000

"""funciones ......................................................................................................."""
def calcularNuevasAntenas():
    arearest = calcular_area_restante(antenas_viejas, area)
    antenas_nuevas = calcular_antenas_nuevas(arearest, datos_a_evaluar[3])
    return(antenas_nuevas)

def calcular_area_restante(datodos, datouno):
    if datodos < 0:
        area_restante=0
    else:
        area_restante=datouno-datodos*ant
    return (area_restante)

"""calcula la cantidad de antenas de cada tipo"""
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

"""solicita la cantidad de departamentos y terrenos deseada, con sus estructuras de control........................."""
try:
    departamento_terreno=list(map(int, input("camtidad de departamentos y terrenos").strip().split()))
    controluno=0
except:
    print("datos ingresados de manera incorrecta")
    controluno=1

while departamento_terreno[1]<1 or controluno==1 or len(departamento_terreno) > 2:
    print("datos ingresados de manera incorrecta")
    departamento_terreno = list(map(int, input("camtidad de departamentos y terrenos").strip().split()))

"""solicitar valores a evaluar......................................................................................."""
departamento=area=antenas_viejas=tipo=0
vector_par_antenas_n=[]
vector_par_departamento=[]
vector_par_tipo=[]
i=0
while i < departamento_terreno[1]:
    try:
        datos_a_evaluar = list(map(str, input("ingresa los 4 datos a evaluar: departamento, area, antenas viejas y tipo de antenas nuevas").strip().split()))
        departamento=int(datos_a_evaluar[0])
        area=int(datos_a_evaluar[1])
        antenas_viejas=int(datos_a_evaluar[2])
        tipo=datos_a_evaluar[3]

        """generar vector de cantidad de antenas nuevas por tipo............................................................"""
        vector_antenas_nuevas_por_tipo = []
        antenas_nuevas=calcularNuevasAntenas()
        if datos_a_evaluar[3] == "a":
            cantidad_aa = cantidad_aa + calcularNuevasAntenas()
        if datos_a_evaluar[3] == "b":
            cantidad_bb = cantidad_bb + calcularNuevasAntenas()
        if datos_a_evaluar[3] == "c":
            cantidad_cc = cantidad_cc + calcularNuevasAntenas()
        if datos_a_evaluar[3] == "d":
            cantidad_dd = cantidad_dd + calcularNuevasAntenas()
        if datos_a_evaluar[3] == "e":
            cantidad_ee = cantidad_ee + calcularNuevasAntenas()

        if antenas_nuevas < 0:
            vector_par_antenas_n.append(0)
        else:
            vector_par_antenas_n.append(antenas_nuevas)

        vector_par_departamento.append(departamento)
        vector_par_tipo.append(tipo)
        i+=1
    except:
        i

vector_antenas_nuevas_por_tipo=[cantidad_aa, cantidad_bb, cantidad_cc, cantidad_dd, cantidad_ee]

vector_acumulado_antenaspordepartamento=[]
vector_acumulado=[]
sumados=0
contaaa=contabb=contacc=contadd=contaee=0
vector_acumulado_de_tipos=[]
for o in range(departamento_terreno[0]):
    for i, j, z in zip(vector_par_departamento, vector_par_antenas_n, vector_par_tipo):
        if i==(o+1):
            sumados=sumados+j

            if z == "a":
                contaaa=contaaa+j
            if z == "b":
                contabb = contabb + j
            if z == "c":
                contacc = contacc + j
            if z == "d":
                contadd = contadd + j
            if z == "e":
                contaee = contaee + j
    vector_acumulado_de_tipos.append(contaaa)
    vector_acumulado_de_tipos.append(contabb)
    vector_acumulado_de_tipos.append(contacc)
    vector_acumulado_de_tipos.append(contadd)
    vector_acumulado_de_tipos.append(contaee)
    contaaa = contabb = contacc = contadd = contaee = 0
    vector_acumulado.append(sumados)
    vector_acumulado_antenaspordepartamento.append(o+1)
    sumados=0

vectoresDivididos=[vector_acumulado_de_tipos[i: i+5] for i in range(0, len(vector_acumulado_de_tipos), 5)]

mayor=-1
menor=100000000000
contador=0
contadordos=0
resultado=""
contadordeciclo=0
suma=0
mayor_tipo=-1
contadortres=0
vector_unido=[]
menor_tipob=10000000000000
vector_unidob=[]
contadordeciclob=0
for i in vectoresDivididos:
    contadordeciclo=contadordeciclo+1

    for w in i:
        suma=suma+w

    for k in i:
        if contador != 4:
            if mayor < k:
                mayor = k
                contadordos = contador
                contador += 1
            else:
                contador+=1
        else:
            contadordos=contadordos+1
            if contadordos == 1:
                resultado = "a"
            if contadordos == 2:
                resultado = "b"
            if contadordos == 3:
                resultado = "c"
            if contadordos == 4:
                resultado = "d"
            if contadordos == 5:
                resultado = "e"
            print(contadordeciclo)
            print(suma)
            print(resultado, mayor)
            contador=0
            mayor=0
            break

    for k in i:
        if contador < 4:
            if menor > k:
                menor = k
                contadordos = contador
                contador += 1
            else:
                contadordos = contadordos + 1
                if contadordos == 1:
                    resultado = "a"
                if contadordos == 2:
                    resultado = "b"
                if contadordos == 3:
                    resultado = "c"
                if contadordos == 4:
                    resultado = "d"
                if contadordos == 5:
                    resultado = "e"
                print(resultado, menor)
                contador = 0
                menor = 100000000000
                break

    mayor = -1
    contador = 0
    contadordos = 0
    menor=10000000000
    suma=0

vectorN=vectoresDivididos




vectorNNN=["a","b","c","d","e"]
vectorNN=[["a","b","c","d","e"]]+vectorN



"""calcular mayor por departamento y letra..........................................................................."""
mayootro=0
vectornuevovu=[]
vectornuevovus=[]
for w in range(5):
    for i in range(departamento_terreno[0]+1):
        if i < 1:
            continue
        else:
            if mayootro < vectorNN[i][w]:
                mayootro = vectorNN[i][w]
                rr=i #1

            elif mayootro ==0 and departamento_terreno[0] ==i:
                mayootro=0
                rr=1
    vectornuevovu.append(mayootro)
    vectornuevovus.append(rr)

    mayootro=0

"""calcular MENOR por departamento y letra..........................................................................."""

menootro=1000000000
vectornuevovuOne=[]
vectornuevovusOne=[]
for l in range(5):
    for t in range(departamento_terreno[0]+1):
        if t < 1:
            continue
        else:
            if menootro > vectorNN[t][l]:
                menootro=vectorNN[t][l]
                tt=t
    vectornuevovusOne.append(tt)
    vectornuevovuOne.append(menootro)
    menootro=1000000000



cant=0
for i, j, k, t, y in zip(vectornuevovus, vectornuevovu, vectorNNN, vectornuevovuOne, vectornuevovusOne):
    print(vectornuevovusOne[cant], vectornuevovuOne[cant], vectorNNN[cant])
    print(vectornuevovus[cant], vectornuevovu[cant], vectorNNN[cant])
    cant = cant + 1

"""ES NECESARIO VERIFICAR LOSR RESULTADOS DE MAYOR, NO ESTA DANDO CON 5X8"""