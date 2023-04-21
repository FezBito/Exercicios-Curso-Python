from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do ângulo em graus:'))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tang = tan(radians(angulo))

print(f'Seno de {angulo} graus = {seno:.2f} \nCosseno de {angulo} graus = {coseno:.2f} \nTangente de {angulo} graus = {tang:.2f}')
