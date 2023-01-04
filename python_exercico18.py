from math import sin, cos, tan, radians

angulo = float(input('Digite do valor do ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Seu Seno é {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}')