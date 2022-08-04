print('-=' * 30)
print('Analisador de triângulos')
print('-=' * 30)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima  podem formar Triangulo')
else:
    print('Os segmentos acima não  podem formar Triangulo!')