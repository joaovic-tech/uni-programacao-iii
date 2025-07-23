# O dicionário também é considerado uma hash.

fruits = dict()

fruits['kiwi'] = 3.12
fruits['abacaxi'] = 1.97
fruits['banana'] = 2.65
fruits['uva'] = 9.99

print('-' * 30)
print('|   Frutas     |   Preços' + '     |')
print('-' * 30)
for fruit, price in fruits.items():
    print(f'| {fruit:<10}   | R$ {price:>5.2f}     |')
print('-' * 30)


print(f'Acessando todo o o dicionário: {fruits}')
print(f'Acessando as chaves do dicionário: {fruits.keys()}')
print(f'Acessando o valor de uma chave específica: fruits["banana"] = {fruits["banana"]}  ')