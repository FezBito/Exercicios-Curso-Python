# Calcular Aprovação de aluno por média de 2 notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'Aluno Aprovado com média: {media}')
elif 5 <= media < 7:
    print(f'Aluno de Recuperação com média: {media}')
else:
    print(f'Aluno Reprovado com média: {media}')