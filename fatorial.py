#Implemente uma função chamada fatorial(n) que recebe um número inteiro n (n ≥ 0) e retorna o fatorial de n.

from math import factorial

def n_fatorial(n):
    
    
    if n <= 0:   
        print(f'O numero {n} não é maior ou igual a zero')
    else:
        f = factorial(n)
        print(f'O fatorial de {n} é  {f}')

    return n

n = int(input(f'Digite um numero maior ou igual a zero: '))
n_fatorial(n)