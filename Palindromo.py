# Questão 2: Palíndromo
# Escreva uma função chamada eh_palindromo(palavra) que recebe uma string palavra e retorna True se ela for um palíndromo
# e False caso contrário. Ignore diferenças entre maiúsculas e minúsculas.

def eh_palindromo(palavra):
    palavra =  palavra.lower()
    inverter = palavra[: : -1]
    return palavra == inverter

palavra = input('insira uma palavra para verificarmos se é um palindromo: ')

if eh_palindromo(palavra):
    print(f'{palavra} é um palindromo!')
else:
    print(f'{palavra} não é um palindromo!')