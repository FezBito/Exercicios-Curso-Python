# Calcular IMC de acordo com a tabela proposta pelo exercício
from math import pow
peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (pow(alt , 2))
print(f'O IMC dessa pessoa é = {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal!')
elif imc <= 30: 
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida')

