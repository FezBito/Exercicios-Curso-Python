from random import choice
name1 = input('Digite o Primeiro Nome:')
name2 = input('Digite o Segundo Nome:')
name3 = input('Digite o Terceiro Nome:')
name4 = input('Digite o Quarto Nome:')
lista = [name1, name2, name3, name4]

print(f'O escolhido foi {choice(lista)}')
