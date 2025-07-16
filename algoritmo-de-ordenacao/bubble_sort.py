import time
import random

def bubble_sort(datas: list): # O(n2)
    for v in range(0, len(datas), 1):
        for i in range(0, len(datas) - 1, 1):
            num_actual = datas[i]
            num_next = datas[i + 1]

            if num_actual > num_next:
                datas[i + 1] = num_actual
                datas[i] = num_next

datas = []

for i in range(0, 10000):
    numbers = random.randint(1, 9999)
    datas.append(numbers)

tic = time.perf_counter()
bubble_sort(datas)
toc = time.perf_counter()

print(f'Bubble sort levou {toc - tic:0.4f} segundos para ordenar {len(datas)} dados')
