#Leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO".

cidade = str(input(f'Digite o nome de uma cidade: '))
cidade.capitalize

if cidade.startswith('Santo'):
    print(f'Sua cidade começa com a palavra Santo')
else:
    print(f'Sua cidade não começa com a palavra Santo')
    
#metodos utilizados: 
# declaração de variaveis
# str() para definir o tipo de variavel 
# input() para entrada de dados do usuário
# f'' para inserir texto no input
#.capitalize para padronizar a string com a resposta esperada
#if else para teste condicional
#.startswith() para comparar a primeira palavra da string do input com a respota esperada
#print() para mostrar uma mensagem para o usuário
