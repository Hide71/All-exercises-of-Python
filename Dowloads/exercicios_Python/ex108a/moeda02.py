def dobro(a=0, formato=False):
    d = a * 2
    return d if formato is False else moeda(d)

def metade(a=0, formato=False):
    m = a / 2
    return m if not formato else moeda(m)

def aumentar(a=0, b=0, formato=False):
    tot = a + (a * b/ 100)
    return tot if not formato else moeda(tot)


def diminuir(a=0, b=0, formato=False):
    dim = a - (a * b / 100)
    return dim if formato is False else moeda(dim)

def moeda(preço=0, moeda='R$'):
    return (f'{moeda} {preço:.2f}'.replace('.', ','))



def resumo(a=0, b=10, c=5):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado \t{moeda(a)}')
    print(f'Dobro do preço \t{dobro(a, True)}')
    print(f'Metade do preço \t{metade(a, True)}')
    print(f'Com {b}% de aumento {aumentar (a, b, True)}')
    print(f'Com redução de {c}% {diminuir(a, b, True)}')


