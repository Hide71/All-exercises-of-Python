def leiaint(a):
    while True:
        try:
            n = int(input(a))
        except(ValueError, TypeError):
            print('ERRO! por favor digite um valor valido!')
        else:
            return n


def leiareal(a):
    while True:
        try:
            n = float(input(a))
        except(ValueError, TypeError):
            print('Erro: Digite um valor real valido!')
        else:
            return n




