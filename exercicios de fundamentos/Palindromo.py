# Questão 2: Palíndromo
# Escreva uma função chamada eh_palindromo(palavra) que recebe uma string palavra e retorna True se ela for um palíndromo
# e False caso contrário. Ignore diferenças entre maiúsculas e minúsculas.

#definindo  a função eh_palindromo
def eh_palindromo(palavra):
    palavra =  palavra.lower() #variavel para  igorar maiscuslas
    inverter = palavra[: : -1] #variavel que vai inverter a palavra
    return palavra == inverter #comparação da palavra com sua  inversão

#entrada da palavra pelo usuario
palavra = input('insira uma palavra para verificarmos se é um palindromo: ')

#teste para verificar se é um palindromo
if eh_palindromo(palavra):
    print(f'{palavra} é um palindromo!')
else:
    print(f'{palavra} não é um palindromo!')