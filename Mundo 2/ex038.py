# Verificar o maior número entre 2 inteiros
n1 = int(input('Digite o primeiro número inteiro:'))
n2 = int(input('Digite o segundo número inteiro:'))

if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é o maior2')
else:
    print('Não existe valor maior. Os dois são iguais')