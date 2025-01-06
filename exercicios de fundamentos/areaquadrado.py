#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

lado = float(input(f'Digite o tamanho de um dos lados do quadrado em centimetros: '))
areaquadrado = lado ** 2
areadobrada = areaquadrado * 2

print(f'A área dobrada do seu quadrado é {areadobrada:.2f} cm²')