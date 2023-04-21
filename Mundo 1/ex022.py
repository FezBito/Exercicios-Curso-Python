nome = input('Digite seu nome completo:').strip()
print(f'Nome em maiúsculo:{nome.upper()}')
print(f'Nome em minúsculo:{nome.lower()}')

print(f'Seu nome tem no total {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")}')
