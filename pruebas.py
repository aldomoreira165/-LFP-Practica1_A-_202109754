arreglo = [10, 20, 30, 40, 50, 60]

def borrar(code):
    for i in range(len(arreglo)-1):
        if code == arreglo[i]:
            arreglo.pop(i)
    #print(len(arreglo))

def imprimir():
    long = len(arreglo)
    for i in range(long):
        print("Dato: ", arreglo[i], " Indice: ", i)

#imprimir()
#print("")
#borrar(60)
#imprimir()

borrar(20)
borrar(10)
borrar(50)
imprimir()



