def fatorial(a, show=False):
    """
    calcula o fatorial
    :param a: numero a ser fatorado
    :param show:(opcional) mostra ou não a conta
    :return: retorna o valor fatorado
    """
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



print(fatorial(5, True))
help(fatorial)

