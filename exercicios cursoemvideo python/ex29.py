#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

speed_limit = int (80)
speed = int(input('Qual é a velocidade registrada? '))
diff_speed =speed - speed_limit
multa = float(diff_speed * 7)

if diff_speed <= 0:
    print('Dentro do limite permitido...')
else: 
    print(f'Acima do limite, a multa a ser paga é de R$ {multa:.2f}')


#Metodos utilizados:
#declaração de variaveis
#operadores matematicos
#Condicional composta