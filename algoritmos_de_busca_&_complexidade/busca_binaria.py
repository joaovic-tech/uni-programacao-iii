"""
Pesquisa binaria
* Jack quer que Joana adivinhe qual numero ele esta pensando, de 1 até 100
* Jack se compromete a dizer para Joana se o valor que ele pensou e maior ou menor
"""
import random

def busca_sequencial(inicio, fim, dados, buscado):
    while inicio <= fim:
        meio = int((inicio + fim) / 2)

        if buscado > dados[meio]:
            inicio = meio + 1
        elif buscado < dados[meio]:
            fim = meio - 1
        else:
            return meio

    return -1

dados = random.sample(range(100), 100)
dados.sort()
print(dados)
buscado = int(input("Digite o valor que deseja buscar: "))
achou = busca_sequencial(0,len(dados), dados, buscado)
if not achou:
    print("Valor nao encontrado.")
else:
    print(f"Valor encontrado na posição {achou}.")