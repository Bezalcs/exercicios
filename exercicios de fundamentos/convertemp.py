#Escreva uma função chamada celsius_para_fahrenheit(celsius) que recebe uma temperatura em graus Celsius e retorna o valor convertido para Fahrenheit.


def celsius_para_fahrenheit(c):


    f = (( 9 * c) / 5) + 32
    print(f'A temperatura {c} graus celcius é {f} em farenheit')
    return (c)

c = float(input(f'insira a temperatura em graus celcius: '))
celsius_para_fahrenheit(c)