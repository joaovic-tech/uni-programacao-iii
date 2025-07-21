class BST:
    def __init__(self, dado=None):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def inserir(self, dado):
        if self.dado is None:
            self.dado = dado
        else:
            if dado < self.dado:
                if self.esquerda:
                    self.esquerda.inserir(dado)
                else:
                    self.esquerda = BST(dado)
            else:
                if self.direita:
                    self.direita.inserir(dado)
                else:
                    self.direita = BST(dado)

    def em_ordem(self, lista: list) -> list:
        if self.esquerda:
            self.esquerda.emOrdem(lista)
        lista.append(self.dado)
        if self.direita:
            self.direita.emOrdem(lista)
        return lista

    def pre_ordem(self, lista: list) -> list:
        lista.append(self.dado)
        if self.esquerda:
            self.esquerda.preOrdem(lista)
        if self.direita:
            self.direita.preOrdem(lista)
        return lista

    def pos_ordem(self, lista: list) -> list:
        if self.esquerda:
            self.esquerda.posOrdem(lista)
        if self.direita:
            self.direita.posOrdem(lista)
        lista.append(self.dado)
        return lista

    def em_nivel(self) -> list:
        nodo_atual = self
        lista = []
        fila = []
        fila.insert(0, nodo_atual)
        while len(fila) > 0:
            nodo_atual = fila.pop()
            lista.append(nodo_atual.dado)
            if nodo_atual.esquerda:
                fila.insert(0, nodo_atual.esquerda)
            if nodo_atual.direita:
                fila.insert(0, nodo_atual.direita)

        return lista

#               Jader
#           /           \
#          /             \
#       Camila          Maria
#      /     \           /     \
#  Ana     Eduardo   Leonardo   Yago

arvore = BST()

while True:
    print('1 - Inserir na árvore binária')
    print('2 - Remover da árvore binária')
    print('3 - Imprimir a árvore binária')
    print('4 - Sair')

    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        dado = input('Qual nome deseja inserir? ')
        arvore.inserir(dado)
    # elif opcao == 2:
    #     dado = input('Qual nome deseja remover? ')
    #     arvore.remover(dado)
    elif opcao == 3:
        print('Em ordem:', arvore.em_ordem([]))
    elif opcao == 4:
        print('Encerrando...')
        break
    else:
        print('Opção inválida, tente novamente.\n')
