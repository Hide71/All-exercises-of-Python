from random import randint
from time import sleep
print(f'\33[33m{"-=" * 30}')
print('\33[34mVou pensar em um numero de 0 a 5  tente adivinhar...')
print(f'\33[33m{"-=" * 30}')
comp = randint(0, 5)
jog = int(input('Em que numero eu pensei?'))
print('\33[37mprocessando...')
sleep(1)
if comp == jog:
    print(f'\33[36mParabéns! voce venceu!! Eu pensei no numero {comp} e voce digitou {jog}')
else:
    print(f'\33[36mGANHEI! Eu pensei no numero {comp} e não no {jog}')