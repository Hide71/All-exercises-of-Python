tab = int(input('\33[45mDigite um numero para ver sua tabuada: \33[m'))
print('\33[33m=' * 30)
print(f'Tabuada do {tab} '.center(30))
print('=' * 30)
print('\33[m')
print(f'\33[34m{tab} x  1 = {tab * 1}\n'
      f'\33[34m{tab} x  2 = {tab * 2}\n'
      f'\33[34m{tab} x  3 = {tab * 3}\n'
      f'\33[34m{tab} x  4 = {tab * 4}\n'
      f'\33[34m{tab} x  5 = {tab * 5}\n'
      f'\33[34m{tab} x  6 = {tab * 6}\n'
      f'\33[34m{tab} x  7 = {tab * 7}\n'
      f'\33[34m{tab} x  8 = {tab * 8}\n'
      f'\33[34m{tab} x  9 = {tab * 9}\n'
      f'\33[34m{tab} x 10 = {tab * 10}')
print('\33[33m-='* 10)