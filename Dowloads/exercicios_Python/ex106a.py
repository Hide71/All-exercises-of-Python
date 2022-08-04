c = ('\33[m,'
     '\33[0;30;40m', '\33[0;30;41m', '\33[0;30;42m', '\33[0;30;43m', '\33[0;30;44m',
     '\33[0;30;45m', '\33[7;30m');
from time import sleep
def ajuda(com):
    titulo(f'Acessando o manual de comando "{com}": ', 4)
    sleep(2)
    print(c[5], end='')
    help(com)
    print(c[0], end='')

def titulo(a, cor=0):
    tam = len(a)
    print(c[cor], end='')
    print('~'* tam)
    print(a)
    print('~'* tam)
    print(c[0], end='')


while True:
   titulo('Sistema de ajuda pyhelp: ', 2)
   comando = str(input('\33[mFunção ou Biblioteca: \33[m'))
   if comando.upper() == 'FIM':
       break
   else:
       ajuda(comando)
titulo('Ate logo', 5)