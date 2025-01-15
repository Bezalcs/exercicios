# Escreva uma função chamada conta_vogais(texto) que recebe uma string e
# retorna a quantidade de vogais presentes no texto.
# Considere vogais tanto maiúsculas quanto minúsculas.

def conta_vogais(palavra):
    palavra = palavra.lower() #para considerar letras maiusculas e minusculas
    vogais = ['a','e','i','o','u'] #definindo as vogais
    total_vogais =  0 #variavel que vai receber a quantidade de vogais

 #teste que percorre a palavra e para cada letra encontrada na lista vogais soma 1 em total_vogais
    for i in palavra:
        if i in vogais:
            total_vogais += 1
    return total_vogais

palavra = input(f'digite uma palavra: ')
print(f'A quantidade de vogais na palavra:',palavra , f' é: ', conta_vogais(palavra))





