# Verificar se uma palavra/frase é um palíndromo
palavra = input('Digite uma palavra: ').lower().split()
s = ''.join(palavra)
d = (s[::-1])
print(f'A palavra ao contrário é {d}')
if d == s:
    print('Esta palavra é um palíndromo.')
else:
    print('Esta palavra não é um palíndromo.')
