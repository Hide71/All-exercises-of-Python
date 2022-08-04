from random import randint
from time import sleep
comp = randint(0, 2)
print('''Suas opções: 
[0] PEDRA 
[1] PAPEL
[3] TESOURA''')
jog = int(input('Qual é sua jogada?:'))
sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
sleep(1)
if comp == 0 and jog == 0:
    print('computador jogou PEDRA\nJogador jogou PEDRA')
    print('EMPATE')
elif comp == 1 and jog == 1:
     print('computador jogou PAPEL\nJogador jogou PAPEL')
     print('EMPATE')
elif comp == 2 and jog == 2:
     print('computador jogou TESOURA\nJogador jogou TESOURA')
     print('EMPATE')
if comp == 1 and jog == 0:
    print('computador jogou PAPEL\nJogador jogou PEDRA')
    print('COMPUTADOR VENCEU!')
elif comp == 2 and jog == 1:
     print('computador jogou TESOURA\nJogador jogou PAPEL')
     print('COMPUTADOR VENCEU!')
elif comp == 0 and jog == 2:
     print('Computador jogou PEDRA\nJogador jogou TESOURA ')
     print('COMPUTADOR VENCEU!')
if comp == 2 and jog == 0:
    print('computador jogou TESOURA\nJogador jogou PEDRA')
    print('JOGADOR VENCEU!')

elif comp == 0 and jog == 1:
    print('computador jogou PEDRA\nJogador jogou PAPEL')
    print('JOGADOR VENCEU!')

elif comp == 1 and jog == 2:
    print('Computador jogou PAPEL\nJogador jogou TESOURA')
    print('JOGADOR VENCEU!')
