lista = ('lapis', 1.75, 'borracha', 2, 'caderno', 15.9, 'estojo', 25, 'transferidor', 4.2,
         'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.9)
print('='*30)
print('\33[34mListagem de preços'.center(30))
print('='*30)
for i, v in enumerate(lista):
    if i % 2 == 0:
        print(f'\33[33m\n{v:.<20}', end='')
    else:
        print(f'R$ {v:.2f}', end='')
print()
print('\33[35m=' * 30)