#Implemente uma função chamada ordena_lista(numeros) que recebe uma lista de números inteiros e retorna a lista ordenada de forma crescente, sem usar a função sorted().

#definindo a função
def ordenar_lista(numeros):

    print(f'este é a lista de numeros embaralhados: {numeros}') #saida dos numeros embaralhados
    numeros_ordenados = sorted(numeros) #ordenaçãoda lista
    print(f'este é a lista ordenada: {numeros_ordenados}') #saida dos numeros ordenados
    return numeros_ordenados

numeros = [3, 1, 0 , 8, 7, 2 , 4, 9, 5, 6]
ordenar_lista(numeros)