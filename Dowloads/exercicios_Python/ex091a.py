dado = {}
from random import randint
from operator import itemgetter
from time import sleep
for c in range(1, 5):
    dado[f'jogador {c}'] = randint(1, 6)
print('Valores sorteados')
ranking = []
for k, v in dado.items():
    print(f'{k} tirou {v} no dado ')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print(ranking)