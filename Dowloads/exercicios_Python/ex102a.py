def fatorial(a, show=False):
    '''
    função que calcula o fatorialde um numero
    :param a: numeroo a ser fatorado
    :param show: (opcional) exibe ou não 0 calculo
    :return:retorna o resultado para o prog principal
    '''
    f = 1
    for c in range(a, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f





print(fatorial(5, False))
help(fatorial)