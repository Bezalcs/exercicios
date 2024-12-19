#Implemente uma função chamada soma_lista(numeros) que recebe uma lista de números inteiros e
# retorna a soma de todos os elementos positivos dessa lista.


#definindo a função
def soma_lista(numeros):
    s = 0 #variavel para armazenar a soma
    n = int #variavel do elemento da lista do laço

 #laço para verificar se um numero é maior  que zero e adciona esse numero a s
    for n in numeros:
     if n > 0:
         s +=  n
    return s

#exemplo
numeros = [1, -2, 4, -7,  8, -10, -11, 13, 14, -15]
resultado = soma_lista(numeros)
print(f'A soma dos números positivos é: {resultado}')