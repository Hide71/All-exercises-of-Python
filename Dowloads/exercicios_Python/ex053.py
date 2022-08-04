frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
reverse = junto[:: -1]
print(reverse)

#reverse = ""
'''for c in range(len(junto)-1, -1, -1):
    reverse += junto[c]
print(f'O inverso de {junto} é {reverse}')
if junto == reverse:
    print('Temos um palindromo!')
else: print('Não forma palindromo')'''