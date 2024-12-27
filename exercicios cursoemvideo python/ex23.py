#Descrição: Leia um número de 0 a 9999 e mostre cada um dos dígitos separados.
#Exemplo: Unidade, Dezena, Centena, Milhar.

def verificar_num (n):
    if n > 9999:
        print('O numero digitado é maior que 9999...')
    elif n < 0:
         print('O número digitado é menor que 0...')
       
    else:
        unidade = n // 1 % 10
        dezena = n // 10 % 10
        centena = n // 100 % 10
        milhar = n // 1000 % 10
        print(f'A unidade é: {unidade} a dezena é {dezena} a centena é {centena} e o milhar é {milhar} do numero {n}')
    return

def entrada_dados():
    try:
        n = int(input('Digite um número de 0 a 9999: '))
        verificar_num(n)
    except ValueError:
        print('Entrada inválida! Por favor, insira apenas números inteiros positivos.')
    return


entrada_dados()
