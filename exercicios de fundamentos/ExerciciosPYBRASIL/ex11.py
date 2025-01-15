#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.


#declarando variaveis
num_a = int(input('Digite o primeiro numero inteiro: '))
num_b = int(input('Digite o segundo numero inteiro: '))

#substituindo a maldita virgula por ponto
num_cstr1 = input('Digite um numero real ')
num_cstr2 = num_cstr1.replace(',', '.')
num_c = float(num_cstr2)

#declarando as variaveis das operações
primeiro_dobro_metade_segundo = (num_a * 2) * (num_b / 2)
primeiro_triplo_terceiro = (num_a * 3) + num_c
terceiro_cubo = num_c ** 3

print(f'o produto do dobro do primeiro com metade do segundo é: {primeiro_dobro_metade_segundo:.0f} a soma do triplo do primeiro com o terceiro é: {primeiro_triplo_terceiro:.0f} o terceiro elevado ao cubo é: {terceiro_cubo:.2f}')



