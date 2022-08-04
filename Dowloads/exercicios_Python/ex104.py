def leiaint(n):
   while True:
       ok = False
       valor = 0
       a = str(input(n))
       if a.isnumeric():
            valor = int(a)
            ok = True
       else:
           print('Erro digite um valor valido')
       if ok:
           break
   return valor


a = leiaint('Digite um numero: ')
print(f'voce acabou de digitar o numero {a}')


