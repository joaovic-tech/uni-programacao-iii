"""
Algoritmo recursivo => Funcao que chama a si proprio.
Muitos algoritmos recursivos têm como principio a sua divisão em partes menores.
"""
def fatorial_recursiva(num):
    if num == 0:
        return 1
    else:
        return num * fatorial_recursiva(num - 1)

def fatorial_iterativo(num):
    fat = 1
    if num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            fat *= i
        return fat

print(f"Chamando a funcao recursiva, 5! = {fatorial_recursiva(5)}")
print(f"Chamando a funcao iterativo, 5! = {fatorial_iterativo(5)}")
