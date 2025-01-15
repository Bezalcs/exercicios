# exercicio: Escreva uma função chamada fizz_buzz(n) que recebe um número inteiro n e retorna uma lista dos números de 1 a n seguindo as regras abaixo:
# Substitua números divisíveis por 3 por "Fizz".
# Substitua números divisíveis por 5 por "Buzz".
# Substitua números divisíveis por 3 e 5 por "FizzBuzz".

#definindo a função fizzbuzz
def fizz_buzz(n):
    resultado = [] #lista para receber os numeros

#laço para fazer os testes
    for i in  range(1, n + 1):
        if i % 3 == 0 and i % 5 ==0:
            resultado.append('fizzbuzz')
        elif i % 5 == 0:
            resultado.append('buzz')
        elif i % 3 ==0:
            resultado.append('fizz')
        else:
            resultado.append(i)
    return resultado

#entrada dos numeros
n = int(input('Digite um numero: '))

#lista mostra os resultados com as substituição apos a operação logica
resultado = fizz_buzz(n)
print(resultado)
