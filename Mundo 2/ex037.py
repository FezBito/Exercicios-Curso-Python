# Converter número para diferentes bases 
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Digite o número da opção desejada: '))

if opcao == 1:
    print(f'{num} em Binário é = {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em Octal é = {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em Hexadecimal é = {hex(num)[2:]}')
else:
    print('Opção Inválida!!!')