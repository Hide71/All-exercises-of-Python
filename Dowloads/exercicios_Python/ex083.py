lista = []
exp = str(input('Digite a expressão: '))
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if simb == 0:
    print('Expressão é valida')
else:
    print('Expressão inválida!')


print(lista)