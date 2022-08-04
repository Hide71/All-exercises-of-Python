from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador 1' : randint(1, 6),
'jogador 2' : randint(1, 6),'jogador 3' : randint(1, 6),
'jogador 4' : randint(1, 6)}
ranking = []
print(dados)
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('=-' * 30)
print('+++  Ranking dos jogadores  +++')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i + 1}o.lugar {v[0]} com {v[1]} pontos')
    sleep(1)