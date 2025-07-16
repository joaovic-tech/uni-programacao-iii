import random
import time


def murge_sort(dados: list) -> list:
    if len(dados) > 1:
        meio = len(dados) // 2
        esquerdo = dados[:meio]
        direito = dados[meio:]

        murge_sort(esquerdo)
        murge_sort(direito)

        i = j = k = 0

        while i < len(esquerdo) and j < len(direito):
            if esquerdo[i] < direito[j]:
                dados[k] = esquerdo[i]
                i += 1
            else:
                dados[k] = direito[j]
                j += 1
            k+=1

        while i < len(esquerdo):
            dados[k] = esquerdo[i]
            i += 1
            k += 1

        while j < len(direito):
            dados[k] = direito[j]
            j += 1
            k += 1


    return dados

datas = []

for i in range(0, 10000):
    numbers = random.randint(1, 9999)
    datas.append(numbers)

tic = time.perf_counter()
murge_sort(datas)
toc = time.perf_counter()

print(f'Murge sort levou {toc - tic:0.4f} segundos para ordenar {len(datas)} dados')
