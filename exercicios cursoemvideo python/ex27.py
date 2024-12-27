#Leia o nome completo de uma pessoa e mostre:
#O primeiro nome.
#O último nome.

nome = str(input('Insira seu nome completo: '))
nome_completo = nome.split()
primeiro_nome = nome_completo[0]
ultimo_nome = nome_completo[-1]


print(f'Seu nome é: {primeiro_nome}')
print(f'Seu ultimo sobrenome é: {ultimo_nome}')