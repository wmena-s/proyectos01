close=[]
matriz=[]
contador1=contador2=contador3=0
contador4=0

def promedioo(matriz):
    suma = 0
    for j in matriz:
        suma=suma+j

    promedio=suma/len(matriz)
    return ("{:.2f}".format(promedio))

"""recibir valores"""
with open('data.csv', 'r', encoding="utf-8") as archivo:
    # lee linea por linea y crea la matriz
    archivo.readline()
    for line in archivo:
        close.append(line.split(','))
    #    "busca en la primera columna la que coincida con barranquilla y agrega
    #    los valores  de la columna 7
    for i in close:
        for j in i:
            if j == "Barranquilla":
                matriz.append(i[6])
    #crea el vector con la cantidad de cada valor
    for i in matriz:
        if i == "sumamente apto\n":
            contador1=contador1+1
        elif i =="moderadamente apto\n":
            contador2=contador2+1
        elif i == "marginalmente apto\n":
            contador3=contador3+1
        elif i == 'no apto\n':
            contador4=contador4+1
    #vector creado
    matrizDos=[contador1, contador2, contador3, contador4]
    #crea una copia del vector creado
    matriztres=matrizDos.copy()

    # metodo de burbuja para organizar la matriz, modifica la matriz tres para que
    # quede organizada
    for i in range(len(matriztres)-1):
        for j in range(len(matriztres)-1):
            if matriztres[j] < matriztres[j+1]:
                temp=matriztres[j]
                matriztres[j]=matriztres[j+1]
                matriztres[j+1]=temp

    matrizcuatro=["sumamente apto", "moderadamente apto", "marginalmente apto", "no apto"]

"""promedio de variables"""
matrizcinco=[]
for i in close:
    for j in i:
        if j == "Barranquilla":
            matrizcinco.append(int(i[2]))

matrizseis=[]
for i in close:
    for j in i:
        if j == "Barranquilla":
            matrizseis.append(int(i[3]))

"""mayores """
menor=10000000000
mayor = 0
mayordos=0
for i in matrizcinco:
    if mayor < i:
        mayor=i

for i in matrizseis:
    if mayordos < i:
        mayordos = i

"""menores """
menor = 1111111111111110
menordos=11111111111110
for i in matrizcinco :
    if menor > i and menordos>0:
        menor=i
    else:
        continue

for i in matrizseis:
    if menordos  > i and menordos>0:
        menordos = i
    else:
        continue

print(promedioo(matrizcinco), promedioo(matrizseis))
print(menor, menordos)
print(mayor, mayordos)

for i in range(4):
    c = 0
    for a in range(3):
        if matriztres[i] == matrizDos[a]:
            break
        else:
            c = c + 1
    print(matrizcuatro[c], matrizDos[c])

#imprime matricez
#print(matriz)
#print(matrizDos)
#print (matriztres)