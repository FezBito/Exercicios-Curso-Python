# Jokenpo com o computador
from time import sleep
from random import randint
print('HORA DO JOKENPO!')
print('''Escolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
player = int(input('Qual sua jogada?'))
if player > 2:
    print('Jogada Inválida!')
else: 
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print(5*'=-=-=')
    print(f'Computador escolheu {(jokenpo[computador])}')
    print(f'Jogador escolheu {(jokenpo[player])}')
    print(5*'=-=-=')

    if computador == 0:
        if player == 0:
            print('O jogo empatou!')
        elif player == 1:
            print('O Jogador Venceu! Parabéns')
        elif player == 2:
            print('O Computador venceu!')

    elif computador == 1:
        if player == 1:
            print('O jogo empatou!')
        elif player == 0:
            print('O Computador venceu!')
        elif player == 2: 
            print('O Jogador Venceu. Parabéns!')
            
    elif computador == 2:
        if player == 2:
            print('O jogo empatou!')
        elif player == 0:
            print('O Jogador Venceu. Parabéns')
        elif player == 1: 
            print('O Computador Venceu!')


 




