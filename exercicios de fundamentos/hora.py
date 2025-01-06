#escreva um programa que receba um horario de entrada e mostra as horas, minutos e segundos separados

entrada_hora = str(input(f'Digite um horario qualquer nesse formato: hh:mm:ss: '))
hor, min, seg = entrada_hora.split(":")
print(f'O horario que você digitou é composto por {hor} horas, {min}, minutos e {seg} segundos')