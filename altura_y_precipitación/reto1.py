#elaborado por Wilder Salas Mena c.c. 1017185939
msnm=float(input("ingrese la altura sobre el nivel del mar"))
c=float(input("ingrese la temperatura media anual"))


if (msnm>=400 and msnm<=800):
    a=4 #   print("sumamente apto")
elif (msnm<400 or (msnm>800 and msnm <=999)):
    a=3  #   print("moderadamente apto")
elif (msnm>=1000 and msnm<=1200):
    a=2   #  print ("marginalmente apto")
elif (msnm>1200):
    a=1    # print("no apto")

if (c>=25 and c<=28):
    b=4   #  print("sumamente apto")
elif((c>=29 and c<=30) or (c>=21 and c<=24)):
    b=3    # print("moderadamente apto")
elif((c>=31 and c<=32) or (c>=18 and c<=20)):
    b=2    # print ("marginalmente apto")
elif (c<18 or c>32):
    b=1    # print("no apto")

if (a==b): #    print (a)
    c=a
elif (a!=b):
    if (a>b):
        c=b
    else:
        c=a #    print (c)

aa="sumamente apto"
bb="moderadamente apto"
cc="marginalmente apto"
dd="no apto"

if (c==4):
    print(aa)
elif(c==3):
    print(bb)
elif(c==2):
    print(cc)
elif(c==1):
    print(dd)
    




