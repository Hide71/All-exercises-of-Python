from random import randint
from time import sleep
quant = int(input("Quer sortear quantos jogos?: "))
lista = []
sorteio = []
a = 1
while a <= quant:
    c = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
             lista.append(n)
             c += 1
        if c >= 6:
             break
    lista.sort()
    sorteio.append(lista[:])
    lista.clear()
    a += 1
for i, v in enumerate(sorteio):
    print(f'Jogo{i + 1}:{v}')
    sleep(1)