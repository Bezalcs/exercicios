#programa para sortear os personagens para a party em baldurs gate 3

import random

nomes = ["Lae'Zel","Umbralma", "Astarion","Gale","Wyll", "Karlach", "Halsin","minthara", "jaheira", "minsc"]
historico = []

def Sort_party():
    party = random.sample(nomes, 3)
    print(f"O grupo escolhido foi: {', '.join(party)}")

Sort_party()
