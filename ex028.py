from random import randint
from time import sleep

numPc = randint(1, 4)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
numUser = int(input('Em que número eu pensei?:'))
print('Processando...')
sleep(3)
if numUser == numPc:
    print('Parabéns! Você acertou o número')
else:
    print(f'Você errou! Eu pensei no {numPc} e não no {numUser}')
