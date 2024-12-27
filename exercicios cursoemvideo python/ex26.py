#Leia uma frase qualquer e diga:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece pela primeira vez.
#Em que posição ela aparece pela última vez.

frase = str(input(f'Digite uma frase: '))
frase = frase.upper()
contar_A = frase.count('A')
pos_inicio = frase.find('A')
pos_final = frase.rfind('A')

print(f'Nessa frase a letra A aparece {contar_A} vezes')
print(f'A primeira vez que a letra A aparece é na posição {pos_inicio}')
print(f'A ultima vez que a letra A aparece é na posição {pos_final}')

#metodos utilizados:
#declaração de variaveis
#str() define o dado como uma string
#input() chamada de entrada de dados do usuário
#.upper torna a string em letras maisculas para padronizar e facilitar a comparação
#.count() conta as ocorrencias
#.find() localiza a primeira ocorrencia
#.rfind() localiza a ultima ocorrencia
#print() mostra uma mensagem para o usuário
#f'' permite mostrar uma mensagem concatenando com as variaveis desejadas