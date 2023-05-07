# Verificar se um número é primo em sequência
n = int(input('Digite um número: '))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[35m', end=' ')
        div += 1
    else:
        print('\33[m', end=' ')
    print(c, end=' ')

if div > 2:
    print(f'\n\33[35mO número {n} foi divisível {div} vezes e por isso ele não é primo')
else:
    print(f'\n\33[32mO número {n} foi divisível {div} vezes e por isso ele é primo')
