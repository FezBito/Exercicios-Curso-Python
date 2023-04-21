vel = int(input('Qual a velocidade do carro? '))
if vel > 80.0:
    print(f'O motorista foi multado!\nA Multa irá custar: R${(vel-80)*7:.2f}')
print('Fim do programa!')
