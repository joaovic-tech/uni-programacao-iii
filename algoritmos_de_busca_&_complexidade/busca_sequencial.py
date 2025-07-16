"""
Pesquisa sequencial
* Jack quer que Joana adivinhe qual numero ele esta pensando, de 1 até 100
* Jack se compromete a dizer para Joana se o valor que ele pensou e maior ou menor
"""
import random

def busca_sequencial(dados, buscado):
    achou = False
    i = 0

    while (i < len(dados)) and (achou == False):
        if dados[i] == buscado:
            achou = True
        else:
            i += 1

    if not achou:
        return False
    else:
        return i + 1

dados = random.sample(range(100), 100)
print(dados)
buscado = int(input("Digite o valor que deseja buscar: "))
achou = busca_sequencial(dados, buscado)
if not achou:
    print("Valor nao encontrado.")
else:
    print(f"Valor encontrado na posição {achou}.")