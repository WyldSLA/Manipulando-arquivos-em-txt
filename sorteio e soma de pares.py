from random import randint
from time import sleep
num = []

def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f"Sorteando 5 valores da lista: ", end="")
    for n in lista:
        print(n, end=" ", flush=True)
        sleep(0.3)

def somaPar(listaPar):
    somap = 0
    for i in listaPar:
        if i % 2 == 0:
            somap+= i
    print(f"\nSomando os valores pares {listaPar}, temos {somap}")

sorteio(num)
somaPar(num)





