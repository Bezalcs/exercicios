#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input(f'Digite o raio do circulo em centimetros: '))
area = 3.14 * (raio**2)

print(f'A área do circulo é: {area:.2f} cm²!')