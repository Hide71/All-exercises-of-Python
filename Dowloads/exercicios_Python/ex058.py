from random import randint
from time import sleep
comp = randint(0, 10)
print('\33[33mSou seu computador...\33[m')
sleep(1)
print('\33[36mAcabei de pensar em um número de 0 a 10.\33[m')
sleep(1)
print('\33[30mSerá que você consegue adivinhar?\33[m')
sleep(1)
c = 0
while True:
    jog = int(input('Qual é o seu palpite?: '))
    if comp != jog:
        c += 1
    if comp < jog:
        print('Menos ... Tente denovo!')
    else:
        print('mais!!! Tente outra vez!!!')
    if comp == jog:
        break
print(f'Acertou eu pensei {comp} e você digitou {jog}')
print(f'Acertou com {c + 1} tentativas! Parabéns!')

