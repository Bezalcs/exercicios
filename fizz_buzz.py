# exercicio: Escreva uma função chamada fizz_buzz(n) que recebe um número inteiro n e retorna uma lista dos números de 1 a n seguindo as regras abaixo:
# Substitua números divisíveis por 3 por "Fizz".
# Substitua números divisíveis por 5 por "Buzz".
# Substitua números divisíveis por 3 e 5 por "FizzBuzz".

n = int(input('digite o numero: '))
i = 1

while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
    i=i+1