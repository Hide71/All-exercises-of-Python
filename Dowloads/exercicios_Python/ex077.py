lista = ('aprender', 'programar', 'python', 'linguagem', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'programador', 'futuro', 'univesp', 'chega')
for palavras in lista:
     print(f'\nNa palavra \33[33m{palavras.upper()}\33[m temos as vogais: ', end='')
     for l in palavras:
         if l in 'aeiou':
             print(f'\33[36m{l}\33[m', end=' ')