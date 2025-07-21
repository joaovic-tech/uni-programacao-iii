def push(pilha, top, tam, num):
    if len(pilha) == tam:
        print('Pilha cheia! Impossivel inserir!')
    else:
        pilha.insert(top, num)
        top += 1
        return pilha, top

def pop(pilha, top):
    if len(pilha) == 0:
        print('Pilha vazia! Impossivel inserir!')
    else:
        del pilha[top]
        top -= 1
        return pilha, top

def menu():
    print('1 - Inserir na pilha')
    print('2 - Remover da pilha')
    print('3 - Listar a pilha')
    print('4 - Sair')

top = 0
pilha = []
tam = 5

if __name__ == '__main__':
    while True:
        menu()
        op = int(input('Escolha uma opcao: '))

        if op == 1:
            num = int(input('Insira um valor: '))
            push(pilha, top, tam, num)
        elif op == 2:
            pop(pilha, top)
        elif op == 3:
            for item in pilha:
                print(item)
        elif op == 4:
            print('Saindo!')
            break
        else:
            print('Selecione outra opcao!\n')

