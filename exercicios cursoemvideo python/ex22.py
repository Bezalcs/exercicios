# Exercício 022
# Descrição: Leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input(f'Digite seu nome: '))
sobrenome = str(input(f'Digite seu sobrenome: '))
nome_completo = str(nome + sobrenome)

print(f'Você se chama {nome.capitalize()} {sobrenome.capitalize()}')

print(f'Esse é seu nome e sobrenome em letras maisculas {nome.upper()} {sobrenome.upper()}')

print(f'Esse é seu nome e sobrenome em letras minusculas {nome.lower()} {sobrenome.lower()}')

nome_completo.strip()
print(f'seu nome completo possui {len(nome_completo)} letras e seu nome possui {len(nome)} letras')