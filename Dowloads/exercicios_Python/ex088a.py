from random import randint
from time import sleep
sorteio = []
mega = []
j = 0
print('\33[33m-='*30)
print('Jogos na mega sena'.center(30))
print('-='*30)
quant = int(input('\33[36mQuantos jogos você quer que eu sorteie?: '))
print(f'\33[31mSorteando {quant} jogos'.center(30))
while j < quant:
    j += 1
    for c in range(0, 6):
        n = randint(1, 60)
        if n not in sorteio:
            sorteio.append(n)
        else:
            sorteio.append(randint(1, 60))
    sorteio.sort()
    mega.append(sorteio[:])
    sorteio.clear()
for i, v in enumerate(mega):
    print(f'\33[32mJogo {i + 1}: {v}')
    sleep(1)
print('\33[40mBoa Sorte!!\33[m'.center(30))

