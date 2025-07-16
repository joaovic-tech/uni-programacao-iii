import time
import random


def quick_sort(datas, start, end):
    if start < end:
        partition_pos = partition(datas, start, end)
        quick_sort(datas, start, partition_pos - 1)
        quick_sort(datas, partition_pos + 1, end)

def partition(datas, start, end):
    pivot = datas[start]
    left = start + 1
    right = end
    flag = False

    while not flag:
        while left <= right and datas[left] <= pivot:
            left += 1
        while datas[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            flag = True
        else:
            temp = datas[left]
            datas[left] = datas[right]
            datas[right] = temp

    temp = datas[start]
    datas[start] = datas[right]
    datas[right] = temp
    return right

datas = []

for i in range(0, 10000):
    numbers = random.randint(1, 9999)
    datas.append(numbers)

tic = time.perf_counter()
quick_sort(datas, 0, len(datas) - 1)
toc = time.perf_counter()

print(f'Quick sort levou {toc - tic:0.4f} segundos para ordenar {len(datas)} dados')
