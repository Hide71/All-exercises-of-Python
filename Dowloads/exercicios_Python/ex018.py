from math import sin, cos, tan, radians
ang = int(input('Digite o angulo que vc deseja:  '))

print(f'O angulo de {ang}º tem o Seno {sin(radians(ang)):.2f}\nO angulo de {ang}º tem o Coseno {cos(radians(ang)):.2f}\n'
      f'O angulo de {ang}º tem a Tangente {tan(radians(ang)):.2f}')