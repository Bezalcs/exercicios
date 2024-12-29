#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um numero inteiro positivo: '))


if n > 0:
    if n % 2 == 0:
        print(f'O numero {n} é par')
    else:
        print(f'O numero {n} é impar')
else:
    print('Por favor digite um numero positivo')


#metodos utilizados:
#declaração de uma varivavel
#estrutura de condicional aninhada para verificar a entrada de dados é um inteiro positivo e depois verificar se essa entrada é impar ou par
#operadores matematicos
