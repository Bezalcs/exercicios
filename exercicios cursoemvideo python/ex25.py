#Leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome completo: '))
nome = nome.upper()


if 'SILVA' in nome:
    print(f'Seu nome possui Silva')
else: 
    print(f'Seu nome não possui Silva')
    
#Metodos utilizados:
#declaração de variaveis
#str() define o tipo da variavel como string
#input() captura a entrada do usuário
#.upper() converte a string em letra maiuscula
#if else condicional para testar a entrada e tomar uma ação
#'SILVA' in nome verifica se a substring está na entrada do usuário
#print() mostra uma mensagem para o usuário