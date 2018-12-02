
def ordenamientoBurbuja(unaLista):
    unaLista.sort() #ordenamos la lista por requerimientos asi se logra que la lista quede en orden
    for numPasada in range(len(unaLista)-1,0,-1): #el ciclo va a empezar desde atras
        for i in range(numPasada):
            if len(unaLista[i]) > len(unaLista[i+1]):
                temp = unaLista[i]#contenedor temporal
                unaLista[i] = unaLista[i+1]#lo mueve
                unaLista[i+1] = temp# lo coloca

unaLista = ['w','a','for','sa','z','abc']
ordenamientoBurbuja(unaLista)
print(unaLista)


for i in range (5,0,-1):
    print(i)