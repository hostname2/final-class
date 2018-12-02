import string
import random


def generador_word(num,max):
    lista=[]#inicializa
    for i in range(num):
        x = 0
        a = ''
        while x < max:
            a += random.choice(string.ascii_letters)#crea letra random y crea la palabra
            x += 1
        if a not in lista:#verifica que la palabra no se repita
            lista.append(a)
    return lista


print(generador_word(5, 3))



