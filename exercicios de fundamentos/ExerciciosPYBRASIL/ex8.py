#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

#armazenando duas variaveis com um unico input usando a função split()
salariostr1, horastr = input('Digite quanto você ganha por hora e quantas horas voce trabalha por mês separados por -: ').split('-')

#ajuste caso o usuário utilize virgula no valor do salario
salariostr2 = salariostr1.replace(',','.' )

#convertendo as strings de entrada em numeros para poder fazer o calculo
salario = float(salariostr2)
hora = int(horastr)

#operação matematica e saida para o usuario
salariomes = salario * hora
print(f'O seu salario no mês é: R$ {salariomes}')