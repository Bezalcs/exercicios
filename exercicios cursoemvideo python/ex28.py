#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5. 
# O usuário deve tentar adivinhar qual foi o número escolhido pelo computador. 
# O programa deve dizer se o usuário venceu ou perdeu.

import random

def end_game():
    print('Game Over')
    return

def guess_game(computer_number):
    while True:
        try:
            user_number = int(input('Tente adivinhar um número de 0 a 5 que o computador pensou: '))
            if 0 <= user_number <= 5:
                if user_number == computer_number:
                    print('Parabéns, você ganhou o jogo!')
                    break
                else:
                    print('Você errou, tente novamente.')
            else:
                print('Por favor, digite um número entre 0 e 5.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
    
    end_game()

computer_number = random.randint(0, 5)
guess_game(computer_number)   


#Metodos utilizados:
#Declaração de variaveis
#Criação de funções end_game e guess_game para modular e facilitar a logica do programa
#biblioteca random para sortear um numero
#while para criar um laço de repetição, o bloco se repetira sempre que a condição for verdadeira e interrompida quando falsa