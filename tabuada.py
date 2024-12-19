#Escreva uma função chamada tabuada(n) que recebe um número inteiro n e retorna uma lista contendo a tabuada de 1 a 10 para o número n.

#definindo a função
def tabuada(n): 
    lista_inteiros = [1,2,3,4,5,6,7,8,9,10] #lista com valores a serem multiplicados a serem  multiplicados
    lista_tabuada = [] #lista com o resultad

 #loop para calcular a tabuada  
    for  i in lista_inteiros: #percorrer toda a lista
     m = n * i  #variavel que vai receber o resultado da multiplicação
     lista_tabuada.append(m) #adciona o resultado m na lista da  tabuada para cada multiplicação n * i
    print(f'a tabuada de {n} é: {lista_tabuada}')     #saida com  o resultado da tabuada          
    return lista_tabuada


n = int(input(f'digite um numero: '))
tabuada(n)