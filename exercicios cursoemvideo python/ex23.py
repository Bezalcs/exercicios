#Descrição: Leia um número de 0 a 9999 e mostre cada um dos dígitos separados.
#Exemplo: Unidade, Dezena, Centena, Milhar.

def verificar_num (n):
    if n > 9999:
        print('O numero digitado é maior que 9999...')
    elif n == str
        entrada_dados(n)
    else:
        unidade = n // 1 % 10
        dezena = n // 10 % 10
        centena = n // 100 % 10
        milhar = n // 1000 % 10
        print(f'A unidade é: {unidade} a dezena é {dezena} a centena é {centena} e o milhar é {milhar} do numero {n}')
    return

def entrada_dados(n):
    n = int(input('Digite um numero de 0 a 9999: '))
    verificar_num(n)
    return

n = int(input('Digite um numero de 0 a 9999: '))
verificar_num(n)
    