#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

peso = 0

#entrada
genero, h1 = input('Digite o seu genero e sua altura separados por espaço: ').split( )

#tratando a entrada
h2 = h1.replace(',','.')
h = float(h2)
genero = genero.capitalize()

if genero not in ['Masculino', 'Homem','H', 'Menino', 'F', 'Feminino','Mulher', 'Menina']:
    print('Entrada inválida. Gênero não reconhecido.')
elif genero in ['F', 'Feminino','Mulher','Menina']:
    genero = 'Feminino'
    peso = (62.1 * h) - 44.7
    print(f'O peso ideal para o sexo {genero} é {peso:.2f} quilos.')
elif genero in ['Masculino','H', 'Homem', 'Menino']:
    genero = 'Masculino'
    peso = (72.7 * h) - 58
    print(f'O peso ideal para o sexo {genero} é {peso:.2f} quilos.') 